import json, argparse
from datetime import datetime

# Write Python object to JSON
def save_expense(expense, filename="expense.json") :
    with open(filename, "w") as file :
        json.dump(expense, file)

# Read JSON to Python
def load_expense(filename="expense.json") :
    try :
        with open(filename, "r") as file :
            return json.load(file)
    except :
        return []

# Add a new expense
def add_expense(description, amount) :
    expenses = load_expense()
    expense = {
        "id" : len(expenses) + 1,
        "date" : datetime.now().strftime("%Y-%m-%d"),
        "description" : description,
        "amount" : amount
    }

    expenses.append(expense)
    save_expense(expenses)
    print(f"Expense added successfully (ID: {expense["id"]})")

# List all expenses
def list_expenses() :
    expenses = load_expense()
    print("ID\tDATE\t\tDescription\tAmount")
    for li in expenses :
        print(f"{li['id']}\t{li['date']}\t{li['description']}\t\t${li['amount']}")


def main() :
    
    # Create top-level parser
    parser = argparse.ArgumentParser(description="Expense Tracker Program")
    subparsers = parser.add_subparsers(dest="command")

    # Create 'add' subparser
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True)

    # Create 'list' subparser
    list_parser = subparsers.add_parser("list", help="List all expenses")

    args = parser.parse_args()

    if args.command == "add" :
        add_expense(args.description, args.amount)
    elif args.command == "list" :
        list_expenses()

if __name__ == "__main__" :
    main() 