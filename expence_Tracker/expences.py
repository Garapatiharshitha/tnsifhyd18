import csv
import datetime

# Function to add an expense to the CSV file
def add_expense(amount, category, description):
    with open('expenses.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        date = datetime.date.today()
        writer.writerow([date, amount, category, description])
    print("Expense added successfully!")1

# Function to view all the expenses in the CSV file
def view_expenses():
    with open('expenses.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Take user input to add or view expenses
while True:
    print("Enter 1 to add an expense")
    print("Enter 2 to view all expenses")
    print("Enter 3 to exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        description = input("Enter a brief description of the expense: ")
        add_expense(amount, category, description)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")