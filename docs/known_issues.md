# Known Issues

## Open Issues

### KI-001: Sequential IDs not reassigned after deletion
IDs are generated as len(dict) + 1, which means after deletion,
new records may get IDs that conflict with deleted record IDs if
the count drops. This is a minor bug in the current ID generation logic.
Workaround: Avoid deleting records unless necessary.
Fix planned: v2.1.0 - Use max(keys) + 1 instead of len(keys) + 1.

### KI-002: Empty string field entry not prevented
Users can press Enter without input, saving empty fields.
Workaround: Ensure all fields are filled before pressing Enter.
Fix planned: v2.1.0 - Add input validation loop.

### KI-003: Time format not validated for appointments
Any string is accepted as a time value.
Workaround: Always enter time in HH:MM format.
Fix planned: v2.1.0 - Add regex validation for time.

### KI-004: Pipe character in input breaks data files
If a user enters | in any field, the pipe-delimited file format breaks.
Workaround: Do not use | in any input field.
Fix planned: v2.2.0 - Escape or strip pipe characters from input.

## Resolved Issues

### RI-001: Patient not removed from room on deletion (FIXED in v2.0.0)
Previously, deleting a patient left their ID in room occupancy lists.
Fixed by iterating rooms in delete_patient() and removing the ID.