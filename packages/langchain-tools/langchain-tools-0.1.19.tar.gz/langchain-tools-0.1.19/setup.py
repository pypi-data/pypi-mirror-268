import subprocess
import pkg_resources
import sys
import shutil
import os
import glob
from setuptools import setup, find_packages

### TODO: 1. Save your API token in the following file
pypi_api_token_file_name = 'pypi_api_token.txt'

### TODO: 2. Define the main version prefix for your package versioning.
# This will be used to increment the version number. 
# For example, if the main version is '0.1', the first version will be '0.1.0', and then '0.1.1', and so on.
# If you want to upgrade to '0.2.0', set main_version = '0.2'
main_version = '0.1'

def load_pypi_api_token():
    try:
        with open(pypi_api_token_file_name, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("PyPI API token file not found. Please ensure 'pypi_api_token.txt' exists.")

pypi_api_token = load_pypi_api_token()

def read_and_increment_version():
    version_file = 'last_version.txt'
    if os.path.exists(version_file):
        with open(version_file, 'r') as file:
            last_version = file.read().strip()
        if last_version.startswith(main_version):
            version_parts = last_version.split('.')
            version_parts[-1] = str(int(version_parts[-1]) + 1)
            new_version = '.'.join(version_parts)
        else:
            new_version = main_version + '.0'
    else:
        new_version = main_version + '.0'
    
    with open(version_file, 'w') as file:
        file.write(new_version)
    
    return new_version

def check_and_install_package(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        print(f"{package_name} is already installed.")
    except pkg_resources.DistributionNotFound:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def remove_build_dirs():
    directories = ['dist', 'build', '*.egg-info']
    for directory in directories:
        if os.path.isdir(directory):
            shutil.rmtree(directory)
        elif glob.glob(directory):
            for dir in glob.glob(directory):
                shutil.rmtree(dir)

def upload_package():
    try:
        subprocess.check_call([sys.executable, '-m', 'twine', 'upload', 'dist/*', '-u', '__token__', '-p', pypi_api_token])
        print("Package uploaded successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to upload package:", e)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append('sdist')
        sys.argv.append('bdist_wheel')

    check_and_install_package('twine')
    remove_build_dirs()
    new_version = read_and_increment_version()

    setup(
        name='langchain-tools',
        version=new_version,
        author='Langchain Tools Team',
        author_email='cheny@cheny.com',
        description='Simplifying, enhancing, and extending the LangChain library functionality',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/MartinChen1973/langchain-tools',
        # Specify the source directory here:
        package_dir={'': 'src'},
        # Now find_packages will look in the 'src' directory.
        packages=find_packages(where='src'),
        install_requires=[
            'langchain',
            'langchain-community',
            'langchain-openai'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10'
        ],
        python_requires='>=3.7',
        keywords='language processing, AI, natural language understanding, LangChain, LLM'
    )

    upload_package()  # Upload the package using twine
