import getpass
import socket

import urllib.error
import urllib.request
import paramiko
import netmiko

import cisco_or_commodity_device
import fqdn_sanitizer


class ConnectionToDevice:

    def __init__(self, device_hostname, log, prelenel, user_password):
        self.device_fqdn = fqdn_sanitizer.returns_fqdn(device_hostname)
        self.device_hostname = fqdn_sanitizer.returns_hostname(device_hostname)
        self.session_log = log
        self.prelenel = prelenel
        self.user_password = user_password
        self.device_ssh_parameters = {"device_type": None,
                                      "host": None,
                                      "username": None,
                                      "password": None,
                                      "secret": None}

    def do_nslookup_on_hostname(self):
        try:
            self.device_ssh_parameters["host"] = socket.gethostbyname(self.device_fqdn)
            return True
        # DNS resolution failure due to management interface or device itself not being created in NARF.
        except socket.gaierror:
            self.session_log.exception(
                f"{self.device_hostname} does not exist or does not have a management interface created in NARF.")
            return False

    def determine_device_platform(self):
        self.device_ssh_parameters["device_type"] = cisco_or_commodity_device.\
            determine_device_platform(self.device_fqdn, self.session_log)

    def determine_ssh_session_username_and_credentials(self):
        if not self.prelenel:
            self.device_ssh_parameters["username"] = getpass.getuser()
            self.device_ssh_parameters["password"] = self.user_password
            self.device_ssh_parameters["secret"] = self.user_password
        else:
            url = f"https://narf.amazon.com/device/{self.device_fqdn}/pre_lenel"
            try:
                # Fetches pre-lenel password for host in URL.
                self.device_ssh_parameters["password"] = urllib.request.urlopen(url).read().decode("ASCII")
                self.device_ssh_parameters["secret"] = self.device_ssh_parameters["password"]
            except urllib.error.HTTPError:  # Failed to retrieve pre-lenel password.
                self.session_log.error(f"Failed to retrieve pre-lenel password for {self.device_hostname}.")
            if "rsw" in self.device_hostname or "fc-ics-sw" in self.device_hostname \
                    or self.device_ssh_parameters["device_type"] == "ubiquiti_edge":
                self.device_ssh_parameters["username"] = "admin"
            else:
                self.device_ssh_parameters["username"] = "local-tech"

    def validate_ssh_session_dictionary_is_populated(self):
        if None in self.device_ssh_parameters.values():
            for key in sorted(self.device_ssh_parameters.keys()):
                if self.device_ssh_parameters.get(key) is None:
                    self.session_log.error(f"Parameter {key} not retrieved properly for {self.device_hostname}. "
                                           f"Unable to attempt SSH connection.")
            return False
        else:
            return True

    def establish_connection_to_device(self):
        if self.do_nslookup_on_hostname():
            self.determine_device_platform()
            self.determine_ssh_session_username_and_credentials()
            if self.validate_ssh_session_dictionary_is_populated():
                try:
                    connection_to_device = netmiko.ConnectHandler(**self.device_ssh_parameters)
                    self.session_log.info(f"Connection established to {self.device_hostname}.")
                    return connection_to_device
                except netmiko.ssh_exception.NetMikoTimeoutException:
                    self.session_log.exception(f"{self.device_hostname} is unreachable.")
                    return None
                except netmiko.ssh_exception.NetMikoAuthenticationException or paramiko.ssh_exception.AuthenticationException:
                    self.session_log.exception(f"Cannot SSH into {self.device_hostname} due to incorrect credentials.")
                    return None
                except ValueError:
                    self.session_log.exception(f"Device platform is not recognized."
                                               f"This error will populate if DNS resolution failed for {self.device_fqdn}")
                    return None
