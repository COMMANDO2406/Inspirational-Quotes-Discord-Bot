from setuptools import setup, find_packages

setup(
    name='inspirational-quotes-bot',
    version='1.0.0',
    description='A Python bot that generates inspirational quotes in images',
    author='Raghav Sethi',
    author_email='',
    url='https://github.com/COMMANDO2406/Inspirational-Quotes-Bot',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pillow',
        'discord'
    ],
)
