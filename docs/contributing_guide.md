# Developer Contributing Guide

## Setting Up Development Environment

`ash
git clone https://github.com/Qadees-Asghar/Linquora2.0.git
cd Linquora2.0
python hospital_management_system.py
`

No virtual environment needed - no external dependencies.

## Branching Strategy

- main: stable production code
- develop: active development branch
- feature/xxx: new features
- fix/xxx: bug fixes
- docs/xxx: documentation changes

## Coding Standards

Follow PEP 8:
- 4 spaces indentation (no tabs)
- Max line length: 100 characters
- Blank lines between functions
- Docstrings on all public functions
- Meaningful variable names

## Adding a New Module

To add a new module (e.g., billing):

1. Define a new file constant:
   BILLING_FILE = 'billing.txt'

2. Load data at startup:
   billing = load_data(BILLING_FILE)

3. Implement CRUD functions with docstrings

4. Create a menu function

5. Add the module to main_menu()

6. Update README.md with the new feature

7. Update CHANGELOG.md

8. Update docs/

## Testing

Currently manual testing only. Use the test plan in tests/test_plan.md.
Automated pytest tests are planned for v2.1.0.

## Commit Messages

Format: type: short description

Examples:
- feat: add billing module
- fix: prevent duplicate room assignment
- docs: update installation guide
- refactor: extract validation logic
- test: add patient module test plan
- chore: update .gitignore