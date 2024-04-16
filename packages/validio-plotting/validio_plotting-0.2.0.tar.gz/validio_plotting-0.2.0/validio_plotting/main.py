#!/usr/bin/env python3

"""This is a tool that fetches metrics and plots them in a graph."""


import asyncio
import contextlib
import os
import sys
import time
import urllib.parse
import webbrowser
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import plotext as plt
import typer
import validio_cli
import validio_sdk.validio_client
from prompt_toolkit.input import Input, create_input
from prompt_toolkit.keys import Keys
from validio_cli.components import radiolist_dialog
from validio_sdk.graphql_client.enums import DecisionBoundsType
from validio_sdk.graphql_client.input_types import (
    TimeRangeInput,
    ValidatorSegmentMetricsInput,
)

MAX_METRIC_PER_RESULT = 1000
FIXED_THRESHOLD_NAME = "ValidatorMetricWithFixedThreshold"

app = validio_cli.AsyncTyper(help="Plot metrics", pretty_exceptions_enable=False)


@dataclass
class _Events:
    ticker: asyncio.Event = field(default_factory=asyncio.Event)
    done: asyncio.Event = field(default_factory=asyncio.Event)
    graph: asyncio.Event = field(default_factory=asyncio.Event)
    history: asyncio.Event = field(default_factory=asyncio.Event)
    interval: asyncio.Event = field(default_factory=asyncio.Event)
    open: asyncio.Event = field(default_factory=asyncio.Event)


# ruff: noqa: PLR0912,PLR0915
@app.async_command()
async def graph(
    config_dir: str = validio_cli.ConfigDir,
    ended_before: datetime = typer.Option(
        datetime.now(),
        "-ended-before",
        "-e",
        help="Data seen before this timestamp",
    ),
    historical_minutes: int = typer.Option(
        5,
        "--historical-minutes",
        "-h",
        help="How many minutes to fetch metrics for before the `end_before` time",
    ),
    refresh_interval: int = typer.Option(
        0, "--refresh-interval", "-r", help="Refresh interval in seconds. 0 = Off"
    ),
) -> None:
    """
    Graph metrics in the terminal.

    Specify a stop timestamp and start an interactive plotting panel where you
    can switch between sources and validators to see graphs in your terminal.
    """
    vc, cfg = await validio_cli.get_client_and_config(config_dir)
    source_id, validator_id, segment_id, start_idx = await _get_validator_and_segment(
        vc
    )

    plt.date_form("Y-m-d H:M:S")
    plt.title("Metrics")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.canvas_color("default")
    plt.axes_color("default")
    plt.ticks_color("white")

    # Reduce the size so we have room for our actions legend
    w, h = plt.terminal_size()
    plt.plot_size(w, h - 2)

    keyboard_input = create_input()
    warning_shown = False
    start = ended_before - timedelta(minutes=historical_minutes)

    events = _Events()
    read_fn = _keys_read_func(keyboard_input, events)

    while True:
        end = start + timedelta(minutes=historical_minutes)

        metrics = await vc.get_validator_segment_metrics(
            ValidatorSegmentMetricsInput(
                validator_id=validator_id,
                segment_id=segment_id,
                time_range=TimeRangeInput(
                    start=start,
                    end=end,
                ),
            )
        )

        if len(metrics.values) == MAX_METRIC_PER_RESULT and not warning_shown:
            warning_shown = True
            _print_limit_warning(
                start,
                end,
                metrics.values[0].end_time,
                metrics.values[-1].end_time,
            )

        plt.clear_data()

        dates = []
        all_datapoints = []
        incident_datapoints = []
        bound1: list[float] = []
        bound2: list[float | None] = []

        for value in metrics.values:
            dates.append(value.end_time)

            if value.typename__ == FIXED_THRESHOLD_NAME:
                bound1.append(value.bound)
                bound2.append(None)
            else:
                match value.decision_bounds_type:
                    case DecisionBoundsType.UPPER_AND_LOWER:
                        bound1.append(value.upper_bound)
                        bound2.append(value.lower_bound)
                    case DecisionBoundsType.UPPER, DecisionBoundsType.LOWER:
                        bound1.append(value.upper_bound)
                        bound2.append(None)

            if value.is_incident:
                incident_datapoints.append(value.value)
            else:
                incident_datapoints.append(None)

            all_datapoints.append(value.value)

        dates = plt.datetimes_to_string(dates)

        plt.plot(dates, bound1, marker="braille", color="green")
        plt.plot(dates, bound2, marker="braille", color="green")

        plt.plot(dates, all_datapoints, marker="hd")
        plt.plot(dates, incident_datapoints, marker="hd", color="red")

        plt.show()

        started_at = time.time()

        options = [
            "[c]hange",
            "[h]istory",
            "refresh [i]nterval",
            "[o]pen in browser",
            "[q]uit",
            "[r]efresh",
        ]

        print("\n" + ", ".join(options), end=" ")
        sys.stdout.flush()

        with keyboard_input.raw_mode(), keyboard_input.attach(read_fn):
            try:
                if refresh_interval > 0:
                    await asyncio.wait_for(
                        events.ticker.wait(), timeout=refresh_interval
                    )
                else:
                    await events.ticker.wait()

                events.ticker.clear()
            except asyncio.TimeoutError:
                pass

        if events.done.is_set():
            break

        if events.graph.is_set():
            events.graph.clear()
            (
                source_id,
                validator_id,
                segment_id,
                start_idx,
            ) = await _get_validator_and_segment(vc, start_idx=start_idx)

        if events.history.is_set():
            events.history.clear()
            while True:
                with contextlib.suppress(ValueError):
                    print()
                    historical_minutes = int(input("Historical minutes: "))
                    break

            start = end - timedelta(minutes=historical_minutes)

        if events.interval.is_set():
            events.interval.clear()
            while True:
                with contextlib.suppress(ValueError):
                    print()
                    refresh_interval = int(input("Refresh interval (0 is off): "))
                    break

        if events.open.is_set():
            events.open.clear()

            start_utc = start - timedelta(hours=1)
            end_utc = end - timedelta(hours=1)
            url_start = start_utc.strftime("%Y-%m-%dT%H!:%M!:%S.000Z")
            url_end = end_utc.strftime("%Y-%m-%dT%H!:%M!:%S.000Z")
            time_range = urllib.parse.quote(
                f"(range:CUSTOM,start:{url_start},end:{url_end})"
            )
            full_url = (
                f"{cfg.endpoint}/sources/{source_id}/validators/"
                f"{validator_id}?segmentId={segment_id}&timeRange={time_range}"
            )
            webbrowser.open(full_url)

        ended_at = time.time()
        start = start + timedelta(seconds=ended_at - started_at)


