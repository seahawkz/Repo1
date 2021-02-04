#!/bin/bash

# rebootTC: Script to mass login and  reboot thinclients at a specific time using a cronjob

# Script accepts a file as input parameter
# input file will contain TC ip addresses, one per line

# Usage: rebootTC.sh ips_file
# Source: https://w.amazon.com/index.php/OTIE/CE/ThinClient/ThinclientMassReboot

# Specify reboot activity start time with local time (the time displayed on thin client screen) with using 24-hour notation

input=$1

echo "Enter password: "
read -s password
echo "Specify the hour: HH (use thinclient's local time, with 24-hour notation)"
read thehour
echo "Specify the minutes: MM"
read theminutes

sleepsec=0

for ip in $(cat $input);do
        echo "============= set on $ip with sleep $sleepsec sec.";

        /usr/bin/expect << EOD
        spawn ssh -x -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -o connecttimeout=2 -l tc $ip;

        expect "Actual Username: ";
        send "$USER\r"

        expect "Actual Password: ";
        send "$password\r"

        expect "$ ";
        send "(sudo crontab -l; echo \"$theminutes $thehour * * * sleep $sleepsec; /sbin/reboot now\")|sudo crontab -\r";

        expect "$ ";
EOD

        # increase speepsec to avoid overflowing the servers with requests
        sleepsec=$(expr $sleepsec + 5)

done