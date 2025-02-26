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
        title=Title("Extension Starter Pack by Paulo Santana - Active Check"),
        help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
        elements={
            "service_description": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Service Name"),
                    prefill=DefaultValue("Extension Starter Pack by Paulo Santana - Active Check"),
                ),
            ),
            # Define a required floating-point parameter named 'element1'
            "element1": DictElement(
                required=True,
                parameter_form=Float(
                    title=Title("Variable Name: element1 / Required: True / cmk.rulesets.v1.form_specs: Float"),
                ),
            ),
            # Define an optional floating-point parameter named 'element2'
            "element2": DictElement(
                required=False,
                parameter_form=Float(
                    title=Title("Variable Name: element2 / Required: False / cmk.rulesets.v1.form_specs: Float"),
                ),
            ),
            # Define a required string parameter named 'user' with a default value
            "user": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Variable Name: user / Required: True / cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("defaultuser"),
                ),
            ),
            # Define a required password parameter named 'password'
            "password": DictElement(
                required=True,
                parameter_form=Password(
                    title=Title("Variable Name: password / Required: True / cmk.rulesets.v1.form_specs: Password"),
                ),
			),
            # Define a required string parameter named 'hostname' with a default value and help text
            "hostname": DictElement(
				required=True,
                parameter_form=String(
                    title=Title("Variable Name: hostname / Required: True / Prefill: $HOSTADDRESS$ / cmk.rulesets.v1.form_specs: String and DefaultValue"),
                    help_text=Help('You can specify a hostname or IP address different from IP address of the host as configured in your host properties.'),
                    prefill=DefaultValue("$HOSTADDRESS$"),
                ),
            ),
            # Define an optional integer parameter named 'port' with a default value, help text, and custom validation
			"port": DictElement(
				required=False,
                parameter_form=Integer(title=Title("Variable Name: port / Required: False / cmk.rulesets.v1.form_specs: Integer and validators"),
                    help_text=Help("Port number for connection. Default: 443"),
                    prefill=DefaultValue(443),
                    custom_validate=(validators.NumberInRange(min_value=1, max_value=65535),),
                ),
            ),
            # Define an optional cascading single choice parameter named 'protocol' with default value and help text
            "protocol": DictElement(
                required=False,
                parameter_form=CascadingSingleChoice(
                    title=Title("Variable Name: protocol / Required: False / cmk.rulesets.v1.form_specs: CascadingSingleChoice and CascadingSingleChoiceElement and FixedValue"),
                    prefill=DefaultValue("https"),
                    help_text=Help(
                        "Protocol for the connection to the Rest API."
                        "https is highly recommended!!!"
                    ),
                    elements=[
                        CascadingSingleChoiceElement(
                            name="http",
                            title=Title("http"),
                            parameter_form=FixedValue(value=None),
                        ),
                        CascadingSingleChoiceElement(
                            name="https",
                            title=Title("https"),
                            parameter_form=FixedValue(value=None),
                        ),
                    ],
                ),
            ),
        }
    )

# Define the special agent with the specified topic, name, title, and parameter form
rule_spec_esp_ps_active_check = ActiveCheck(
    topic=Topic.APPLICATIONS,
    name="esp_ps_active_check",
    title=Title("Extension Starter Pack by Paulo Santana - ActiveCheck"),
    help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
    parameter_form=_formspec
)