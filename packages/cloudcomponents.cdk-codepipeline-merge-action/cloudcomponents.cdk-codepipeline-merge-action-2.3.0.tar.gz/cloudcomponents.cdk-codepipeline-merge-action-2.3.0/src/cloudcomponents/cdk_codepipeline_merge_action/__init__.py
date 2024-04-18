'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-codepipeline-merge-action

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-codepipeline-merge-action)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-codepipeline-merge-action/)

> Cdk component that automatically merge branches in codepipelines

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-codepipeline-merge-action
```

Python:

```bash
pip install cloudcomponents.cdk-codepipeline-merge-action
```

## How to use

```python
import { CodePipelineMergeAction } from '@cloudcomponents/cdk-codepipeline-merge-action';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { Pipeline, Artifact } from 'aws-cdk-lib/aws-codepipeline';
import { CodeCommitSourceAction } from 'aws-cdk-lib/aws-codepipeline-actions';
import { Construct } from 'constructs';

export class CodePipelineMergeActionStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const repository = new Repository(this, 'Repository', {
      repositoryName: 'merge-action-repository',
    });

    const sourceArtifact = new Artifact();

    const sourceAction = new CodeCommitSourceAction({
      actionName: 'CodeCommit',
      repository,
      output: sourceArtifact,
      branch: 'next',
    });

    const mergeAction = new CodePipelineMergeAction({
      actionName: 'Merge',
      repository,
      sourceCommitSpecifier: 'next',
      destinationCommitSpecifier: 'master',
    });

    new Pipeline(this, 'Pipeline', {
      pipelineName: 'merge-action-pipeline',
      stages: [
        {
          stageName: 'Source',
          actions: [sourceAction],
        },
        {
          stageName: 'Merge',
          actions: [mergeAction],
        },
      ],
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-merge-action/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-merge-action/LICENSE)
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

import aws_cdk.aws_codecommit as _aws_cdk_aws_codecommit_ceddda9d
import aws_cdk.aws_codepipeline as _aws_cdk_aws_codepipeline_ceddda9d
import aws_cdk.aws_codepipeline_actions as _aws_cdk_aws_codepipeline_actions_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class CodePipelineMergeAction(
    _aws_cdk_aws_codepipeline_actions_ceddda9d.Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-merge-action.CodePipelineMergeAction",
):
    '''Represents a reference to a CodePipelineMergeAction.'''

    def __init__(
        self,
        *,
        destination_commit_specifier: builtins.str,
        repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
        source_commit_specifier: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_commit_specifier: The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
        :param repository: The CodeCommit repository.
        :param source_commit_specifier: The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
        :param cross_account_role: Role for crossAccount permission.
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodePipelineMergeActionProps(
            destination_commit_specifier=destination_commit_specifier,
            repository=repository,
            source_commit_specifier=source_commit_specifier,
            cross_account_role=cross_account_role,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: _constructs_77d1e7e8.Construct,
        _stage: _aws_cdk_aws_codepipeline_ceddda9d.IStage,
        *,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        role: _aws_cdk_aws_iam_ceddda9d.IRole,
    ) -> _aws_cdk_aws_codepipeline_ceddda9d.ActionConfig:
        '''This is a renamed version of the ``IAction.bind`` method.

        :param scope: -
        :param _stage: -
        :param bucket: 
        :param role: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994cb87057a4d5dfdb233340676b8ded26d173c324d9b8fb5185ce4c550a61ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument _stage", value=_stage, expected_type=type_hints["_stage"])
        options = _aws_cdk_aws_codepipeline_ceddda9d.ActionBindOptions(
            bucket=bucket, role=role
        )

        return typing.cast(_aws_cdk_aws_codepipeline_ceddda9d.ActionConfig, jsii.invoke(self, "bound", [scope, _stage, options]))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-merge-action.CodePipelineMergeActionProps",
    jsii_struct_bases=[_aws_cdk_aws_codepipeline_ceddda9d.CommonAwsActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "destination_commit_specifier": "destinationCommitSpecifier",
        "repository": "repository",
        "source_commit_specifier": "sourceCommitSpecifier",
        "cross_account_role": "crossAccountRole",
    },
)
class CodePipelineMergeActionProps(
    _aws_cdk_aws_codepipeline_ceddda9d.CommonAwsActionProps,
):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        destination_commit_specifier: builtins.str,
        repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
        source_commit_specifier: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param destination_commit_specifier: The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
        :param repository: The CodeCommit repository.
        :param source_commit_specifier: The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
        :param cross_account_role: Role for crossAccount permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76481d694b7c4913bab4639536c6b711b3296b3ecaf5db49a28c554b9ba7186e)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument destination_commit_specifier", value=destination_commit_specifier, expected_type=type_hints["destination_commit_specifier"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument source_commit_specifier", value=source_commit_specifier, expected_type=type_hints["source_commit_specifier"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "destination_commit_specifier": destination_commit_specifier,
            "repository": repository,
            "source_commit_specifier": source_commit_specifier,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The physical, human-readable name of the Action.

        Note that Action names must be unique within a single Stage.
        '''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_order(self) -> typing.Optional[jsii.Number]:
        '''The runOrder property for this Action.

        RunOrder determines the relative order in which multiple Actions in the same Stage execute.

        :default: 1

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html
        '''
        result = self._values.get("run_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''The name of the namespace to use for variables emitted by this action.

        :default:

        - a name will be generated, based on the stage and action names,
        if any of the action's variables were referenced - otherwise,
        no namespace will be set
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''The Role in which context's this Action will be executing in.

        The Pipeline's Role will assume this Role
        (the required permissions for that will be granted automatically)
        right before executing this Action.
        This Action will be passed into your ``IAction.bind``
        method in the ``ActionBindOptions.role`` property.

        :default: a new Role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def destination_commit_specifier(self) -> builtins.str:
        '''The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).'''
        result = self._values.get("destination_commit_specifier")
        assert result is not None, "Required property 'destination_commit_specifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> _aws_cdk_aws_codecommit_ceddda9d.IRepository:
        '''The CodeCommit repository.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(_aws_cdk_aws_codecommit_ceddda9d.IRepository, result)

    @builtins.property
    def source_commit_specifier(self) -> builtins.str:
        '''The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).'''
        result = self._values.get("source_commit_specifier")
        assert result is not None, "Required property 'source_commit_specifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Role for crossAccount permission.'''
        result = self._values.get("cross_account_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineMergeActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MergeBranchesFunction(
    _aws_cdk_aws_lambda_ceddda9d.Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-merge-action.MergeBranchesFunction",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param repository: The CodeCommit repository.
        :param cross_account_role: Role for crossAccount permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80aa45b2e474535d128b838d8aaae971564f3da490f40fbf295d1bc6f7ea7c8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MergeBranchesFunctionProps(
            repository=repository, cross_account_role=cross_account_role
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-merge-action.MergeBranchesFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "repository": "repository",
        "cross_account_role": "crossAccountRole",
    },
)
class MergeBranchesFunctionProps:
    def __init__(
        self,
        *,
        repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''
        :param repository: The CodeCommit repository.
        :param cross_account_role: Role for crossAccount permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70461caad314c9ac8fc666ab322614429ad6a1470c51d7f88c873718a902b2a)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository": repository,
        }
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role

    @builtins.property
    def repository(self) -> _aws_cdk_aws_codecommit_ceddda9d.IRepository:
        '''The CodeCommit repository.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(_aws_cdk_aws_codecommit_ceddda9d.IRepository, result)

    @builtins.property
    def cross_account_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Role for crossAccount permission.'''
        result = self._values.get("cross_account_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MergeBranchesFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CodePipelineMergeAction",
    "CodePipelineMergeActionProps",
    "MergeBranchesFunction",
    "MergeBranchesFunctionProps",
]

publication.publish()

def _typecheckingstub__994cb87057a4d5dfdb233340676b8ded26d173c324d9b8fb5185ce4c550a61ca(
    scope: _constructs_77d1e7e8.Construct,
    _stage: _aws_cdk_aws_codepipeline_ceddda9d.IStage,
    *,
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    role: _aws_cdk_aws_iam_ceddda9d.IRole,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76481d694b7c4913bab4639536c6b711b3296b3ecaf5db49a28c554b9ba7186e(
    *,
    action_name: builtins.str,
    run_order: typing.Optional[jsii.Number] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    destination_commit_specifier: builtins.str,
    repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
    source_commit_specifier: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80aa45b2e474535d128b838d8aaae971564f3da490f40fbf295d1bc6f7ea7c8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70461caad314c9ac8fc666ab322614429ad6a1470c51d7f88c873718a902b2a(
    *,
    repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass
