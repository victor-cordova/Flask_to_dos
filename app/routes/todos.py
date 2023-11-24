from flask import flash, redirect, render_template, request, session, url_for, Blueprint

todos = Blueprint("todos", __name__, url_prefix="/todos")

@todos.route("/")
def home():
    return ""

@todos.route("/new")
def new():
    return "new todo"

@todos.route("/delete", methods=["DELETE"])
def delete():
    return "delete todo"

@todos.route("/update")
def update():
    return "update todo"
