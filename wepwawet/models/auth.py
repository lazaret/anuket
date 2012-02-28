# -*- coding: utf-8 -*-
from datetime import datetime
from cryptacular.bcrypt import BCRYPTPasswordManager
from sqlalchemy import Column, DateTime, Integer, Unicode
from sqlalchemy.ext.hybrid import hybrid_property
from . import Base

#__all__ = ['User']

bcrypt = BCRYPTPasswordManager()


class User(Base):
    """ User definition.
    """
    __tablename__ = 'auth_user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(Unicode(16), unique=True, nullable=False, index=True)
    first_name = Column(Unicode(255))
    last_name = Column(Unicode(255))
    email = Column(Unicode(255), unique=True)
    created = Column(DateTime, default=datetime.now)

    _password = Column('password', Unicode(80))


#    def __init__(self, username):
#        self.username = username

    def __repr__(self):
        return '<User: %s>' % self.username

#    def __unicode__(self):
#        return self.username

    @hybrid_property
    def password(self):
        """Return the account's (hashed) password."""
        return self._password

    @password.setter
    def _set_password(self, raw_password):
        """Hash raw_password with bcrypt and set it as the account password."""
        hashed_password = bcrypt.encode(raw_password, rounds=12)
        self._password = unicode(hashed_password)


    def check_password(self, password):
        return bcrypt.check(self.password, password)
