# 🏥 Linquora 2.0 — Hospital Management System

<p align="center">
  <b>A smart CLI-based hospital management system built with Python</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Qadees-Asghar/Linquora2.0?style=social">
  <img src="https://img.shields.io/github/forks/Qadees-Asghar/Linquora2.0?style=social">
  <img src="https://img.shields.io/github/issues/Qadees-Asghar/Linquora2.0">
  <img src="https://img.shields.io/github/last-commit/Qadees-Asghar/Linquora2.0">
</p>

---

## 📋 Overview

**Linquora 2.0** is a simple and efficient command-line based Hospital Management System built in Python. It allows hospital staff to manage patients, doctors, appointments, and rooms — all stored persistently using flat text files. The system focuses on core Python concepts like file handling, modular design, and clean menu-driven interaction.

---

## ✨ Features

### 👤 Patient Management
- Register new patients (Name, Age, Gender, CNIC, Phone, Disease)
- View all registered patients
- Update patient disease information
- Delete single or multiple patients (comma-separated IDs)
- Auto-removes patient from assigned room on deletion

### 🩺 Doctor Management
- Add doctors with their department
- View all doctors
- Update doctor's department
- Delete doctors

### 📅 Appointment Management
- Book appointments (links Patient ID + Doctor ID + Time)
- View all appointments
- Cancel individual appointments
- Clear all appointments at once

### 🛏️ Room Management
- Add rooms with type: `General`, `Semi-Private`, `Private`, `ICU`
- Auto-enforced capacity per room type:
  | Room Type | Capacity |
  |-----------|----------|
  | General | 5 patients |
  | Semi-Private | 2 patients |
  | Private | 1 patient |
  | ICU | 1 patient |
- Allot rooms to patients (prevents double-booking)
- Discharge single or multiple patients from a room
- View all rooms with occupancy and remaining slots

---

## 📁 File Structure

```
Linquora2.0/
├── hospital_management_system.py   # Main application file
├── patients.txt                    # Patient data (auto-generated)
├── doctors.txt                     # Doctor data (auto-generated)
├── appointments.txt                # Appointment data (auto-generated)
├── rooms.txt                       # Room data (auto-generated)
├── CONTRIBUTORS.md                 # Project contributors
└── README.md                       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/Qadees-Asghar/Linquora2.0.git

# Navigate to the project directory
cd Linquora2.0

# Run the system
python hospital_management_system.py
```

---

## 🖥️ Usage

On launch, you will see the main menu:

```
=================================
 Hospital Management System
=================================

1 Patient Management
2 Doctor Management
3 Appointment Management
4 Room Management
5 Exit
```

Navigate using number keys. All data is automatically saved to `.txt` files after every operation.

---

## 🗂️ Data Storage

All data is persisted in pipe-delimited (`|`) text files:

| File | Contents |
|------|----------|
| `patients.txt` | ID \| Name \| Age \| Gender \| CNIC \| Phone \| Disease |
| `doctors.txt` | ID \| Name \| Department |
| `appointments.txt` | ID \| Patient ID \| Doctor ID \| Time |
| `rooms.txt` | Room No \| Type \| Capacity \| Patient IDs |

---

## 🛠️ Built With

- **Language:** Python 3.x
- **Storage:** File-based (`.txt` flat files)
- **Interface:** Command-Line (CLI)
- **Concepts:** File I/O, Modular functions, Menu-driven architecture

---

## 👨‍💻 Author

**Qadees Asghar**
- GitHub: [@Qadees-Asghar](https://github.com/Qadees-Asghar)

---

## 🤖 AI Assistance

This project was developed with the assistance of **Antigravity** — Google DeepMind's AI coding assistant.

---

## 📄 License

This project is licensed under the MIT License.