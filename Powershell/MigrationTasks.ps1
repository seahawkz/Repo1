

$csv = Import-Csv "\\des\NETLOGON\UserList1.csv"


$DESID = $($csv | Select-Object -Property * | Where-Object { $_.DESID.trim() -ieq "$env:USERNAME" }).DESID.trim()
$Eclient = $($csv | Select-Object -Property * | Where-Object { $_.DESID.trim() -ieq "$env:USERNAME" }).EclientID.trim()
$EmailID = $($csv | Select-Object -Property * | Where-Object { $_.DESID.trim() -ieq "$env:USERNAME" }).Email.trim()
$FirstName = $($csv | Select-Object -Property * | Where-Object { $_.DESID -ieq "$env:USERNAME" }).FirstName.trim()
$LastName = $($csv | Select-Object -Property * | Where-Object { $_.DESID -ieq "$env:USERNAME" }).LastName.trim()
$FullName = "$FirstName.$LastName"

if ($(test-path "C:\Users\$env:USERNAME") -eq $true) {
  $username = $env:USERNAME
}
elseif ($(test-path "C:\Users\$Eclient") -eq $true) {
  $username = $Eclient
  Write-Host $username
} 
elseif ($(test-path "C:\Users\$EmailID") -eq $true) {
  $username = $EmailID
  if ($(test-path "C:\Users\$username\AppData\Local\DO-NOT-DELETE.txt") -eq $false) {
    $Body = "Note: User Profile Path is Email `n`nDESID: $DESID `neClientID: $Eclient `nEmail Address: $EmailID  `nComputername: $env:COMPUTERNAME"
    send-mailmessage -to 'DESDLMigrationTeam@des.wa.gov' -from "MigrationTasks.ps1 <DoNotReply@des.wa.gov>" `
      -subject "Note: User Profile Path is Email" -body ($Body | Out-String) -priority High -dno onSuccess, onFailure -smtpServer warelay.des.wa.gov
  }
}
elseif ($(test-path "C:\Users\$FullName") -eq $true) {
  $username = $FullName
  if ($(test-path "C:\Users\$username\AppData\Local\DO-NOT-DELETE.txt") -eq $false) {
    $Body = "Note: User Profile Path is FirstName.LastName `n`nDESID: $DESID `neClientID: $Eclient `nEmail Address: $EmailID  `nComputername: $env:COMPUTERNAME"
    send-mailmessage -to 'DESDLMigrationTeam@des.wa.gov' -from "MigrationTasks.ps1 <DoNotReply@des.wa.gov>" `
      -subject "Note: User Profile Path is FirstName.LastName" -body ($Body | Out-String) -priority High -dno onSuccess, onFailure -smtpServer warelay.des.wa.gov
  }
}
else {
  $Body = "Error: Unable to ID users Profile path.  `n`nDESID: $env:USERNAME  `nEclientID: $Eclient  `nEmail Address: $EmailID `nComputername: $env:COMPUTERNAME"
  send-mailmessage -to 'DESDLMigrationTeam@des.wa.gov' -from "MigrationTasks.ps1 <DoNotReply@des.wa.gov>" `
    -subject "Error: User Profile path issue" -body ($Body | Out-String) -priority High -dno onSuccess, onFailure -smtpServer warelay.des.wa.gov

  exit
}

if ($(test-path "C:\Users\$username\AppData\Local\DO-NOT-DELETE.txt") -eq $false) {

  # Redirect User Shell Folders back to local machine 

  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders' -Name Desktop -Value '%USERPROFILE%\Desktop'
  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders' -Name Favorites -Value '%USERPROFILE%\Favorites'
  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders' -Name Personal -Value '%USERPROFILE%\Documents'

  # Remove Key from old User Shell Folders
  Remove-ItemProperty -Name '{754AC886-DF64-4CBA-86B5-F7FBF4FBCEF5}' -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders'
  Remove-ItemProperty -Name '{F42EE2D3-909F-4907-8871-4C22FC0BF756}' -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders'


  # Copy files
  Copy-Item "\\des\NETLOGON\DO-NOT-DELETE.txt" "C:\Users\$username\AppData\Local\DO-NOT-DELETE.txt"

  # Shell folders reset

  $desktop = "$env:USERPROFILE\Desktop"
  $favorites = "$env:USERPROFILE\Favorites"
  $documents = "$env:USERPROFILE\Documents"

  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders' -Name Desktop    -value $desktop
  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders' -Name Favorites  -value $Favorites
  Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders' -Name Personal   -value $documents


  # Remove old cert
  Get-ChildItem Cert:\CurrentUser\My | Where-Object {
  ($TmplExt = $_.Extensions | Where-Object {
      $_.Oid.FriendlyName -match 'Certificate Template'
    }) -and 
    $TmplExt.format(0) -match 'WA User'
  } | Remove-Item  



  # Restart Computer 
  shutdown /r /t 15

}
else {
  Write-Host 'Exiting'
  exit
}
