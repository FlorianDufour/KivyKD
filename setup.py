# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kivy-desktop',
    version='0.1.0',
    description='A package to add widgets to Kivy',
    author='Florian Dufour',
    author_email='flodufour@laposte.net',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

