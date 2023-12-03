from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Date, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from uuid import uuid4
from typing import List
from datetime import datetime, date

db = SQLAlchemy()

class Base(DeclarativeBase):
    pass

class User(db.Model):
    id = db.Column(db.Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(String, nullable=False, name="password")
    roles: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    firstname: Mapped[str] = mapped_column(String, nullable=True)
    lastname: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True, name="email", nullable=True)

    @property
    def rolenames(self):
        """
        *Required Attribute or Property*

        flask-praetorian requires that the user class has a ``rolenames`` instance
        attribute or property that provides a list of strings that describe the roles
        attached to the user instance
        """
        try:
            return self.roles.split(",")
        except Exception:
            return []
        
    @property
    def identity(self):
        """
        *Required Attribute or Property*

        flask-praetorian requires that the user class has an ``identity`` instance
        attribute or property that provides the unique id of the user instance
        """
        return self.id
    
    @property
    def password(self):
        """
        *Required Attribute or Property*

        flask-praetorian requires that the user class has a ``password`` instance
        attribute or property that provides the hashed password assigned to the user
        instance
        """
        return self.hash_password

    @classmethod
    def identify(cls, id):
        """
        *Required Method*

        flask-praetorian requires that the user class implements an ``identify()``
        class method that takes a single ``id`` argument and returns user instance if
        there is one that matches or ``None`` if there is not.
        """
        return cls.query.get(id)
    
    @classmethod
    def lookup(cls, username):
        """
        *Required Method*

        flask-praetorian requires that the user class implements a ``lookup()``
        class method that takes a single ``username`` argument and returns a user
        instance if there is one that matches or ``None`` if there is not.
        """
        return cls.query.filter_by(username=username).one_or_none()

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'
    
    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "roles": self.rolenames,
            "active": self.is_active,
            "name": self.full_name,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

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