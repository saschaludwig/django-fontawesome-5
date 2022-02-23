import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fontawesome-5',
    version='1.0.18.1',
    packages=['fontawesome_5'],
    include_package_data=True,
    license='BSD License',
    description='A utility for using icons in models, forms, and templates.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/BenjjinF/django-fontawesome-5',
    author='Benjamin Frost',
    author_email='info@btfrost.com',
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
