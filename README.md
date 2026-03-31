# Coding Tracker

**Name:** Shreeya Raj  
**Roll No.:** 25BAI10515  
**Course:** CSE AI & ML (1st Year)  

---

## Overview

**Coding Tracker** is a simple command-line application designed to help students and programmers track their **daily coding practice**. The main goal of this project is to provide a **habit-forming tool** that motivates users to stay consistent with coding by recording the number of problems solved each day and displaying streaks and progress history.

Many beginners and students face the challenge of **losing track of their daily coding**, which can affect consistency and learning outcomes. This tool provides a **straightforward way** to record, monitor, and visualize coding activity without the complexity of advanced apps.

---

## Features

- **Add daily coding progress:** Input the number of problems solved each day.
- **View progress:** See all previous entries along with the number of problems solved per day.
- **Streak tracker:** Automatically calculates the current streak of consecutive days with progress.
- **Simple CLI interface:** Easy to use without any complex installation.
- **File-based storage:** Saves data in `data.txt`, so progress is maintained even after closing the program.
- **Error handling:** Handles invalid inputs gracefully and prompts the user to enter a valid number.

---

## How It Works

1. When you run the program (`main.py`), a menu appears asking you to choose an action:  

```

Type 'add' to add progress
Type 'view' to see progress
Type 'exit' to quit

```

2. **Add progress:**  
   - Type `add`  
   - Enter the number of problems solved today  
   - The program saves this number in `data.txt`  

3. **View progress:**  
   - Type `view`  
   - The program reads all past entries from `data.txt`  
   - Displays day-wise progress and current streak  

4. **Exit:**  
   - Type `exit` to quit the program  

---

## Example Usage

```

What do you want to do? add
How many problems did you solve today? 3
Progress saved!

What do you want to do? view

Your Progress:
Day 1: 3 problems
🔥 Current Streak: 1 days

What do you want to do? add
How many problems did you solve today? 5
Progress saved!

What do you want to do? view

Your Progress:
Day 1: 3 problems
Day 2: 5 problems
🔥 Current Streak: 2 days

````

---

## Installation and Setup

1. **Install Python:** Make sure Python 3.x is installed on your computer.  
   [Download Python](https://www.python.org/downloads/)

2. **Clone or download repository:**  
   - Clone via Git:
   ```bash
   git clone https://github.com/YOUR_USERNAME/coding-tracker.git
````

 Or download ZIP and extract the folder.

3. Navigate to the project folder in terminal/command prompt:

```bash
cd coding-tracker
```

4. Run the program:

```bash
python main.py
```

5. Follow the on-screen menu (`add`, `view`, `exit`) to use the application.

---

File Structure

```
coding-tracker/
│
├── main.py      # Main Python program
├── data.txt     # Stores daily progress (created automatically if empty)
└── README.md    # Project documentation and instructions
```

---

Why I Built This

As a student in CSE AI & ML, I realized it is easy to lose track of coding practice, which is crucial for skill development.
I wanted a simple tool that helps me and others track coding consistently, understand progress trends, and maintain motivation over time.

By building this project, I also practiced file handling, CLI design, and logical thinking in Python.

---

Challenges Faced

* Designing a simple menu system that is user-friendly for beginners
* Handling invalid inputs (like text instead of numbers)
* Implementing the streak calculation logic correctly
* Ensuring persistent data storage with `data.txt`

---

What I Learned

* Basics of Python file handling (reading/writing data)
* How to structure a small project professionally
* Command-line interface design principles
* Using GitHub for version control and project submission
* The importance of tracking progress for habit building

---

Future Improvements

* Add graphs to visualize daily/weekly progress
* Allow users to edit or delete past entries
* Create a web-based version with more interactive features
* Add notifications or reminders to encourage coding daily

---

Conclusion

This project is a small but meaningful tool that applies programming concepts learned in the course to solve a real problem: staying consistent with coding.
It shows how simple automation can make a practical difference in daily habits and learning outcomes.

---
Enjoy tracking your coding journey! 
