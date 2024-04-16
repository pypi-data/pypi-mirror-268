
from setuptools import setup, find_packages

setup(
    name='arion_library',  # Replace with your package name
    version='1.1rc64.dev64',  # Replace with your package version
    author='Heni Nechi',  # Replace with your name
    author_email='h.nechi@arion-tech.com',  # Replace with your email
    url='https://github.com/Ariontech/ArionLibrary.git',  # Replace with your repository URL
    packages=find_packages(),  # Automatically find all packages
    python_requires='>=3.8',  # Specify Python version requirements
    install_requires=['pysftp==0.2.9', 'azure-core==1.29.6', 'azure-data-tables==12.5.0', 'azure-storage-blob==12.19.1', 'python-dotenv==1.0.1', 'pytest==8.1.1', 'pandas==2.0.3', 'pytest'],
)
