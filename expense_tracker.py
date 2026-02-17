import os

# مسیر پوشه و فایل
folder_path = "C:\\h-motevalihabibi\\python-expense-tracker"
file_path = os.path.join(folder_path, "expenses.txt")

# اگر پوشه وجود نداشت، بساز
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

while True:
    print("Welcome to Expense Tracker")
    print("1. Add expense")
    print("2. View total")
    print("3. Exit")
    x = input("Choose an option: ")

    if x == "1":
        print("You selected: Add expense")
        amount = input("Enter expense amount: ")
        category = input("Enter category: ")
        # اضافه کردن به فایل
        with open(file_path, "a") as f:
            f.write(amount + "," + category + "\n")
        print("Expense added successfully!\n")

    elif x == "2":
        print("You selected: View total")
        total = 0
        try:
            with open(file_path, "r") as f:
                for line in f:
                    amt, cat = line.strip().split(",")
                    total += float(amt)
            print(f"Total expenses: {total}\n")
        except FileNotFoundError:
            print("No expenses recorded yet.\n")

    elif x == "3":
        print("You selected: Exiting")
        break

    else:
        print("Invalid option\n")
