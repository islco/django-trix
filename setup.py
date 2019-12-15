from setuptools import setup

long_description = open('README.rst').read()

setup(
    name="django-trix",
    version='0.3.2',
    packages=["trix"],
    include_package_data=True,
    description="Trix rich text editor widget for Django",
    url="https://github.com/bodedev/django-trix",
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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
