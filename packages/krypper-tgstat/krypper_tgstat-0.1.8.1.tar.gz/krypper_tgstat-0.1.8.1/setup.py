from setuptools import setup

"""
:authors: Evgeny Momotov (KrymmyEM)
:license: MIT License
Copyright: (c) 2024 Evgeny
"""

version = "0.1.8.1"

long_description = ""

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "krypper_tgstat",
    version = version,
    description = "Wrapper for TG Stat API writing on Python\nTGStat (https://tgstat.ru API wrapper)",
    long_description = long_description,

    author = "Evgeny Momotov (KrymmyEM)",
    author_email = "evgeny.momotov@gmail.com",
    url = "https://github.com/KrymmyEM/krypper_tgstat",
    download_url = "https://github.com/KrymmyEM/krypper_tgstat/archive/main.zip",

    license = "MIT License. See LICENSE file",
    packages = ["krypper_tgstat"],
    install_requires=[
        "requests",
        "aiohttp"
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)


