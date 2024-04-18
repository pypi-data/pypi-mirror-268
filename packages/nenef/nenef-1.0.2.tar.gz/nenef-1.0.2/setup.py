from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='nenef',
    version='1.0.2',
    author='ktotozdesest',
    author_email='kto00210@gmail.com',
    description='This is module for neuronetworks',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/ktotozdesest/nenef',
    packages=find_packages(),
    install_requires=['numpy>=1.24.1'],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='python neuronetworks neurenet',
    project_urls={
        'Documentation': 'https://github.com/ktotozdesest/nenef'
    },
    python_requires='>=3.7'
)
