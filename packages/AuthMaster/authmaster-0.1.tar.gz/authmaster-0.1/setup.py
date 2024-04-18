# auth_package/setup.py

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='AuthMaster',
    version='0.1',
    author='Jasper',
    author_email='xifaxo-dulo72@outlook.com',
    description='A package for Flask authentication',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CrystalV2/flask_simple_auth',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-Login',
        'SQLAlchemy',
        'Werkzeug',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
