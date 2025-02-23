# Extension Starter Pack by Paulo Santana
A toolkit for developing custom extensions.

## Overview
This extension is designed to assist users in writing and implementing rulesets in Checkmk. It provides a structured example of a Special Agent, showcasing best practices for defining parameters, handling authentication, and integrating with external services. As part of the Extension Starter Pack by Paulo Santana, this tool serves as a foundation for those looking to create custom monitoring solutions within Checkmk.

## Features
- **Structured Example**: Provides a clear example of a Special Agent.
- **Best Practices**: Demonstrates best practices for defining parameters and handling authentication.
- **Integration**: Seamlessly integrates with external services.

## Ruleset Options
| Variable Name | Required | cmk.rulesets.v1.form_specs                          |
|---------------|----------|-----------------------------------------------------|
| element1      | True     | Float                                               |
| element2      | False    | Float                                               |
| user          | True     | String                                              |
| password      | True     | Password and migrate_to_password                    |
| hostname      | True     | String and DefaultValue / Prefill: $HOSTADDRESS     |
| port          | False    | Integer and validators                              |
| protocol      | False    | CascadingSingleChoice, CascadingSingleChoiceElement, FixedValue |

## Screenshots

![image](https://github.com/user-attachments/assets/fdc1a5f1-435b-4a6c-af8a-36a22c5761f4)




![image](https://github.com/user-attachments/assets/3b37481e-5fb0-4c13-afe9-1fbd71293ac2)


![image](https://github.com/user-attachments/assets/aa04876c-a402-4633-9c4c-63fdd272df82)
