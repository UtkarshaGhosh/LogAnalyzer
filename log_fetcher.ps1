# Save as log_fetcher.ps1
$today = Get-Date -Format "yyyy-MM-dd"
Get-WinEvent -LogName System | Where-Object {
    $_.LevelDisplayName -in @('Error', 'Warning') -and
    $_.TimeCreated.Date -eq (Get-Date).Date
} | Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message |
Export-Csv -Path "./logs/extracted_logs.csv" -NoTypeInformation -Encoding UTF8
