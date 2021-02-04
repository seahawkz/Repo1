import json, urllib3, certifi, requests, barcode
from PIL import Image
from barcode.writer import ImageWriter
from io import BytesIO
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
from retryer import requests_retry_session


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_partial(login):
    try:
        site = 'https://fclm-portal.amazon.com/ajax/partialEmployeeSearch'
        param = f"?term={login}"
        url = site + param
        with requests_retry_session() as req:
            resp = req.get(url,
                           timeout=30,
                           verify=False,
                           allow_redirects=True,
                           auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL))

            if resp.status_code == 200:
                employee_info = json.loads(resp.text)["value"]
                return employee_info

                # if len(json.loads(resp.text)["value"]) > 1:
                # employee_info = json.loads(resp.text)["value"][0]

            else:
                return resp.raise_for_status()
    except Exception as e:
        return e


def get_full(login):
    try:
        site = "https://hrwfs.amazon.com/"
        params = f'?Operation=empInfoByUid&ContentType=JSON&employeeUid={login}'
        url = site + params
        with requests_retry_session() as req:
            resp = req.get(url,
                           timeout=30,
                           verify=False,
                           allow_redirects=True,
                           auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL))
            if resp.status_code == 200:
                employee_info = json.loads(resp.text)['empInfoByUidResponse']['empInfoByUidResult']
                return employee_info
            else:
                return resp.raise_for_status()

    except Exception as e:
        return e


def set_image(emp_id, filename):
    try:
        site = "https://internal-cdn.amazon.com/badgephotos.amazon.com/"
        param = f'?uid={emp_id}'
        url = site + param

        response = requests.get(url, verify=False, allow_redirects=True,
                                auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL))
        im = Image.open(BytesIO(response.content))
        im.save(filename)
    except Exception as e:
        return e


class ImageWithoutTextWriter(ImageWriter):
    def _paint_text(self, xpos, ypos):
        pass


def set_barcode(badge_id, filename):
    try:
        barcode_type = 'ean8'
        this_barcode = barcode.get(barcode_type, badge_id, writer=ImageWithoutTextWriter())
        options = {'module_width': 0.15, 'quiet_zone': 2.5}
        file = this_barcode.save(filename, options=options)
    except Exception as e:
        return e


#def get_all(login):
#    badge = get_req(login)
#    image = get_image(badge['employeeLogin'])
#    barcode_image(badge['employeeId'])
#    return badge, image


# Depreciated function
# def badge_number(login: str) -> str:
#
#     """
#         :param login: login string.
#         :return badge: badge string.
#     """
#
#     with requests_retry_session() as req:
#         resp = req.get(url,
#                        timeout=30,
#                        verify=False,
#                        allow_redirects=True,
#                        auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL))
#
#         if resp.status_code == 200:
#             badge = json.loads(resp.text)["value"][0]["badgeBarcodeId"]
#             return badge
#
#         else:
#             print(resp.raise_for_status())

