from setuptools import setup


setup(
    name='brynq_sdk_personio',
    version='0.1.0',
    description='Personio wrapper from BrynQ',
    long_description='Personio wrapper from BrynQ',
    author='BrynQ',
    author_email='support@brynq.com',
    packages=["brynq_sdk.personio"],
    license='BrynQ License',
    install_requires=[
        'brynq-sdk-brynq>=1',
        'pandas>=2.2.0,<3.0.0',
    ],
    zip_safe=False,
)