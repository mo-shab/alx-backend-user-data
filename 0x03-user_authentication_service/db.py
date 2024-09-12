#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound as ORMNoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.
        Args :
            email (str) : the user's Email.
            hashed_password (str): The user's hashed password
            Return : the newly created user object
        """
        new_user = User(
            email=email,
            hashed_password=hashed_password,
        )
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find user by a given attribute
            Args:
                - Dictionary of attributes to use as search
                  parameters
            Return:
                - User object
        """
        attrs, vals = [], []
        for attr, val in kwargs.items():
            if not hasattr(User, attr):
                raise InvalidRequestError()
            attrs.append(getattr(User, attr))
            vals.append(val)

        session = self._session
        query = session.query(User)
        user = query.filter(tuple_(*attrs).in_([tuple(vals)])).first()
        if not user:
            raise NoResultFound()
        return user
