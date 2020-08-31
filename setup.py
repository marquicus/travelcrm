import os
import sys
try:
    from subprocess import check_output
except ImportError:
    pass

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

if 'sdist' in sys.argv or 'bdist' in sys.argv:
    with open(os.path.join(here, 'VERSION.txt'), 'w') as f:
        build = (
            check_output([
                "hg", "log", "-r", ".", "--template", "{branch} b.{node|short}"
            ])
        )
        f.write(build)


requires = [
    'setuptools',
    'pyramid==1.8.6',
    'pyramid_mako==1.0.2',
    'pyramid_debugtoolbar==3.0.4',
    'pyramid_tm==1.0',
    'SQLAlchemy==1.0.15',
    'transaction==1.6.1',
    'zope.sqlalchemy==0.7.7',
    'waitress==1.0.1',
    'colander==1.3',
    'wsgithumb',
    'alembic==0.8.8',
    'WebHelpers2==2.0b5',
    'pyramid_layout',
    'psycopg2==2.7.3.1',
    'pyramid_beaker',
    'Babel==2.3.4',
    'phonenumbers==7.7.2',
    'pyramid_storage==0.1.2',
    'pyramid_mailer==0.14.1',
    'Sphinx==1.4.8',
    'sphinx-bootstrap-theme==0.4.12',
    'pdfkit==0.6.0',
    'apscheduler==3.2.0',
    'bitmath==1.0.2-3',
    'smpplib==0.1',
    'Mock==2.0.0',
    'python_dateutil==2.4.0',
    'nose',
    'redis==2.10.5',
    'pyramid_robot==1.1',
    'Pygments==2.1.3',
    'Jinja2==2.8',
    'MarkupSafe==0.23',
    'Pillow==3.4.2',
    'beautifulsoup4==4.5.1',
    'iso8601==0.1.11',
]

setup(
    name='travelcrm',
    version='0.6.4-beta2',
    description='travelcrm',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
      "Programming Language :: Python",
      "Framework :: Pyramid",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3.5",
      ],
    author='Vitalii Mazur',
    author_email='vitalii.mazur@gmail.com',
    url='http://www.travelcrm.org.ua',
    keywords='web wsgi bfg pylons pyramid travel crms',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='travelcrm',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = travelcrm:main
    [console_scripts]
    initialize_travelcrm_db = travelcrm.scripts.initializedb:main
    [pyramid.scaffold]
    travelcrm = scaffold:TravelcrmProjectTemplate
    """,
    message_extractors={
        'travelcrm': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
            ('static/**', 'ignore', None)
        ]
    },
)
