from setuptools import setup, find_packages

setup(
    name='vythonT',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'vythonT=src.run:main'
        ]
    }
)