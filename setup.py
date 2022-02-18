from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_usa/__init__.py
from erpnext_usa import __version__ as version

setup(
	name="erpnext_usa",
	version=version,
	description="App to hold regional code for the United States, built on top of ERPNext.",
	author="Frappe Technologies Private Limited",
	author_email="contact@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
