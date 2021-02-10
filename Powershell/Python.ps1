## Install Python
$wshell = New-Object -ComObject Wscript.Shell -ErrorAction Stop
Start-Process -FilePath .\python-3.9.1-amd64.exe -ArgumentList '/quiet','InstallAllUsers=1','PrependPath=1' -Wait
$wshell.Popup("Python 3.9.1 should now be installed",60,"Python is being installed now",48+1)
## update pip
python -m pip install --upgrade pip
## intall netmiko
pip install netmiko
## install pyserial
pip install pyserial
## install urllib3
pip install urllib3
##
## Create Firewall Rules
New-NetFirewallRule -DisplayName "Port 8080" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow
New-NetFirewallRule -Program "C:\Program Files\Python39\python.exe" -Action Allow -Profile Private, Public -DisplayName "InboundPython" -Direction Inbound
New-NetFirewallRule -Program "C:\Program Files\Python39\python.exe" -Action Allow -Profile Private, Public -DisplayName "OutboundPython" -Direction Outbound

Start-Process -FilePath .\Git-2.30.0.2-64-bit.exe -ArgumentList '/VERYSILENT' -Wait

$wshell.Popup("Git 2.30 should now be installed",60,"Git is being installed now",48+1)


