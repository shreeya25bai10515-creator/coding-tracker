# Coding Tracker - CLI Based AI Project

def load_data():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines()
            return [int(x.strip()) for x in data if x.strip().isdigit()]
    except FileNotFoundError:
        return []


def save_data(value):
    with open("data.txt", "a") as file:
        file.write(str(value) + "\n")


def calculate_streak(data):
    streak = 0
    for value in reversed(data):
        if value > 0:
            streak += 1
        else:
            break
    return streak


def give_suggestion(data):
    if len(data) < 2:
        print("💡 Start coding daily to build a strong habit!")
        return

    last = data[-1]
    prev = data[-2]

    if last > prev:
        print(f"📈 Improvement detected! Try solving {last + 1} problems tomorrow.")
    elif last < prev:
        print(f"⚠ Performance dropped. Try solving at least {prev} problems tomorrow.")
    else:
        print("👍 Consistent work! Try increasing your target gradually.")


def add_entry():
    try:
        value = int(input("How many problems did you solve today? "))
        if value < 0:
            print("Please enter a non-negative number.")
            return
        save_data(value)
        print("✅ Progress saved!")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")


def view_progress():
    data = load_data()

    if not data:
        print("No data available. Start by adding progress!")
        return

    print("\n📊 Your Progress:")
    for i, val in enumerate(data, start=1):
        print(f"Day {i}: {val} problems")

    streak = calculate_streak(data)
    print(f"\n🔥 Current Streak: {streak} days")

    # AI Suggestion
    give_suggestion(data)


def main():
    print("=== Coding Tracker CLI ===")

    while True:
        print("\nWhat do you want to do?")
        print("Type 'add'  → Add today's progress")
        print("Type 'view' → View progress")
        print("Type 'help' → Show commands")
        print("Type 'exit' → Quit")

        choice = input("Enter command: ").lower()

        if choice == "add":
            add_entry()
        elif choice == "view":
            view_progress()
        elif choice == "help":
            print("\nCommands:")
            print("add  → Add progress")
            print("view → View progress")
            print("exit → Exit program")
        elif choice == "exit":
            print("Goodbye! Keep coding 🚀")
            break
        else:
            print("❌ Invalid command. Type 'help' for options.")


if __name__ == "__main__":
    main()
