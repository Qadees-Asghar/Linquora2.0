# Linquora 2.0 - Hospital Management System

A smart CLI-based hospital management system built with Python.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Stars](https://img.shields.io/github/stars/Qadees-Asghar/Linquora2.0?style=social)
![Forks](https://img.shields.io/github/forks/Qadees-Asghar/Linquora2.0?style=social)
![Issues](https://img.shields.io/github/issues/Qadees-Asghar/Linquora2.0)
![Last Commit](https://img.shields.io/github/last-commit/Qadees-Asghar/Linquora2.0)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Data Storage](#data-storage)
- [Built With](#built-with)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## Overview

Linquora 2.0 is a simple and efficient command-line based Hospital Management System built in Python. It allows hospital staff to manage patients, doctors, appointments, and rooms. All data is stored persistently using flat text files. The system focuses on core Python concepts like file handling, modular design, and clean menu-driven interaction.

---

## Features

### Patient Management
- Register new patients (Name, Age, Gender, CNIC, Phone, Disease)
- View all registered patients
- Update patient disease information
- Delete single or multiple patients using comma-separated IDs
- Auto-removes patient from assigned room on deletion

### Doctor Management
- Add doctors with their department
- View all doctors
- Update doctor department
- Delete doctors

### Appointment Management
- Book appointments linking Patient ID, Doctor ID, and Time
- View all appointments
- Cancel individual appointments
- Clear all appointments at once

### Room Management
- Add rooms with type: General, Semi-Private, Private, ICU
- Auto-enforced capacity per room type:

  | Room Type    | Max Capacity |
  |--------------|--------------|
  | General      | 5 patients   |
  | Semi-Private | 2 patients   |
  | Private      | 1 patient    |
  | ICU          | 1 patient    |

- Allot rooms to patients (prevents double-booking)
- Discharge single or multiple patients from a room
- View all rooms with occupancy and remaining slots

---

## File Structure

`
Linquora2.0/
|-- hospital_management_system.py   # Main application
|-- patients.txt                    # Patient records (auto-generated)
|-- doctors.txt                     # Doctor records (auto-generated)
|-- appointments.txt                # Appointment records (auto-generated)
|-- rooms.txt                       # Room records (auto-generated)
|-- CONTRIBUTORS.md                 # Contributors list
|-- CONTRIBUTING.md                 # Contribution guidelines
|-- CHANGELOG.md                    # Version history
|-- LICENSE                         # MIT License
|-- README.md                       # Project documentation
`

---

## Getting Started

### Prerequisites

- Python 3.x installed

### Installation

`ash
git clone https://github.com/Qadees-Asghar/Linquora2.0.git
cd Linquora2.0
python hospital_management_system.py
`

---

## Usage

On launch you will see the main menu:

`
=================================
 Hospital Management System
=================================

1 Patient Management
2 Doctor Management
3 Appointment Management
4 Room Management
5 Exit
`

Navigate using number keys. All data is automatically saved after every operation.

---

## Data Storage

All data is stored in pipe-delimited text files:

| File               | Format                                          |
|--------------------|------------------------------------------------|
| patients.txt       | ID|Name|Age|Gender|CNIC|Phone|Disease          |
| doctors.txt        | ID|Name|Department                              |
| appointments.txt   | ID|PatientID|DoctorID|Time                     |
| rooms.txt          | RoomNo|Type|Capacity|PatientIDs               |

---

## Built With

- Language: Python 3.x
- Storage: File-based flat text files
- Interface: Command-Line (CLI)
- Concepts: File I/O, Modular functions, Menu-driven architecture

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Author

Qadees Asghar
- GitHub: https://github.com/Qadees-Asghar

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.