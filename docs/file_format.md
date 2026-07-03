# File Format Specification

## Overview

All Linquora 2.0 data files use pipe-delimited (|) plain text format.
Each line represents one record. The first field is always the ID.

---

## patients.txt

Format:
`
ID|Name|Age|Gender|CNIC|Phone|Disease
`

Field details:
- ID: Auto-generated sequential integer (string)
- Name: Full name (string)
- Age: Numeric age (string)
- Gender: Male/Female/Other (string)
- CNIC: Pakistani CNIC number (string, no validation)
- Phone: Phone number (string, no validation)
- Disease: Current disease or condition (string)

Example:
`
1|Ali Khan|30|Male|35202-1234567-1|0300-1234567|Fever
`

---

## doctors.txt

Format:
`
ID|Name|Department
`

Example:
`
1|Dr. Ahmed Raza|Cardiology
`

---

## appointments.txt

Format:
`
ID|PatientID|DoctorID|Time
`

Example:
`
1|1|2|10:30
`

---

## rooms.txt

Format:
`
RoomNumber|Type|MaxCapacity|PatientID1,PatientID2,...
`

Notes:
- PatientIDs field is comma-separated (no spaces)
- If room is empty, PatientIDs field is empty string
- MaxCapacity is stored as integer

Example:
`
101|General|5|1,3,5
102|ICU|1|2
103|Private|1|
`
"@

# 39
C "docs/api_reference.md" "docs: add internal API / function reference" @"
# Function Reference

## Common Functions

### load_data(file)
Load records from a pipe-delimited text file.

Parameters:
- file (str): Path to the data file

Returns:
- dict: {id: [field1, field2, ...]}

### save_data(file, data)
Save a dictionary to a pipe-delimited text file.

Parameters:
- file (str): Path to the data file
- data (dict): Records to write

### generate_id(data)
Generate the next sequential ID.

Parameters:
- data (dict): Existing records

Returns:
- str: New ID

---

## Patient Functions

### add_patient() -> None
Interactively registers a new patient.

### view_patients() -> None
Prints all patients to stdout.

### update_patient() -> None
Interactively updates a patient's disease.

### delete_patient() -> None
Interactively deletes one or more patients.

### search_patient() -> None
Searches patients by name substring.

---

## Doctor Functions

### add_doctor() -> None
Registers a new doctor.

### view_doctors() -> None
Lists all doctors.

### update_doctor() -> None
Updates a doctor's department.

### delete_doctor() -> None
Removes a doctor.

### search_doctor() -> None
Searches doctors by department substring.

---

## Appointment Functions

### book_appointment() -> None
Books a new appointment with validation.

### view_appointments() -> None
Lists all appointments with resolved names.

### view_appointments_by_patient() -> None
Filters appointments by patient ID.

### view_appointments_by_doctor() -> None
Filters appointments by doctor ID.

### cancel_appointment() -> None
Cancels an appointment by ID.

---

## Room Functions

### add_room() -> None
Adds a new room with type-based capacity.

### allot_room() -> None
Assigns a patient to a room.

### discharge_room() -> None
Removes one patient from a room.

### discharge_multiple_from_room() -> None
Removes multiple patients from a room.

### view_rooms() -> None
Displays room occupancy.