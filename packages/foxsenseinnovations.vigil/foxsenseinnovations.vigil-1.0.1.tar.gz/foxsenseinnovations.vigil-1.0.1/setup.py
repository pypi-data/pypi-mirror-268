from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='foxsenseinnovations.vigil',
    version='1.0.1',
    description='Official SDK for Vigil - A comprehensive solution for all your monitoring requirements, including exceptions, jobs, APIs, and website availability',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(exclude=['foxsenseinnovations.vigil.flask']),
    install_requires=[
        'setuptools',
        'requests',
        'werkzeug',
        'django',
    ],
    license='ISC'
)
