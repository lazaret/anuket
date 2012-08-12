# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for authentification."""
from datetime import datetime
from cryptacular.bcrypt import BCRYPTPasswordManager
from sqlalchemy import Column, ForeignKey, DateTime, Integer, Unicode
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from anuket.models import Base, DBSession


class AuthUser(Base):
    """ AuthUser table and model definition.

    Define the database `auth_user` table for the authenticated users and the
    methods for querring the table or check the validity of the password.
    """
    __tablename__ = 'auth_user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(Unicode(16), unique=True, nullable=False, index=True)
    first_name = Column(Unicode(255))
    last_name = Column(Unicode(255))
    email = Column(Unicode(255), unique=True, index=True)
    created = Column(DateTime, default=datetime.utcnow)
    _password = Column('password', Unicode(80))
    #many-to-one
    group_id = Column(Integer, ForeignKey('auth_group.group_id'))
    group = relationship('AuthGroup')

    def __repr__(self):  # pragma: no cover
        return '<AuthUser: %s>' % self.username

    @classmethod
    def get_by_id(cls, user_id=None):
        """ Query the `auth_user` table by `user_id`.

        :param user_id: the user id
        :type username: integer
        :return: a ``sqlalchemy.orm.query.Query`` object
        """
        if user_id:
            return DBSession.query(cls).get(user_id)

    @classmethod
    def get_by_username(cls, username=None):
        """ Query the `auth_user` table by username.

        :param username: the user username
        :type username: unicode
        :return: a ``sqlalchemy.orm.query.Query`` object
        """
        if username:
            return DBSession.query(cls).filter(
                       cls.username == username).first()

    @classmethod
    def get_by_email(cls, email=None):
        """ Query the auth_user table by email.

        :param username: the user email
        :type username: unicode
        :return: a ``sqlalchemy.orm.query.Query`` object
        """
        if email:
            return DBSession.query(cls).filter(cls.email == email).first()

    @classmethod
    def check_password(cls, username, password):
        """ Check the user password.

        Check if the submited password for username is the same than the
        encrypted one recorded in the database. Return None if the username
        did not exist.

        :param username: the user username
        :type username: unicode
        :param username: the submited password
        :type username: unicode
        :return: True if the password is correct. false if incorect
        :rtype: boolean
        """
        bcrypt = BCRYPTPasswordManager()
        user = cls.get_by_username(username)
        if user:
            return bcrypt.check(user.password, password)

    @hybrid_property
    def password(self):
        """ Return the account's (crypted) password."""
        return self._password

    @password.setter
    def _set_password(self, raw_password):
        """ Encrypt the password.

        Encrypt `raw_password` with bcrypt and set it as the account
        password.

        :param raw_password: the unencrypted user password
        :type username: unicode
        :return: the bcrypt encrypted password
        :rtype: unicode
        """
        bcrypt = BCRYPTPasswordManager()
        self._password = unicode(bcrypt.encode(raw_password, rounds=12))


class AuthGroup(Base):
    """ AuthGroup table and model definition.

    Define the database `auth_group` table for the users groups and a method
    to query the table. This table is used used for ACLs principals.
    """
    __tablename__ = 'auth_group'

    group_id = Column(Integer, autoincrement=True, primary_key=True)
    groupname = Column(Unicode(16), unique=True, nullable=False, index=True)

    def __repr__(self):  # pragma: no cover
        return '<AuthGroup: %s>' % self.groupname

    @classmethod
    def get_by_id(cls, group_id):
        """ Query the `auth_group` table by `group_id`.

        :param group_id: the group id
        :type group_id: integer
        :return: a ``sqlalchemy.orm.query.Query`` object
        """
        return DBSession.query(cls).get(group_id)
