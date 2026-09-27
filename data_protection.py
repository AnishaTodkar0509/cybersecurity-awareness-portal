import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    else:
        score += 1
        
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%).")
        
    if score <= 1:
        strength = "Weak"
        color = "danger"
    elif score == 2 or score == 3:
        strength = "Medium"
        color = "warning"
    else:
        strength = "Strong"
        color = "success"
        feedback.append("Great password! Keep it secure.")
        
    return {
        "strength": strength,
        "color": color,
        "feedback": feedback
    }

def mask_sensitive_data(text):
    # Mask Indian Phone Numbers (e.g., 9876543210 -> 98******10)
    phone_pattern = r'\b([6-9]\d{1})(\d{6})(\d{2})\b'
    text = re.sub(phone_pattern, r'\1******\3', text)
    
    # Mask Aadhaar Numbers (e.g., 1234 5678 9012 -> **** **** 9012)
    aadhaar_pattern = r'\b(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})\b'
    text = re.sub(aadhaar_pattern, r'**** **** \3', text)
    
    # Mask Credit Cards (e.g., 4532 1234 5678 9010 -> **** **** **** 9010)
    cc_pattern = r'\b(?:\d[ -]*?){13,16}\b'
    def mask_cc(match):
        val = match.group(0)
        digits_only = re.sub(r'\D', '', val)
        if len(digits_only) >= 13:
            return '*' * (len(val) - 4) + val[-4:]
        return val
    text = re.sub(cc_pattern, mask_cc, text)
    
    # Mask Emails (e.g., user123@example.com -> u***3@example.com)
    email_pattern = r'\b([a-zA-Z0-9_.-]+)@([a-zA-Z0-9_.-]+)\.([a-zA-Z]{2,5})\b'
    def mask_email(match):
        local = match.group(1)
        domain = match.group(2)
        tld = match.group(3)
        if len(local) > 2:
            local = local[0] + '*' * (len(local)-2) + local[-1]
        else:
            local = '*' * len(local)
        return f"{local}@{domain}.{tld}"
    text = re.sub(email_pattern, mask_email, text)
    
    return text
