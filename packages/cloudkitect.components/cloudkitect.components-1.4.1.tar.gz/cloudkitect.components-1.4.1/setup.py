import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cloudkitect.components",
    "version": "1.4.1",
    "description": "CloudKitect freemium components are scaled down versions of CloudKitect enhanced components offered as monthly or yearly subscription. These are well architected components that offer out of the box monitoring, alerting and compliance to various standards.",
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
        "cloudkitect.components",
        "cloudkitect.components._jsii"
    ],
    "package_data": {
        "cloudkitect.components._jsii": [
            "components@1.4.1.jsii.tgz"
        ],
        "cloudkitect.components": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.137.0, <3.0.0",
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
