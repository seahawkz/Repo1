##  Compare 2 files find differnces.


## Get files and remove duplicates from list - case insensitive 

$file1 = gc "C:\Users\andedre\Documents\Joe.txt" | Sort-Object -Unique | Get-Unique -AsString
$file2 = gc "C:\Users\andedre\Documents\Derek.txt" | Sort-Object -Unique | Get-Unique -AsString

## Remove whitespace

$file1 | ForEach-Object {$_.Trim()} | Out-File "C:\Users\andedre\Documents\Joe.txt"
$file2 | ForEach-Object {$_.Trim()} | Out-File "C:\Users\andedre\Documents\Derek.txt"

## Compare files, output results to csv file

$file1 | ?{$file2 -notcontains $_ } | Out-File "C:\Users\andedre\Documents\Permission_Groups.csv" -Force

