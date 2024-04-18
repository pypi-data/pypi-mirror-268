# auth_package/auth.py

from flask import redirect, url_for, session
from flask_login import current_user
from functools import wraps
from .models import db, User

class Auth:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return user
        return None

    @staticmethod
    def logout():
        session.pop('user_id', None)

    @staticmethod
    def require_logged_in(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for('login'))
            return func(*args, **kwargs)
        return wrapper
