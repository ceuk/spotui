from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('spotui/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="spotui",
    version=main_ns['__version__'],
    author="ceuk",
    description="Spotify TUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="spotify spotifytui",
    url="https://github.com/ceuk/spotui",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.4",
    install_requires=["spotipy==2.22.1"],
    entry_points={"console_scripts": ["spotui=spotui.__main__:main"]},
)
