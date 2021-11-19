##  Compare 2 files find differnces.


## Get files from list 

$file1 = Get-Content "C:\Users\andedre\Documents\Joe.csv" | Sort-Object
$file2 = Get-Content "C:\Users\andedre\Documents\Derek.csv" | Sort-Object

## Remove whitespace

$file1 | ForEach-Object { $_.Trim() } | Out-File "C:\Users\andedre\Documents\Joe.csv"
$file2 | ForEach-Object { $_.Trim() } | Out-File "C:\Users\andedre\Documents\Derek.csv"

## Compare files, output results to csv file

$file1 | Where-Object { $file2 -notcontains $_ } | Out-File "C:\Users\andedre\Documents\Permission_Groups.csv" -Force




