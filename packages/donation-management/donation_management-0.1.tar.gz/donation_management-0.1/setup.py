from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='donation_management',  # Replace with your package name
    version='0.1',  # Replace with your package version
    author='Ruban Thirukumaran',
    author_email='rubanthirukumaran@gmail.com',
    description='A library for managing donations in Django projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Rubanthirukumaran/Cpp-library.git',  # Replace with your package URL
    packages=find_packages(),
    install_requires=[
        'Django>=3.2',  # Adjust version as needed
        # Add any other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
