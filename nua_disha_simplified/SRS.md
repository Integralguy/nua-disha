# Software Requirements Specification — Nua Disha

## 1. Purpose
Nua Disha is a web-based vocational learning discovery and registration concept for KISS students in Odisha. It helps students view practical skill courses and submit their interest in a selected course.

## 2. Scope
The MVP contains a homepage, course catalogue, course detail pages, student registration, About and Contact pages. It stores registration details in a MySQL database.

## 3. User
- Student: visits the website, explores courses and submits registration details.

## 4. Functional requirements
- FR1: The system shall display an introduction to Nua Disha on the homepage.
- FR2: The system shall display available vocational courses.
- FR3: The system shall show the description and expected learning outcome of a selected course.
- FR4: The system shall allow a student to submit name, email, phone number and selected course.
- FR5: The system shall validate required fields before storing a registration.
- FR6: The system shall save valid registration details in MySQL.
- FR7: The system shall show a success message after successful registration.

## 5. Non-functional requirements
- Usability: navigation and forms should be easy to understand.
- Responsiveness: pages should adapt to mobile and desktop screens.
- Performance: normal pages should load without unnecessary processing.
- Reliability: invalid form submissions should not be stored.
- Security: use parameterized SQL queries and keep database credentials outside source code.

## 6. Constraints and assumptions
- The prototype assumes a working local Flask and MySQL installation.
- Course catalogue data is maintained in the application code.
- The prototype is for academic demonstration and does not include student login or administrator access.
