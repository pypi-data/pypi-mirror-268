import requests

# disables warnings from the unverified HTTPS requests
requests.packages.urllib3.disable_warnings()

from washpy.device_user import DeviceUser
from washpy.authenticate import authenticate
from washpy.post_new_password import post_new_password


if __name__ == "__main__":
    print("Hello World!")
