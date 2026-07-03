# Project Architecture

## Design Pattern

Linquora 2.0 follows a procedural, function-based architecture with
a menu-driven CLI interface. The system is divided into four main modules:

`
hospital_management_system.py
|
|-- Common Functions
|   |-- load_data()
|   |-- save_data()
|   |-- generate_id()
|
|-- Patient Module
|   |-- add_patient()
|   |-- view_patients()
|   |-- update_patient()
|   |-- delete_patient()
|   |-- search_patient()
|   |-- patient_menu()
|
|-- Doctor Module
|   |-- add_doctor()
|   |-- view_doctors()
|   |-- update_doctor()
|   |-- delete_doctor()
|   |-- search_doctor()
|   |-- doctor_menu()
|
|-- Appointment Module
|   |-- book_appointment()
|   |-- view_appointments()
|   |-- view_appointments_by_patient()
|   |-- view_appointments_by_doctor()
|   |-- cancel_appointment()
|   |-- appointment_menu()
|
|-- Room Module
|   |-- add_room()
|   |-- allot_room()
|   |-- discharge_room()
|   |-- discharge_multiple_from_room()
|   |-- view_rooms()
|   |-- room_menu()
|
|-- Main Menu
    |-- main_menu()
`

## Data Flow

1. On startup: load_data() reads .txt files into memory (dicts)
2. During runtime: all operations modify in-memory dicts
3. After each write operation: save_data() persists changes to disk
4. On exit: all data is already saved, no flush needed