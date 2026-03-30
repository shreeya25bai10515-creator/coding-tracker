def add_entry():
    try:
        problems = int(input("How many problems did you solve today? "))
    except ValueError:
        print("Please enter a valid number!\n")
        return

    with open("data.txt", "a") as file:
        file.write(str(problems) + "\n")

    print("Progress saved!\n")


def view_progress():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines()

        if not data:
            print("No progress found.\n")
            return

        print("\nYour Progress:")

        for i, entry in enumerate(data, start=1):
            print(f"Day {i}: {entry.strip()} problems")

        # current streak
        streak = 0
        for entry in reversed(data):
            if int(entry.strip()) > 0:
                streak += 1
            else:
                break

        print(f"\n🔥 Current Streak: {streak} days\n")

    except FileNotFoundError:
        print("No data found.\n")


def menu():
    while True:
        print("====== Coding Tracker ======")
        print("Type 'add' to add progress")
        print("Type 'view' to see progress")
        print("Type 'exit' to quit")

        choice = input("What do you want to do? ").lower()

        if choice == "add":
            add_entry()
        elif choice == "view":
            view_progress()
        elif choice == "exit":
            print("Goodbye! Keep coding 🚀")
            break
        else:
            print("Invalid input, try again.\n")


menu()