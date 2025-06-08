import pandas as pd
import os
from datetime import datetime

def generate_report(errors, warnings):
    os.makedirs("reports", exist_ok=True)
    file_name = f"./reports/log_report_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        if errors:
            pd.DataFrame(errors).to_excel(writer, index=False, sheet_name="Errors")
        if warnings:
            pd.DataFrame(warnings).to_excel(writer, index=False, sheet_name="Warnings")
