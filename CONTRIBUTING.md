# Contributing to Student Management System

Thank you for helping improve this Python Turtle-based student records and grading application.

## Set up the project
```bash
git clone https://github.com/joshuaarao42-arch/STUDENT-MANAGER.git
cd STUDENT-MANAGER
```
Follow the run instructions in the README and use the Python version supported by the project.

## Contribution areas
- Student registration, search, profile display, and record maintenance.
- Grade entry and percentage-to-grade conversion.
- General Weighted Average (GWA) calculations.
- Academic status and term summaries.
- Turtle interface clarity, navigation, and error handling.
- Safe and reliable local text-file persistence.

## Correctness requirements
- Preserve the existing grading rules unless a change is explicitly proposed and agreed upon.
- Test calculations with normal values, boundary values, and incomplete records.
- Avoid duplicate student records and accidental overwrites.
- Handle missing or malformed local data without crashing.
- Use fictional student data in screenshots, tests, and examples. Never commit real student IDs or grades.

## Before submitting
Run the application and test the affected student and grading workflows from the interface. Include sample inputs and expected results for calculation changes.

Use branches such as `feature/student-search` or `fix/gwa-calculation`. Explain any change to grading behavior clearly in the pull request.
