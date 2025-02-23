# Extension Starter Pack by Paulo Santana
A toolkit for developing custom extensions.

## Overview
This extension is designed to assist users in writing and implementing rulesets in Checkmk. It provides a structured example of a Special Agent, showcasing best practices for defining parameters, handling authentication, and integrating with external services. As part of the Extension Starter Pack by Paulo Santana, this tool serves as a foundation for those looking to create custom monitoring solutions within Checkmk.

## Features
- **Structured Example**: Provides a clear example of a Special Agent.
- **Best Practices**: Demonstrates best practices for defining parameters and handling authentication.
- **Integration**: Seamlessly integrates with external services.
- **AI Assistance**: Leverages AI to generate code and provide recommendations for creating and modifying rulesets.

## Ruleset Options
| Variable Name | Required | cmk.rulesets.v1.form_specs                          |
|---------------|----------|-----------------------------------------------------|
| element1      | True     | Float                                               |
| element2      | False    | Float                                               |
| user          | True     | String                                              |
| password      | True     | Password                                            |
| hostname      | True     | String and DefaultValue / Prefill: '$HOSTADDRESS$'  |
| port          | False    | Integer and validators                              |
| protocol      | False    | CascadingSingleChoice, CascadingSingleChoiceElement, FixedValue |

## AI Capability
This repository is being improved to utilize AI for generating code. It provides the necessary context to assist AI in understanding and creating what is needed. A Checkmk Ruleset Specialist persona is provided along with several examples of ruleset creation.

### Checkmk Ruleset Specialist Persona
The Checkmk Ruleset Specialist is an AI assistant designed to help users create and implement structured rulesets in Checkmk. The specialist provides recommendations, guidance, and code snippets to achieve the desired functionality in Checkmk monitoring configurations.

### How to Use the AI Assistant
1. **Provide Context**: Start by providing the AI assistant with the context of your project and what you want to achieve.
2. **Ask Questions**: Ask the AI assistant specific questions about creating or modifying rulesets in Checkmk.
3. **Receive Recommendations**: The AI assistant will provide recommendations based on your requirements.
4. **Generate Code**: The AI assistant will generate the necessary code to implement the desired functionality.
5. **Understand the Code**: The AI assistant will explain the generated code, providing context and details to help you understand how it works.

### Loading the AI Context
To use the AI assistant, you need to load the context from the `esp_ps.py` file and the `persona.ai` file. Here is a prompt to load these files:

```plaintext
Please read the following files to understand the context and assist in creating new rulesets:
1. [esp_ps.py](./esp_ps/esp_ps.py)
2. [persona.ai](./AI/persona.ai)






## Screenshots

![image](https://github.com/user-attachments/assets/fdc1a5f1-435b-4a6c-af8a-36a22c5761f4)




![image](https://github.com/user-attachments/assets/3b37481e-5fb0-4c13-afe9-1fbd71293ac2)


![image](https://github.com/user-attachments/assets/a3e80a3e-024c-4965-9f5a-64422c7b03f4)

