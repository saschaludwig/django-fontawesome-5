import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fontawesome-6',
    version='1.0.0.0',
    packages=['fontawesome_6'],
    include_package_data=True,
    license='BSD License',
    description='A utility for using icons in models, forms, and templates.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/saschaludwig/django-fontawesome-6',
    author='Sascha Ludwig',
    author_email='sascha@astrastudio.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
    install_requires=[
        'Django>=2.1',
    ],
)
