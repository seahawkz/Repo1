## Find local user accounts

$Computers = Get-ADComputer -SearchBase 'OU=Workstations,OU=Devices,DC=des,DC=wa,DC=lcl' -Filter * | Select-Object name
foreach ($Computer in $Computers) {
   $pc = $Computer.name
   Get-WmiObject -Class Win32_UserAccount -Filter  "LocalAccount='True'" -ComputerName $pc -ErrorAction SilentlyContinue |
   Select-Object PSComputername, Name, Disabled | Where-Object { $_.name -notlike 'administrator' -and $_.name -notlike 'blitz' -and $_.name -notlike 'DefaultAccount' `
         -and $_.name -notlike 'WDAGUtilityAccount' } | Export-Csv C:\Users\DerekA179\Documents\LocalUsers.csv -NoTypeInformation -Append 


}
