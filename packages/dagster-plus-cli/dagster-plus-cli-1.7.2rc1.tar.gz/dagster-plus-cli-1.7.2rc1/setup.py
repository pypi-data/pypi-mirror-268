from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup


def get_version() -> str:
    version: Dict[str, str] = {}
    with open(Path(__file__).parent / "dagster_plus_cli/version.py", encoding="utf8") as fp:
        exec(fp.read(), version)

    return version["__version__"]


setup(
    name="dagster-plus-cli",
    version=get_version(),
    author_email="hello@elementl.com",
    packages=find_packages(exclude=["dagster_plus.cli_tests*"]),
    include_package_data=True,
    install_requires=[
        "packaging>=20.9",
        "questionary",
        "requests",
        "typer[all]>=0.4.1",
        "PyYAML>=5.1",
        "github3.py",
    ],
    extras_require={
        "tests": [
            "freezegun",
        ],
    },
    author="Elementl",
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "dagster-plus = dagster_plus_cli.entrypoint:app",
            "dagster-cloud = dagster_plus_cli.entrypoint:app",
        ]
    },
)
