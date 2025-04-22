import os
import json


print("-------DAILY EXPENSE TRACKER--------")
if not os.path.exists("expense_tracker_data.json"):
    file_name = os.mkdir("expense_tracker_data.json")

#initializing balance and history
balance = 0
history = ["History: "]


#load data from file if it exists
def load_data():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            balance = data.get('balance', 0)
            history = data.get('history', [])
    except FileNotFoundError:
        print("File does not exists!")

#save data to file
def save_data():
    data = {
        'balance': balance,
        'history': history
    }
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


#function to add the amount
def add_amount():
    global balance
    global history
    add_income = int(input("\nEnter amount: "))
    balance += add_income
    note = input("Enter note: ")
    print(f"\n>>> Income amount added <<<")
    history.append({
        "type": "income",
        "amount": add_income,
        "note": note
    })
    print("\n...\n")
    

#function to expense amount
def expense_amount():
    global balance, history
    expense_amount = int(input("Enter amount: "))
    if expense_amount <= balance:
        category = input("Enter category: ")
        note = input("Enter note: ")
        balance = balance - expense_amount
        print("\n>>> Expense amount added <<<")
        history.append({
            "type": "expense",
            "amount": expense_amount,
            "category": category,
            "note": note
        })
    else:
        print("Balance not enough")
        print(f"Balance = {balance}")
    print("\n...\n")
    # return expense_amount

#function to show balance
def show_balance():
    print(f"\nCurrent balance is Rs.{balance}")
    print("\n...\n")

# function to show history
def show_history():
    global history
    for item in history[1:]:
        if(item["type"] == "income"):
            print(f"Income: +{item['amount']} ({item['note']})")
        elif(item["type"] == "expense"):
            print(f"Expense: -{item['amount']} for ({item['category']} - {item['note']})")
        print("\n...\n")
while True:
    try:
        total_tasks = int(input("1. Add Income\n2. Add Expense\n3. Show Balance\n4. Show History\n5. Exit\nChoose: "))
        if(total_tasks == 1):
            add_amount()
        elif(total_tasks == 2):
            expense_amount() 
        elif(total_tasks == 3):
            show_balance()
        elif(total_tasks == 4):
            show_history()   
        elif total_tasks == 5:
            print("Exiting app... ")
            break

    except ValueError:
        print("Invalid input! amount should be only in numbers")





# #FILE HANDLING CONCEPTS UNDERSTANDING HERE
# import json
# import os

# person = {
#     "name": "Ali",
#     "age": 17,
#     "skills": ["Python", "Web"]
# }

# file_name = "myfile.json"

# if not os.path.exists(file_name):
#     with open(file_name, "w") as file:
#         json.dump(person, file)
#     print("File created and data saved!")

# elif os.path.getsize(file_name) > 0:
#        with open(file_name, "r") as file:
#         data = json.load(file)
#         name = data.get('name')
#         age = data.get('age')
#         print("✅ File loaded: Name =", name, "Age =", age)

# else:
#     print("⚠️ File exists but is empty.")






