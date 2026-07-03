# Edge Cases - Linquora 2.0

## Patient Module Edge Cases

- Deleting a patient who is assigned to a room:
  System removes patient from room automatically.

- Entering empty name or fields:
  System accepts empty strings (no validation currently).

- Deleting a patient referenced in an appointment:
  Appointment still exists but will show 'Unknown' for patient name.

## Doctor Module Edge Cases

- Deleting a doctor referenced in an appointment:
  Appointment still exists but will show 'Unknown' for doctor name.

## Appointment Module Edge Cases

- Booking the same time slot twice for the same doctor:
  System allows it (no conflict detection yet - planned for v2.1.0).

- Clearing all appointments does not affect patient/doctor records.

## Room Module Edge Cases

- Adding a room number that already exists:
  System overwrites the existing room entry.

- Patient assigned to room, then patient deleted:
  Room assignment is cleaned up automatically.

- Discharging a patient not in the specified room:
  System shows 'Patient not found in this room'.