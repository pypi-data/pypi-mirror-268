import copy
import json
from typing import Annotated, Any, Callable, Literal, TypeVar, Union, cast
from urllib.parse import urljoin

import click
import requests
from gable.openapi import (
    CheckComplianceDataAssetsPySparkRequest,
    CheckComplianceDataAssetsTypeScriptRequest,
    CheckDataAssetCommentMarkdownResponse,
    CheckDataAssetDetailedResponse,
    CheckDataAssetErrorResponse,
    CheckDataAssetMissingAssetResponse,
    CheckDataAssetNoContractResponse,
    ErrorResponse,
    ErrorResponseDeprecated,
    GetNpmCredentialsResponse,
    IngestDataAssetResponse,
    RegisterDataAssetPySparkRequest,
    RegisterDataAssetTypeScriptRequest,
    ResponseType,
)
from loguru import logger
from pydantic import Field, parse_obj_as

T = TypeVar("T")

# Discriminated union for the response from the /data-assets/check endpoint
CheckDataAssetDetailedResponseUnion = Annotated[
    Union[
        CheckDataAssetDetailedResponse,
        CheckDataAssetErrorResponse,
        CheckDataAssetNoContractResponse,
        CheckDataAssetMissingAssetResponse,
    ],
    Field(discriminator="responseType"),
]


