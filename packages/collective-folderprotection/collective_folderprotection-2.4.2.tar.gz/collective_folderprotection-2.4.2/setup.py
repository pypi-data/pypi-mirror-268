from setuptools import setup, find_packages
import os

version = '2.4.2'

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective_folderprotection',
      version=version,
      description="Provide delete, rename and password protection for Plone items.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='folder protection plone',
      author='Enfold Systems, Inc.',
      author_email='info@enfoldsystems.com',
      url='https://github.com/collective/collective_folderprotection',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'six',
          'plone.app.contenttypes',
      ],
      extras_require={
          'test': [
              'cssselect',
              'lxml',
              'mock',
              'plone.api >=1.8.5',
              'plone.app.robotframework',
              'plone.app.testing [robot]',
              'plone.browserlayer',
              'plone.cachepurging',
              'plone.testing',
              'robotsuite',
              'testfixtures',
              'transaction',
              'tzlocal',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
