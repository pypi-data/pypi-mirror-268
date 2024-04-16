import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "waitcondition-hook-for-aws-fargate-task",
    "version": "1.0.4",
    "description": "AWS CDK Construct that run a Fargate task. Stack will process only when Fargate task executed successfully and all containers exit with code 0, otherwise rollback",
    "license": "MIT-0",
    "url": "https://github.com/aws-samples/waitcondition-hook-for-aws-fargate-task.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon.com, Inc. or its affiliates. All Rights Reserved.<fanhongy@amazon.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws-samples/waitcondition-hook-for-aws-fargate-task.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "waitcondition-hook-for-aws-fargate-task",
        "waitcondition-hook-for-aws-fargate-task._jsii"
    ],
    "package_data": {
        "waitcondition-hook-for-aws-fargate-task._jsii": [
            "waitcondition-hook-for-aws-fargate-task@1.0.4.jsii.tgz"
        ],
        "waitcondition-hook-for-aws-fargate-task": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.137.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.93.0, <2.0.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
