import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RoboCupDBA",
    version="0.3",
    author="blueboxdev",
    author_email="thanakorn.vsalab@gmail.com",
    description="A small example package MongoDB Robo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bluebox-dev/RoboCupDBA",
    packages=setuptools.find_packages(),
    install_requires=[
        'dnspython',
        'install',
        'pymongo'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)