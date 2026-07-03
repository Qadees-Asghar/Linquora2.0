# =====================================================
# HOSPITAL MANAGEMENT SYSTEM
# Linquora 2.0
# =====================================================
# Author      : Qadees Asghar
# Version     : 2.0.0
# License     : MIT
# Repository  : https://github.com/Qadees-Asghar/Linquora2.0
# Description : A CLI-based hospital management system
#               for managing patients, doctors, appointments,
#               and rooms with persistent file storage.
# =====================================================

PATIENT_FILE     = "patients.txt"
DOCTOR_FILE      = "doctors.txt"
APPOINTMENT_FILE = "appointments.txt"
ROOM_FILE        = "rooms.txt"

# =====================================================
#                  COMMON FUNCTIONS
# =====================================================

def load_data(file):
    """
    Load records from a pipe-delimited text file into a dictionary.

    Args:
        file (str): Path to the data file.

    Returns:
        dict: Dictionary where keys are record IDs and values are field lists.
    """
    data = {}
    try:
        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if parts and parts[0]:
                    data[parts[0]] = parts[1:]
    except FileNotFoundError:
        pass
    return data


def save_data(file, data):
    """
    Save an in-memory dictionary to a pipe-delimited text file.

    Args:
        file (str): Path to the data file.
        data (dict): Dictionary of records to save.
    """
    with open(file, "w") as f:
        if file == ROOM_FILE:
            for k, v in data.items():
                f.write(k + "|" + v[0] + "|" + str(v[1]) + "|" + ",".join(v[2]) + "\n")
        else:
            for k, v in data.items():
                f.write(k + "|" + "|".join(v) + "\n")


def generate_id(data):
    """
    Generate a simple sequential numeric ID.

    Args:
        data (dict): Existing records dictionary.

    Returns:
        str: New unique ID as a string.
    """
    return str(len(data) + 1)


# Load all data on startup
patients     = load_data(PATIENT_FILE)
doctors      = load_data(DOCTOR_FILE)
appointments = load_data(APPOINTMENT_FILE)
rooms        = {}

# Load rooms with patient list (custom format with nested comma list)
try:
    with open(ROOM_FILE, "r") as f:
        for line in f:
            parts        = line.strip().split("|")
            room_num     = parts[0]
            room_type    = parts[1]
            max_capacity = int(parts[2])
            patient_ids  = parts[3].split(",") if len(parts) > 3 and parts[3] else []
            rooms[room_num] = [room_type, max_capacity, patient_ids]
except FileNotFoundError:
    pass

# =====================================================
#                  PATIENT MODULE
# =====================================================

def add_patient():
    """Register a new patient with full details and save to file."""
    pid = generate_id(patients)
    patients[pid] = [
        input("Enter patient name: "),
        input("Enter age: "),
        input("Enter gender: "),
        input("Enter CNIC: "),
        input("Enter phone number: "),
        input("Enter disease: ")
    ]
    save_data(PATIENT_FILE, patients)
    print(f"Patient {patients[pid][0]} has been registered with ID {pid}.")


def view_patients():
    """Display all registered patients."""
    if not patients:
        print("No patients found.")
        return
    for pid, p in patients.items():
        print(f"ID:{pid} | Name:{p[0]} | Age:{p[1]} | Disease:{p[5]}")


def update_patient():
    """Update the disease field of an existing patient."""
    pid = input("Enter Patient ID to update: ")
    if pid in patients:
        patients[pid][5] = input("Enter new disease: ")
        save_data(PATIENT_FILE, patients)
        print(f"Patient {patients[pid][0]} updated successfully.")
    else:
        print("Patient not found.")


