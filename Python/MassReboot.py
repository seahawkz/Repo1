#!/bin/bash
 
# rebootTC: Script to mass login and  reboot thinclients
 
# Script accepts a file as input parameter
# input file will contain TC ip addresses, one per line
 
# Usage: rebootTC.sh ips_file
# Source: https://w.amazon.com/index.php/OTIE/CE/ThinClient/ThinclientMassReboot
 
input=$1
 
echo "Enter password: "
read -s password
 
for ip in $(cat $input);do
        echo "============= $ip ";
 
        /usr/bin/expect << EOD
        spawn ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oConnectTimeout=2 -l tc $ip;
 
        expect "Actual Username: ";
        send "$USER\r"
 
        expect "Actual Password: ";
        send "$password\r"
 
        expect "$ ";
        send "sudo reboot && exit\r";
 
        expect "$ ";
EOD

        # Wait a few seconds to avoid overflowing the servers with requests
        sleep 5
done
