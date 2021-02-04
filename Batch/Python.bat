::Install Python
::C:\Users\andedre\Downloads\python-3.9.1-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
::
::Update PIP
powershell.exe python -m pip install --upgrade pip
::
::Install virtualenv
pip install virtualenv
::
cd C:\Users\andedre\Desktop\
::
mkdir PyBox
::
cd .\PyBox\
::
::pause
::
virtualenv Captainslair -p "C:\Program Files\Python39\python.exe"
::
pause
::activate the virtual environment 
.\Captainslair\Scripts\activate
::
pause
::
pip install --upgrade pip
::
pip install netmiko
::
pip install pyserial
::
pip install urllib3
::
::
pause