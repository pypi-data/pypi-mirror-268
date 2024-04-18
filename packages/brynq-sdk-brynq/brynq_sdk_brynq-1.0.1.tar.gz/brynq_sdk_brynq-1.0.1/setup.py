from setuptools import setup


setup(
    name='brynq_sdk_brynq',
    version='1.0.1',
    description='BrynQ SDK for the BrynQ.com platform',
    long_description='BrynQ SDK for the BrynQ.com platform',
    author='BrynQ',
    author_email='support@brynq.com',
    packages=["brynq_sdk.brynq"],
    license='BrynQ License',
    install_requires=[
        'requests>=2,<=3'
    ],
    zip_safe=False,
)
