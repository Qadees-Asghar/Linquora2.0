# Release Notes - v2.0.0

## New Features in v2.0.0

- Search patient by name
- Search doctor by department
- View appointments filtered by patient or doctor
- Full docstrings on all functions
- Improved menu formatting with version header
- Bulk patient deletion with comma-separated IDs
- Bulk room discharge with comma-separated IDs
- Room capacity enforcement by type
- Auto-cleanup of room assignments on patient deletion
- if __name__ == "__main__" guard added

## Bug Fixes

- Fixed room data persistence across sessions
- Fixed patient ID display in appointments view

## Known Limitations

- IDs are sequential and do not re-sequence after deletion
- No login/authentication system
- Data stored in plain text (not encrypted)