#!/usr/bin/env python3
from cmk.rulesets.v1.form_specs import CascadingSingleChoice, CascadingSingleChoiceElement, DefaultValue, Dictionary, DictElement, FixedValue, Float, Integer, migrate_to_password, String, Password, validators
from cmk.rulesets.v1.rule_specs import SpecialAgent, Topic, Help, Title
def _formspec():
    return Dictionary(
        title=Title("Extension Starter Pack by Paulo Santana - Special Agent"),
        help_text=Help("A structured example to help users write and implement rulesets in Checkmk, covering parameters, authentication, and external integrations."),
        elements={
            "element1": DictElement(
                required=True,
                parameter_form=Float(
                    title=Title("Variable Name: element1 / Required: True / cmk.rulesets.v1.form_specs: Float"),
                ),
            ),
            "element2": DictElement(
                required=False,
                parameter_form=Float(
                    title=Title("Variable Name: element2 / Required: False / cmk.rulesets.v1.form_specs: Float"),
                ),
            ),
            "user": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Variable Name: user / Required: True / cmk.rulesets.v1.form_specs: String"),
                    prefill=DefaultValue("defaultuser"),
                ),
            ),
            "password": DictElement(
                required=True,
                parameter_form=Password(
                    title=Title("Variable Name: password / Required: True / cmk.rulesets.v1.form_specs: Password and migrate_to_password"),
                    migrate=migrate_to_password,
                ),
			),
            "hostname": DictElement(
				required=True,
                parameter_form=String(
                    title=Title("Variable Name: hostname / Required: True / Prefill: $HOSTADDRESS / cmk.rulesets.v1.form_specs: String and DefaultValue"),
                    help_text=Help('You can specify a hostname or IP address different from IP address of the host as configured in your host properties.'),
                    prefill=DefaultValue("$HOSTADDRESS$"),
                ),
            ),
			"port": DictElement(
				required=False,
                parameter_form=Integer(title=Title("Variable Name: port / Required: False / cmk.rulesets.v1.form_specs: Integer and validators"),
                    help_text=Help("Port number for connection. Default: 443"),
                    prefill=DefaultValue(443),
                    custom_validate=(validators.NumberInRange(min_value=1, max_value=65535),),
                ),
            ),
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
rule_spec_hellospecial = SpecialAgent(
    topic=Topic.APPLICATIONS,
    name="check_esp_ps",
    title=Title("Extension Starter Pack by Paulo Santana"),
    parameter_form=_formspec
)