def _clear_screen() -> None:
    os.system("cls") if os.name == "nt" else os.system("clear")


def _print_limit_warning(
    start: datetime, end: datetime, first_start: datetime, last_start: datetime
) -> None:
    _clear_screen()

    start_fmt = start.strftime("%Y-%m-%d %H:%M:%S")
    end_fmt = end.strftime("%Y-%m-%d %H:%M:%S")
    first_start_fmt = first_start.strftime("%Y-%m-%d %H:%M:%S")
    last_start_fmt = last_start.strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"WARNING!!! The current time window ({start_fmt} - {end_fmt}) contains"
        " more than 1000 datapoints!"
    )
    print(
        "The graph will only contain the first 1000 data points which is"
        f" between {last_start_fmt} - {first_start_fmt}"
    )
    print()
    input("Press enter to continue")


async def _get_validator_and_segment(
    vc: validio_sdk.validio_client.ValidioAPIClient,
    start_idx: tuple[int, int, int] = (0, 0, 0),
) -> tuple[str, str, str, tuple[int, int, int]]:
    _clear_screen()

    sources = await vc.list_sources()
    source_items = [(i, x.resource_name) for i, x in enumerate(sources)]
    source_idx = await _get_resource(source_items, "source", start_idx[0])
    source = sources[source_idx]

    if source_idx != start_idx[0]:
        start_idx = (source_idx, 0, 0)

    validators = await vc.list_validators(id=source.id)
    validator_items = [(i, x.resource_name) for i, x in enumerate(validators)]
    validator_idx = await _get_resource(validator_items, "validator", start_idx[1])
    validator = validators[validator_idx]

    if validator_idx != start_idx[1]:
        start_idx = (source_idx, validator_idx, 0)

    segments = await vc.segments(validator.source_config.segmentation.id)
    segment_items = [
        (
            i,
            ", ".join(
                f"{segment_field.field} = {segment_field.value}"
                for segment_field in segment.fields
            ),
        )
        for i, segment in enumerate(segments)
    ]
    segment_idx = await _get_resource(segment_items, "segment", start_idx[2])
    segment = segments[segment_idx]

    return source.id, validator.id, segment.id, (source_idx, validator_idx, segment_idx)


async def _get_resource(items: list, type_: str, start_idx: int = 0) -> int:
    if len(items) == 0:
        raise Exception(f"No {type_}s found...")

    if len(items) == 1:
        return 0

    idx = await radiolist_dialog(
        title=f"Select {type_}",
        values=items,
        navigation_help=True,
        default_value_index=start_idx,
    )

    # If the user hits ^c `idx` will be `None` so just exit.
    if idx is None:
        sys.exit(1)

    return idx


def _keys_read_func(keyboard_input: Input, events: _Events) -> Callable:
    def keys_ready() -> None:
        for key_press in keyboard_input.read_keys():
            if key_press.key == Keys.ControlC or key_press.key.lower() == "q":
                events.ticker.set()
                events.done.set()

            if key_press.key.lower() == "r":
                events.ticker.set()

            if key_press.key.lower() == "c":
                events.ticker.set()
                events.graph.set()

            if key_press.key.lower() == "h":
                events.ticker.set()
                events.history.set()

            if key_press.key.lower() == "i":
                events.ticker.set()
                events.interval.set()

            if key_press.key.lower() == "o":
                events.ticker.set()
                events.open.set()

    return keys_ready


def main() -> None:
    """Main entrypoint for the app."""
    app()


if __name__ == "__main__":
    main()
