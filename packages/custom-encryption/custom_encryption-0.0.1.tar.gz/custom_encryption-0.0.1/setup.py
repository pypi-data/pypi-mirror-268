from setuptools import find_packages,setup
import os


base_dir = os.path.abspath(os.path.dirname('encrypt_dir'))


setup(
    name='custom_encryption',
    version='0.0.1',
    description='A custom cryptography script using python',
    packages=find_packages(where='ct_encrypt'),
    long_description='A custom cryptography script',
    long_description_content_type='text/markdown',
    url='https://github.com/Boluex/custom-cryptography-python-script.git',
    author='Oladeji Olaoluwa',
    author_email='oladejiolaoluwa46@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators', 
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    keywords='custom crytography script build',
)