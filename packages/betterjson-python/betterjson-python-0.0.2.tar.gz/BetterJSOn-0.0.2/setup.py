from setuptools import setup

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
    name = 'BetterJSOn' ,
    version ='0.0.2',
    author = 'ruxixa',
    description ='BetterJSON is an enhanced version of the JSON data format',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages = ['modules'],
    install_requires = [],
    license = 'MIT',
    project_urls = {'Source': 'https://github.com/ruxixa/BetterJSON/'},
)