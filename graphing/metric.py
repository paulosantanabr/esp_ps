#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# License: GNU General Public License v2

# Documentation:
# This script defines custom metric objects using Checkmk's graphing API (v1).
# Metrics are used to represent specific resources (fictional animals with colors in this case) 
# and are visualized in Checkmk's UI. Each metric includes:
# - `name`: A unique identifier for the metric, used to reference it in Checkmk configurations.
# - `title`: A human-readable name for the metric, displayed in the UI.
# - `unit`: Specifies how the metric's values are formatted (e.g., decimal notation).
# - `color`: Defines the color used to represent the metric in graphs.

# Purpose:
# - This script is part of a Checkmk extension and is used to define metrics for monitoring and visualization.
# - Metrics defined here must be linked to corresponding perfometers or graph definitions for proper visualization.

# Maintenance Notes:
# - To add a new metric:
#   1. Define a new `metrics.Metric` object with a unique `name`.
#   2. Provide a `title` (human-readable name), `unit` (value formatting), and `color` (graph display color).
#   3. Ensure the new metric is referenced in the corresponding perfometer or graph definition.
# - To update an existing metric:
#   1. Modify the relevant properties (`name`, `title`, `unit`, or `color`) as needed.
#   2. Verify that the changes are consistent with the associated perfometer or graph definitions.

from cmk.graphing.v1 import metrics, Title  # Import Checkmk graphing metric utilities and title wrapper

# Define a metric for "Brown Dogs"
# - Represents the "brown_dogs" resource.
# - Uses brown as the display color.
metric_input_power = metrics.Metric(
    name="brown_dogs",  # Unique identifier for the metric
    title=Title("Brown Dogs"),  # Human-readable title shown in UI
    unit=metrics.Unit(metrics.DecimalNotation("Brown Dogs")),  # Unit formatting using decimal notation
    color=metrics.Color.BROWN,  # Display color for the graph
)

# Define a metric for "Green Cats"
# - Represents the "green_cats" resource.
# - Uses green as the display color.
metric_input_energy = metrics.Metric(
    name="green_cats",
    title=Title("Green Cats"),
    unit=metrics.Unit(metrics.DecimalNotation("Green Cats")),
    color=metrics.Color.GREEN,
)

# Define a metric for "Blue Birds"
# - Represents the "blue_birds" resource.
# - Uses blue as the display color.
metric_output_power = metrics.Metric(
    name="blue_birds",
    title=Title("Blue Birds"),
    unit=metrics.Unit(metrics.DecimalNotation("Blue Birds")),
    color=metrics.Color.BLUE,
)

# Define a metric for "Red Fishes"
# - Represents the "red_fishes" resource.
# - Uses red as the display color.
metric_output_energy = metrics.Metric(
    name="red_fishes",
    title=Title("Red Fishes"),
    unit=metrics.Unit(metrics.DecimalNotation("Red Fishes")),
    color=metrics.Color.RED,
)

# Define a metric for "Yellow Ducks"
# - Represents the "yellow_ducks" resource.
# - Uses yellow as the display color.
metric_water_flow = metrics.Metric(
    name="yellow_ducks",
    title=Title("Yellow Ducks"),
    unit=metrics.Unit(metrics.DecimalNotation("Yellow Ducks")),
    color=metrics.Color.YELLOW,
)

# Additional Notes:
# - These metrics are fictional and used for demonstration purposes.
# - Ensure that any new or updated metrics are consistent with the overall design and purpose of the Checkmk extension.
# - For more information on Checkmk's graphing API, refer to the official documentation.