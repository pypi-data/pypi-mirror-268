from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ComradeAI',
    version='0.18.21',
    packages=find_packages(),
    description='A protocol and SDK for unified AI service interaction',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    author='Sergei Karulin',
    author_email='sk@spellsystems.com',
    url='https://github.com/SergeiKarulin/ComradeAI',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)