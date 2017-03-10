from setuptools import setup

long_description = open('README.rst').read()

setup(
    name="django-trix",
    version='0.2.4',
    packages=["trix"],
    include_package_data=True,
    description="Trix rich text editor widget for Django",
    url="https://github.com/istrategylabs/django-trix",
    author="Jeremy Carbaugh",
    author_email="jeremy@isl.co",
    license='BSD',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
