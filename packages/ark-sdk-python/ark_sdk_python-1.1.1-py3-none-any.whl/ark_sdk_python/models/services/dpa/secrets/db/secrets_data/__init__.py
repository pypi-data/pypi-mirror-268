from typing import Union

from ark_sdk_python.models.services.dpa.secrets.db.secrets_data.ark_dpa_db_iam_user_secret_data import (
    ArkDPADBExposedIAMUserSecretData,
    ArkDPADBIAMUserSecretData,
)
from ark_sdk_python.models.services.dpa.secrets.db.secrets_data.ark_dpa_db_user_password_secret_data import (
    ArkDPADBExposedUserPasswordSecretData,
    ArkDPADBUserPasswordSecretData,
)

ArkDPADBSecretDataTypes = Union[ArkDPADBUserPasswordSecretData, ArkDPADBIAMUserSecretData]
ArkDPADBSecretExposedDataTypes = Union[ArkDPADBExposedUserPasswordSecretData, ArkDPADBExposedIAMUserSecretData]
