from setuptools import setup, find_packages

setup(
    name='sanloop',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'requests'
    ],
    author='AKSHAY PIRANAV B',
    author_email='akshaypiranavb@gmail.com',
    description='Python library for integrating Arduino boards with Python through APIs.',
    url='https://github.com/akshaypiranav/pyduino',
    license='MIT',  
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
