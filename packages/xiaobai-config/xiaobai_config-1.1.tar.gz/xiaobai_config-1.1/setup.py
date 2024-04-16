import setuptools
import xiaobai_config

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaobai_config",
    version=xiaobai_config.__version__,
    author="xiaobai",
    author_email="xiaobaizrx@gmail.com",
    description="A small tool to parse and store project config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
