

# dynamic_reader_aws

dynamic_reader_aws is a Python library that simplifies the integration of AWS Secrets Manager with Django applications. It enables the seamless retrieval of secret values from AWS Secrets Manager and their direct integration into Django settings.py files.

## Features

- **Seamless Integration:** Utilizes boto3 to seamlessly interact with AWS Secrets Manager, enabling smooth retrieval of secret values.
- **Direct Integration with Django Settings:** Streamlines the integration of secret key values into Django settings.py files, eliminating the need for manual configuration.
- **Enhanced Security:** Ensures the secure handling of sensitive information by leveraging AWS Secrets Manager's encryption and access control features.
- **Simplified Configuration:** Requires minimal configuration, including the Secrets Manager name, AWS region, and AWS credentials (AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY), making it easy to get started.

## Installation

```bash
pip install dynamic_reader_aws



from dynamic_reader_aws import dynamic_secret_manager

# Provide AWS credentials and secret details
secrets_manager_name = "your_secrets_manager_name"
secret_key_name = "your_secret_key_name_in_secrets_manager"
region = "your_aws_region"
aws_access_key = "your_aws_access_key"
aws_secret_access_key = "your_aws_secret_access_key"
secret_key_name = "your_secret_key_name_in_secrets_manager"
# Integrate secrets with Django settings
dynamic_secret_manager(secrets_manager_name, secret_key_name, region, aws_access_key, aws_secret_access_key)
