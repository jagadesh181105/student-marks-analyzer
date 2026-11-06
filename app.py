
from flask import Flask, render_template, request
from database import create_table, add_student, get_students
from flask import send_file
from pdf_report import generate_report
app = Flask(__name__)

# Create the database table
create_table()


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        name = request.form["name"]

        subjects = {
            "Python": int(request.form["python"]),
            "Java": int(request.form["java"]),
            "SQL": int(request.form["sql"]),
            "Maths": int(request.form["maths"]),
            "English": int(request.form["english"])
        }

        if any(mark < 0 or mark > 100 for mark in subjects.values()):
            error = "Marks must be between 0 and 100."
        else:
            total = sum(subjects.values())
            average = total / 5

            if any(mark < 35 for mark in subjects.values()):
                grade = "F"
                status = "Fail"
            elif average >= 90:
                grade, status = "A+", "Pass"
            elif average >= 80:
                grade, status = "A", "Pass"
            elif average >= 70:
                grade, status = "B", "Pass"
            elif average >= 60:
                grade, status = "C", "Pass"
            else:
                grade, status = "D", "Pass"

            result = {
                "name": name,
                "subjects": subjects,
                "total": total,
                "average": round(average, 2),
                "grade": grade,
                "status": status,
                "highest": max(subjects, key=subjects.get),
                "lowest": min(subjects, key=subjects.get)
            }

            # Save student details in the database
            add_student((
                name,
                subjects["Python"],
                subjects["Java"],
                subjects["SQL"],
                subjects["Maths"],
                subjects["English"],
                total,
                round(average, 2),
                grade,
                status
            ))

   
    students = get_students()

    search_name = request.args.get("search", "").strip()

    if search_name:
        students = [
            student for student in students
            if search_name.lower() in student[1].lower()
        ]

    return render_template(
        "index.html",
        result=result,
        students=students,
        error=error
    )



@app.route("/download/<int:student_id>")
def download_student_report(student_id):
    students = get_students()

    student = next(
        (s for s in students if s[0] == student_id),
        None
    )

    if student is None:
        return "Student not found", 404

    file_name = generate_report(student)

    return send_file(file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
