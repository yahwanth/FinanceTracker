from collections import defaultdict
from Tracker.utils import read_records

def generate_report():
    records = read_records()

    if not records:
        print("No transactions found.")
        return

    summary = defaultdict(float)

    for record in records:
        category = record['category']
        amount = record['amount']
        type_ = record['type']

        if type_ == 'income':
            summary[category] += amount
        elif type_ == 'expense':
            summary[category] -= amount

    print("\nFinancial Report:")
    for category, total in summary.items():
        print(f"- {category} ${total}")
