#!/usr/bin/env python3

from typing import Iterator
from pydantic import BaseModel
from cmk.server_side_calls.v1 import ActiveCheckCommand, ActiveCheckConfig


# Custom parser for metrics in the format "value;warn;crit"
def parse_metric_string(metric_str: str) -> tuple[int, int, int]:
    value_str, warn_str, crit_str = metric_str.strip().split(";")
    return int(value_str), int(warn_str), int(crit_str)


# Define the parameters that will come from the rule
class CustomMetricParams(BaseModel):
    service_description: str | None = "	Extension Starter Pack - Active Check - Custom Metrics"
    brown_dog: str | None = None
    green_cat: str | None = None
    blue_bird: str | None = None
    red_fish: str | None = None
    yellow_duck: str | None = None


# This function generates the active check command to be executed
def generate_custom_metrics_command(params: CustomMetricParams, _host_config) -> Iterator[ActiveCheckCommand]:
    args = []
    metrics = {
        "brown_dogs": params.brown_dog,
        "green_cats": params.green_cat,
        "blue_birds": params.blue_bird,
        "red_fishes": params.red_fish,
        "yellow_ducks": params.yellow_duck,
    }

    for metric_name, value in metrics.items():
        if value:
            args.append(f"--{metric_name} {value}")

    yield ActiveCheckCommand(
        service_description=params.service_description,
        command_arguments=tuple(" ".join(args).split())  # flatten into tuple of args
    )


# Register the check in Checkmk
active_check_esp_ps_active_check_custom_metrics = ActiveCheckConfig(
    name="esp_ps_active_check_custom_metrics",
    parameter_parser=CustomMetricParams.model_validate,
    commands_function=generate_custom_metrics_command,
)