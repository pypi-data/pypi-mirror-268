from setuptools import setup, find_packages

setup(
    name='dynamic_reader_aws',
    version='1.0.1',
    description='This package is used to read the files directly from the Secrets manager in AWS using Secret name and secret key value',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hunaid Vekariya',
    author_email='alihunaid185@gmail.com',
    url='https://github.com/HunaidV/scripts/dynamic_reader_aws',
    packages=find_packages(),
    install_requires=[
        'boto3',
        # Add any other dependencies here
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)