class GableClient:
    def __init__(self, endpoint: str, api_key: str) -> None:
        self.endpoint = endpoint
        self.api_key = api_key
        self.ui_endpoint = endpoint.replace("api-", "", 1).replace("api.", "", 1)

    def _validate_api_key(self):
        if not self.api_key:
            raise click.ClickException(
                "API Key is not set. Use the --api-key argument or set GABLE_API_KEY "
                "environment variable."
            )

    def _validate_endpoint(self):
        if not self.endpoint:
            raise click.ClickException(
                "API Endpoint is not set. Use the --endpoint or set GABLE_API_ENDPOINT "
                "environment variable."
            )
        if not self.endpoint.startswith("https://"):
            if not self.endpoint.startswith("http://localhost"):
                raise click.ClickException(
                    f"Gable API Endpoint must start with 'https://'. Received: {self.endpoint}"
                )

    def _get(
        self, path: str, **kwargs: Any
    ) -> tuple[Union[list[Any], dict[str, Any]], bool, int]:
        return self._request(path, method="GET", **kwargs)

    def _post(
        self, path: str, **kwargs: Any
    ) -> tuple[Union[list[Any], dict[str, Any]], bool, int]:
        return self._request(path, method="POST", **kwargs)

    def _request(
        self,
        path: str,
        method: Literal["GET", "POST", "DELETE"],
        log_payload_filter: Callable = lambda json_payload: json_payload,
        **kwargs: Any,
    ) -> tuple[Union[list[Any], dict[str, Any]], bool, int]:
        self._validate_api_key()
        self._validate_endpoint()
        url = urljoin(self.endpoint, path)

        # Filter the JSON payload to remove spammy/secret request data
        kwargs_copy = copy.deepcopy(kwargs)
        if "json" in kwargs_copy:
            kwargs_copy["json"] = log_payload_filter(kwargs_copy["json"])

        logger.debug(f"{method} {url}: {kwargs_copy}")

        headers = {"X-API-KEY": self.api_key, "Content-Type": "application/json"}

        try:
            response = requests.request(method, url, headers=headers, **kwargs)
        except requests.exceptions.ConnectionError as e:
            raise click.ClickException(
                f"Failed to connect to Gable API at {self.endpoint}: {e}"
            )
        except requests.exceptions.RequestException as e:
            raise click.ClickException(
                f"Error making request to Gable API at {self.endpoint}: {e}"
            )

        # Log the response
        logger.debug(
            f"{'OK' if response.ok else 'ERROR'} ({response.status_code}): {response.text}"
        )

        # Check for missing api key
        if response.status_code == 403:
            raise click.ClickException("Invalid API Key")

        # Try parsing the response as JSON
        try:
            parsed_response = response.json()
        except json.JSONDecodeError:
            raise click.ClickException(
                f"Unable to parse server response as JSON: {response.text}"
            )

        return (
            cast(dict[str, Any], parsed_response),
            response.status_code == 200,
            response.status_code,
        )

    def get_data_asset_infer_contract(
        self,
        data_asset_id: str,
    ) -> tuple[dict[str, Any], bool, int]:
        """Use the infer contract endpoint to generate a contract for a data asset"""
        response, success, status_code = self._get(
            f"v0/data-asset/{data_asset_id}/infer-contract"
        )
        return cast(dict[str, Any], response), success, status_code

    def get_auth_npm(self) -> GetNpmCredentialsResponse:
        """
        Get the NPM credentials for the current user
        """
        try:
            response, success, status_code = self._get("v0/auth/npm")
            response = GetNpmCredentialsResponse.parse_obj(response)
        except Exception as e:
            logger.opt(exception=e).debug("Error getting NPM credentials")
            raise click.ClickException(
                f"Error getting NPM credentials: {e}. Re-run with --debug for more information."
            )
        if not success:
            raise click.ClickException(
                f"Failed to get NPM credentials: ({status_code}) {response}"
            )
        return response

    def post_data_assets_check(self, request) -> Union[list[Any], dict[str, Any]]:
        result, _success, _status_code = self._post(
            "v0/data-assets/check",
            json=del_none(request),
        )
        return result

    def post_data_asset_ingest(self, request):
        result, success, status_code = self._post(
            "v0/data-asset/ingest",
            json=del_none(request),
        )
        return cast(dict[str, Any], result), success, status_code

    def post_data_asset_register_typescript(
        self, request: RegisterDataAssetTypeScriptRequest
    ):
        json_payload = request.dict(by_alias=True)

        # Convert the OpenAPI Enum string
        for asset in json_payload["assets"]:
            asset["library"] = asset["library"].value

        result, success, status_code = self._post(
            "v0/data-asset/register/typescript", json=json_payload
        )
        if isinstance(result, dict) and "registered" in result:
            response = IngestDataAssetResponse.parse_obj(result)
        else:
            response = ErrorResponseDeprecated.parse_obj(result)
        return (
            response,
            success,
            status_code,
        )

    def post_data_asset_register_pyspark(
        self, request: RegisterDataAssetPySparkRequest
    ) -> tuple[Union[IngestDataAssetResponse, ErrorResponseDeprecated], bool, int]:
        response, success, status_code = self._post(
            "v0/data-asset/register/pyspark",
            json=request.dict(by_alias=True),
        )
        if isinstance(response, dict) and "registered" in response:
            result = IngestDataAssetResponse.parse_obj(response)
        else:
            result = ErrorResponseDeprecated.parse_obj(response)
        return (
            result,
            success,
            status_code,
        )

    def post_data_asset_check_typescript(self, request):
        response, _success, _status_code = self._post(
            "v0/data-assets/check-compliance/typescript",
            json=request.json(),
        )
        if request.responseType == ResponseType.DETAILED:
            if isinstance(response, list):
                return [parse_check_data_asset_response(r) for r in response]
            return ErrorResponse.parse_obj(response)
        return parse_obj_as(CheckDataAssetCommentMarkdownResponse, response)

    def post_check_compliance_data_assets_pyspark(
        self, request: CheckComplianceDataAssetsPySparkRequest
    ) -> Union[
        ErrorResponse,
        CheckDataAssetCommentMarkdownResponse,
        list[CheckDataAssetDetailedResponseUnion],
    ]:
        response, _success, _status_code = self._post(
            "v0/data-assets/check-compliance/pyspark", data=request.json(by_alias=True)
        )
        if request.responseType == ResponseType.DETAILED:
            if isinstance(response, list):
                return [parse_check_data_asset_response(r) for r in response]
            else:
                return ErrorResponse.parse_obj(response)
        else:  # request.responseType == ResponseType.COMMENT_MARKDOWN:
            return parse_obj_as(CheckDataAssetCommentMarkdownResponse, response)

    def post_check_compliance_data_assets_typescript(
        self, request: CheckComplianceDataAssetsTypeScriptRequest
    ) -> Union[
        ErrorResponse,
        CheckDataAssetCommentMarkdownResponse,
        list[CheckDataAssetDetailedResponseUnion],
    ]:
        response, _success, _status_code = self._post(
            "v0/data-assets/check-compliance/typescript",
            data=request.json(by_alias=True),
        )
        if request.responseType == ResponseType.DETAILED:
            if isinstance(response, list):
                return [parse_check_data_asset_response(r) for r in response]
            else:
                return ErrorResponse.parse_obj(response)
        else:  # request.responseType == ResponseType.COMMENT_MARKDOWN:
            return parse_obj_as(CheckDataAssetCommentMarkdownResponse, response)

    def get_data_assets(self):
        return self._get("v0/data-assets")

    def get_pyping(self):
        return self._get("v0/pyping")

    def get_ping(self):
        return self._get("v0/ping")

    def post_contract_validate(self, request):
        return self._post("v0/contract/validate", data=request.json())

    def post_contract(self, request):
        return self._post("v0/contract", data=request.json())


def del_none(d):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.
    """
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


# Pylance was struggling to understand the union type when calling parse_obj_as
# I created this function to prevent a '# type ignore' annotation in the code
def parse_check_data_asset_response(response) -> CheckDataAssetDetailedResponseUnion:
    response_mapping = {
        "NO_CONTRACT": CheckDataAssetNoContractResponse,
        "DETAILED": CheckDataAssetDetailedResponse,
        "ERROR": CheckDataAssetErrorResponse,
        "MISSING_DATA_ASSET": CheckDataAssetMissingAssetResponse,
    }
    response_type = response["responseType"]
    if response_type in response_mapping:
        return parse_obj_as(response_mapping[response_type], response)
    raise ValueError(f"Unknown response type: {response_type} in response: {response}")
