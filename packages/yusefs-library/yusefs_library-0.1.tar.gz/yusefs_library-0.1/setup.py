from setuptools import setup, find_packages

setup(
    name='yusefs_library',
    version = '0.1', #increment this every release!
    packages = find_packages(),
    install_requires=[ #add dependencies here
        'numpy>=1.11.1'
    ],
)

