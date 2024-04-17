import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywchat",
    version="1.5.0",
    author="Hangjau",
    author_email="hangjau818@gmail.com",
    description="Custom WeChat push information database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms='any',
    url="https://github.com/HangJau/pywchat",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.22.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],

)
