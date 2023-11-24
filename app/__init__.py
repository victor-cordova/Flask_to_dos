from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .routes.auth import auth

def create_app():
    app = Flask(__name__) #Se crea una instancia de Flask
    Bootstrap(app)#Se llama a bootstrap para usarlo en el proyecto
    app.config.from_object(Config)
    # Colocando el link de conexión de la DB con el proyecto.
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://sa:123456@localhost/usersdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    SQLAlchemy(app)
    # Se registra el blueprint al crear la app. En este caso el bluprint de auth
    app.register_blueprint(auth)

    return app