"""
To push a new version to PyPi, update the version number
in rfhub_static/version.py and then run the following commands:
    $ python setup.py sdist
    $ python3 -m twine upload dist/*
"""
from setuptools import setup

__version__: str = "0.0.0"
filename: str = 'robot_doc_only/version.py'
exec(open(filename).read())

setup_requires_packages: list = ['wheel']
install_requires_packages: list = [
    'robotframework>=3.2.2'
]

setup(
    name='robotframework-doc-only',
    version=__version__,
    author='Bert Lindemann',
    author_email='bert.lindemann@gmail.com',
    maintainer='Bert Lindemann',
    maintainer_email='bert.lindemann@gmail.com',
    url='https://github.com/bli74/robotframework-doc-only/',
    keywords='robotframework',
    license='Apache License 2.0',
    description='Create test documentation without technical details',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    zip_safe=True,
    include_package_data=True,
    python_requires=">=3.6",
    setup_requires=setup_requires_packages,
    install_requires=install_requires_packages,
    extras_require={
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Robot Framework",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Intended Audience :: Developers",
    ],
    packages=[
        'robot_doc_only',
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            "testdoc_small = robot_doc_only.testdoc:create_testdoc_small",
            "testdoc_full = robot_doc_only.testdoc:create_testdoc_full"
        ]
    }
)