# Installation Guide

## System Requirements

- Operating System: Windows, macOS, or Linux
- Python: 3.6 or higher
- Disk Space: < 1 MB
- RAM: Any modern system

## Installing Python

### Windows
1. Download Python from https://python.org/downloads
2. Run the installer
3. Make sure to check 'Add Python to PATH'
4. Verify: open Command Prompt and run: python --version

### Linux/macOS
Python is usually pre-installed. Verify with:
`ash
python3 --version
`

## Installing Linquora 2.0

### Method 1 - Clone from GitHub (recommended)
`ash
git clone https://github.com/Qadees-Asghar/Linquora2.0.git
cd Linquora2.0
python hospital_management_system.py
`

### Method 2 - Download ZIP
1. Go to https://github.com/Qadees-Asghar/Linquora2.0
2. Click Code > Download ZIP
3. Extract the ZIP file
4. Open a terminal in the extracted folder
5. Run: python hospital_management_system.py

## Verifying Installation

If the system starts and shows the main menu, installation is successful.

## Troubleshooting

### 'python' is not recognized
Use 'python3' instead of 'python' on some Linux/macOS systems.

### Permission denied on files
Ensure you have write permission in the project directory.