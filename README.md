# Coding Tracker (CLI-Based AI Project)

**Student Name:** Shreeya Raj
**Reg No:** 25BAI10515
**Course:** Fundamentals in AI and ML (CSA2001)
**Branch:** CSE (AI & ML)

---

##  Overview

Coding Tracker is a command line based utility which helps students to track whether they have coded on that day or not. It enables users to check how many problems they’ve solved on a given day, track their progress and keep a streak of consecutive learning.

Most Students find it hard to be consistent in Coding. This project offers a clean and gentle way to track daily activity and develop an habitual practice.

---

##  Problem Statement

It is common for students to forget about coding practice, which affects their efficiency in learning. But there is a need for basic system in place to record daily progress and pave the way for consistent growth.

---

##  Objective of the Project

* For  light CLI based application

* For every day coding track

* Such as Streak Tracking for Maintaining Consistency

* Employ basic AI terminology to performance analytics

* To help give smart suggestions to a person on his/her data

---

##  AI-Based Feature  

This project include a simple AI-based suggestion system.  

The system analyze past coding data and:  

- Detects improvement or decline in performance  
- Suggest increasing or maintaining daily targets  
- Encourage consistency in coding habits  

This demonstrate basic Artificial Intelligence using rule-based decision making on user data.  

---

##  Features  

- Add daily coding progress  
- View complete progress history  
- Automatic streak calculation  
- AI-based suggestions for improvement  
- Simple and interactive CLI interface  
- File-based storage using `data.txt`  
- Error handling for invalid inputs  

---

##  Hardware and Software Requirements

**Hardware:**

* Basic computer/laptop

**Software:**

* Python 3.x
* Command Prompt / Terminal

No external libraries are required.

---

##  Methodology

1. User inputs daily coding data  
2. Data gets stored in a file (`data.txt`)  
3. Program reads stored data whenever required  
4. Streak is calculated based on consecutive entries  
5. AI logic analyze recent entries  
6. Suggestions are generated depending on performance trends  

---

##  Functional Modules

* Input Module (add progress)  
* Display Module (view progress)  
* Storage Module (file handling)  
* Streak Calculation Module  
* AI Suggestion Module  

---

##  Algorithm (Simplified)

1. Start the program  
2. Display menu (add / view / exit)  
3. If user selects add → input is stored in file  
4. If user selects view:  
   * Read the file  
   * Display the data  
   * Calculate streak  
   * Generate AI suggestion  
5. Repeat steps until user exit the program  

---

##  Installation and Setup

1. Install Python 3.x
   Check installation:

```bash
python --version
```

2. Clone the repository:

```bash
git clone https://github.com/shreeya25bai10515-creator/coding-tracker.git
```

Or download ZIP and extract.

3. Navigate to folder:

```bash
cd coding-tracker
```

4. Run the program:

```bash
python main.py
```

or

```bash
python3 main.py
```

---

##  How to Use

* Type `add` → Add daily progress
* Type `view` → View progress and suggestions
* Type `help` → Show commands
* Type `exit` → Exit program

---

##  File Structure

```
coding-tracker/
│
├── main.py
├── data.txt
├── README.md
```

Note: `data.txt` is created automatically.

---

##  Example Output

```
Your Progress:
Day 1: 3 problems
Day 2: 5 problems

Current Streak: 2 days
Improvement detected! Try solving 6 problems tomorrow.
```

---

## Challenges Faced

* Designing simple CLI interface  
* Handling invalid user inputs  
* Implementing correct streak logic  
* Adding AI-based suggestions  

---

## What I Learned

* File handling in Python  
* CLI application design  
* Basic AI concepts (rule based logic)  
* GitHub project management  
* Importance of consistency in coding  

---

## Real-World Applicability

This project can used by:

* Students preparing for coding interviews  
* Beginners learning programming  
* Anyone wanting to build coding consistency  

---

## Limitations

* Works only in CLI no GUI  
* Basic AI logic rule based not ML  
* No editing or deletion of past data  

---

## Future Enhancements

* Add graphical visualization  
* Use machine learning for prediction  
* Add login system  
* Build web or mobile version  

---

## Conclusion

This project successfully demonstrate how simple CLI tool can solve real world problem. It combine programming fundamentals with basic AI logic to create useful and practical application.  

---

##  References

* Python Documentation
* Course Materials (Fundamentals of AI & ML)
* Online coding resources

---

 This project is fully CLI-based and can be executed directly from the terminal without any GUI
