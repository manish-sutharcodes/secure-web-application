import re

def sanitize_input(data):
    return re.sub(r"[<>\"']", "", data)

def validate_username(username):
    return re.match(r"^[a-zA-Z0-9_]{4,20}$", username)