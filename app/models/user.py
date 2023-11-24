from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from utils.db import db

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password