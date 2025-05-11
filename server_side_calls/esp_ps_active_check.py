# This script defines the configuration for an active check in Checkmk.
# It includes parameter parsing and command generation for the ESP PS active check.

from collections.abc import Iterator, Sequence
from pydantic import BaseModel
from cmk.server_side_calls.v1 import ActiveCheckCommand, ActiveCheckConfig, HostConfig, Secret 

# Define a class for the check parameters using pydantic.BaseModel.
# This class includes all the parameters required for the check.
class EspPsParams(BaseModel):
    service_description: str | None = None
    hostname: str | None = None
    port: int | None = None
    user: str | None = None
    password: Secret | None = None
#    password: str | None = None
    protocol: str | None = None
    element1: float | None = None
    element2: float | None = None
    state: str | None = None
    servicename: str | None = None

# Define a function to generate the command arguments for the check.
# This function uses the provided parameters and default values if parameters are not provided.
def generate_esp_ps_commands(params, _host_config):
    # Create the command arguments tuple with default values if parameters are not provided.
    args = (
        "-H",
        params.hostname or _host_config.primary_ip_config.address,
        "-p",
        f"{params.port or 443}",
        "-u",
        params.user or "defaultuser",
        "-P",
        params.password.unsafe() or "defaultpassword",
        "-r",
        params.protocol or "https",
        "-e1",
        f"{params.element1 or 0.0}",
        "-e2",
        f"{params.element2 or 0.0}",
        "-s",
        params.state or "OK",
        "-n",
        params.servicename or "Extension Starter Pack by Paulo Santana - Active Check",
    )

    # Yield an ActiveCheckCommand with the service description and command arguments.
    yield ActiveCheckCommand(service_description=params.service_description, command_arguments=args)

# Define the active check configuration using ActiveCheckConfig.
# This includes the name of the check, the parameter parser, and the command generation function.
active_check_esp_ps_active_check = ActiveCheckConfig(
    name="esp_ps_active_check",
    parameter_parser=EspPsParams.model_validate,
    commands_function=generate_esp_ps_commands,
)
