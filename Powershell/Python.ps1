## Install Python
$wshell = New-Object -ComObject Wscript.Shell -ErrorAction Stop
Start-Process -FilePath .\python-3.9.1-amd64.exe -ArgumentList '/quiet','InstallAllUsers=1','PrependPath=1' -Wait
$wshell.Popup("Python 3.9.1 should now be installed",60,"Python is being installed now",48+1)




