from Tracker.transaction import add_transaction
from Tracker.tracker import generate_report

def main():
    print("Options:")
    print("1. Add transaction")
    print("2. View financial report")
    choice = input("Select option (1/2): ").strip()

    if choice == '1':
        add_transaction()
    elif choice == '2':
        generate_report()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
