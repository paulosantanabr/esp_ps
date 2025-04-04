#!/usr/bin/env python3

# Import necessary modules from Checkmk's graphing API
# - metrics: Provides tools for defining metrics (not used directly here but imported for context).
# - Title: Used for defining human-readable titles (not used directly here but imported for context).
# - graphs: Provides tools for creating graphs (not used directly here but imported for context).
# - perfometers: Provides tools for creating perfometers, which are visual representations of performance data.
from cmk.graphing.v1 import metrics, Title, graphs, perfometers

# Define a perfometer for "Brown Dogs"
# - name: Unique identifier for the perfometer.
# - focus_range: Defines the range of values the perfometer focuses on (0 to 100 in this case).
# - segments: Specifies the metric(s) this perfometer represents (e.g., "brown_dogs").
perfometer_brown_dogs = perfometers.Perfometer(
        name="brown_dogs",
        focus_range=perfometers.FocusRange(
                perfometers.Closed(0), perfometers.Closed(100)),  # Closed range from 0 to 100
        segments=["brown_dogs"],  # Metric associated with this perfometer
)

# Define a perfometer for "Green Cats"
# - Similar structure to "Brown Dogs" but represents the "green_cats" metric.
perfometer_green_cats = perfometers.Perfometer(
        name="green_cats",
        focus_range=perfometers.FocusRange(
                perfometers.Closed(0), perfometers.Closed(100)),  # Closed range from 0 to 100
        segments=["green_cats"],  # Metric associated with this perfometer
)

# Define a perfometer for "Blue Birds"
# - Represents the "blue_birds" metric.
# - Displays values in the range of 0 to 100.
perfometer_blue_birds = perfometers.Perfometer(
        name="blue_birds",
        focus_range=perfometers.FocusRange(
                perfometers.Closed(0), perfometers.Closed(100)),  # Closed range from 0 to 100
        segments=["blue_birds"],  # Metric associated with this perfometer
)

# Define a perfometer for "Red Fishes"
# - Represents the "red_fishes" metric.
# - Displays values in the range of 0 to 100.
perfometer_red_fishes = perfometers.Perfometer(
        name="red_fishes",
        focus_range=perfometers.FocusRange(
                perfometers.Closed(0), perfometers.Closed(100)),  # Closed range from 0 to 100
        segments=["red_fishes"],  # Metric associated with this perfometer
)

# Define a perfometer for "Yellow Ducks"
# - Represents the "yellow_ducks" metric.
# - Displays values in the range of 0 to 100.
perfometer_yellow_ducks = perfometers.Perfometer(
        name="yellow_ducks",
        focus_range=perfometers.FocusRange(
                perfometers.Closed(0), perfometers.Closed(100)),  # Closed range from 0 to 100
        segments=["yellow_ducks"],  # Metric associated with this perfometer
)

# Note:
# - Perfometers are used in Checkmk to provide a quick visual representation of performance data.
# - Each perfometer is linked to a specific metric (e.g., "brown_dogs", "green_cats", "blue_birds", "red_fishes", "yellow_ducks").
# - The `focus_range` defines the range of values that the perfometer will display, which helps in scaling the visualization.
# - The `segments` parameter allows associating one or more metrics with the perfometer.
# - To add more perfometers:
#   1. Define a new `perfometers.Perfometer` object with a unique `name`.
#   2. Specify a `focus_range` that matches the expected range of the metric's values.
#   3. Add the corresponding metric name(s) to the `segments` parameter.
#   4. Ensure the new perfometer is consistent with the metric definitions in the `metric.py` file.