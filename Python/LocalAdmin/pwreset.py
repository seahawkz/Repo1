
import json
import boto3
import string
import random


def random_pass():
    length = 20
    schar = '!@#$%&*+=?'
    all = string.ascii_letters + string.digits + schar
    temp = "".join(random.sample(all, length))

    return(temp)


def put_secret(paramer_name, parameter_value):
    ssm = boto3.client('ssm')
    ssm.put_parameter(
        Name=paramer_name,
        Value=parameter_value,
        Type='SecureString',
        Overwrite=True
    )


secrets = {
    "tcc-linux-local-admin": random_pass(),
}

for parameter_name, parameter_value in secrets.items():
    put_secret(parameter_name, parameter_value)

username = 'tccadmin'

ssm = boto3.client('ssm')
FIOS_PARAMETER = ssm.get_parameter(
    Name="tcc-linux-local-admin", WithDecryption=True)
FIOS_PASSWORD = FIOS_PARAMETER['Parameter']['Value']

ssm.send_command(
    InstanceIds=['mi-008866d675d8fc47b', 'i-0f9e31661f2b8b039', 'mi-06e9ee72df01dcb2f',
                 'mi-08fcfbc61097878ae', 'mi-0b88e90f5dbae498e', 'mi-0c708ace0fca826b2', 'mi-08c8a9d7c7dd43da8'],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': ['echo ' + "'" + FIOS_PASSWORD + "'" + ' | passwd --stdin ' + username]}, )


def localAdmin(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Passwords have been reset!')
    }
