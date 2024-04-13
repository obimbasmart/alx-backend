#!/usr/bin/env python3


"""Task 0x05 - Mock logging in
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel

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


@babel.localeselector
def get_locale():
    """Selector function"""
    locale = request.args.get("locale")
    if not locale:
        return app.config["BABEL_DEFAULT_LOCALE"]

    if locale in [lang for lang in app.config["LANGUAGES"]]:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


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
    return render_template("5-index.html",
                           home_title="Welcome to Holberton",
                           home_header="Hello world", user=g.user)


if __name__ == "__main__":
    app.run()
