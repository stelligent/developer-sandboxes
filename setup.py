import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="dev_sandbox",
    version="0.1.0",
    description="Demonstrates 3 solutions for creating a Developer Sandbox using tags on AWS using attribute based access control.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Scott Nixon <scott.nixon@stelligent.com>",
    package_dir={"": "dev_sandbox"},
    packages=setuptools.find_packages(where="dev_sandbox"),
    install_requires=[
        "aws-cdk.core==1.32.2",
        "boto3==1.12.30",
        "aws-cdk.aws-iam==1.32.2",
        "aws-cdk.aws-ec2==1.32.2",
        "pytest",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
