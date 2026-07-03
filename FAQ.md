# Frequently Asked Questions

## Q: Where is my data stored?
A: All data is stored in .txt files in the same directory as the script:
   patients.txt, doctors.txt, appointments.txt, rooms.txt

## Q: What happens if I delete a patient?
A: The patient is removed from the system and automatically unassigned from any room they were in.

## Q: Can I have multiple patients in one room?
A: Yes, depending on room type. General rooms hold up to 5 patients,
   Semi-Private up to 2, while Private and ICU hold 1 each.

## Q: What if a room type is full?
A: The system will notify you and not assign the patient.
   You must either add more rooms or discharge existing patients.

## Q: Can I book multiple appointments for one patient?
A: Yes, there is no limit on how many appointments a patient can have.

## Q: What Python version is required?
A: Python 3.6 or higher is recommended.

## Q: Are there any external dependencies?
A: No. Linquora 2.0 uses only the Python standard library.