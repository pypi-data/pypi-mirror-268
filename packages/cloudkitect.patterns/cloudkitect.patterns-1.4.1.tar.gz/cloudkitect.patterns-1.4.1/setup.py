import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cloudkitect.patterns",
    "version": "1.4.1",
    "description": "CloudKitect freemium patterns are built on top of CloudKitect freemium components which comply to various standards. Using these patterns you can host your website, or run your containerized app using ECS Fargate within a couple hours",
    "license": "Apache-2.0",
    "url": "https://github.com/cloudkitect/freemium",
    "long_description_content_type": "text/markdown",
    "author": "CloudKitect Inc<support@cloudkitect.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cloudkitect/freemium"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cloudkitect.patterns",
        "cloudkitect.patterns._jsii"
    ],
    "package_data": {
        "cloudkitect.patterns._jsii": [
            "patterns@1.4.1.jsii.tgz"
        ],
        "cloudkitect.patterns": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.137.0, <3.0.0",
        "cloudkitect.components>=1.4.0, <2.0.0",
        "constructs>=10.3.0, <11.0.0",
        "jsii>=1.97.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
