# expense-tracker



## Installation
```
git clone https://github.com/jms020524/expense-tracker.git
cd expense-tracker
```

## Feature
1. Users can add an expense with a description and amount.
2. Users can update an expense.
3. Users can delete an expense.
4. Users can view all expenses.
5. Users can view a summary of all expenses.
6. Users can view a summary of expenses for a specific month.


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