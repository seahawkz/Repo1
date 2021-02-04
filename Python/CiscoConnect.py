from paramiko import client
from paramiko.ssh_exception import AuthenticationException
import threading
import time
import re
from .driver import Driver, DriverError

class sshMult:
    def __init__(self, target, username='', password='', port=22, auto_add_keys=True):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self._client = client.SSHClient()
        if auto_add_keys:
            self._client.set_missing_host_key_policy(client.AutoAddPolicy())
        self._streams = {
            'in': None,
            'out': None,
            'err': None
        }