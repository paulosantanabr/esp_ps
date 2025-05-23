# Extension Starter Pack by Paulo Santana
A toolkit for developing custom extensions.

## Author
Paulo Santana

## References
- redfish-2.3.38
- ometemp-0.1.0
- rdp-active-check-2.0

## Overview
This extension is designed to assist users in writing and implementing rulesets in Checkmk. It provides a structured example of a Special Agent, showcasing best practices for defining parameters, handling authentication, and integrating with external services. As part of the Extension Starter Pack by Paulo Santana, this tool serves as a foundation for those looking to create custom monitoring solutions within Checkmk.

## Ruleset Name: Extension Starter Pack - ActiveCheck - Minimal
Using this ruleset you will be able to deploy a basic extension using an active check which will need the mandatory field Service Name and Initial State which is optional. This is the starting point when creating extensions and I recommend using it to start. 

![image](https://github.com/user-attachments/assets/9e01cfef-d8fc-4bae-811a-c5c272d6564f)


## Ruleset Name: Extension Starter Pack by Paulo Santana - ActiveCheck
Using this ruleset you will be able to evaluate different types of fields and values. The active check will print all values in use. It's useful because it contains several fields that would likely be available in a real extension. 

## Ruleset Name: Extension Starter Pack by Paulo Santana - Special Agent
Work in Progress

## Features
- **Structured Example**: Provides a clear example of a Special Agent.
- **Best Practices**: Demonstrates best practices for defining parameters and handling authentication.
- **Integration**: Seamlessly integrates with external services.
- **AI Assistance**: Leverages AI to generate code and provide recommendations for creating and modifying rulesets.

## Ruleset Options
| Variable Name | Required | cmk.rulesets.v1.form_specs                          |
|---------------|----------|-----------------------------------------------------|
| service_description | True     | String                                               |
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

To use the AI assistant, you need to load the context from the `esp_ps.py` file and the `persona.ai` file. Here is a prompt to load these files:

Please read the following files to understand the context and assist in creating new rulesets:
1. [esp_ps_active_check.py](./rulesets/esp_ps_active_check.py)
2. [esp_ps_special_agent.py](./rulesets/esp_ps_special_agent.py)
3. [persona.ai](./AI/persona.ai)

## AI Folder
In the `AI` folder, you will find examples of code generated by AI and the interactions that can be provided. This includes:
- `persona.ai`: The persona description for the Checkmk Ruleset Specialist.
- `example_interaction.md`: An example interaction with the Checkmk Ruleset Specialist.

## Screenshots
- Ruleset:
  
![image](https://github.com/user-attachments/assets/dec8e1ff-b050-4076-ab1c-9eb73cf9e84e)

- AI Generated Code:
  
![image](https://github.com/user-attachments/assets/5300ecc8-497a-4bd4-bade-50c260a9e9f2)

- Active Agent in Action
  
![image](https://github.com/user-attachments/assets/c15342c4-8679-4afd-b700-d4960e0a9151)

- Minimal Active Check:
  
![image](https://github.com/user-attachments/assets/2b6a2739-0a27-4d4f-a30e-d4a90b569865)

![image](https://github.com/user-attachments/assets/07a033cd-a619-40fd-9451-624cd1c4b3fa)


## Example
- Ruleset:
- <img width="566" alt="image" src="https://github.com/user-attachments/assets/9aab7b69-cd98-46ab-870c-4d9ef6a9aabb" />

- Active Check:
- <img width="463" alt="image" src="https://github.com/user-attachments/assets/0bc43775-cfee-47c0-9b26-3c9a6e478a0d" />

## Known Issues
- Problem when using a password that is not the default.
- Problem when defining a protocol different than the default.

## Upcoming Features
- Include Graphics
- Include Initial State
- Include Special Agent Example



## Version History
0.1.3
server_side_calls/esp_ps_active_check.py
- Added HostConfig, Secret in cmk.server_side_calls.v1 
- Changed password from str to Secret inside class EspPsParams

0.1.4
server_side_calls/esp_ps_active_check.py
- Added HostConfig, Secret in cmk.server_side_calls.v1 
- Changed password from str to Secret inside class EspPsParams

0.1.5
libexec/esp_ps_active_check_minimal 
server_side_calls/esp_ps_active_check_minimal.py 
rulesets/esp_ps_active_check_minimal.py 
- Added minimal pack which is the minimal active checkmk extension possible, which reads the service name and initial status.

0.1.6
- A dashboard named **"Extension Starter Pack - ActiveCheck - Minimal"**  
has been added under the **Applications** section.  
It is available when selecting **Show More**.

0.1.7
- A manual page was added to  **"Extension Starter Pack - ActiveCheck - Minimal"** .

0.1.8
- Include components related to  **"Extension Starter Pack - ActiveCheck - Authentication"** containing ruleset, server_side_calls, libexec and checkman.
  
0.1.9
- Include components related to  **"Extension Starter Pack - ActiveCheck - Custom Metrics"** containing ruleset, graphing, server_side_calls, libexec and checkman.

1.0.0
- Added Perfometer into **"Extension Starter Pack - ActiveCheck - Custom Metrics"**

1.1.0
- Fixed issues with password
- Renamed rulesets from Extenstion Starter Pack to ESP

1.2.0
- Renamed service descriptions from Extension Starter Pack to ESP
- Fixed issue with server_side_calls to read protocol information from ruleset
- Improved ESP - Active Check - All in One libexec script to improve the output