def delete_patient():
    """Delete one or more patients by ID (comma-separated for bulk delete)."""
    ids       = input("Enter Patient ID(s) to delete (comma-separated for multiple): ").split(",")
    deleted   = []
    not_found = []
    for pid in ids:
        pid = pid.strip()
        if pid in patients:
            name = patients[pid][0]
            del patients[pid]
            for r in rooms.values():
                if pid in r[2]:
                    r[2].remove(pid)
            deleted.append(name)
        else:
            not_found.append(pid)
    save_data(PATIENT_FILE, patients)
    save_data(ROOM_FILE, rooms)
    if deleted:
        print("Deleted patients:", ", ".join(deleted))
    if not_found:
        print("Patient IDs not found:", ", ".join(not_found))


def search_patient():
    """Search for patients by name using case-insensitive partial match."""
    query   = input("Enter patient name to search: ").lower()
    results = [(pid, p) for pid, p in patients.items() if query in p[0].lower()]
    if not results:
        print("No matching patients found.")
    else:
        for pid, p in results:
            print(f"ID:{pid} | Name:{p[0]} | Age:{p[1]} | Disease:{p[5]}")


def patient_menu():
    """Display and handle the patient management menu."""
    while True:
        print("""
==========================
    Patient Management
==========================

1 Register Patient
2 View Patients
3 Update Patient
4 Delete Patient
5 Search Patient
6 Back
""")
        c = input("Select: ")
        if   c == "1": add_patient()
        elif c == "2": view_patients()
        elif c == "3": update_patient()
        elif c == "4": delete_patient()
        elif c == "5": search_patient()
        elif c == "6": break

# =====================================================
#                  DOCTOR MODULE
# =====================================================

def add_doctor():
    """Add a new doctor with name and department."""
    did = generate_id(doctors)
    doctors[did] = [
        input("Enter doctor name: "),
        input("Enter department: ")
    ]
    save_data(DOCTOR_FILE, doctors)
    print(f"Doctor {doctors[did][0]} added with ID {did}.")


def view_doctors():
    """Display all registered doctors."""
    if not doctors:
        print("No doctors found.")
        return
    for did, d in doctors.items():
        print(f"ID:{did} | Name:{d[0]} | Department:{d[1]}")


def update_doctor():
    """Update the department of an existing doctor."""
    did = input("Enter Doctor ID to update: ")
    if did in doctors:
        doctors[did][1] = input("Enter new department: ")
        save_data(DOCTOR_FILE, doctors)
        print(f"Doctor {doctors[did][0]} updated successfully.")
    else:
        print("Doctor not found.")


def delete_doctor():
    """Delete a doctor by ID."""
    did = input("Enter Doctor ID to delete: ")
    if did in doctors:
        name = doctors[did][0]
        del doctors[did]
        save_data(DOCTOR_FILE, doctors)
        print(f"Doctor {name} has been deleted.")
    else:
        print("Doctor not found.")


def search_doctor():
    """Search doctors by department using case-insensitive partial match."""
    query   = input("Enter department to search: ").lower()
    results = [(did, d) for did, d in doctors.items() if query in d[1].lower()]
    if not results:
        print("No matching doctors found.")
    else:
        for did, d in results:
            print(f"ID:{did} | Name:{d[0]} | Department:{d[1]}")


def doctor_menu():
    """Display and handle the doctor management menu."""
    while True:
        print("""
============================
    Doctor Management
============================

1 Add Doctor
2 View Doctors
3 Update Doctor
4 Delete Doctor
5 Search by Department
6 Back
""")
        c = input("Select: ")
        if   c == "1": add_doctor()
        elif c == "2": view_doctors()
        elif c == "3": update_doctor()
        elif c == "4": delete_doctor()
        elif c == "5": search_doctor()
        elif c == "6": break

# =====================================================
#                APPOINTMENT MODULE
# =====================================================

