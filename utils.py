from datetime import datetime

def parse_datetime(dt_str):
    try:
        return datetime.strptime(dt_str, "%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        return None
