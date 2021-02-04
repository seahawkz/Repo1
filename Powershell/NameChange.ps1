

$Path = "C:\Users\andedre\Documents\Scripts\Powershell\Test"
$directories = Get-ChildItem $Path -Directory -Recurse
$TextInfo = (Get-Culture).TextInfo

foreach ($directory in $directories) {
    $newname = $TextInfo.ToLower($directory) +"1"
    Rename-Item $directory.FullName -NewName $newname
}

$directories1 = Get-ChildItem $Path -Directory -Recurse
foreach ($directory1 in $directories1) {
    $newname = $TextInfo.ToTitleCase($directory1) +"1"
    Rename-Item $directory1.FullName -NewName $newname
}

$directories2 = Get-ChildItem $Path -Directory -Recurse
foreach ($directory2 in $directories2) {
    $newname = $directory2 -replace ".$"
    Rename-Item $directory2.FullName -NewName $newname
}

$directories3 = Get-ChildItem $Path -Directory -Recurse
foreach ($directory3 in $directories3) {
    $newname = $directory3 -replace ".$"
    Rename-Item $directory3.FullName -NewName $newname
}

Get-ChildItem $Path -Filter *.mp4 -Recurse | foreach {$newname = $TextInfo.ToLower($_.BaseName)+".mp4"; Rename-Item $_.FullName $newname }
Get-ChildItem $Path -Filter *.mp4 -Recurse | foreach {$newname = $TextInfo.ToTitleCase($_.BaseName)+".mp4"; Rename-Item $_.FullName $newname }
Get-ChildItem $Path -Filter *.mp4 -Recurse | Rename-Item -NewName {$_.name -replace "\bIi\b", "II"}
Get-ChildItem $Path -Filter *.mp4 -Recurse | Rename-Item -NewName {$_.name -replace "\bIii\b", "III"}
Get-ChildItem $Path -Filter *.mp4 -Recurse | Rename-Item -NewName {$_.name -replace "\bIv\b", "IV"}
Get-ChildItem $Path -Filter *.mp4 -Recurse | Rename-Item -NewName {$_.name -replace "\bVi\b", "VI"}
Get-ChildItem $Path -Filter *.mp4 -Recurse | Rename-Item -NewName {$_.name -replace "\bVii\b", "VII"}
Get-ChildItem $Path -Filter *.mp4 -Recurse | Rename-Item -NewName {$_.name -replace "\bViii\b", "VIII"}