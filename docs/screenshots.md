# Screenshots

## Main Menu

The main menu provides access to all four management modules:

`
=================================
 Hospital Management System
 Linquora 2.0
=================================

1 Patient Management
2 Doctor Management
3 Appointment Management
4 Room Management
5 Exit
`

## Patient Management Menu

`
==========================
    Patient Management
==========================

1 Register Patient
2 View Patients
3 Update Patient
4 Delete Patient
5 Search Patient
6 Back
`

## Room View Example

`
Room 101 | Type: General | Patients: Ali Khan, Sara Ahmed | Remaining Slots: 3
Room 102 | Type: ICU | Patients: Bilal Raza | Remaining Slots: 0
Room 103 | Type: Private | Patients: Vacant | Remaining Slots: 1
`
"@

# 42
C "docs/design_decisions.md" "docs: document key design decisions" @"
# Design Decisions

## Why File-Based Storage?

File-based storage (plain .txt files) was chosen because:
1. No external dependencies - pure Python standard library
2. Easy to inspect and understand the stored data
3. Portable - works on any OS without setup
4. Suitable for a learning/demonstration project

Trade-off: Not suitable for concurrent access or large datasets.

## Why Sequential IDs?

Simple auto-increment IDs were chosen for:
1. Simplicity of implementation
2. Easy to reference in the CLI

Trade-off: IDs are not re-used after deletion, leaving gaps.

## Why Pipe Delimiter?

The pipe (|) character was chosen because:
1. It rarely appears in natural language text like names
2. More readable than CSV comma-separated format in raw files

Trade-off: If a user enters | in a field, it would break parsing.

## Why Procedural (Not OOP)?

A procedural, function-based design was chosen to:
1. Keep the code accessible and easy to understand
2. Demonstrate core Python concepts (file I/O, functions, dicts)
3. Avoid the overhead of class design for a small system

The v3.0.0 roadmap item includes a full OOP refactor.

## Why In-Memory Dict Loading?

All data is loaded into memory on startup so that:
1. Every function has fast O(1) access to records
2. No repeated file reads during a session
3. Save operations are explicit and controlled