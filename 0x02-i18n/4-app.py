#!/usr/bin/env python3


"""Get locale from request
"""


from flask import Flask, render_template, request
from flask_babel import Babel


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
        return babel.default_locale

    if locale in [_locale.language for _locale in babel.list_translations()]:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Basic route"""
    return render_template("4-index.html",
                           home_title="Welcome to Holberton",
                           home_header="Hello world")


if __name__ == "__main__":
    app.run()
