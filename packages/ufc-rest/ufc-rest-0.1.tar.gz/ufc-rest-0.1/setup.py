from setuptools import setup, find_packages

setup(
    name='ufc-rest',
    version='0.1',
    packages=find_packages(),
    author='Jackson Massey',
    author_email='jackmassey2000@gmail.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jackinthebox52/ufc-rest-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)