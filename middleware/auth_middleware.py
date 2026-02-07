from flask_login import current_user
from flask import render_template
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != "admin":
            return render_template("403.html"), 403
        return f(*args, **kwargs)
    return decorated_function