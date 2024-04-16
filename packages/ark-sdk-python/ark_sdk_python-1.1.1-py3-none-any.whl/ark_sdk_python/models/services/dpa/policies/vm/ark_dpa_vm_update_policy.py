from typing import List, Optional

from pydantic import Field, validator

from ark_sdk_python.models.common import ArkWorkspaceType
from ark_sdk_python.models.services.dpa.policies.common.ark_dpa_base_update_policy import ArkDPABaseUpdatePolicy
from ark_sdk_python.models.services.dpa.policies.vm.ark_dpa_vm_authorization_rule import ArkDPAVMAuthorizationRule
from ark_sdk_python.models.services.dpa.policies.vm.ark_dpa_vm_policies_workspace_type_serializer import (
    serialize_dpa_vm_policies_workspace_type,
)
from ark_sdk_python.models.services.dpa.policies.vm.ark_dpa_vm_providers import ArkDPAVMProvidersDict


class ArkDPAVMUpdatePolicy(ArkDPABaseUpdatePolicy):
    providers_data: Optional[ArkDPAVMProvidersDict] = Field(description='New cloud providers to update')
    user_access_rules: Optional[List[ArkDPAVMAuthorizationRule]] = Field(description='New access rules to update')

    # pylint: disable=no-self-use,no-self-argument
    @validator('providers_data', pre=True)
    def validate_providers_data(cls, val):
        if val is not None:
            for k in val.keys():
                if isinstance(val[k], dict):
                    val[k]['providerName'] = serialize_dpa_vm_policies_workspace_type(ArkWorkspaceType(k))
                else:
                    val[k].provider_name = serialize_dpa_vm_policies_workspace_type(ArkWorkspaceType(k))
                if ArkWorkspaceType(k) not in [ArkWorkspaceType.AWS, ArkWorkspaceType.AZURE, ArkWorkspaceType.GCP, ArkWorkspaceType.ONPREM]:
                    raise ValueError('Invalid Platform / Workspace Type')
        return val
