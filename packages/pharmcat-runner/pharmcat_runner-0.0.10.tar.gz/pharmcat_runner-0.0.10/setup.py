from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
    name="pharmcat_runner",
    version="0.0.10",
    description="Installs, runs, and parsers PharmCAT using Pharmacoscan input.",
    author="Andrew Haddad, PharmD",
    author_email="andrew.haddad@pitt.edu",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["pharmcat_runner = pharmcat_runner.__main__:main"]
    },
    install_requires=["pandas"],
    package_data={"pharmcat_runner": ["lib/*"]},
    include_package_data=True,
)
