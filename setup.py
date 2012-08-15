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
    'pyramid_beaker',
    'pyramid_debugtoolbar',
    'pyramid_exclog',
    'pyramid_simpleform',
    'pyramid_tm',
    'zope.sqlalchemy',
    'waitress',
    'alembic',
    'Babel',
    'cryptacular',
    'formencode'
    ]

if not 'READTHEDOCS' in os.environ:
    # hack for ReadTheDocs
    install_requires.extend(['cracklib'])
#TODO: replace this by something better and make cracklib an optional require

tests_require = [
    'WebTest',
    ]

setup(
    name='anuket',
    version='0.5.2',
    description='Anuket web application',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author='LDPL - Laboratoire Départemental de Préhistoire du Lazaret',
    author_email='opensource@lazaret.unice.fr',
    url='http://github.com/lazaret/anuket',
    license='Expat licence (or MIT licence)',
    keywords='web wsgi pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='anuket',
    message_extractors= {'anuket': [
        ('**.py', 'python', None),
        ('templates/**.mako', 'mako', None),
        ('static/**', 'ignore', None)]},
    entry_points="""\
    [paste.app_factory]
    main = anuket:main
    [console_scripts]
    backup_anuket_db = anuket.scripts.backupdb:main
    initialize_anuket_db = anuket.scripts.initializedb:main
    upgrade_anuket_db = anuket.scripts.upgradedb:main
    """,
    )
