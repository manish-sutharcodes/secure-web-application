from middleware.auth_middleware import admin_required
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from database.db import get_db
from database.models import User
from security.password import verify_password, hash_password

auth_routes = Blueprint("auth", __name__)
dashboard_routes = Blueprint("dashboard", __name__)

# -------- LOGIN --------
@auth_routes.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.get_by_username(username)

        if user and verify_password(password, user[2]):
            login_user(User(user[0], user[1], user[3]))
            return redirect(url_for("dashboard.dashboard"))

        flash("Incorrect password", "error")

    return render_template("login.html")


# -------- REGISTER --------
@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hash_password(password), "user")
        )
        conn.commit()
        conn.close()

        flash("Registered successfully. Please login.")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# -------- LOGOUT --------
@auth_routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


# -------- DASHBOARD --------

@dashboard_routes.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        username=current_user.username,
        role=current_user.role
    )


    #-------ADMIN-ONLY----------

@dashboard_routes.route("/admin")
@login_required
@admin_required
def admin_dashboard():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id, username, role FROM users")
    users = cur.fetchall()

    conn.close()

    return render_template(
        "admin_dashboard.html",
        users=users,
        admin=current_user.username
    )