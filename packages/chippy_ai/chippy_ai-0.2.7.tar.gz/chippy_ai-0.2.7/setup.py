from setuptools import setup, find_packages

setup(
    name='chippy_ai',
    version='0.1',
    description='A description of your package.',  # Add a brief description
    author='Your Name',                            # Optionally add author name
    author_email='your.email@example.com',         # Optionally add author email
    url='https://github.com/yourusername/chippy_ai',  # Optionally add the URL of your project
    packages=find_packages(),
    include_package_data=True,  # Uncomment this if you use MANIFEST.in for including non-code files
    package_data={
        'chippy_ai': ['config.ini', 'README.md']
    },
    install_requires=[
        'OpenAI',          # Ensure these are the correct package names on PyPI
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'chip=chippy_ai.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
