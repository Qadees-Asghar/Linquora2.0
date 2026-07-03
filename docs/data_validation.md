# Data Validation

## Current Validation

### Patient Registration
- Patient ID: auto-generated, always valid
- All fields accept any string input (no format enforcement)

### Appointment Booking
- Validates Patient ID exists in patients dict
- Validates Doctor ID exists in doctors dict
- If either is invalid, booking is rejected with an error message

### Room Allotment
- Validates Patient ID exists
- Validates patient is not already assigned to any room
- Validates room type is one of: General, Semi-Private, Private, ICU
- Validates selected room has remaining capacity

### Room Addition
- Validates room type against the ROOM_CAPACITY dictionary

## Known Gaps (Planned for Future Versions)

- No format validation on CNIC (should be XX-XXXXXXX-X)
- No format validation on phone number
- No format validation on time (HH:MM) in appointments
- No minimum/maximum age validation
- No empty-field prevention
- No duplicate patient prevention (same name + CNIC)
- No duplicate room number prevention

These gaps are documented in the roadmap and planned for v2.1.0.