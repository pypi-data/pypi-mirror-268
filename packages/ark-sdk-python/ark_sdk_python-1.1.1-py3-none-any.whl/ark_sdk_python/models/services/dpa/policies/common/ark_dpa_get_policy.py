from typing import Optional

from pydantic import Field, root_validator

from ark_sdk_python.models import ArkModel


class ArkDPAGetPolicy(ArkModel):
    policy_id: Optional[str] = Field(description='Policy id to get')
    policy_name: Optional[str] = Field(description='Policy name to get')

    # pylint: disable=no-self-use,no-self-argument
    @root_validator
    def validate_either(cls, values):
        if 'policy_id' not in values and 'policy_name' not in values:
            raise ValueError('Either policy id or policy name needs to be provided')
        return values
