import pandas as pd
import subprocess
import os
from error_tracker import update_unresolved, save_tracker
from report_generator import generate_report
from utils import parse_datetime

def run_powershell_script():
    os.makedirs("logs", exist_ok=True)
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "log_fetcher.ps1"], check=True)

def analyze_logs():
    df = pd.read_csv("./logs/extracted_logs.csv")
    errors, warnings = [], []
    
    for _, row in df.iterrows():
        entry = {
            "Timestamp": row["TimeCreated"],
            "EventID": int(row["Id"]),
            "Source": row["ProviderName"],
            "Message": row["Message"],
            "Resolved": False
        }
        if row["LevelDisplayName"] == "Error":
            errors.append(entry)
        elif row["LevelDisplayName"] == "Warning":
            warnings.append(entry)

    return errors, warnings

def main():
    run_powershell_script()
    errors, warnings = analyze_logs()

    updated_errors = update_unresolved(errors)
    save_tracker(updated_errors)
    generate_report(updated_errors, warnings)

if __name__ == "__main__":
    main()
