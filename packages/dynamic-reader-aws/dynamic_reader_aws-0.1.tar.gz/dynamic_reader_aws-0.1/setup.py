from setuptools import setup, find_packages

setup(
    name='dynamic_reader_aws',
    version='0.1',
    packages=find_packages(),
    description='Directly use AWS Secrets Manager with Django settings.py',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hunaid Vekariya',
    author_email='itsmehunaid@gmail.com',
    install_requires=[
        'boto3>=1.18.0'
    ]
)

