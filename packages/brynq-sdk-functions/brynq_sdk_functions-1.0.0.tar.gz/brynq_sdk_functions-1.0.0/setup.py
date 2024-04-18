from setuptools import setup


setup(
    name='brynq_sdk_functions',
    version='1.0.0',
    description='Helpful functions from BrynQ',
    long_description='Helpful functions from BrynQ',
    author='BrynQ',
    author_email='support@brynq.com',
    packages=["brynq_sdk.functions"],
    license='BrynQ License',
    install_requires=[
        'pandas>=1,<3',
        'requests>=2,<=3',
        'pyarrow>=10,<11'
    ],
    zip_safe=False,
)