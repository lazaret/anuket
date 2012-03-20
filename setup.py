# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

install_requires = [
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
    ]

tests_require = [
    'WebTest',
    ]

setup(name='wepwawet',
    version='0.2a',
    description='Wepwawet web application',
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
    license='LICENSE.txt',
    keywords='web wsgi pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='wepwawet',
    message_extractors = {'wepwawet': [
        ('**.py', 'python', None),
        ('templates/**.mako', 'mako', None),
        ('static/**', 'ignore', None)]},
    entry_points="""\
    [paste.app_factory]
    main = wepwawet:main
    [console_scripts]
    initialize_wepwawet_db = wepwawet.scripts.initializedb:main
    """,
    )
