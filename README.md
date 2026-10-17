# Student Management System (Turtle GUI)

A simple desktop app for teachers to **add, update, delete, search, and view students**, built with Python's `turtle` module and SQLite. It also has a **profile viewer** that shows one student at a time, with a grade, class rank info, and comparison to the class average.

Made as a beginner Python project covering Topics 1 to 4 of the course (see [Topics Covered](#topics-covered)).

<!-- Add a screenshot after you run it:
![Main menu](screenshots/menu.png)
-->

## Features

- **Add student**: ID, name, branch, semester, and total marks, with input checking
- **Update student**: shows the current values, then saves the new ones
- **Delete student**: asks for confirmation (type `YES`) before deleting
- **Search / view list**: search by ID or name, or leave it blank to see everyone. Results appear in a table with pages and a letter grade
- **Student profiles (one by one)**: flip through students with the **Prev / Next** buttons or the **Left / Right arrow keys**. Each profile shows:
  - Year level and term (computed from the semester)
  - Total marks and percentage
  - Grade and remark (A, B, C, or F; Passed, Passed with honors, or Failed)
  - Class average, and whether the student is above or below it
- **Dashboard**: the main menu shows the number of students, class average, highest marks, and lowest marks

## Requirements

- Python 3.8 or newer
- `tkinter` (it comes with most Python installs, and `turtle` needs it)

No other libraries are needed. `sqlite3`, `math`, and `turtle` are all part of Python.

## How to Run

1. Download or clone this repository
2. Open a terminal in the project folder
3. Run:

```bash
python main.py
```

On the first run, the program creates a `data.db` file in the same folder to store the students.

## How to Use

| Button | What it does |
|---|---|
| Add student | Pop-up boxes ask for ID, name, branch, semester, marks |
| Update student | Enter an ID, then type the new details |
| Delete student | Enter an ID, then type `YES` to confirm |
| Search / View list | Type an ID or name (blank shows all students) |
| Student profiles | Opens the one-by-one profile viewer |
| Exit | Closes the program |

Inputs are typed into small pop-up boxes (turtle's `textinput`), which work like Python's `input()`. Pressing **Cancel** stops the action.

**Input rules**
- ID: whole number
- Name: letters and spaces only (saved in Title Case)
- Branch: cannot be empty (saved in UPPERCASE)
- Semester: 1 to 12
- Total marks: 0 to 100

## Grading Scale

| Percentage | Grade | Remark |
|---|---|---|
| 90 and above | A | Passed with honors |
| 80 to 89 | B | Passed |
| 75 to 79 | C | Passed |
| Below 75 | F | Failed |

You can change the scale at the top of `main.py` by editing `MAX_MARKS` and `PASSING`.

## Project Structure

```
.
├── main.py       # the turtle GUI (screens, buttons, input checking, grades)
├── student.py    # the Data class: talks to the SQLite database
└── data.db       # created automatically on first run
```

## Database

`student.py` stores students in a single SQLite table:

| Column | Type |
|---|---|
| id | INTEGER (primary key) |
| name | TEXT |
| branch | TEXT |
| semester | INTEGER |
| total_marks | REAL |

## Topics Covered

| Topic | Where it appears in the code |
|---|---|
| **1. Computers, Programs and Python** | Input → process → output design, `import`, comments, `print()` for the console banner and logs |
| **2. Elementary Programming** | Constants (`MAX_MARKS`, `PASSING`), variables, `int()` / `float()` conversion, `+=`, `//` and `%` for year level and term, simultaneous assignment |
| **3. Math Functions, Strings and Objects** | `math.ceil`, `max`, `min`, `abs`, `round`; string methods `strip`, `title`, `upper`, `lower`, `isdigit`, `isalpha`, `replace`, slicing, `in`; `type()` and `id()` on the database object |
| **4. Selections** | `if` / `elif` / `else` for grades, nested `if` for honors, `and` / `or` / `not`, comparison operators |

Each concept is tagged in the code with a `[Topic N]` comment.

## Notes

- The marks scale is assumed to be out of 100. Change `MAX_MARKS` in `main.py` if yours is different.
- Add `data.db` and `__pycache__/` to a `.gitignore` file so student data is not uploaded to GitHub.

## Author

Made by Joshua C. Arao.
