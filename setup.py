from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-fso',
    version=version,
    description="CKAN extension for the FSO for the OGD portal of Switzerland",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.fso'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    fso=ckanext.fso.plugins:FsoHarvest
    fso_harvester=ckanext.fso.harvesters:FSOHarvester
    [paste.paster_command]
    harvester=ckanext.fso.commands.harvester:Harvester
    """,
)
