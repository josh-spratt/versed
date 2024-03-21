from setuptools import setup

setup(
    name="versed",
    version="0.1.0",
    packages=["versed"],
    entry_points={"console_scripts": ["versed = versed.__main__:main"]},
)
