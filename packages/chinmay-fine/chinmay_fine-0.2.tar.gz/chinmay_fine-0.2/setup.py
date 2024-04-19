# setup.py

from setuptools import setup, find_packages

setup(
    name='chinmay_fine',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Chinmay',
    author_email='your@email.com',
    description='A Python library for interacting with the News API',
    url='https://github.com/your_username/news-api-python',
)