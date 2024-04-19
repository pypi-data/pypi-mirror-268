
#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name                 = "litesata",
    description          = "Small footprint and configurable SATA core",
    author               = "Florent Kermarrec",
    author_email         = "florent@enjoy-digital.fr",
    url                  = "http://enjoy-digital.fr",
    download_url         = "https://github.com/enjoy-digital/litesata",
    test_suite           = "test",
    license              = "BSD",
    python_requires      = "~=3.7",
    packages             = find_packages(exclude=("test*", "sim*", "doc*", "examples*")),
    include_package_data = True,
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    version="2023.12",
    entry_points         = {
        "console_scripts": [
            "litesata_gen=litesata.gen:main",
        ],
    },
)
