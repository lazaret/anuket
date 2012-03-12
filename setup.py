# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'Babel',
    'cryptacular',
    'formencode',
    'pyramid_simpleform',
    'WebTest',
    ]

setup(name='wepwawet',
    version='0.2a',
    description='wepwawet',
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author='Bertrand Lecervoisier',
    author_email='miniwark@gmail.com',
    url='',
    license='',
    keywords='web wsgi pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite='wepwawet',
    message_extractors = {'wepwawet': [
        ('**.py', 'python', None),
        ('templates/**.mako', 'mako', None),
        ('static/**', 'ignore', None)]},
    entry_points="""\
    [paste.app_factory]
    main = wepwawet:main
    [console_scripts]
    populate_wepwawet = wepwawet.scripts.populate:main
    """,
    )
