#!/usr/bin/env python3


"""Task 0x05 - Mock logging in
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Basic flask configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.timezoneselector
def get_timezone():
    """timezone selector"""
    timezone = request.args.get("timezone")

    if not timezone and g.user:
        timezone = g.user.get("timezone")
    try:
        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError as err:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@babel.localeselector
def get_locale():
    """locale selector"""
    supported_languages = [lang for lang in app.config["LANGUAGES"]]
    locale = request.args.get("locale")
    if locale in supported_languages:
        return locale
    if (g.user and g.user.get("locale") in supported_languages):
        return g.user.get("locale")
    if request.headers.get('Accept-Language'):
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_user(login_as=None):
    """get user by ID"""
    if not login_as or not login_as.isdigit():
        return None
    return (users.get(int(login_as)))


@app.before_request
def before_request():
    """---- ----- ----"""
    user_id = request.args.get("login_as")
    g.user = get_user(login_as=user_id)


@app.route("/")
def index():
    """Basic route"""
    return render_template("index.html",
                           home_title="Welcome to Holberton",
                           home_header="Hello world",
                           current_time=format_datetime(
                               datetime.now()),
                           user=g.user)


if __name__ == "__main__":
    app.run()
