from setuptools import setup, find_packages

import lazyvpn

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='lazyvpn',
    version=lazyvpn.version,
    install_requires=requirements,
    author='Yuzhong Li, Clayton Blythe, Kareem Harouny, Karsten Roberts',
    author_email='yuzhongl@zillowgroup.com, claytonb@zillowgroup.com, kareemharouny@gmail.com, karstenr@zillowgroup.com',
    description="A CLI to connect to vpn via cisco anyconnect in one step",
    url='https://gitlab.zgtools.net/zillow/hackweek/lazyvpn',
    license='Apache License, v2.0',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite="tests",
    scripts=['bin/lazyvpn', 'bin/lazyvpn.cmd'],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License'
    ]
)
