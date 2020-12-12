# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in item_batch_history/__init__.py
from item_batch_history import __version__ as version

setup(
	name='item_batch_history',
	version=version,
	description='Item_Batch_History',
	author='frappe',
	author_email='shajeer@craftinteractive.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
