import setuptools
import xiaobai_id_validator

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaobai_id_validator",
    version=xiaobai_id_validator.__version__,
    author="xiaobai",
    author_email="",
    description="Chinese idcard validator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)