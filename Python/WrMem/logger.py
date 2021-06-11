import logging
import pathlib


def logging_session_creator(logger_name):
    session_log = logging.getLogger(logger_name)
    session_log.setLevel(logging.DEBUG)

    console_log_handler = logging.StreamHandler()
    console_log_handler.setLevel(logging.INFO)
    console_log_handler.setFormatter(logging.Formatter("%(name)s - %(message)s"))
    session_log.addHandler(console_log_handler)
    return session_log



# def logging_session_creator(device_hostname, logfile_filepath, logger_name):
#     session_log = logging.getLogger(logger_name)
#     session_log.setLevel(logging.DEBUG)
#
#     console_log_handler = logging.StreamHandler()
#     console_log_handler.setLevel(logging.INFO)
#     console_log_handler.setFormatter(logging.Formatter("%(name)s - %(message)s"))
#     session_log.addHandler(console_log_handler)
#
#     logfile_log_handler = logging.FileHandler(filename=(pathlib.Path(logfile_filepath / f"{device_hostname}.log")))
#     logfile_log_handler.setLevel(logging.DEBUG)
#     logfile_log_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
#     session_log.addHandler(logfile_log_handler)
#     return session_log
