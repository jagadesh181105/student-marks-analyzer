from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

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
            return render_template("index.html",
                                   error="Marks must be between 0 and 100.")

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

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)