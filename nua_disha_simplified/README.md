# Nua Disha — Simplified Vocational Learning Website

A compact full-stack academic project concept for vocational skill discovery and student registration for KISS students in Odisha.

## Features
- Responsive homepage with modern forest-green, warm-cream and orange visual identity
- Browse six vocational learning paths
- Individual course detail pages
- Student registration form
- Flask backend and MySQL enrollment storage
- Basic server-side validation and parameterized SQL query

## Technology
HTML, CSS, JavaScript, Python Flask, MySQL.

## Run locally

### 1. Requirements
Install Python 3.10 or newer and MySQL Server. Open this folder in VS Code.

### 2. Create and activate a virtual environment
Windows PowerShell:
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install packages
```powershell
pip install -r requirements.txt
```

### 4. Create the database
Open MySQL Workbench, open `schema.sql`, and execute it. This creates the `nua_disha` database and `enrollments` table.

### 5. Set database environment variables
PowerShell example:
```powershell
$env:DB_HOST="localhost"
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_NAME="nua_disha"
$env:SECRET_KEY="use-a-random-secret"
```
Use the password configured on your own MySQL installation.

### 6. Start the website
```powershell
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

## Project structure
```text
nua_disha_simplified/
├── app.py
├── schema.sql
├── requirements.txt
├── .env.example
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── courses.html
│   ├── course_detail.html
│   ├── register.html
│   ├── success.html
│   ├── about.html
│   ├── contact.html
│   └── 404.html
└── static/
    ├── css/style.css
    └── js/main.js
```

## Scope and academic note
This is a classroom demonstration MVP, not a production student-management system. Course information is stored in a simple Python list; student enrollment records are stored in MySQL. Authentication, admin management, trainer management, certificates, payments and notifications are intentionally excluded to keep the project small and explainable.

Before any real deployment, add CSRF protection, stronger validation, secure secret management, privacy notices, access controls, database migrations, backups and production server configuration.
