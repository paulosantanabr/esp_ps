#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# License: GNU General Public License v2

# This script defines custom metric objects using Checkmk's graphing API (v1).
# Each metric represents a fictional resource (animals with colors) and includes:
# - a unique identifier (`name`)
# - a display title (`title`)
# - a unit (with decimal formatting)
# - a color for visualization in graphs

from cmk.graphing.v1 import metrics, Title  # Import Checkmk graphing metric utilities and title wrapper

# Define a metric for "Brown Dogs"
metric_input_power = metrics.Metric(
    name="brown_dogs",  # Unique identifier for the metric
    title=Title("Brown Dogs"),  # Human-readable title shown in UI
    unit=metrics.Unit(metrics.DecimalNotation("Brown Dogs")),  # Unit formatting using decimal notation
    color=metrics.Color.BROWN,  # Display color for the graph
)

# Define a metric for "Green Cats"
metric_input_energy = metrics.Metric(
    name="green_cats",
    title=Title("Green Cats"),
    unit=metrics.Unit(metrics.DecimalNotation("Green Cats")),
    color=metrics.Color.GREEN,
)

# Define a metric for "Blue Birds"
metric_output_power = metrics.Metric(
    name="blue_birds",
    title=Title("Blue Birds"),
    unit=metrics.Unit(metrics.DecimalNotation("Blue Birds")),
    color=metrics.Color.BLUE,
)

# Define a metric for "Red Fishes"
metric_output_energy = metrics.Metric(
    name="red_fishes",
    title=Title("Red Fishes"),
    unit=metrics.Unit(metrics.DecimalNotation("Red Fishes")),
    color=metrics.Color.RED,
)

# Define a metric for "Yellow Ducks"
metric_water_flow = metrics.Metric(
    name="yellow_ducks",
    title=Title("Yellow Ducks"),
    unit=metrics.Unit(metrics.DecimalNotation("Yellow Ducks")),
    color=metrics.Color.YELLOW,
)

# Note:
# These metrics are typically used in Checkmk extensions (e.g., for graphing monitoring data)
# and must be referenced in the corresponding check or datasource plugin logic.
