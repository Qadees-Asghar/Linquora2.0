# Troubleshooting Guide

## Common Issues

### System starts but shows no patients/doctors/rooms

This is normal on first run. The system creates empty data files.
You need to add records manually through the menus.

### Error: 'python' is not recognized

Use 'python3' instead:
`ash
python3 hospital_management_system.py
`

### Data not saving between runs

Ensure the script has write access to its directory.
Check that you are running the script from within the project folder.

### Patient ID not found after deletion

Patient IDs are not re-assigned after deletion.
If patient 2 is deleted, ID 2 does not get reassigned.
Check remaining IDs using View Patients.

### Room shows wrong capacity

This can happen if the rooms.txt file was manually edited incorrectly.
Check the file format: RoomNumber|Type|Capacity|PatientIDs

### Appointment shows Unknown for patient/doctor name

This means the patient or doctor ID referenced in the appointment
no longer exists. Cancel the appointment and rebook.

## Resetting the System

To start fresh, delete all .txt files:
- patients.txt
- doctors.txt
- appointments.txt
- rooms.txt

The system will recreate them empty on next run.