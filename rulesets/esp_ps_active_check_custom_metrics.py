#!/usr/bin/env python3

# Author: Paulo Santana
# References:
# redfish-2.3.38
# ometemp-0.1.0
# rdp-active-check-2.0

# AI Context: Checkmk is a monitoring tool that helps organizations identify and resolve issues in their IT infrastructure. This script is an example of a structured ruleset implementation in Checkmk, covering parameters, authentication, and external integrations.

# Import necessary modules from Checkmk's rulesets
from cmk.rulesets.v1.form_specs import DefaultValue, Dictionary, DictElement, String, Password
from cmk.rulesets.v1.rule_specs import ActiveCheck, Topic, Help, Title

# Define the form specification function
def _formspec():
    return Dictionary(
        title=Title("Extension Starter Pack - Active Check - Custom Metrics"),
        help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
        elements={
            "service_description": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Service Name"),
                    help_text=Help("Define the name. Any value is allowed in here. Variable Name: service_description \ required=True \ parameter_form=String \ prefill=DefaultValue(Extension Starter Pack - Active Check - Minimal)"),
                    prefill=DefaultValue("Extension Starter Pack - Active Check - Custom Metrics"),
                ),
            ),
           "brown_dog": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Brown Dog (Value;Warning Threshold;Critical Threshold)"),
                    help_text=Help("Define the value for Brown Dog. Variable Name: brown_dog \\ Required: False \\ cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("10;20;30"),
                ),
            ),

            "green_cat": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Green Cat (Value;Warning Threshold;Critical Threshold)"),
                    help_text=Help("Define the value for Green Cat. Variable Name: green_cat \\ Required: False \\ cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("10;15;25"),
                ),
            ),

            "blue_bird": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Blue Bird (Value;Warning Threshold;Critical Threshold)"),
                    help_text=Help("Define the value for Blue Bird. Variable Name: blue_bird \\ Required: False \\ cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("5;10;20"),
                ),
            ),

            "red_fish": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Red Fish (Value;Warning Threshold;Critical Threshold)"),
                    help_text=Help("Define the value for Red Fish. Variable Name: red_fish \\ Required: False \\ cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("8;12;18"),
                ),
            ),

            "yellow_duck": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Yellow Duck (Value;Warning Threshold;Critical Threshold)"),
                    help_text=Help("Define the value for Yellow Duck. Variable Name: yellow_duck \\ Required: False \\ cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("9;14;19"),
                ),
            ),
        }
    )

# Define the special agent with the specified topic, name, title, and parameter form
rule_spec_esp_ps_active_check_authentication = ActiveCheck(
    topic=Topic.APPLICATIONS,
    name="esp_ps_active_check_custom_metrics",
    title=Title("ESP - ActiveCheck - Custom Metrics"),
    help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
    parameter_form=_formspec
)
