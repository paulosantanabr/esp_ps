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
        title=Title("Extension Starter Pack - Active Check - Authentication"),
        help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
        elements={
            "service_description": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Service Name"),
                    help_text=Help("Define the name. Any value is allowed in here. Variable Name: service_description \ required=True \ parameter_form=String \ prefill=DefaultValue(Extension Starter Pack - Active Check - Minimal)"),
                    prefill=DefaultValue("Extension Starter Pack - Active Check - Authentication"),
                ),
            ),
          # Define a required string parameter named 'user' with a default value
            "user": DictElement(
                required=False,
                parameter_form=String(
                    title=Title("Username"),
                    help_text=Help("Define the username. Variable Name: user \ Required: True \ cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("defaultuser"),
                ),
            ),
            # Define a required password parameter named 'password'
            "password": DictElement(
                required=False,
                parameter_form=Password(
                    title=Title("Password"),
                    help_text=Help("Define the password. Variable Name: password \ Required: True \ cmk.rulesets.v1.form_specs: Password"),
                ),
			),
        }
    )

# Define the special agent with the specified topic, name, title, and parameter form
rule_spec_esp_ps_active_check_authentication = ActiveCheck(
    topic=Topic.APPLICATIONS,
    name="esp_ps_active_check_authentication",
    title=Title("Extension Starter Pack - ActiveCheck - Authentication"),
    help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
    parameter_form=_formspec
)