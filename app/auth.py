import re
from app.models import LoginRequest

def validate_login(data: LoginRequest):
    username_pattern = r"^[A-Za-z]{1,15}$"
    password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{12,}$"

    if not re.match(username_pattern, data.username):
        return {"status": "error", "message": "Invalid username"}

    if not re.match(password_pattern, data.password):
        return {"status": "error", "message": "Invalid password"}

    return {"status": "success", "message": "Login successful"}
