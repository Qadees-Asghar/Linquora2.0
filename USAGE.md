# Usage Guide

## Starting the System

`ash
python hospital_management_system.py
`

---

## Patient Workflow

1. Go to Patient Management (option 1 from main menu)
2. Select Register Patient and fill in the details
3. Note the Patient ID shown after registration
4. Use View Patients to see all registered patients

## Doctor Workflow

1. Go to Doctor Management (option 2)
2. Add doctors with their name and department
3. Note the Doctor ID for booking appointments

## Booking an Appointment

1. Go to Appointment Management (option 3)
2. Select Book Appointment
3. Enter the Patient ID and Doctor ID
4. Enter the time in HH:MM format

## Room Assignment

1. First add rooms via Room Management > Add Room
2. Select room type (General, Semi-Private, Private, ICU)
3. Use Allot Room to assign a patient to an available room
4. Use View Rooms to see occupancy status

## Discharging Patients

- Single discharge: Room Management > Discharge Patient from Room
- Multiple discharge: Room Management > Discharge Multiple Patients from Room
  - Enter IDs separated by commas: 1,3,5