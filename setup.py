from pathlib import Path
from typing import Union

from setuptools import setup

THIS_DIR = Path(__file__).resolve().parent


def get_long_description(path: Union[str, Path]) -> str:
    absolute_path = THIS_DIR / path
    with open(absolute_path) as f:
        return f.read()


setup(
    name="asyncio-throttle",
    version="0.1.1",
    url="https://github.com/hallazzang/asyncio-throttle",
    license="MIT",
    author="hallazzang",
    author_email="hallazzang@gmail.com",
    description="Simple, easy-to-use throttler for asyncio",
    long_description=get_long_description("README.rst"),
    py_modules=["asyncio_throttle"],
    python_requires=">=3.5",
    zip_safe=False,
    platforms="any",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
