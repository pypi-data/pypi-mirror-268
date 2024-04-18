import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cloudcomponents.cdk-chatops",
    "version": "2.3.0",
    "description": "Constructs for chattool integration: #slack / msteams",
    "license": "MIT",
    "url": "https://github.com/cloudcomponents/cdk-constructs",
    "long_description_content_type": "text/markdown",
    "author": "hupe1980",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cloudcomponents/cdk-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cloudcomponents.cdk_chatops",
        "cloudcomponents.cdk_chatops._jsii"
    ],
    "package_data": {
        "cloudcomponents.cdk_chatops._jsii": [
            "cdk-chatops@2.3.0.jsii.tgz"
        ],
        "cloudcomponents.cdk_chatops": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.28.0, <3.0.0",
        "constructs>=10.0.41, <11.0.0",
        "jsii>=1.95.0, <2.0.0",
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
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
