def returns_fqdn(argparse_hostname_provided):
    if not argparse_hostname_provided.endswith(".amazon.com"):
        return '.'.join([argparse_hostname_provided, "amazon.com"])


def returns_hostname(argparse_hostname_provided):
    if argparse_hostname_provided.endswith(".amazon.com"):
        return argparse_hostname_provided[:len(argparse_hostname_provided)-11]
    else:
        return argparse_hostname_provided
