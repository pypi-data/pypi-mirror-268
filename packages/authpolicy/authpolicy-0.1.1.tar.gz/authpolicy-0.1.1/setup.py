import os

import setuptools

os.chdir(os.path.abspath(os.path.dirname(__file__)))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="authpolicy",
    version="0.1.1",
    author="Arpit Maheshwari",
    author_email="hello@authpolicy.com",
    description="Python SDK for AuthPolicy.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AuthPolicy/sdk-python",
    license="MIT",
    keywords="auth policy, permissions, authentication, authorization, rbac, abac, permissions as service",
    packages=setuptools.find_packages(where='src',
                                      exclude=["tests", "tests.*"]),
    package_dir={'': 'src'},
    install_requires=['requests >= 2.20'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    setup_requires=["wheel"],
)
