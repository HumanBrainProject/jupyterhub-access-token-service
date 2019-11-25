from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

requirements = ['jupyterhub>=1.0']

setup(
    name='jupyterhub-access-token-service',
    version='0.1.0',
    description='Jupyterhub Access Token Service',
    long_description=long_description,
    author= "Jonathan Villemaire-Krajden, EPFL",
    author_email= "jonathan.villemaire-krajden@epfl.ch",
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'access-token-service=access_token_service:main',
        ],
    },
)
