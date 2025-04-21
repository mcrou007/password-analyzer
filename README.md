# 🔐 Password Analyzer

A Python-based command-line password analyzer that evaluates password strength, checks for data breaches using the HaveIBeenPwned API, and generates a clean PDF report in Times New Roman.

Built with secure coding practices and real-world logic, this tool provides instant feedback and a polished audit trail — ideal for security-focused development or as a resume-ready portfolio piece.

---

## ✨ Features

- ✅ **Common Password Detection**  
  Flags passwords found in a bundled `common_passwords.txt` file (top weak passwords).

- 🔐 **Data Breach Lookup via HaveIBeenPwned**  
  Verifies if a password has been exposed in known data breaches using SHA-1 hashing + k-anonymity API queries.

- 📊 **Strength Scoring (Out of 10)**  
  Passwords are evaluated for character diversity and length, then rated as `Weak`, `Okay`, `Good`, or `Strong` along with a numerical score (e.g. `6/10`).

- 📄 **PDF Report (Times New Roman)**  
  At the end of a session, a professional PDF report (`password_report.pdf`) is automatically generated.

- 🔁 **Session-Based Analysis**  
  You can test multiple passwords in one run. All results are saved to the report.

- 🧠 Skills Demonstrated
  SHA-1 hashing and API communication

  Password strength heuristics

  CLI input handling and feedback

  PDF generation using reportlab

  Secure programming principles

---

## 🚀 How to Run This Program

### 🧰 Requirements

- Python 3.8 or later
- Internet access (for data breach API)

---

### ▶️ Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/password-analyzer.git
   cd password-analyzer

2. Install Required Python Packages
 pip install requests reportlab

3. Run the Program 
