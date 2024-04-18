from setuptools import setup, find_packages

setup(
    name='wonder-diffusion-sdk',
    version='0.0.4-dev0',
    description='Python SDK for common Wonder diffusion models',
    author='basri',
    author_email='basri@wonder.co',
    packages=find_packages(),
    install_requires=[
      'diffusers==0.26.3'
    ],
)