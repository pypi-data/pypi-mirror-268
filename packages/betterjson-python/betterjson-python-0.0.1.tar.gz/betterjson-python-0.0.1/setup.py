from setuptools import setup

setup (
    name = 'betterjson-python' ,
    version ='0.0.1',
    author = 'ruxixa',
    description ='BetterJSON is an enhanced version of the JSON data format',
    packages = ['modules'],
    install_requires = [],
    license = 'MIT',
    project_urls = {'Source': 'https://github.com/ruxixa/BetterJSON/'},
    scripts = ['betterjson.py', '__version__.py']
)