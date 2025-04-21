import string
import hashlib
import requests

# Load common passwords
with open("common_passwords.txt", "r") as file:
    common_passwords = file.read().splitlines()

def check_common_passwords(password):
    return password in common_passwords

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError("HIBP API request failed")

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digits]

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    score += sum(characters) - 1  # max of 3

    raw_score = score  # max = 7
    score_out_of_10 = round((raw_score / 7) * 10)

    if raw_score < 4:
        return "Weak", score_out_of_10
    elif raw_score == 4:
        return "Okay", score_out_of_10
    elif 4 < raw_score < 6:
        return "Good", score_out_of_10
    else:
        return "Strong", score_out_of_10

def feedback(password):
    if check_common_passwords(password):
        msg = "❌ Password found in a common password list. Please try again."
        return msg, "Weak", 0, 0

    breach_count = check_password_breach(password)
    if breach_count > 0:
        msg = f"⚠️ Password appeared in {breach_count} breaches. Choose a different one."
        return msg, "Weak", 0, breach_count

    strength, score = password_strength(password)

    msg = f"✅ Password strength: {strength} ({score}/10)\n"

    if score < 6:
        msg += "Suggestions to improve:\n"
        if len(password) <= 8:
            msg += "- Use more than 8 characters.\n"
        if not any(c.isupper() for c in password):
            msg += "- Add uppercase letters.\n"
        if not any(c.islower() for c in password):
            msg += "- Add lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            msg += "- Add special characters.\n"
        if not any(c.isdigit() for c in password):
            msg += "- Include numbers.\n"

    return msg, strength, score, breach_count