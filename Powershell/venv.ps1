## Update PIP
python -m pip install --upgrade pip
##
Set-Location $env:USERPROFILE\Documents\
##
##mkdir PyBox 
New-Item .\Pybox -ItemType Directory
##
Set-Location .\PyBox
New-Item .\logfiles -ItemType Directory
New-Item .\httpServerFiles -ItemType Directory
##
## Create virtual environment
python -m venv $env:USERPROFILE\Documents\PyBox\CaptainsLair --upgrade-deps
##
##activate the virtual environment 
.\CaptainsLair\Scripts\activate
##
pip install netmiko
##
pip install pyserial
##
pip install urllib3
##
##
Set-Location .\httpServerFiles
wget http://narf-cloudfront.aka.amazon.com/device_images/cat9k_lite_iosxe.16.12.03a.SPA.bin -OutFile cat9k_lite_iosxe.16.12.03a.SPA.bin
wget http://narf-cloudfront.aka.amazon.com/device_images/cat9k_iosxe.V169_3_ES2.SPA.bin -OutFile cat9k_iosxe.V169_3_ES2.SPA.bin
