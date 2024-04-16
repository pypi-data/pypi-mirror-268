import os
from datetime import datetime

import requests
import json
import time
import logging

from typing import Tuple, Dict, Any

from requests import Response
from http import HTTPStatus

from guardian_client.python.credentials import GuardianClientCredentialContext

logger = logging.getLogger("GUARDIAN_CLIENT")


class GuardianAPIClient:
    """
    Client for Guardian API
    """

    def __init__(
        self,
        base_url: str,
        scan_endpoint: str = "scans",
        api_version: str = "v1",
        log_level: str = "INFO",
    ) -> None:
        """
        Initializes the Guardian API client.
        Args:
            base_url (str): The base URL of the Guardian API.
            scan_endpoint (str, optional): The endpoint for scanning. Defaults to "scans".
            api_version (str, optional): The API version. Defaults to "v1".
            log_level (str, optional): The log level. Defaults to "INFO".
        Raises:
            ValueError: If the log level is not one of "DEBUG", "INFO", "ERROR", or "CRITICAL".
        """
        self.endpoint = f"{base_url.rstrip('/')}/{api_version}/{scan_endpoint}"
        log_string_to_level = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

        log_level_enum = log_string_to_level.get(log_level.upper(), logging.INFO)
        logging.basicConfig(
            level=log_level_enum,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

        # client credential context is tied to a client instance.
        # In it's current state, a new client instance is created on each new call
        # to the guardian scanner, so a new context (and consequently a token)
        # is created for each scan request.
        self._access_token_context = GuardianClientCredentialContext()

    def scan(self, model_uri: str, poll_interval_secs: int = 5) -> Dict[str, Any]:
        """
        Submits a scan request for the given URI and polls for the scan status until it is completed.

        Args:
            uri (str): The URI to be scanned.
            poll_interval_secs (int, optional): The interval in seconds to poll for the scan status. Defaults to 5.

        Returns:
            dict: A dictionary containing the HTTP status code and the scan status JSON.
                  If an error occurs during the scan submission or polling, the dictionary
                  will also contain the error details.
        """
        logging.info(f"Submitting scan for {model_uri}")

        headers = {
            "Authorization": f"Bearer {self._access_token_context.access_token}",
        }
        response = requests.post(
            self.endpoint,
            json={"model_uri": model_uri},
            headers=headers,
        )
        if response.status_code != HTTPStatus.ACCEPTED:
            return {
                "http_status_code": response.status_code,
                "error": self._decode_error(response),
            }

        logging.info(
            f"Scan submitted successfully for {model_uri} with status_code: {response.status_code}"
        )

        response_json = response.json()
        id = response_json["id"]

        # Polling
        scan_status_json = None
        status_response = None

        logging.info(f"Polling for scan status for {id} for {model_uri}")
        while True:
            # reload header to check if token is still valid during this processing.
            headers = {
                "Authorization": f"Bearer {self._access_token_context.access_token}",
            }

            status_response = requests.get(
                url=f"{self.endpoint}/{id}",
                headers=headers,
            )
            if status_response.status_code == HTTPStatus.OK:
                scan_status_json = status_response.json()
                if scan_status_json["status"] not in ["IN_PROGRESS", "ACCEPTED"]:
                    break
            else:
                return {
                    "http_status_code": status_response.status_code,
                    "error": self._decode_error(status_response),
                }

            logger.debug(
                f"Scan status for {id} is {scan_status_json['status']}. Sleeping for 5 seconds before next check"
            )
            time.sleep(poll_interval_secs)  # Wait for 5 seconds before next check

        logging.info(f"Scan complete for {id} for {model_uri}")

        return {
            "http_status_code": (
                status_response.status_code if status_response else None
            ),
            "scan_status_json": scan_status_json,
        }

    def evaluate(
        self,
        status_json: Dict[str, Any],
        threshold: str = "CRITICAL",
        block_on_scan_errors: bool = False,
    ) -> Tuple[str, bool]:
        """
        Evaluates the status of a scan based on the provided status JSON.

        Args:
            status_json (object): The status JSON object containing scan information obtained from scan method.
            threshold (str, optional): The threshold level to consider for blocking. Defaults to "CRITICAL".
            block_on_scan_errors (bool, optional): Whether to block if there are errors in scanning. Defaults to False.

        Returns:
            Tuple[str, bool]: A tuple containing the evaluation result message and a boolean indicating if blocking is required.
        """
        if status_json["status"] != "FINISHED":
            return "Scan was in-complete or failed", True

        if block_on_scan_errors and status_json["scan_summary"]["total_errors"] > 0:
            return (
                "Blocked due to errors in scanning. This could indicate an issue with the model itself",
                True,
            )

        thresholds = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        threshold = threshold.upper() if threshold else "CRITICAL"
        if threshold not in thresholds:
            raise ValueError(f"Threshold must be one of {thresholds}")

        issues = 0
        for t in thresholds[thresholds.index(threshold) :]:
            issues += status_json["scan_summary"]["issue_counts"][t]

        if issues > 0:
            return (
                f"Blocked due to {issues} issues at or above {threshold} in the model",
                True,
            )

        return "", False

    def _decode_error(self, response: Response) -> str:
        try:
            response_json = response.json()
            if "detail" in response_json and response_json["detail"]:
                if isinstance(response_json["detail"], list):
                    concat_msg = ""
                    for item_ in response_json["detail"]:
                        concat_msg += f"- {item_['msg']}\n"
                    return concat_msg
                elif isinstance(response_json["detail"], str):
                    return response_json["detail"]

            return "Unknown error"
        except json.JSONDecodeError:
            return "Response is not in JSON format"
