from setuptools import setup, find_packages
setup(
name='lens_xai',
version='0.0.1',
author='Dwane van der Sluis',
author_email='your.email@example.com',
description='A short description of your package',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.10',
)


# To build the package
# python3 setup.py sdist

# To upload the package
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*