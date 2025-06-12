import os
import json

def get_file_path():
    os.makedirs("data", exist_ok=True)
    return os.path.join("data", "records.json")

def read_records():
    file_path = get_file_path()
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def write_records(records):
    file_path = get_file_path()
    with open(file_path, "w") as f:
        json.dump(records, f, indent=4)

def calculate_total_savings(records):
    total = 0
    for record in records:
        if record['type'] == 'income':
            total += record['amount']
        elif record['type'] == 'expense':
            total -= record['amount']
    return total
