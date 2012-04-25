# -*- coding: utf-8 -*-
from alembic.config import Config
from alembic import command


def main():
    """ Upgrade the database schema with alembic."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