def book_appointment():
    """Book an appointment between a patient and a doctor with time."""
    aid  = generate_id(appointments)
    pid  = input("Enter Patient ID: ")
    did  = input("Enter Doctor ID: ")
    time = input("Enter Time (HH:MM): ")
    if pid in patients and did in doctors:
        appointments[aid] = [pid, did, time]
        save_data(APPOINTMENT_FILE, appointments)
        print(f"Appointment booked for {patients[pid][0]} with Dr. {doctors[did][0]} at {time}.")
    else:
        print("Invalid Patient or Doctor ID.")


def view_appointments():
    """Display all scheduled appointments with resolved patient and doctor names."""
    if not appointments:
        print("No appointments found.")
        return
    for aid, a in appointments.items():
        pname = patients.get(a[0], ["Unknown"])[0]
        dname = doctors.get(a[1], ["Unknown"])[0]
        print(f"ID:{aid} | Patient:{pname} ({a[0]}) | Doctor:{dname} ({a[1]}) | Time:{a[2]}")


def view_appointments_by_patient():
    """View all appointments for a specific patient ID."""
    pid     = input("Enter Patient ID: ")
    results = [(aid, a) for aid, a in appointments.items() if a[0] == pid]
    if not results:
        print("No appointments found for this patient.")
    else:
        for aid, a in results:
            dname = doctors.get(a[1], ["Unknown"])[0]
            print(f"Appointment ID:{aid} | Doctor:{dname} | Time:{a[2]}")


def view_appointments_by_doctor():
    """View all appointments for a specific doctor ID."""
    did     = input("Enter Doctor ID: ")
    results = [(aid, a) for aid, a in appointments.items() if a[1] == did]
    if not results:
        print("No appointments found for this doctor.")
    else:
        for aid, a in results:
            pname = patients.get(a[0], ["Unknown"])[0]
            print(f"Appointment ID:{aid} | Patient:{pname} | Time:{a[2]}")


def cancel_appointment():
    """Cancel an appointment by its ID."""
    aid = input("Enter Appointment ID to cancel: ")
    if aid in appointments:
        del appointments[aid]
        save_data(APPOINTMENT_FILE, appointments)
        print("Appointment cancelled.")
    else:
        print("Appointment not found.")


def appointment_menu():
    """Display and handle the appointment management menu."""
    while True:
        print("""
============================
    Appointment Management
============================

1 Book Appointment
2 View All Appointments
3 View Appointments by Patient
4 View Appointments by Doctor
5 Cancel Appointment
6 Clear All Appointments
7 Back
""")
        c = input("Select: ")
        if   c == "1": book_appointment()
        elif c == "2": view_appointments()
        elif c == "3": view_appointments_by_patient()
        elif c == "4": view_appointments_by_doctor()
        elif c == "5": cancel_appointment()
        elif c == "6":
            appointments.clear()
            save_data(APPOINTMENT_FILE, appointments)
            print("All appointments cleared.")
        elif c == "7": break

# =====================================================
#                  ROOM MODULE
# =====================================================

ROOM_CAPACITY = {
    "General":      5,
    "Semi-Private": 2,
    "Private":      1,
    "Icu":          1
}


def add_room():
    """Add a new room with auto-assigned capacity based on room type."""
    rn    = input("Enter Room Number: ")
    rtype = input("Enter Room Type (General/Semi-Private/Private/ICU): ").capitalize()
    if rtype == "Icu":
        rtype = "Icu"
    if rtype not in ROOM_CAPACITY:
        print("Invalid room type! Choose: General, Semi-Private, Private, ICU")
        return
    rooms[rn] = [rtype, ROOM_CAPACITY[rtype], []]
    save_data(ROOM_FILE, rooms)
    print(f"{rtype} Room {rn} added successfully with capacity {ROOM_CAPACITY[rtype]}.")


