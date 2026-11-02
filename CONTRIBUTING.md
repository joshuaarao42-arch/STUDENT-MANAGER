# Contributing to Student Management System

This Python Turtle application manages student records, academic grades, and General Weighted Average (GWA).

## Clone
```bash
git clone https://github.com/joshuaarao42-arch/STUDENT-MANAGER.git
cd STUDENT-MANAGER
```
Follow the README for the supported Python version and launch instructions.

## Project-specific contributions
- Student registration, search, profiles, updates, and deletion.
- Grade entry and percentage-to-grade conversion.
- GWA calculations, term summaries, and academic remarks.
- Turtle interface usability and local text-file persistence.

## Correctness and privacy
Preserve the documented grading rules unless a change is discussed first. Test normal values, boundaries, incomplete records, and malformed saved data. Check duplicate IDs and accidental overwrites. Use fictional student records only; never commit real IDs, names, or grades.

Use branches such as `feature/student-search` or `fix/gwa-calculation`. For calculation changes, include sample inputs and expected results in the pull request.
