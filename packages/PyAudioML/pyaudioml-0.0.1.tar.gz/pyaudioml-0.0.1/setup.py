from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyAudioML",
    version="0.0.1",
    author="Fabio Scielzo Ortiz",
    author_email="fabioscielzo98@gmail.com",
    description="This is a package that contains ML utils to deal with audio problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FabioScielzoOrtiz/PyAudioML_Package",  # add your project URL here
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas','numpy'],
    python_requires=">=3.7"
)
