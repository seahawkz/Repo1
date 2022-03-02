
import subprocess
import crypt
import boto3

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')
ssm = boto3.client('ssm')
FIOS_PARAMETER = ssm.get_parameter(
    Name="tcc-linux-local-admin", WithDecryption=True)
FIOS_PASSWORD = FIOS_PARAMETER['Parameter']['Value']

encPass = crypt.crypt(FIOS_PASSWORD)
username = 'tccadmin'


def adduser():
    subprocess.run(['sudo', 'useradd', '-m', '-p', encPass, username])

    file = open("/etc/sudoers.d/tccadmin", "w")
    file.write("tccadmin  ALL=(ALL) NOPASSWD:ALL")
    file.close()

    print('The user', username, 'was created.')


def change_passwd():
    subprocess.run(['sudo', 'usermod', '-p', encPass, username])


getUsers = open("/etc/passwds", "r")
flag = 0

for line in getUsers:
    if username in line:
        flag = 1
        break

if flag == 0:
    adduser()
else:
    change_passwd()

getUsers.close()
