import json
import os

TRACKER_DIR = "./tracker"
TRACKER_FILE = os.path.join(TRACKER_DIR, "unresolved_errors.json")

# Ensure the directory exists
os.makedirs(TRACKER_DIR, exist_ok=True)

# Initialize the file if it doesn't exist
if not os.path.exists(TRACKER_FILE):
    with open(TRACKER_FILE, 'w') as f:
        json.dump([], f)

def load_tracker():
    with open(TRACKER_FILE, 'r') as f:
        return json.load(f)

def save_tracker(errors):
    with open(TRACKER_FILE, 'w') as f:
        json.dump(errors, f, indent=2)

def update_unresolved(current_errors):
    previous = load_tracker()
    combined = previous + current_errors

    # Deduplicate based on timestamp + message
    seen = set()
    unique = []
    for err in combined:
        key = (err["Timestamp"], err["Message"])
        if key not in seen:
            seen.add(key)
            unique.append(err)
    return unique
