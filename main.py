from flask import make_response, redirect, render_template, session

from app import create_app
from .app.utils.db import db

app = create_app()
todos = {"todo1": "ss"}

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
