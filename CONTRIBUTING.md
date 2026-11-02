# Contributing to Student Management System

Thank you for helping improve this Python Turtle application for student records, academic grades, and General Weighted Average (GWA).

## Getting started

```bash
git clone https://github.com/joshuaarao42-arch/STUDENT-MANAGER.git
cd STUDENT-MANAGER
```

Follow the README for the supported Python version, dependencies, and launch instructions.

## What you can contribute

- Student registration, search, profile display, updates, and deletion.
- Grade entry and percentage-to-grade conversion.
- GWA calculations, term summaries, and academic remarks.
- Turtle interface usability and local data persistence.
- Bug fixes and clearer documentation.

## Project-specific guidelines

Preserve the documented grading rules unless a change is discussed and agreed upon. Test normal values, boundary values, incomplete records, and malformed saved data. Check duplicate student IDs and accidental overwrites. Use fictional student records only; never commit real student names, IDs, grades, or school records.

## Development standards

Follow the existing Python naming and formatting conventions. Keep input, calculation, storage, and display logic understandable. Validate user input before saving or calculating. Avoid changing the grading scale or file format without documenting the impact.

## Testing your changes

Run the application and test the affected student and grading workflows through the interface. For calculation changes, include sample inputs, step-by-step expected calculations, and expected outputs. Check that existing records still load correctly after storage-related changes.

## Branch and commit workflow

Use a focused branch such as `feature/student-search`, `fix/gwa-calculation`, or `docs/usage-guide`. Use commit prefixes such as `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, and `test:`.

## Opening a pull request

Describe the student or grading workflow affected, explain the change, and list the tests performed. Include screenshots for interface changes and example calculations for grading changes. Mention any changes to saved-data compatibility.

## Reporting issues

Provide reproduction steps, expected and actual results, Python version, and relevant error messages. Use fictional sample records and remove personal information from screenshots or logs.

## Code of conduct

Be respectful and constructive. Review code fairly, welcome questions, and keep discussions focused on improving the project.
