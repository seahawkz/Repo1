import urllib.error
import urllib.request


def retrieve_narf_generated_config(device_fqdn, session_log):
    try:
        narf_generated_config_for_device = urllib.request. \
            urlopen(f"https://narf.amazon.com/device/{device_fqdn}/config").read().decode("ASCII")
        return narf_generated_config_for_device
    except urllib.error.HTTPError as error:  # Failed to retrieve NARF config.
        session_log.error(error)
        session_log.error(f"Unable to retrieve NARF-generated config for {device_fqdn}.")


def determine_device_platform(device_fqdn, session_log):
    narf_generated_config_for_device = retrieve_narf_generated_config(device_fqdn, session_log)
    if narf_generated_config_for_device is not None:
        if "vtp" not in narf_generated_config_for_device:
            return "ubiquiti_edge"
        else:
            return "cisco_ios"


