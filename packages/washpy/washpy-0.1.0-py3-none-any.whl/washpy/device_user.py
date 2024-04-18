from typing import Any, Dict, Final, Optional, Union
import requests

import datetime
import isodate

from washpy.authenticate import authenticate
from washpy.status import *


class DeviceUser:
    """
    device_url: e.g. 'https://192.168.1.251/Devices/000116343328'

    token: a bearer-token, used for authenticating a user with a device at every other XKM API endpoint
    """

    device_url: str
    user: Final[str]
    password: Final[str]
    token: str
    timeout: datetime.timedelta
    last_used: datetime.datetime

    def __init__(self, device_url: str, user: str, password: str) -> None:
        """
        device_url: e.g. 'https://192.168.1.251/Devices/000116343328'

        user: a username

        password: the password of user

        Authenticates the user at the specified machine
        """
        self.user = user
        self.password = password
        self.device_url = device_url
        self.last_used = datetime.datetime.now()
        (self.token, self.timeout) = authenticate(
            self.device_url, self.user, self.password
        )

    def __repr__(self) -> str:
        return (
            f"DeviceUser(device_url='{self.device_url}', "
            f"user='{self.user}', "
            f"password='~~ HIDDEN ~~', "
            f"token='{self.token}', "
            f"timeout={self.timeout.__repr__()}, "
            f"last_used={self.last_used.__repr__()}) "
        )

    def _do_get_request(self, api_endpoint: str) -> Dict[str, Any]:
        """
        queries the api_endpoint, e.g. the `/State` endpoint, of the machine.

        returns: the body of the response as an unpacked json object

        raises: ValueError, if the authentication was unsuccessfull
        """
        url = self.device_url + api_endpoint

        payload = {}
        headers = {"Authorization": f"Bearer {self.token}"}

        now = self.refresh_authentication()
        response = requests.request(
            "GET", url, headers=headers, data=payload, verify=False
        )

        if response.status_code != 200:
            raise ValueError(f"Unable to authenticate: got HTTP response {response}")
        self.last_used = now
        return response.json()

    def refresh_authentication(self) -> datetime.datetime:
        """
        if self.token is only valid for less then 10 seconds
        or if it is invalid,
        refresh it.

        returns: the point in time at which the check has happened
        """
        now = datetime.datetime.now()
        token_valid_date = self.last_used + self.timeout
        if now > token_valid_date - datetime.timedelta(seconds=10):
            (self.token, self.timeout) = authenticate(
                self.device_url, self.user, self.password
            )
            self.last_used = now
        return now

    def get_State(self) -> Dict[str, Any]:
        """
        queries the `/State` endpoint.

        returns: a complete json state of the machine

        raises: ValueError, if the authentication was unsuccessfull
        """
        return self._do_get_request("/State")

    def get_Status(self) -> Status:
        """
        queries the `/State` endpoint.

        returns: the status of the machine

        raises: ValueError, if the authentication was unsuccessfull
        """

        response = self._do_get_request("/State")
        return status_from_code(response["Status"])

    def get_ProgramPhase(self, verify_preconditions: bool = True) -> Optional[int]:
        """
        queries the `/State` endpoint.

        `verify_preconditions`: default: `True`. If set to `False`, the method does not verify, if
        the machine has the correct status. This might be desirable, if each request to the machine
        takes a significant amount of time; the lack of status validation omits one request.

        returns:
            - ProgramPhase, a device specific 16 bit integer denoting the program phase
            - `None`, if the machine is not in the RUNNING state.

        raises: ValueError, if the authentication was unsuccessfull
        """

        if verify_preconditions and self.get_Status() != Status.RUNNING:
            return None

        return int(self._do_get_request("/State")["ProgramPhase"])

    def get_pRemainingTime(
        self, verify_preconditions: bool = True
    ) -> Optional[Union[isodate.Duration, datetime.timedelta]]:
        """
        queries the `/State` endpoint.

        `verify_preconditions`: default: `True`. If set to `False`, the method does not verify, if
        the machine has the correct status. This might be desirable, if each request to the machine
        takes a significant amount of time; the lack of status validation omits one request.

        returns:
            - pRemainingTime, the remaining time of the currently active program.
            - `None`, if the machine is not in the RUNNING state, or if the returned date from the machine is not valid.

        raises: ValueError, if the authentication was unsuccessfull
        """

        if verify_preconditions and self.get_Status() != Status.RUNNING:
            return None

        pRemainingTimeStr: str = self._do_get_request("/State")["pRemainingTime"]
        try:
            pRemainingTime: isodate.Duration = isodate.parse_duration(pRemainingTimeStr)
            return pRemainingTime
        except:
            return None

    def get_pElapsedTime(
        self, verify_preconditions: bool = True
    ) -> Optional[Union[isodate.Duration, datetime.timedelta]]:
        """
        queries the `/State` endpoint.

        `verify_preconditions`: default: `True`. If set to `False`, the method does not verify, if
        the machine has the correct status. This might be desirable, if each request to the machine
        takes a significant amount of time; the lack of status validation omits one request.

        returns:
            - pElapsedTime, the elapsed time of the currently active program.
            - `None`, if the machine is not in the
              RUNNING, PAUSE, END_PROGRAMMED, FAILURE, or PROGRAMME_INTERRUPTED state,
              or if the returned date from the machine is not valid.


        raises: ValueError, if the authentication was unsuccessfull
        """

        if verify_preconditions and self.get_Status() not in {
            Status.RUNNING,
            Status.PAUSE,
            Status.END_PROGRAMMED,
            Status.FAILURE,
            Status.PROGRAMME_INTERRUPTED,
        }:
            return None

        pElapsedTimeStr: str = self._do_get_request("/State")["pElapsedTime"]
        try:
            pElapsedTime: isodate.Duration = isodate.parse_duration(pElapsedTimeStr)
            return pElapsedTime
        except:
            return None

    def get_pSystemTime(self) -> datetime.datetime:
        """
        queries the `/State` endpoint

        returns: the pSystemTime

        raises: ValueError, if the authentication was unsuccessfull
        """

        pSystemTimeStr: str = self._do_get_request("/State")["pSystemTime"]
        return isodate.parse_datetime(pSystemTimeStr)
