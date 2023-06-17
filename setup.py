import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TabularDataInvestigation',
    packages=['TabularDataInvestigation'],
    version='0.0.7',
    license='MIT',
    description='This package provide a fast tabular data investigation and it will eligible for ML model building and also helps to developers in their projects when needed ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Tanvir Islam',
    author_email='islamtanvir659@gmail.com',
    url='https://github.com/Tanvir223/TabularDataInvestigation',
    project_urls = {
        "Bug Tracker": "https://github.com/Tanvir223/TabularDataInvestigation/issues"
    },
    install_requires=['requests'],

    download_url="https://github.com/Tanvir223/TabularDataInvestigation/archive/refs/tags/0.0.7.tar.gz",
    keywords=["pypi", "TabularDataInvestigation", "TabularData", "Data-Manupulation", "Data-Preprocessing", "Data Cleaning","Machine Learning", "Artificial Intelligence", "Industry Data" , "Data Science"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ]
)