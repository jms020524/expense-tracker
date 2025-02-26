# expense-tracker
A simple Expense tracker application to manage user's finances.

This project is inspired from [Roadmap Project](https://roadmap.sh/projects/expense-tracker)


## Feature
- Users can add an expense with a description and amount.
- Users can update an expense.
- Users can delete an expense.
- Users can view all expenses.
- Users can view a summary of all expenses.
- Users can view a summary of expenses for a specific month.


## Installation
```
git clone https://github.com/jms020524/expense-tracker.git
cd expense-tracker
```


## Usage
- Add expense
```
python expense_tracker.py add --description 'Lunch' --amount 20
```

- Update expense
```
python expense_tracker.py update --id 1 --description 'Breakfast' --amount 15
```

- Delete expense
```
python expense_tracker.py delete --id 2
```

- List all expenses.
```
python expense_tracker.py list
```

- Show summary of all expenses.
```
python expense_tracker.py summary
```

- Show summary of expenses for a specific month.
```
python expense_tracker.py summary --month 2
```