<#
.DESCRIPTION
  This script will downloaded the current .bin files needed for the commodity lifecycle project

.NOTES
  Version:        1.0
  Author:         Derek Anderson
  Creation Date:  2/19/2021
  Purpose/Change: Initial script development

#>
#Set Error Action to Silently Continue
$ErrorActionPreference = "SilentlyContinue"
## Make new directory
New-Item .\httpServerFiles\MD5Files -ItemType Directory
## Create md5 test files
Set-Location .\httpServerFiles
New-Item .\MD5Files\ref1.md5 -ItemType File -Value "97F3F447B88F75B8CE8B1B2CB9C7344E"
New-Item .\MD5Files\ref2.md5 -ItemType File -Value "EFB93F376DA258335360F0BBB85DE3F8"
New-Item .\MD5Files\ref3.md5 -ItemType File -Value "3CC37B28A564064485E767EBC3A1F2F8"

## Download and verify .bin files
function file1{
    for ($n = 0; $n -lt 3; $n ++){
        Invoke-WebRequest http://narf-cloudfront.aka.amazon.com/device_images/cat9k_lite_iosxe.16.12.03a.SPA.bin -OutFile cat9k_lite_iosxe.16.12.03a.SPA.bin
        Get-FileHash .\cat9k_lite_iosxe.16.12.03a.SPA.bin -Algorithm MD5 | Select-Object -ExpandProperty Hash > .\MD5Files\cat9k_lite_iosxe.16.12.03a.SPA.bin.md5
        if (Compare-Object -ReferenceObject $(Get-Content .\MD5Files\ref1.md5) -DifferenceObject $(Get-Content .\MD5Files\cat9k_lite_iosxe.16.12.03a.SPA.bin.md5))
            {
                Remove-Item .\cat9k_lite_iosxe.16.12.03a.SPA.bin
                if ($n -eq 2){
                    Write-Host "There appears to be an issue downloading this file, please check your connection and try again."
                }
                else {
                    Write-Host "MD5 checksum values are different, attempting to  download again"
                }
            }
        else 
            {
                Write-Host "MD5 checksum values are the same"
                $n = 3
            }
    }
}
function file2{
    for ($n = 0; $n -lt 3; $n ++){
        Invoke-WebRequest http://narf-cloudfront.aka.amazon.com/device_images/cat9k_iosxe.V169_3_ES2.SPA.bin -OutFile cat9k_iosxe.V169_3_ES2.SPA.bin
        Get-FileHash .\cat9k_iosxe.V169_3_ES2.SPA.bin -Algorithm MD5 | Select-Object -ExpandProperty Hash > .\MD5Files\cat9k_iosxe.V169_3_ES2.SPA.bin.md5
        if (Compare-Object -ReferenceObject $(Get-Content .\MD5Files\ref2.md5) -DifferenceObject $(Get-Content .\MD5Files\cat9k_iosxe.V169_3_ES2.SPA.bin.md5))
        {
            Remove-Item .\cat9k_iosxe.V169_3_ES2.SPA.bin
            if ($n -eq 2){
                Write-Host "There appears to be an issue downloading this file, please check your connection and try again."
            }
            else {
                Write-Host "MD5 checksum values are different, attempting to  download again"
            }
        }
        else
        {
            Write-Host "MD5 checksum values are the same"
            $n = 3
        }
    }
}
function file3{
    for ($n = 0; $n -lt 3; $n ++){
        Invoke-WebRequest http://narf-cloudfront.aka.amazon.com/device_images/cat9k_iosxe.17.03.02a.SPA.bin -OutFile cat9k_iosxe.17.03.02a.SPA.bin
        Get-FileHash .\cat9k_iosxe.17.03.02a.SPA.bin -Algorithm MD5 | Select-Object -ExpandProperty Hash > .\MD5Files\cat9k_iosxe.17.03.02a.SPA.bin.md5
        if(Compare-Object -ReferenceObject $(Get-Content .\MD5Files\ref3.md5) -DifferenceObject $(Get-Content .\MD5Files\cat9k_iosxe.17.03.02a.SPA.bin.md5))
        {
            Remove-Item .\cat9k_iosxe.17.03.02a.SPA.bin
            if ($n -eq 2){
                Write-Host "There appears to be an issue downloading this file, please check your connection and try again."
            }
            else {
                Write-Host "MD5 checksum values are different, attempting to  download again"
            }
        }
        else
        {
            Write-Host "MD5 checksum values are the same"
            $n = 3
        }
    }
}

file1
file2
file3
Pause