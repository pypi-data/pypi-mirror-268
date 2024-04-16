from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='stringformatter03201',
    version='0.0.2',
    description='string formatter by eggSushi0320',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='eggSushi0320',
    author_email='astar5327z@gmail.com',
    url='https://github.com/lazarus0320/oss.git',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['stringformatter03201'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)