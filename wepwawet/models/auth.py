# -*- coding: utf-8 -*-
from datetime import datetime
from cryptacular.bcrypt import BCRYPTPasswordManager
from sqlalchemy import Column, DateTime, Integer, Unicode
from sqlalchemy.ext.hybrid import hybrid_property

from wepwawet.models import Base, DBSession


bcrypt = BCRYPTPasswordManager()


class AuthUser(Base):
    """ AuthUser definition.
    """
    __tablename__ = 'auth_user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(Unicode(16), unique=True, nullable=False, index=True)
    first_name = Column(Unicode(255))
    last_name = Column(Unicode(255))
    email = Column(Unicode(255), unique=True)
    created = Column(DateTime, default=datetime.now)

    _password = Column('password', Unicode(80))


    def __repr__(self):
        return '<AuthUser: %s>' % self.username

    def __unicode__(self):
        return self.username

    @classmethod
    def get_by_id(cls, user_id):
        return DBSession.query(cls).get(user_id)

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
