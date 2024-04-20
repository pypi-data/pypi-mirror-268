from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup


def get_version() -> str:
    version: Dict[str, str] = {}
    with open(Path(__file__).parent / "dagster_cloud_cli/version.py", encoding="utf8") as fp:
        exec(fp.read(), version)

    return version["__version__"]


ver = get_version()
pin = "" if ver == "1!0+dev" else f"=={ver}"
setup(
    name="dagster-cloud-cli",
    version=get_version(),
    author_email="hello@elementl.com",
    packages=find_packages(exclude=["dagster_cloud.cli_tests*"]),
    include_package_data=True,
    install_requires=["dagster-plus-cli==1.7.2rc4"],
    extras_require={
        "tests": [f"dagster-plus-cli[tests]{pin}"],
    },
    author="Elementl",
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["dagster-cloud = dagster_plus_cli.entrypoint:app"]},
)
