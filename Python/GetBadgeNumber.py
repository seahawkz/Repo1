import json

import urllib3
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
import Python.Swagger.retryer
from Python.Swagger.retryer import requests_retry_session


def badge_number(login: str) -> str:

    """
        :param login: login string.
        :return badge: badge string.
    """

    url = f"https://fclm-portal.amazon.com/ajax/partialEmployeeSearch?term={login}"

    with requests_retry_session() as req:
        resp = req.get(url,
                       timeout=30,
                       verify=False,
                       allow_redirects=True,
                       auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL))

        if resp.status_code == 200:

            badge = json.loads(resp.text)["value"][0]["badgeBarcodeId"]

            return badge

        else:
            print(resp.raise_for_status())