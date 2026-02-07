import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def password_policy(password):
    if len(password) < 8:
        return False
    if password.islower() or password.isupper():
        return False
    if password.isalnum():
        return False
    return True