def allot_room():
    """Allot an available room to a patient based on selected room type."""
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Invalid Patient ID!")
        return

    for r in rooms.values():
        if pid in r[2]:
            print(f"{patients[pid][0]} already has a room assigned.")
            return

    print("Available room types: General, Semi-Private, Private, ICU")
    room_type = input("Which type of room do you want to allot? ").capitalize()
    if room_type not in ROOM_CAPACITY:
        print("Invalid room type!")
        return

    for rn, r in rooms.items():
        if r[0] == room_type and len(r[2]) < r[1]:
            r[2].append(pid)
            save_data(ROOM_FILE, rooms)
            print(f"{patients[pid][0]} has been assigned {room_type} Room {rn}.")
            return

    print(f"Sorry, all {room_type} rooms are full.")


def discharge_room():
    """Discharge a single patient from a specified room."""
    rn = input("Enter Room Number to vacate a patient: ")
    if rn in rooms:
        if not rooms[rn][2]:
            print(f"Room {rn} is already empty.")
            return
        print("Patients in room:")
        for pid in rooms[rn][2]:
            print(f"  {pid}: {patients.get(pid, ['Unknown'])[0]}")
        pid_to_remove = input("Enter Patient ID to remove: ")
        if pid_to_remove in rooms[rn][2]:
            rooms[rn][2].remove(pid_to_remove)
            save_data(ROOM_FILE, rooms)
            print(f"Patient {patients.get(pid_to_remove, ['Unknown'])[0]} removed from Room {rn}.")
        else:
            print("Patient not found in this room.")
    else:
        print("Room not found.")


def discharge_multiple_from_room():
    """Discharge multiple patients from a room using comma-separated IDs."""
    rn = input("Enter Room Number: ")
    if rn not in rooms:
        print("Room not found.")
        return
    if not rooms[rn][2]:
        print(f"Room {rn} is already empty.")
        return
    print("Patients in room:")
    for pid in rooms[rn][2]:
        print(f"  {pid}: {patients.get(pid, ['Unknown'])[0]}")
    ids        = input("Enter Patient IDs to discharge (comma-separated): ").split(",")
    discharged = []
    not_found  = []
    for pid in ids:
        pid = pid.strip()
        if pid in rooms[rn][2]:
            rooms[rn][2].remove(pid)
            discharged.append(patients.get(pid, ["Unknown"])[0])
        else:
            not_found.append(pid)
    save_data(ROOM_FILE, rooms)
    if discharged:
        print("Discharged from room:", ", ".join(discharged))
    if not_found:
        print("Patient IDs not found in room:", ", ".join(not_found))


def view_rooms():
    """Display all rooms with current occupancy and remaining capacity."""
    if not rooms:
        print("No rooms found.")
        return
    for rn, r in rooms.items():
        patient_list    = [patients[pid][0] for pid in r[2] if pid in patients]
        remaining_slots = r[1] - len(r[2])
        patient_info    = ", ".join(patient_list) if patient_list else "Vacant"
        print(f"Room {rn} | Type: {r[0]} | Patients: {patient_info} | Remaining Slots: {remaining_slots}")


def room_menu():
    """Display and handle the room management menu."""
    while True:
        print("""
==========================
    Room Management
==========================

1 Add Room
2 Allot Room
3 Discharge Patient from Room
4 Discharge Multiple Patients from Room
5 View Rooms
6 Back
""")
        c = input("Select: ")
        if   c == "1": add_room()
        elif c == "2": allot_room()
        elif c == "3": discharge_room()
        elif c == "4": discharge_multiple_from_room()
        elif c == "5": view_rooms()
        elif c == "6": break

# =====================================================
#                    MAIN MENU
# =====================================================

def main_menu():
    """Display and handle the main system menu."""
    while True:
        print("""
=================================
 Hospital Management System
 Linquora 2.0
=================================

1 Patient Management
2 Doctor Management
3 Appointment Management
4 Room Management
5 Exit
""")
        c = input("Select: ")
        if   c == "1": patient_menu()
        elif c == "2": doctor_menu()
        elif c == "3": appointment_menu()
        elif c == "4": room_menu()
        elif c == "5":
            print("System Closed.")
            break


if __name__ == "__main__":
    main_menu()