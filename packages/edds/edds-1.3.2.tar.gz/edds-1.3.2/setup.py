from setuptools import setup, find_packages

setup(
    name="edds",  
    version="1.3.2",  
    author="Altan Alaybeyoğlu",
    author_email="altanalaybeyoglu@gmail.com",
    description="The Central Bank of the Republic of Türkiye Electronic Data Distribution System Data Access Package", 
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/altanalaybeyoglu/edds",  
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
    ],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)