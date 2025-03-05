
# This script defines the configuration for an active check in Checkmk.
# It includes parameter parsing and command generation for the ESP PS active check.

from collections.abc import Iterator, Sequence
from pydantic import BaseModel
from cmk.server_side_calls.v1 import ActiveCheckCommand, ActiveCheckConfig, HostConfig, Secret

# Define a class for the check parameters using pydantic.BaseModel.
# This class includes all the parameters required for the check.
class EspPsParams(BaseModel):
    service_description: str | None = None
    servicename: str | None = None
    state: str | None = None

# Define a function to generate the command arguments for the check.
# This function uses the provided parameters and default values if parameters are not provided.
def generate_esp_ps_commands(params, _host_config):
    # Create the command arguments tuple with default values if parameters are not provided.
    args = (
        "-n",
        params.servicename or "Extension Starter Pack - Active Check - Minimal",
        "-s",
        params.state or "OK",
    )

    # Yield an ActiveCheckCommand with the service description and command arguments.
    yield ActiveCheckCommand(service_description=params.service_description, command_arguments=args)

# Define the active check configuration using ActiveCheckConfig.
# This includes the name of the check, the parameter parser, and the command generation function.
active_check_esp_ps_active_check_minimal = ActiveCheckConfig(
    name="esp_ps_active_check_minimal",
    parameter_parser=EspPsParams.model_validate,
    commands_function=generate_esp_ps_commands,
)
