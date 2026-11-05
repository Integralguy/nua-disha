# Nua Disha — Basic Test Plan

| Test ID | Test case | Expected result |
|---|---|---|
| T01 | Open homepage | Homepage and navigation display |
| T02 | Open Explore Skills | Six course cards display |
| T03 | Open a course card | Correct course details display |
| T04 | Submit registration with an empty field | Browser/server validation prevents incomplete submission |
| T05 | Submit valid registration with MySQL running | Record is saved and success page displays |
| T06 | Submit registration with database unavailable | Friendly error message displays |
| T07 | Open website on a narrow screen | Layout adapts for mobile |
| T08 | Open an invalid course URL | Custom 404 page displays |

## Testing approach
- Unit-level checks: validate course lookup and required form data.
- Integration checks: verify Flask can insert a registration into MySQL.
- System checks: navigate through homepage, catalogue, details and registration.
- Usability checks: verify labels, navigation clarity and responsive layout.
