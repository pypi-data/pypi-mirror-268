# setup.py

from setuptools import setup, find_packages

setup(
    name='chippy_ai',
    version='0.1',
    packages=find_packages(),
    #include_package_data=True,
    package_data={'chippy_ai': ['config.ini', 'README.md']}, 
    entry_points={
        'console_scripts': [
            'chip=chippy_ai.main:main',
            #'chip=chip.main:main',
        ],
    }
)
