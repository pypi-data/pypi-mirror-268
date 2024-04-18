from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='sembansurga',
    version='1.1.1',
    author='sidharth',
    author_email='sidharthss2690@gmail.com',
    description='Simply superb',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'libtorrent',
        'usellm',

    

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    options={'easy_install': {'quiet': True}},

)