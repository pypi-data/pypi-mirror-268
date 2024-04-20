from setuptools import setup, find_packages
import os
import dotenv
# Get the absolute path to the requirements.txt file
# requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')

# Read the dependencies from requirements.txt
# with open(requirements_file) as f:
#     requirements = f.read().splitlines()

# Get the absolute path to the .env file
env_file = os.path.join(os.path.dirname(__file__), '.env')

# Load the environment variables from the .env file
dotenv.load_dotenv(dotenv_path=env_file)

setup(
    name='accusort',
    version='0.6',
    description="AccuSort is a Python package that sorts image PDF files into segregated folders based on the accuracy of PN numbers detected in the image and the file name.",
    long_description='''
    AccuSort
    ========

    AccuSort is a Python package that sorts image PDF files into segregated folders based on the accuracy of PN numbers detected in the image and the file name.

    Installation
    ------------

    1. Run the `export_variables.sh` script on Mac or Linux, and the corresponding batch file on Windows in the terminal or command prompt.
    2. Install AccuSort using pip:
       ```
       pip install accusort
       ```

    Usage
    -----

    1. In your teminal/command prompt, Navigate to the directory containing the image master folder (the folder containing the image sub-folders).
    2. Run the following command to sort the images:
       ```
       accusort <image_master_folder_name>
       ```
    3. The script saves the segragated folders in the respective subfolders of images.

    ''',
    long_description_content_type='text/markdown',
    author='Sixtysix Technologies',
    author_email='sangeeth@sixtysixtech.com',
        packages=find_packages(include=['eagle', 'eagle.*','eagle.scripts']),
        package_data={
            'eagle': ['scripts/banner.txt'],
        },
    install_requires=[
        'art>=6.1',
        'beautifulsoup4>=4.12.3',
        'cachetools>=5.3.3',
        'certifi>=2024.2.2',
        'charset-normalizer>=3.3.2',
        'colorama>=0.4.6',
        'fire>=0.6.0',
        'google-api-core>=2.18.0',
        'google-auth>=2.29.0',
        'google-cloud-documentai>=2.25.0',
        'googleapis-common-protos>=1.63.0',
        'grpcio>=1.62.1',
        'grpcio-status>=1.62.1',
        'idna>=3.7',
        'pip-chill>=1.0.3',
        'proto-plus>=1.23.0',
        'protobuf>=4.25.3',
        'pyasn1>=0.6.0',
        'pyasn1_modules>=0.4.0',
        'pyfiglet>=1.0.2',
        'python-dotenv>=1.0.1',
        'requests>=2.31.0',
        'rsa>=4.9',
        'six>=1.16.0',
        'soupsieve>=2.5',
        'termcolor>=2.4.0',
        'text2art>=0.2.0',
        'tqdm>=4.66.2',
        'urllib3>=2.2.1'
    ],
    entry_points={
        'console_scripts': [
            'accusort=eagle.main:main',
        ],
    },
)