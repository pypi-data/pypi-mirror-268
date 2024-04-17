from setuptools import setup, find_packages

setup(
    name='betterjson-python',
    version='0.1.0',
    packages=['betterjson', 'betterjson.modules'],
    author='Jan Kowalski',
    author_email='a@a.com',
    description='BetterJSON is an enhanced version of the JSON data format',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ruxixa/BetterJSON',
    classifiers=[
        'Programming Language :: Python'
    ],
    keywords='kilka, słów, kluczowych, opisujących, Twoją, bibliotekę',
    python_requires='>=3.0',
    install_requires=[],
    project_urls={
        'Source': 'https://github.com/ruxixa/BetterJSON',
        'Bug Reports': 'https://github.com/ruxixa/BetterJSON/issues',
    },
)
