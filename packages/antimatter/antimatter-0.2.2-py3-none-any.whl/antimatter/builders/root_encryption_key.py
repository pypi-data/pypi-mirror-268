
import base64

from typing import List

from antimatter.client import (
    AWSServiceAccountKeyInfo, GCPServiceAccountKeyInfo, AntimatterDelegatedAWSKeyInfo, KeyInfosKeyInformation,
    KeyInfos
)

class OverrideKeyInfosKeyInformation(KeyInfosKeyInformation):
    one_of_schemas: List[str] = ["AWSServiceAccountKeyInfo", "AntimatterDelegatedAWSKeyInfo", "GCPServiceAccountKeyInfo"]


def aws_service_account_key_info(access_key_id: str, secret_access_key: str, key_arn: str) -> KeyInfos:
    """
    Create a KeyInfos object with AWS service account key information

    Example usage:
    ```
    key_info = aws_service_account_key_info(
        access_key_id="access_key_id", secret_access_key="secret_access_key", key_arn="key_arn"
    )
    ```

    :param access_key_id: The access key ID
    :param secret_access_key: The secret access key
    :param key_arn: The key ARN

    :return: A KeyInfos object with the specified key information
    """
    return KeyInfos(
        keyInformation=OverrideKeyInfosKeyInformation(
            actual_instance=AWSServiceAccountKeyInfo(
                access_key_id=access_key_id, secret_access_key=secret_access_key, key_arn=key_arn, provider_name="aws_sa"
            )
        )
    )

def antimatter_delegated_aws_key_info(key_arn: str) -> KeyInfos:
    """
    Create a KeyInfos object with Antimatter delegated AWS key information

    Example usage:
    ```
    key_info = antimatter_delegated_aws_key_info(key_arn="key_arn")
    ```

    :param key_arn: The key ARN

    :return: A KeyInfos object with the specified key information
    """
    return KeyInfos(
        keyInformation=OverrideKeyInfosKeyInformation(
            actual_instance=AntimatterDelegatedAWSKeyInfo(key_arn=key_arn, provider_name="aws_am"),
        )
    )

def gcp_service_account_key_info(
        project_id: str, location: str, key_ring_id: str, key_id: str,
        service_account_credentials: str = "",
        service_account_credentials_path: str = ""
    ) -> KeyInfos:
    """
    Create a KeyInfos object with GCP service account key information

    Example usage:
    ```
    key_info = gcp_service_account_key_info(
        project_id="project_id", location="location",
        key_ring_id="key_ring_id", key_id="key_id",
        service_account_credentials="<service_account_credentials_as_json_string>", 
        service_account_credentials_path="/path/to/service_account_credentials.json"
    )
    ```
    Either `service_account_credentials` or `service_account_credentials_path` should be provided.

    :param project_id: The project ID
    :param location: The location
    :param key_ring_id: The key ring ID
    :param key_id: The key ID
    :param service_account_credentials: The service account credentials as JSON string
    :param service_account_credentials_path: The path to the service account credentials

    :return: A KeyInfos object with the specified key information
    """
    if not service_account_credentials and not service_account_credentials_path:
        raise ValueError("Either service_account_credentials or service_account_credentials_path should be provided")

    if service_account_credentials and service_account_credentials_path:
        raise ValueError("Only one of service_account_credentials or service_account_credentials_path should be provided")
    
    encoded_service_account_credentials = None
    if service_account_credentials_path:
        with open(service_account_credentials_path, "r") as f:
            encoded_service_account_credentials = base64.b64encode(f.read().encode()).decode('utf-8')

    if service_account_credentials:
        encoded_service_account_credentials = base64.b64encode(service_account_credentials.encode()).decode('utf-8')

    return KeyInfos(
        keyInformation=OverrideKeyInfosKeyInformation(
            actual_instance=GCPServiceAccountKeyInfo(
                service_account_credentials=encoded_service_account_credentials, project_id=project_id, location=location,
                keyring_id=key_ring_id, key_id=key_id, provider_name="gcp_sa"
            )
        )
    )
