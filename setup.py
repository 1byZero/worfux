from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in worfux/__init__.py
from worfux import __version__ as version

setup(
	name="worfux",
	version=version,
	description="UI app for Worf",
	author="Amit Kumar",
	author_email="amit@worf.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
