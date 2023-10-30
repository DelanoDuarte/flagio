from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Date, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from uuid import uuid4
from typing import List
from datetime import datetime, date

db = SQLAlchemy()

class Base(DeclarativeBase):
    pass

class Flag(db.Model):
    __tablename__ = "flag"

    id = db.Column(db.Text(length=36), default=lambda: str(uuid4()), primary_key=True)    
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_on: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.utcnow())
    expiration_date: Mapped[date] = mapped_column(Date, nullable=True)

    environments: Mapped[List['Environment']] = relationship(
         secondary='environment_flags', back_populates="flags"
    )

    def __init__(self, name, description, expiration_date) -> None:
        self.name = name
        self.description = description
        self.expiration_date = expiration_date

    def has_expiration(self) -> bool:
        return self.expiration_date is not None

    def toJson(self, with_environments: bool = True):
        flag = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "active": self.active,
            "created_on": self.created_on,
            "expiration_date": self.expiration_date
        }

        if with_environments: flag['environments'] = list(map(lambda env: env.toJson(), self.environments))
        return flag

class Environment(db.Model):
    __tablename__ = "environment"

    id = db.Column(db.Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    created_on: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.utcnow())
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    key = db.Column(db.Text(length=36))

    # relationships
    flags: Mapped[List[Flag]] = relationship(
        secondary='environment_flags', back_populates="environments"
    )

    def __init__(self, name, key = None) -> None:
        self.name = name
        self.key = key

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "key": self.key,
            "created_on": self.created_on
        }

environment_flags = Table(
    "environment_flags",
    Flag.metadata,
    Column("flag_id", ForeignKey("flag.id"), primary_key=True, nullable=False),
    Column("environment_id", ForeignKey("environment.id"), primary_key=True, nullable=False),
)