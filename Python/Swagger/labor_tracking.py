import json
import os
import pandas as pd
import lxml
from bs4 import BeautifulSoup
import urllib3
import PySimpleGUI as sg
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
from retryer import requests_retry_session

fc = "BFI7"
req = requests_retry_session()
urllib3.disable_warnings()


def get_tasks():

    return tasks


def badge_id(login):
    url = 'https://fclm-portal.amazon.com/ajax/partialEmployeeSearch?term=' + login
    resp = req.post(url, auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL), verify=False)
    barcode = json.loads(resp.text)['value'][0]['badgeBarcodeId']
    return barcode


def task_change(badge, task):
    url = 'http://fcmenu-dub-regionalized.corp.amazon.com/do/laborTrackingKiosk'
    payload = {'trackingBadgeId': badge, 'calmCode': task, 'warehouseId': fc}
    resp = req.post(url, auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL), params=payload, verify=False)
    print(resp.text)


actions = ['Employee ID', 'Badge RFID', 'Supervisor Name']


combo_1 = sg.Combo(actions, key='combo_1', size=(30, 1), default_value=actions[0])
text_1 = sg.Text("Login")
input_1 = sg.InputText('', key='input_1', size=(30, 1))
submit_1 = sg.Button('Submit')
output_1 = sg.Output(size=(30, 1))


layout = [[combo_1], [text_1, input_1, submit_1], [output_1]]


window = sg.Window('Badge Number', layout, keep_on_top=True)


if __name__ == "__main__":
    while True:  # Event Loop
        event, values = window.Read()

        if event is 'Submit':

            task_change("ICQALQA")