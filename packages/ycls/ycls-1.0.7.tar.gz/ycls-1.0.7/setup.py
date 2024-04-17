from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="ycls",
    version="1.0.7",
    description="YCLS is a Python module for calculating loudness metrics for audio (or video) files, particularly aimed at determining the loudness level suitable for YouTube content.",
    packages=find_packages(),
    install_requires=requirements,
    long_description=description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'ycls=ycls:run_cli',
        ],
    },
)