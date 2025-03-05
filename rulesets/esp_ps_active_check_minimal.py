#!/usr/bin/env python3

# Author: Paulo Santana
# References:
# redfish-2.3.38
# ometemp-0.1.0
# rdp-active-check-2.0

# AI Context: Checkmk is a monitoring tool that helps organizations identify and resolve issues in their IT infrastructure. This script is an example of a structured ruleset implementation in Checkmk, covering parameters, authentication, and external integrations.

# Import necessary modules from Checkmk's rulesets
from cmk.rulesets.v1.form_specs import CascadingSingleChoice, CascadingSingleChoiceElement, DefaultValue, Dictionary, DictElement, FixedValue, Float, Integer, String, Password, validators
from cmk.rulesets.v1.rule_specs import ActiveCheck, Topic, Help, Title

# Define the form specification function
def _formspec():
    return Dictionary(
        title=Title("Extension Starter Pack by Paulo Santana - Active Check - Minimal"),
        help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
        elements={
            "service_description": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Service Name"),
                    prefill=DefaultValue("Extension Starter Pack - Active Check - Minimal"),
                ),
            ),
            "state": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Initial State"),
                    prefill=DefaultValue("OK"),
                ),
            ),
        }
    )

# Define the special agent with the specified topic, name, title, and parameter form
rule_spec_esp_ps_active_check_minimal = ActiveCheck(
    topic=Topic.APPLICATIONS,
    name="esp_ps_active_check_minimal",
    title=Title("Extension Starter Pack - ActiveCheck - Minimal"),
    help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
    parameter_form=_formspec
)