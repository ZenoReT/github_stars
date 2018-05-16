from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='github_stars',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
        entry_points={
        'console_scripts':
            ['github_stars = github_stars.github_stars:main']
        },
)