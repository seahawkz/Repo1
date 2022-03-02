import os
import crypt

pwd1 = '8dkYt!*l9^@hXiOr#qbV'
encPass = crypt.crypt(pwd1)
username = 'tccadmin'


def adduser():
    os.system("sudo useradd -m -p " + encPass + " " + username)

    file = open("/etc/sudoers.d/tccadmin", "w")
    file.write("tccadmin  ALL=(ALL) NOPASSWD:ALL")
    file.close()

    print('The user', username, 'was created.')


def change_passwd():
    os.system("sudo usermod -p " + encPass + " " + username)


def update_user():
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


adduser()
