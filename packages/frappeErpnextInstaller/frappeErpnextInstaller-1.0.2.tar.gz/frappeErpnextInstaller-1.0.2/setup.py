from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='frappeErpnextInstaller',
    version='1.0.2',
    author='Akinkunmi Nasiru',
    description='PIP Installer for Frappe Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'installer = installer:main',
        ],
    },
)
