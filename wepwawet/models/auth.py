# -*- coding: utf-8 -*-
from datetime import datetime
from cryptacular.bcrypt import BCRYPTPasswordManager
from sqlalchemy import Column, ForeignKey, DateTime, Integer, Unicode
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from wepwawet.models import Base, DBSession


class AuthUser(Base):
    """ AuthUser definition.
    """
    __tablename__ = 'auth_user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(Unicode(16), unique=True, nullable=False, index=True)
    first_name = Column(Unicode(255))
    last_name = Column(Unicode(255))
    email = Column(Unicode(255), unique=True)
    created = Column(DateTime, default=datetime.utcnow)
    _password = Column('password', Unicode(80))
    #many to one
    group_id = Column(Integer, ForeignKey('auth_group.group_id'))
    group = relationship('AuthGroup')

    def __repr__(self):
        return '<AuthUser: %s>' % self.username

    def __unicode__(self):
        return self.username

    @classmethod
    def get_by_id(cls, user_id):
        return DBSession.query(cls).get(user_id)

    @classmethod
    def get_by_username(cls, username):
        return DBSession.query(cls).filter(cls.username == username).first()

    @classmethod
    def check_password(cls, username, password):
        bcrypt = BCRYPTPasswordManager()
        user = cls.get_by_username(username)
        if user:
            return bcrypt.check(user.password, password)

    @hybrid_property
    def password(self):
        """Return the account's (hashed) password."""
        return self._password

    @password.setter
    def _set_password(self, raw_password):
        """Hash raw_password with bcrypt and set it as the account password."""
        bcrypt = BCRYPTPasswordManager()
        self._password = unicode(bcrypt.encode(raw_password, rounds=12))


class AuthGroup(Base):
    """ AuthUser definition.
    """
    __tablename__ = 'auth_group'

    group_id = Column(Integer, autoincrement=True, primary_key=True)
    groupname = Column(Unicode(16), unique=True, nullable=False, index=True)

    def __repr__(self):
        return '<AuthGroup: %s>' % self.groupname

    def __unicode__(self):
        return self.groupname

    @classmethod
    def get_by_id(cls, group_id):
        return DBSession.query(cls).get(user_id)
