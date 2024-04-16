import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "apidays24pj",
    "version": "0.0.14",
    "description": "@vianho/apidays24pj",
    "license": "Apache-2.0",
    "url": "https://github.com/vianho/projen-projects",
    "long_description_content_type": "text/markdown",
    "author": "Silviana<email@example.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/vianho/projen-projects"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "apidays24pj",
        "apidays24pj._jsii"
    ],
    "package_data": {
        "apidays24pj._jsii": [
            "apidays24pj@0.0.14.jsii.tgz"
        ],
        "apidays24pj": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "constructs>=10.3.0, <11.0.0",
        "jsii>=1.97.0, <2.0.0",
        "projen>=0.81.0, <0.82.0",
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
