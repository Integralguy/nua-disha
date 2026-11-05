import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-this-development-key")

COURSES = [
    {"id": 1, "name": "Digital Foundations", "category": "Digital Skills", "duration": "6 weeks",
     "level": "Beginner", "icon": "⌘", "description": "Build confidence with computers, internet safety, email and everyday digital tools.",
     "outcome": "Use computers and essential online tools independently."},
    {"id": 2, "name": "Tailoring & Fashion Design", "category": "Design & Craft", "duration": "8 weeks",
     "level": "Beginner", "icon": "✂", "description": "Learn basic stitching, measurements, garment construction and creative design.",
     "outcome": "Create simple garments and understand basic tailoring techniques."},
    {"id": 3, "name": "Handicrafts & Handloom", "category": "Design & Craft", "duration": "6 weeks",
     "level": "Beginner", "icon": "✿", "description": "Explore craft traditions, material handling, product making and finishing.",
     "outcome": "Make handcrafted products and understand quality finishing."},
    {"id": 4, "name": "Electrical Essentials", "category": "Technical Skills", "duration": "8 weeks",
     "level": "Beginner", "icon": "⚡", "description": "Understand basic electrical concepts, tools, components and safe practices.",
     "outcome": "Recognise common components and follow essential safety practices."},
    {"id": 5, "name": "Organic Farming", "category": "Agriculture", "duration": "6 weeks",
     "level": "Beginner", "icon": "♧", "description": "Learn soil care, composting, seed selection and sustainable growing methods.",
     "outcome": "Apply basic sustainable cultivation and composting methods."},
    {"id": 6, "name": "Entrepreneurship Basics", "category": "Business Skills", "duration": "4 weeks",
     "level": "Beginner", "icon": "↗", "description": "Turn an idea into a simple plan with budgeting, customer understanding and communication.",
     "outcome": "Prepare a basic business idea and a simple cost plan."},
]

def get_db_connection():
    """Create a MySQL connection using environment variables."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "nua_disha")
    )

@app.route("/")
def home():
    return render_template("index.html", courses=COURSES[:3])

@app.route("/courses")
def courses():
    return render_template("courses.html", courses=COURSES)

@app.route("/courses/<int:course_id>")
def course_detail(course_id):
    course = next((item for item in COURSES if item["id"] == course_id), None)
    if course is None:
        return render_template("404.html"), 404
    return render_template("course_detail.html", course=course)

@app.route("/register", methods=["GET", "POST"])
def register():
    selected_course = request.args.get("course", type=int)
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        course_id = request.form.get("course_id", type=int)

        if not name or not email or not phone or not course_id:
            flash("Please complete all fields.", "error")
            return redirect(url_for("register"))

        if not any(c["id"] == course_id for c in COURSES):
            flash("Please select a valid course.", "error")
            return redirect(url_for("register"))

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO enrollments (student_name, email, phone, course_id) VALUES (%s, %s, %s, %s)",
                (name, email, phone, course_id)
            )
            connection.commit()
            cursor.close()
            connection.close()
            return render_template("success.html", name=name)
        except Error as error:
            app.logger.error("Database error: %s", error)
            flash("We couldn't save your registration. Check the database setup and try again.", "error")
            return redirect(url_for("register"))

    return render_template("register.html", courses=COURSES, selected_course=selected_course)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
