from setuptools import setup, find_packages

setup(
    name='simple-ddl-parser',
    version='0.30.0',
    author='Iuliia Volkova <xnuinside@gmail.com>',
    description='Simple DDL Parser to parse SQL & dialects like HQL, TSQL (MSSQL), Oracle, AWS Redshift, Snowflake, MySQL, PostgreSQL, etc ddl files to json/python dict with full information about columns: types, defaults, primary keys, etc.; sequences, alters, custom types & other entities from ddl.',
    url='https://github.com/xnuinside/simple-ddl-parser',
    license='MIT',
    packages=find_packages(
        '.',
        include=['simple_ddl_parser'],
        exclude=['tests', 'docs'],
    ),
    requires=['ply'],
    entry_points={
        'console_scripts': [
            'simple_ddl_parser = simple_ddl_parser.cli:main',
        ],
    },
)
