'''
# Waitcondition Hook for AWS Fargate task

WaitCondition hook for AWS Fargate tasks is a AWS CDK Construct that helps builders to run a AWS Fargate task with one or multiple container embedded into a CloudFormation lifecycle. You can use this construct add dependency between resources and the AWS Fargate task execution result (eg. Database migration, image build and packing, invoking third party/on-prem API). waitcondition-hook-for-aws-fargate-task construct will also handle the failure of the task, and rollback the CloudFormation stack after.

## Prerequisites

1. An AWS account
2. AWS Cloud Development Kit (CDK). For more information about this, see AWS CDK Toolkit (cdk command) in the AWS CDK documentation.
3. Node package manager (npm), installed and configured for CDK Typescript. For more information about this, see Downloading and installing Node.js and npm in the npm documentation.

## Target architecture

![Workflow](./image/workflow.png)

## Deployment steps

### Install the package:

```bash
yarn add aitcondition-hook-for-aws-fargate-task
```

### Usage:

```python
import * as cdk from 'aws-cdk-lib';
import { RemovalPolicy } from 'aws-cdk-lib';
import { Vpc } from 'aws-cdk-lib/aws-ec2';
import * as ecr from 'aws-cdk-lib/aws-ecr';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import { LogGroup } from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import { FargateRunner } from 'waitcondition-hook-for-aws-fargate-task';
import { Queue } from 'aws-cdk-lib/aws-sqs';

export class FargateRunnerTestStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);
        // Define the VPC
        const vpc = new Vpc(this, 'MyVpc')
        // Define the Fargate Task
        const taskDefinition = new ecs.FargateTaskDefinition(this, 'MyTask', {});
        // Import exiting ecr repo
        const repo = ecr.Repository.fromRepositoryName(this, 'MyRepo', 'RepoName');
        // Add a container to the task
        taskDefinition.addContainer('MyContainer', {
            image: ecs.ContainerImage.fromEcrRepository(repo),
        });
        // Create the Fargate runner
        const myFargateRunner = new FargateRunner(this, 'MyRunner', {
            fargateTaskDef: taskDefinition,
            timeout: `${60 * 5}`,
            vpc: vpc,
        });
        // Create the SQS queue
        const myQueue = new Queue(this, 'MyQueue', {});
        // Add dependency
        myQueue.node.addDependency(myFargateRunner);
    }
}
const app = new cdk.App();

const env = {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
};
new FargateRunnerTestStack(app, 'FargateRunnerTestStack', { env: env });
```

### Deploy!

```bash
cdk deploy
```

## Useful CDK commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_ecs as _aws_cdk_aws_ecs_ceddda9d
import constructs as _constructs_77d1e7e8


class FargateRunner(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="waitcondition-hook-for-aws-fargate-task.FargateRunner",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        fargate_task_def: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
        count: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param fargate_task_def: 
        :param count: 
        :param timeout: 
        :param vpc: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c536ce137484a9efb567d2d86eaa79f87152c8e5c72026802927dff06c09470)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FargateRunnerProps(
            fargate_task_def=fargate_task_def, count=count, timeout=timeout, vpc=vpc
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="waitConditionHanlderEndpoint")
    def wait_condition_hanlder_endpoint(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "waitConditionHanlderEndpoint"))


@jsii.data_type(
    jsii_type="waitcondition-hook-for-aws-fargate-task.FargateRunnerProps",
    jsii_struct_bases=[],
    name_mapping={
        "fargate_task_def": "fargateTaskDef",
        "count": "count",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class FargateRunnerProps:
    def __init__(
        self,
        *,
        fargate_task_def: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
        count: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param fargate_task_def: 
        :param count: 
        :param timeout: 
        :param vpc: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a841bd9d9e28253fa3dd9dc3999a0dd2545f9fffe4e55641c87bc6a965dfa1)
            check_type(argname="argument fargate_task_def", value=fargate_task_def, expected_type=type_hints["fargate_task_def"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fargate_task_def": fargate_task_def,
        }
        if count is not None:
            self._values["count"] = count
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def fargate_task_def(self) -> _aws_cdk_aws_ecs_ceddda9d.TaskDefinition:
        '''
        :stability: experimental
        '''
        result = self._values.get("fargate_task_def")
        assert result is not None, "Required property 'fargate_task_def' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.TaskDefinition, result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''
        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FargateRunner",
    "FargateRunnerProps",
]

publication.publish()

def _typecheckingstub__0c536ce137484a9efb567d2d86eaa79f87152c8e5c72026802927dff06c09470(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    fargate_task_def: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
    count: typing.Optional[jsii.Number] = None,
    timeout: typing.Optional[builtins.str] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a841bd9d9e28253fa3dd9dc3999a0dd2545f9fffe4e55641c87bc6a965dfa1(
    *,
    fargate_task_def: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
    count: typing.Optional[jsii.Number] = None,
    timeout: typing.Optional[builtins.str] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass
