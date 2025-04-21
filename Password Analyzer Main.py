from PasswordAnalyzer import feedback
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

session_log = []

def save_report_as_pdf(log, filename="password_report.pdf"):
    pdf = canvas.Canvas(filename, pagesize=letter)
    _, height = letter

    pdf.setFont("Times-Bold", 14)
    pdf.drawString(50, height - 50, "Password Analysis Report")
    pdf.line(50, height - 55, 550, height - 55)

    y = height - 80
    pdf.setFont("Times-Bold", 10)
    pdf.drawString(50, y, "Password")
    pdf.drawString(250, y, "Strength (Score/10)")
    pdf.drawString(420, y, "Breaches")

    y -= 20
    pdf.setFont("Times-Roman", 10)

    for entry in log:
        pdf.drawString(50, y, entry['password'])
        pdf.drawString(250, y, f"{entry['strength']} ({entry['score']}/10)")
        pdf.drawString(420, y, str(entry['breaches']))
        y -= 20
        if y < 60:
            pdf.showPage()
            y = height - 80
            pdf.setFont("Times-Roman", 10)

    pdf.save()

# 🔁 Main input loop
while True:
    password = input("Enter your password: ")
    result, strength, score, breaches = feedback(password)
    print("\n" + result)

    session_log.append({
        "password": password,
        "strength": strength,
        "score": score,
        "breaches": breaches
    })

    again = input("\nTest another password? (y/n): ").strip().lower()
    if again != 'y':
        break

# 💾 Save report AFTER user exits
save_report_as_pdf(session_log)
print("\n✅ PDF report saved as 'password_report.pdf'")