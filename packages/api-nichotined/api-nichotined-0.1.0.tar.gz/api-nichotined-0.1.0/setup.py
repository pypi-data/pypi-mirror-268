import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="api-nichotined",
    version="0.1.0",
    author="Nicholas Frederich",
    author_email="nicholas.frederich.lagaunne@gmail.com",
    description="Simple lib for testing rest API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nichotined/simple-api",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'curlify',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
