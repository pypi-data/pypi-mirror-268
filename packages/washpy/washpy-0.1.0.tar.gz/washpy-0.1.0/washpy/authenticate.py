from typing import Tuple
import datetime
import json
import requests


def authenticate(
    device_url: str, user: str, password: str
) -> Tuple[str, datetime.timedelta]:
    """
    device_url: e.g. 'https://192.168.1.251/Devices/000116343328'

    user: e.g. 'MYUSER'

    password e.g. 'verySecurePassword!'

    returns: a string, containing a bearer token, and a time duration for which the token is valid.
    If the token is used again within the valid time period, the valid time period is refreshed.

    raises: ValueError, if the authentication was unsuccessfull
    """
    url = device_url + "/profSession"

    payload = json.dumps({"LoginName": user, "Password": password})
    headers = {"Content-Type": "application/json"}

    response = requests.request(
        "POST", url, verify=False, headers=headers, data=payload
    )

    if response.status_code != 200:
        raise ValueError(f"Unable to authenticate: got HTTP response {response}")
    return (
        response.json()["SessionId"],
        datetime.timedelta(seconds=response.json()["Timeout"]),
    )
