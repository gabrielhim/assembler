from setuptools import setup, find_packages

setup(
    name="assembler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click", "setuptools"],
    entry_points={
        "console_scripts": [
            "assembler = assembler.scripts.main:main",
        ],
    },
)
