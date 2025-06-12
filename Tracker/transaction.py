from Tracker.utils import read_records, write_records, calculate_total_savings

class Transaction:
    def __init__(self, amount, type, category):
        self.amount = amount
        self.type = type
        self.category = category

    def to_dict(self):
        return {
            "amount": self.amount,
            "type": self.type,
            "category": self.category
        }

def add_transaction():
    print("> add transaction")
    amount = float(input("amount: "))
    type_ = input("type (income/expense): ").strip().lower()
    category = input("category (freelance/full-time job/full-time business): ").strip()

    transaction = Transaction(amount, type_, category)
    records = read_records()
    records.append(transaction.to_dict())
    write_records(records)

    print("Transaction added")
    total_savings = calculate_total_savings(records)
    print(f"total savings : {total_savings}")
