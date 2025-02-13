import json, argparse, calendar
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

    if len(expenses) == 0 :
        expense_id = 1
    else :
        expense_id = expenses[-1]['id'] + 1

    expense = {
        "id" : expense_id,
        "date" : datetime.now().strftime("%Y-%m-%d"),
        "description" : description,
        "amount" : amount
    }

    expenses.append(expense)
    save_expense(expenses)
    print(f"Expense added successfully (ID: {expense["id"]})")

# Update selected expense
def update_expense(id, description=None, amount=None) :
    expenses = load_expense()

    for li in expenses :
        if li['id'] == int(id) :
            if description != None : 
                li['description'] = description
            if amount != None : 
                li['amount'] = amount
            save_expense(expenses)
            print(f"Expense with ID: {id} is successfully updated.")
            return
        
    print(f"Expense with ID: {id} is not found.")


# List all expenses
def list_expenses() :
    expenses = load_expense()
    print("ID\tDATE\t\tDescription\tAmount")
    for li in expenses :
        print(f"{li['id']}\t{li['date']}\t{li['description']}\t\t${li['amount']}")

# View summary of expenses
def show_summary(month=None) :
    expenses = load_expense()
    if not expenses :
        print("No expenses found")
        return

    if month :
        month = int(month)
        if not 1 <= month <= 12 :
            print("Invalid month value")
            return

    summary = 0
    for li in expenses :
        date_obj = datetime.strptime(li['date'],"%Y-%m-%d")
        if month is None or date_obj.month == int(month) :
            summary += int(li['amount'])

    if month :
        month_name = calendar.month_name[month]
        print(f"Total expenses for {month_name} : ${summary}")
    else :
        print(f"Total expenses : ${summary}")


# Remove selected expense
def delete_expense(id) :
    expenses = load_expense()
    
    for li in expenses :
        if li['id'] == int(id) :
            expenses.remove(li)
            print("Expense deleted successfully")
            save_expense(expenses)
            return
        
    print(f"Expense with ID: {id} is not found.")


def main() :
    
    # Create top-level parser
    parser = argparse.ArgumentParser(description="Expense Tracker Program")
    subparsers = parser.add_subparsers(dest="command")

    # Create 'add' subparser
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True)

    # Create 'update' subparser
    update_parser = subparsers.add_parser("update", help="Update a selected expense")
    update_parser.add_argument("--id", required=True)
    update_parser.add_argument("--description")
    update_parser.add_argument("--amount")

    # Create 'list' subparser
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Create 'summary' subparser
    summary_parser = subparsers.add_parser("summary", help="View summary of all expenses")
    summary_parser.add_argument("--month")

    # Create 'delete' subparser
    delete_parser = subparsers.add_parser("delete", help="Remove selected expense")
    delete_parser.add_argument("--id", required=True)

    args = parser.parse_args()

    if args.command == "add" :
        add_expense(args.description, args.amount)
    elif args.command == "update" :
        update_expense(args.id, args.description, args.amount)
    elif args.command == "list" :
        list_expenses()
    elif args.command == "summary" :
        show_summary(args.month)
    elif args.command == "delete" :
        delete_expense(args.id)


if __name__ == "__main__" :
    main() 