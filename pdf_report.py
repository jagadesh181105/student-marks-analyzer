
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def generate_report(student):
    file_name = f"student_report_{student[0]}.pdf"

    pdf = canvas.Canvas(file_name, pagesize=A4)

    width, height = A4

    pdf.setTitle("Student Performance Report")

    # Heading
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(
        width / 2, height - 60,
        "STUDENT PERFORMANCE REPORT"
    )

    pdf.setStrokeColor(colors.blue)
    pdf.line(50, height - 80, width - 50, height - 80)

    # Student details
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(60, height - 120, f"Student ID: {student[0]}")
    pdf.drawString(60, height - 150, f"Student Name: {student[1]}")

    # Subject marks
    pdf.drawString(60, height - 200, "SUBJECT MARKS")

    pdf.setFont("Helvetica", 12)

    subjects = [
        ("Python", student[2]),
        ("Java", student[3]),
        ("SQL", student[4]),
        ("Maths", student[5]),
        ("English", student[6])
    ]

    y = height - 230

    for subject, mark in subjects:
        pdf.drawString(80, y, f"{subject}: {mark}/100")
        y -= 25

    # Results
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(60, y - 20, f"Total Marks: {student[7]}/500")
    pdf.drawString(60, y - 50, f"Average: {student[8]}%")
    pdf.drawString(60, y - 80, f"Grade: {student[9]}")
    pdf.drawString(60, y - 110, f"Status: {student[10]}")

    pdf.save()

    return file_name
