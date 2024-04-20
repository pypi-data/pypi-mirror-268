from setuptools import setup, find_packages

setup(
    name='yusefs_library',
    version = '0.2', #increment this every release!
    packages = find_packages(),
    install_requires=[ #add dependencies here
        'numpy>=1.11.1'
    ],
    entry_points={
        "console_scripts":[
            "yusefs_library = yusefs_library:hello",
        ],
    },
)

# python3 setup.py sdist bdist_wheel
