import argparse
from datetime import date
import getpass

import cisco_or_commodity_device
import fqdn_sanitizer
import logger
import ssh_session


WRITE_MEM_LOG = logger.logging_session_creator("write_memory.py")


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", required=True,
                        help="Filename with list of devices to have their configs saved. MUST end in .txt extension."
                             "Ex: --filename bfi1.txt")
    return parser.parse_args()


def connect_to_device_and_write_mem(device, WRITE_MEM_LOG, user_password):
    connection_to_device = ssh_session.ConnectionToDevice(device, WRITE_MEM_LOG, False, user_password).establish_connection_to_device()
    connection_to_device.open_session_log(filename=f"write_mem-{date.today()}.txt", mode="append")
    connection_to_device.enable()
    if cisco_or_commodity_device.determine_device_platform(fqdn_sanitizer.returns_fqdn(device), WRITE_MEM_LOG) == "cisco_ios":
        connection_to_device.send_command("write mem")
        WRITE_MEM_LOG.info(f"{device}'s running-config successfully saved to startup.")
    elif cisco_or_commodity_device.determine_device_platform(fqdn_sanitizer.returns_fqdn(device), WRITE_MEM_LOG) == "ubiquiti_edge":
        command_output = connection_to_device.send_command_timing("write memory")
        if "Are you sure you want to save? (y/n)" in command_output:
            connection_to_device.send_command_timing("y")
    else:
        WRITE_MEM_LOG.warning(f"{device}'s running-config NOT saved to startup.")
    connection_to_device.disconnect()


def main():
    user_arguments = argument_parser()
    user_password = getpass.getpass(prompt="Password: ", stream=None)
    with open(f"{user_arguments.filename}", "r") as file:
        for device in file:
            connect_to_device_and_write_mem(device.rstrip(), WRITE_MEM_LOG, user_password)
main()
