from setuptools import setup
import pathlib

version: str = "1.1.1"
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="zcached.py",
    version=version,
    description="A lightweight client-side library for zcached, written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xXenvy/zcached.py",
    author="xXenvy",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=["typing-extensions"],
    python_requires=">=3.8",
    project_urls={
        "Bug Reports": "https://github.com/xXenvy/zcached.py/issues",
        "Source": "https://github.com/xXenvy/zcached.py"
    },
)