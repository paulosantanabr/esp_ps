# extensionstarterpackbypaulosantana
Extension Starter Pack by Paulo Santana. A toolkit for developing custom extensions.

This extension is designed to assist users in writing and implementing rulesets in Checkmk. It provides a structured example of a Special Agent, showcasing best practices for defining parameters, handling authentication, and integrating with external services. As part of the Extension Starter Pack by Paulo Santana, this tool serves as a foundation for those looking to create custom monitoring solutions within Checkmk. 
Ruleset options available:
Variable Name: element1 / Required: True / cmk.rulesets.v1.form_specs: Float
Variable Name: element2 / Required: False / cmk.rulesets.v1.form_specs: Float
Variable Name: user / Required: True / cmk.rulesets.v1.form_specs: String
Variable Name: password / Required: True / cmk.rulesets.v1.form_specs: Password and migrate_to_password
Variable Name: hostname / Required: True / Prefill: $HOSTADDRESS / cmk.rulesets.v1.form_specs: String and DefaultValue
Variable Name: port / Required: False / cmk.rulesets.v1.form_specs: Integer and validators
Variable Name: protocol / Required: False / cmk.rulesets.v1.form_specs: CascadingSingleChoice and CascadingSingleChoiceElement and FixedValue






![image](https://github.com/user-attachments/assets/fdc1a5f1-435b-4a6c-af8a-36a22c5761f4)




![image](https://github.com/user-attachments/assets/3b37481e-5fb0-4c13-afe9-1fbd71293ac2)


![image](https://github.com/user-attachments/assets/aa04876c-a402-4633-9c4c-63fdd272df82)
