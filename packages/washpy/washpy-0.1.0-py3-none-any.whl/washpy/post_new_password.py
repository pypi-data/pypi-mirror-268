import requests
import json


def post_new_password(
    device_url: str, user: str, password_old: str, password_new: str
) -> None:
    """
    device_url: e.g. 'https://192.168.1.251/Devices/000116343328'

    user: e.g. 'MYUSER'

    password_old: old password

    password_new: the new password to be set

    raises: ValueError, if the password change was unsuccessfull
    """
    payload = json.dumps(
        {"LoginName": user, "Password": password_old, "PasswordNew": password_new}
    )
    headers = {"Content-Type": "application/json"}

    response = requests.request(
        "POST", device_url, headers=headers, data=payload, verify=False
    )
    if response.status_code != 200:
        raise ValueError(f"something went wrong: got HTTP response {response}")
