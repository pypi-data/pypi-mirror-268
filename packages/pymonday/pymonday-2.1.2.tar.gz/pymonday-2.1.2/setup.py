from setuptools import setup, find_packages

setup(
    name='pymonday',
    version='2.1.2',
    packages=['pymonday'],
    include_package_data=True,
    description="PyMonday is a monday.com API Python Client Library, compatible with API version 2023-10 and later.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['httpx', 'python-dotenv', 'PyYAML', 'asyncio']
)
