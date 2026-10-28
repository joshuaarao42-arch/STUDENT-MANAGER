# 🎓 Student Management System

<p align="center">
  <strong>A Python Turtle-Based Student Records and Grading Application</strong>
  <br>
  A simple desktop application for managing student information, tracking academic performance, and calculating General Weighted Average (GWA).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Turtle-2E8B57?style=for-the-badge" alt="Turtle GUI">
  <img src="https://img.shields.io/badge/Storage-Text%20File-orange?style=for-the-badge" alt="Text File Storage">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Project Status">
</p>

---

## 📌 Table of Contents

- [📖 About the Project](#-about-the-project)
- [✨ Features](#-features)
- [🛠️ Built With](#️-built-with)
- [📋 System Requirements](#-system-requirements)
- [🚀 Getting Started](#-getting-started)
- [🖥️ System Modules](#️-system-modules)
- [📊 Grading System](#-grading-system)
- [🧮 GWA Calculation](#-gwa-calculation)
- [📁 Project Structure](#-project-structure)
- [💾 Data Storage](#-data-storage)
- [⚠️ Limitations](#️-limitations)
- [🔮 Future Enhancements](#-future-enhancements)
- [🎯 Learning Objectives](#-learning-objectives)
- [👨‍💻 Author](#-author)

---

## 📖 About the Project

The **Student Management System** is a desktop application developed using Python and its built-in `turtle` module. It provides an interactive graphical interface that allows teachers to organize student records, manage academic grades, and monitor student performance.

The application simplifies basic academic record management by combining student information, grade conversion, GWA computation, and academic status monitoring in one system.

Student information is stored locally in a text file, allowing records to persist between application sessions without requiring an external database.

### 🎯 Project Objectives

- Organize student information in a centralized application.
- Automate the conversion of percentage scores into numerical grades.
- Calculate students' GWA based on recorded academic grades.
- Monitor academic standing across four academic terms.
- Demonstrate fundamental Python programming concepts through a practical project.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👨‍🎓 Student Registration | Add students with a unique 10-digit ID, name, course, and year level. |
| 📋 Student Directory | View student records, GWA, and academic status in a paginated list. |
| 🔎 Student Search | Find records using a student ID or name. |
| 🪪 Student Profiles | View personal information, grades, GWA, and academic remarks. |
| 📝 Grade Management | Enter percentage scores for Prelims, Midterms, Semi-finals, and Finals. |
| 🔄 Record Updates | Update a student's name, course, and year level. |
| 🗑️ Record Deletion | Delete a student record after confirmation. |
| 🎲 Random Selection | Select a student from the registered records. |
| 🧮 Automatic GWA | Calculate the average of all grades recorded so far. |
| 📈 Academic Monitoring | Identify students with no grades, incomplete grades, passing standing, conditional standing, or failing standing. |
| 💾 Persistent Storage | Save and load student records using `students.txt`. |
| 🎨 Graphical Interface | Navigate the application using clickable buttons and visual student profiles. |

![image alt](https://github.com/joshuaarao42-arch/STUDENT-MANAGER/blob/main/IMAGESS/Screenshot%202026-10-28%20174117.png?raw=true)
![image alt]()
![image alt]()
---

## 🛠️ Built With

<p>
  <img src="https://img.shields.io/badge/Python-Programming%20Language-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Turtle-Graphics%20Library-2E8B57?style=flat-square" alt="Turtle">
</p>

| Technology | Purpose |
|---|---|
| **Python 3** | Implements the system's logic and functionality. |
| **Turtle** | Draws the interface, buttons, shapes, and student profile layouts. |
| **File Handling** | Reads and writes student records to a local file. |
| **Lists** | Stores and manages student records during execution. |
| **Functions** | Organizes the application into reusable operations. |
| **Conditional Statements** | Handles validation, grade conversion, and academic status. |
| **Event Handling** | Processes mouse clicks and button interactions. |

> **Dependencies:** The project uses Python's built-in `turtle` module and standard library, so no third-party packages are required.

---

## 📋 System Requirements

| Requirement | Details |
|---|---|
| Programming Language | Python 3 |
| Operating System | Windows, macOS, or Linux with a supported graphical environment |
| GUI Support | Tkinter/Turtle support |
| Storage | Local file system |
| Internet Connection | Not required for normal operation |
| Additional Packages | None |

---

## 🖥️ System Modules

### 🏠 1. Main Menu

The main menu serves as the application's central navigation screen.

| Option | Function |
|---|---|
| Add Student | Register a new student. |
| Student List | Display and search student records. |
| View Profiles | Browse individual student profiles. |
| Random Student | Select a random student from the records. |
| Exit | Close the application. |

### 👨‍🎓 2. Student Registration

Each student record contains the following information:

| Field | Validation |
|---|---|
| Student ID | Exactly 10 numeric digits, unique per record |
| Student Name | Required, maximum of 30 characters |
| Course | Required, stored in uppercase |
| Year Level | Integer from 1 to 4 |
| Academic Grades | Initially empty until grades are entered |

### 📋 3. Student Directory

The student directory presents records in a compact, table-like layout.

It includes:

- Student ID
- Student name
- Course
- Current GWA
- Academic status
- Page navigation
- Search and show-all controls

The list displays up to **7 students per page**.

### 🪪 4. Student Profile

The profile screen displays the selected student's information and academic performance, including:

- Student identification details
- Grades for all four academic terms
- Grade descriptions
- GWA or GWA so far
- Number of recorded grades
- Academic status and visual indicators

The profile also provides navigation and controls for adding grades, updating information, and deleting records.

### 📝 5. Grade Management

Teachers can enter a percentage score for a selected academic term. The application automatically converts the score into its corresponding numerical grade and descriptive remark.

The supported terms are:

1. Prelims
2. Midterms
3. Semi-finals
4. Finals

### 🔎 6. Search and Navigation

The search feature accepts a student ID or name. The student directory supports pagination, while profile navigation allows users to move between registered students.

### 🎲 7. Random Student Selection

The random selection feature chooses one of the currently registered students and displays the selected student's profile.

---

## 📊 Grading System

The system uses a percentage-to-grade conversion scale implemented in the source code.

| Percentage Score | Numerical Grade | Description |
|:---:|:---:|---|
| 97%–100% | 1.00 | Excellent |
| 94%–less than 97% | 1.25 | Excellent |
| 91%–less than 94% | 1.50 | Very Good |
| 88%–less than 91% | 1.75 | Very Good |
| 85%–less than 88% | 2.00 | Above Average |
| 82%–less than 85% | 2.25 | Above Average |
| 79%–less than 82% | 2.50 | Average |
| 76%–less than 79% | 2.75 | Average |
| 75%–less than 76% | 3.00 | Passing |
| 72%–less than 75% | 3.25 | Conditional |
| 69%–less than 72% | 3.50 | Conditional |
| 66%–less than 69% | 3.75 | Failed |
| 65%–less than 66% | 4.00 | Failed |
| Below 65% | 5.00 | Failed |

**Note:** The grade descriptions and thresholds represent the program's implemented rules, not necessarily the official grading policy of any particular university.

---

## 🧮 GWA Calculation

The application calculates the General Weighted Average (GWA) using the arithmetic mean of the recorded term grades.

### Formula

\[
\text{GWA} = \frac{\text{Sum of Recorded Grades}}{\text{Number of Recorded Grades}}
\]

### Example

Suppose a student has the following grades:

| Academic Term | Grade |
|---|---:|
| Prelims | 1.50 |
| Midterms | 2.00 |
| Semi-finals | 2.25 |
| Finals | 1.75 |
| **Total** | **7.50** |

The resulting GWA is:

\[
\text{GWA} = \frac{7.50}{4} = \boxed{1.88}
\]

The result is rounded to two decimal places.

### Academic Status Classification

| Condition | Status |
|---|---|
| No grades recorded | `NO GRADES` |
| One or more terms remain ungraded | `INCOMPLETE` |
| All four grades entered, GWA ≤ 3.00 | `PASSED` |
| All four grades entered, 3.00 < GWA ≤ 3.50 | `CONDITIONAL` |
| All four grades entered, GWA > 3.50 | `FAILED` |

The system does not assign a final academic status while grades remain incomplete.

---

## 📁 Project Structure

```text
Student-Management-System/
│
├── student_management.py    # Main Python application
├── students.txt             # Student records, generated automatically
└── README.md                # Project documentation
```

| File | Description |
|---|---|
| `student_management.py` | Contains the application logic, interface, grade conversion, student operations, and event handlers. |
| `students.txt` | Stores student information and term grades in comma-separated format. Created automatically when needed. |
| `README.md` | Documents the project's purpose, features, setup, and usage. |

---

## 💾 Data Storage

The system uses a local text file named `students.txt` to store student records.

Each record consists of **eight comma-separated fields**:

| Position | Field | Example |
|:---:|---|---|
| 1 | Student ID | `2026676796` |
| 2 | Student Name | `Juan Dela Cruz` |
| 3 | Course | `BSCS` |
| 4 | Year Level | `1` |
| 5 | Prelims Grade | `1.50` |
| 6 | Midterms Grade | `2.00` |
| 7 | Semi-finals Grade | `2.25` |
| 8 | Finals Grade | `1.75` |

### Sample Record

```text
2026676796,Juan Dela Cruz,BSCS,1,1.50,2.00,2.25,1.75
```

### How Persistence Works

- **Loading:** Existing records are read when the program starts.
- **Saving:** Student records are written to the file after successful additions, updates, grade entries, and deletions.
- **Initialization:** If the file does not exist, the program creates it automatically.
- **Retention:** Records remain on disk after the application closes.

> ⚠️ **Important:** Keep the data file in the appropriate working directory. The application overwrites the file when saving, so keep backups of important records. The current plain-text storage format is intended for educational use and does not provide encryption or access control.

---

## ⚠️ Limitations

The current implementation has the following limitations:

- Student records are stored in a plain-text file rather than a database.
- There is no login system or user authentication.
- The application is designed for local use rather than simultaneous multi-user access.
- GWA calculation uses an unweighted arithmetic mean.
- The current interface does not include a dedicated feature for correcting an already-recorded grade.
- The grading scale is fixed in the source code.
- Student names and courses cannot contain commas in the stored record format.
- The interface requires a graphical environment capable of running Turtle.

---

## 🔮 Future Enhancements

Potential improvements for future versions include:

- [ ] SQLite database integration
- [ ] Teacher authentication and account management
- [ ] Grade editing and correction
- [ ] Export student reports to CSV or PDF
- [ ] Import student records from CSV
- [ ] Advanced sorting and filtering
- [ ] Customizable grading scales
- [ ] Improved validation and error handling
- [ ] Student performance charts and analytics
- [ ] Modernized GUI using Tkinter or CustomTkinter
- [ ] Automated data backup and recovery

---

## 🎯 Learning Objectives

This project demonstrates the practical application of fundamental programming concepts.

| Concept | Application in the Project |
|---|---|
| Variables and Constants | Store configuration values, student details, and application state. |
| Lists | Organize student records and clickable button information. |
| Functions | Separate the system into reusable operations. |
| Conditional Statements | Validate inputs and determine grades and academic status. |
| Loops | Process records, grades, and visible list entries. |
| File Handling | Load and save student records. |
| Input Validation | Check student IDs, names, scores, and year levels. |
| Event-Driven Programming | Respond to mouse clicks and button actions. |
| GUI Programming | Draw menus, buttons, profiles, and status indicators using Turtle. |
| Mathematical Operations | Calculate GWA and convert percentage scores into grades. |

---

## 🤝 Contributing

Suggestions and improvements are welcome.

If you would like to improve the project:

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement and test your improvements.
4. Commit your changes with a descriptive message.
5. Open a pull request describing the changes.

---

## 👨‍💻 Author

**Joshua C. Arao**

First-year Bachelor of Science in Computer Science student with an interest in programming, software development, and building practical applications.

<p>
  <img src="https://img.shields.io/badge/Focus-Computer%20Science-blue?style=flat-square" alt="Computer Science">
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Project-Educational-purple?style=flat-square" alt="Educational Project">
</p>

---

This project is intended for educational purposes. You may use, modify, and extend the source code for learning and personal projects.

If you plan to distribute this project publicly, consider adding a dedicated `LICENSE` file to specify the permissions and conditions for reuse.

---

<p align="center">
  <strong>Built with Python, curiosity, and a commitment to learning.</strong>
  <br>
  ⭐ If you find this project useful, consider giving the repository a star!
</p>
