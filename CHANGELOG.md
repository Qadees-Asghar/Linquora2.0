# Changelog

All notable changes to Linquora 2.0 will be documented here.

---

## [2.0.0] - 2024

### Added
- Patient registration with CNIC and phone number fields
- Bulk patient deletion using comma-separated IDs
- Room management with capacity enforcement
- Room types: General (5), Semi-Private (2), Private (1), ICU (1)
- Bulk patient discharge from rooms
- Appointment system linking patients and doctors
- Clear all appointments feature
- Auto-removal of patient from room on patient deletion
- Persistent data storage using flat text files

### Changed
- Upgraded from Linquora 1.0 architecture
- Modular function-based design
- Improved menu formatting

### Fixed
- Patient ID collision on deletion
- Room occupancy tracking across sessions

---

## [1.0.0] - Initial Release

### Added
- Basic patient and doctor management
- Simple appointment booking
- File-based data persistence