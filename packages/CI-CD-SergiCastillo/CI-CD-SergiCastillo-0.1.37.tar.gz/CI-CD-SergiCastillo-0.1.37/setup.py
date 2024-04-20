from setuptools import setup, find_packages

setup(
    name='CI-CD-SergiCastillo',
    version='0.1.37',
    packages=find_packages(),
    install_requires=[
        'coverage',
        'pylint',
        'pytest',
        'ggshield',
        'psycopg2',
        'flask',
        'json-log-formatter',
        'twine'
              
    ],
    author='Sergi Castillo',
    description='KeepCoding',
    url='https://github.com/sergicastin/CI-CD-SergiCastillo',
)
