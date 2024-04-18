from setuptools import setup, find_packages

setup(
    name='brat_tools',
    version='0.1',
    packages=find_packages(),
    description='A unofficial copy of BRAT toolkit for easy access.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='fx',
    author_email='itisfuqixu@gmail.com',
    url="https://github.com/nlplab",
    install_requires=[
            ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

