# Manual Test Plan - Linquora 2.0

## Patient Module Tests

| Test Case | Steps | Expected Result |
|-----------|-------|-----------------|
| Register patient | Menu 1 > 1 > fill details | Patient registered with ID |
| View patients | Menu 1 > 2 | List of all patients shown |
| Update patient | Menu 1 > 3 > enter ID | Disease updated |
| Delete single patient | Menu 1 > 4 > enter ID | Patient deleted |
| Delete multiple patients | Menu 1 > 4 > enter 1,2 | Both patients deleted |
| Search patient | Menu 1 > 5 > enter name | Matching patients shown |
| Delete non-existent ID | Menu 1 > 4 > enter 999 | Not found message |

## Doctor Module Tests

| Test Case | Steps | Expected Result |
|-----------|-------|-----------------|
| Add doctor | Menu 2 > 1 > fill details | Doctor added with ID |
| View doctors | Menu 2 > 2 | List of doctors shown |
| Update department | Menu 2 > 3 > enter ID | Department updated |
| Delete doctor | Menu 2 > 4 > enter ID | Doctor removed |
| Search by department | Menu 2 > 5 > enter dept | Matching doctors shown |

## Appointment Module Tests

| Test Case | Steps | Expected Result |
|-----------|-------|-----------------|
| Book valid appointment | Menu 3 > 1 > valid PID, DID | Appointment booked |
| Book with invalid IDs | Menu 3 > 1 > bad IDs | Error message |
| View appointments | Menu 3 > 2 | All appointments with names |
| Filter by patient | Menu 3 > 3 > enter PID | Patient appointments shown |
| Filter by doctor | Menu 3 > 4 > enter DID | Doctor appointments shown |
| Cancel appointment | Menu 3 > 5 > enter AID | Appointment cancelled |
| Clear all | Menu 3 > 6 | All appointments removed |

## Room Module Tests

| Test Case | Steps | Expected Result |
|-----------|-------|-----------------|
| Add General room | Menu 4 > 1 > General | Room added, capacity 5 |
| Add ICU room | Menu 4 > 1 > ICU | Room added, capacity 1 |
| Allot room | Menu 4 > 2 > valid PID | Patient assigned to room |
| Double allot | Menu 4 > 2 > same PID | Already assigned message |
| Full room allot | Fill room, try again | Room full message |
| Discharge patient | Menu 4 > 3 | Patient removed from room |
| Bulk discharge | Menu 4 > 4 > IDs | Multiple patients discharged |
| View rooms | Menu 4 > 5 | Room list with occupancy |