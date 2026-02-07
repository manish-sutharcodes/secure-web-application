from flask import Flask
from flask_login import LoginManager
from database.db import init_db
from database.models import User
from routes import auth_routes, dashboard_routes

app = Flask(__name__)

app.secret_key = "this-is-a-test-secret-key"

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

app.register_blueprint(auth_routes)
app.register_blueprint(dashboard_routes)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)