'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-codepipeline-check-parameter-action

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-codepipeline-check-parameter-action)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-codepipeline-check-parameter-action/)

> Cdk component that checks if system parameters are set correctly

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-codepipeline-check-parameter-action
```

Python:

```bash
pip install cloudcomponents.cdk-codepipeline-check-parameter-action
```

## How to use

```python
import { CodePipelineCheckParameterAction } from '@cloudcomponents/cdk-codepipeline-check-parameter-action';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { Pipeline, Artifact } from 'aws-cdk-lib/aws-codepipeline';
import { CodeCommitSourceAction } from 'aws-cdk-lib/aws-codepipeline-actions';
import { Construct } from 'constructs';

export class CodePipelineCheckParameterActionStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const repository = new Repository(this, 'Repository', {
      repositoryName: 'MyRepositoryName',
    });

    const sourceArtifact = new Artifact();

    const sourceAction = new CodeCommitSourceAction({
      actionName: 'CodeCommit',
      repository,
      output: sourceArtifact,
      branch: 'master',
    });

    const checkAction = new CodePipelineCheckParameterAction({
      actionName: 'Check',
      parameterName: '/test',
      regExp: /^The.*Spain$/,
      logParameter: true,
    });

    new Pipeline(this, 'MyPipeline', {
      pipelineName: 'MyPipeline',
      stages: [
        {
          stageName: 'Source',
          actions: [sourceAction],
        },
        {
          stageName: 'Check',
          actions: [checkAction],
        },
      ],
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-check-parameter-action/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-check-parameter-action/LICENSE)
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

import aws_cdk.aws_codepipeline as _aws_cdk_aws_codepipeline_ceddda9d
import aws_cdk.aws_codepipeline_actions as _aws_cdk_aws_codepipeline_actions_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class CheckParameterFunction(
    _aws_cdk_aws_lambda_ceddda9d.Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CheckParameterFunction",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c362f914d2df13095b245a9c3f90defe554c7141fb177b536db62387c9cfec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CheckParamterFunctionProps(
            parameter_name=parameter_name, cross_account_role=cross_account_role
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CheckParamterFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "cross_account_role": "crossAccountRole",
    },
)
class CheckParamterFunctionProps:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceaf2e1ad361bb4c2972d0cd85dbbc56e4059f0cf822d74984499c5b12ab2b2a)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
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
        return "CheckParamterFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodePipelineCheckParameterAction(
    _aws_cdk_aws_codepipeline_actions_ceddda9d.Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CodePipelineCheckParameterAction",
):
    '''Represents a reference to a CodePipelineCheckParameterAction.'''

    def __init__(
        self,
        *,
        reg_exp: typing.Optional[typing.Union["RegExp", typing.Dict[builtins.str, typing.Any]]] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param reg_exp: Regular expression to validate the parameter.
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodePipelineCheckParameterActionProps(
            reg_exp=reg_exp,
            parameter_name=parameter_name,
            cross_account_role=cross_account_role,
            log_parameter=log_parameter,
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b72dc9d91286e2f3e16a7c62df65566101f5cf5633956bb7cf96253ea01f193)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument _stage", value=_stage, expected_type=type_hints["_stage"])
        options = _aws_cdk_aws_codepipeline_ceddda9d.ActionBindOptions(
            bucket=bucket, role=role
        )

        return typing.cast(_aws_cdk_aws_codepipeline_ceddda9d.ActionConfig, jsii.invoke(self, "bound", [scope, _stage, options]))


class CodePipelineCheckUrlParameterAction(
    CodePipelineCheckParameterAction,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CodePipelineCheckUrlParameterAction",
):
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.bool] = None,
        strict: typing.Optional[builtins.bool] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Only match an exact string. Default: true
        :param strict: Force URLs to start with a valid protocol or www.
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodePipelineCheckUrlParameterActionProps(
            exact=exact,
            strict=strict,
            parameter_name=parameter_name,
            cross_account_role=cross_account_role,
            log_parameter=log_parameter,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CommonCodePipelineCheckParameterActionProps",
    jsii_struct_bases=[_aws_cdk_aws_codepipeline_ceddda9d.CommonAwsActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "parameter_name": "parameterName",
        "cross_account_role": "crossAccountRole",
        "log_parameter": "logParameter",
    },
)
class CommonCodePipelineCheckParameterActionProps(
    _aws_cdk_aws_codepipeline_ceddda9d.CommonAwsActionProps,
):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b10f02cfdeaece2823930ff6ec66fa2a3fb45e59b9e05e0f4a3193250f3e3fd1)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
            check_type(argname="argument log_parameter", value=log_parameter, expected_type=type_hints["log_parameter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "parameter_name": parameter_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role
        if log_parameter is not None:
            self._values["log_parameter"] = log_parameter

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
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Role for crossAccount permission.'''
        result = self._values.get("cross_account_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def log_parameter(self) -> typing.Optional[builtins.bool]:
        '''Parameter is logged after successful check.

        :default: false The parameter is not logged
        '''
        result = self._values.get("log_parameter")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonCodePipelineCheckParameterActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.RegExp",
    jsii_struct_bases=[],
    name_mapping={"source": "source"},
)
class RegExp:
    def __init__(self, *, source: builtins.str) -> None:
        '''
        :param source: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa03c023475c8f6d0b01f06a1a4b1a4b173a566ef3196f25ddded8d712150b3)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
        }

    @builtins.property
    def source(self) -> builtins.str:
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegExp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodePipelineCheckEmailParameterAction(
    CodePipelineCheckParameterAction,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CodePipelineCheckEmailParameterAction",
):
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.bool] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Only match an exact string. Default: true
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = CodePipelineCheckEmailParameterActionProps(
            exact=exact,
            parameter_name=parameter_name,
            cross_account_role=cross_account_role,
            log_parameter=log_parameter,
            role=role,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CodePipelineCheckEmailParameterActionProps",
    jsii_struct_bases=[CommonCodePipelineCheckParameterActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "parameter_name": "parameterName",
        "cross_account_role": "crossAccountRole",
        "log_parameter": "logParameter",
        "exact": "exact",
    },
)
class CodePipelineCheckEmailParameterActionProps(
    CommonCodePipelineCheckParameterActionProps,
):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
        exact: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        :param exact: Only match an exact string. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eac801e191eec52fef8d933737323c4cfec5ca55b93d08917bdb4075d5f2eeb)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
            check_type(argname="argument log_parameter", value=log_parameter, expected_type=type_hints["log_parameter"])
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "parameter_name": parameter_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role
        if log_parameter is not None:
            self._values["log_parameter"] = log_parameter
        if exact is not None:
            self._values["exact"] = exact

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
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Role for crossAccount permission.'''
        result = self._values.get("cross_account_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def log_parameter(self) -> typing.Optional[builtins.bool]:
        '''Parameter is logged after successful check.

        :default: false The parameter is not logged
        '''
        result = self._values.get("log_parameter")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exact(self) -> typing.Optional[builtins.bool]:
        '''Only match an exact string.

        :default: true
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineCheckEmailParameterActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CodePipelineCheckParameterActionProps",
    jsii_struct_bases=[CommonCodePipelineCheckParameterActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "parameter_name": "parameterName",
        "cross_account_role": "crossAccountRole",
        "log_parameter": "logParameter",
        "reg_exp": "regExp",
    },
)
class CodePipelineCheckParameterActionProps(
    CommonCodePipelineCheckParameterActionProps,
):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
        reg_exp: typing.Optional[typing.Union[RegExp, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        :param reg_exp: Regular expression to validate the parameter.
        '''
        if isinstance(reg_exp, dict):
            reg_exp = RegExp(**reg_exp)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c455f546e9d8fb079b4d790adf324e2cce4017128035b693f73316a0f962d1ef)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
            check_type(argname="argument log_parameter", value=log_parameter, expected_type=type_hints["log_parameter"])
            check_type(argname="argument reg_exp", value=reg_exp, expected_type=type_hints["reg_exp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "parameter_name": parameter_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role
        if log_parameter is not None:
            self._values["log_parameter"] = log_parameter
        if reg_exp is not None:
            self._values["reg_exp"] = reg_exp

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
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Role for crossAccount permission.'''
        result = self._values.get("cross_account_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def log_parameter(self) -> typing.Optional[builtins.bool]:
        '''Parameter is logged after successful check.

        :default: false The parameter is not logged
        '''
        result = self._values.get("log_parameter")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reg_exp(self) -> typing.Optional[RegExp]:
        '''Regular expression to validate the parameter.'''
        result = self._values.get("reg_exp")
        return typing.cast(typing.Optional[RegExp], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineCheckParameterActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-check-parameter-action.CodePipelineCheckUrlParameterActionProps",
    jsii_struct_bases=[CommonCodePipelineCheckParameterActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "role": "role",
        "parameter_name": "parameterName",
        "cross_account_role": "crossAccountRole",
        "log_parameter": "logParameter",
        "exact": "exact",
        "strict": "strict",
    },
)
class CodePipelineCheckUrlParameterActionProps(
    CommonCodePipelineCheckParameterActionProps,
):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        parameter_name: builtins.str,
        cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        log_parameter: typing.Optional[builtins.bool] = None,
        exact: typing.Optional[builtins.bool] = None,
        strict: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param role: The Role in which context's this Action will be executing in. The Pipeline's Role will assume this Role (the required permissions for that will be granted automatically) right before executing this Action. This Action will be passed into your ``IAction.bind`` method in the ``ActionBindOptions.role`` property. Default: a new Role will be generated
        :param parameter_name: The name of the parameter.
        :param cross_account_role: Role for crossAccount permission.
        :param log_parameter: Parameter is logged after successful check. Default: false The parameter is not logged
        :param exact: Only match an exact string. Default: true
        :param strict: Force URLs to start with a valid protocol or www.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__983e9f5850c8ce86bea7ae1453114f672708de88dd8533d1fa85cc13f7ee7783)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
            check_type(argname="argument log_parameter", value=log_parameter, expected_type=type_hints["log_parameter"])
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "parameter_name": parameter_name,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if role is not None:
            self._values["role"] = role
        if cross_account_role is not None:
            self._values["cross_account_role"] = cross_account_role
        if log_parameter is not None:
            self._values["log_parameter"] = log_parameter
        if exact is not None:
            self._values["exact"] = exact
        if strict is not None:
            self._values["strict"] = strict

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
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Role for crossAccount permission.'''
        result = self._values.get("cross_account_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def log_parameter(self) -> typing.Optional[builtins.bool]:
        '''Parameter is logged after successful check.

        :default: false The parameter is not logged
        '''
        result = self._values.get("log_parameter")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exact(self) -> typing.Optional[builtins.bool]:
        '''Only match an exact string.

        :default: true
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def strict(self) -> typing.Optional[builtins.bool]:
        '''Force URLs to start with a valid protocol or www.'''
        result = self._values.get("strict")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineCheckUrlParameterActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CheckParameterFunction",
    "CheckParamterFunctionProps",
    "CodePipelineCheckEmailParameterAction",
    "CodePipelineCheckEmailParameterActionProps",
    "CodePipelineCheckParameterAction",
    "CodePipelineCheckParameterActionProps",
    "CodePipelineCheckUrlParameterAction",
    "CodePipelineCheckUrlParameterActionProps",
    "CommonCodePipelineCheckParameterActionProps",
    "RegExp",
]

publication.publish()

def _typecheckingstub__40c362f914d2df13095b245a9c3f90defe554c7141fb177b536db62387c9cfec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameter_name: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceaf2e1ad361bb4c2972d0cd85dbbc56e4059f0cf822d74984499c5b12ab2b2a(
    *,
    parameter_name: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b72dc9d91286e2f3e16a7c62df65566101f5cf5633956bb7cf96253ea01f193(
    scope: _constructs_77d1e7e8.Construct,
    _stage: _aws_cdk_aws_codepipeline_ceddda9d.IStage,
    *,
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    role: _aws_cdk_aws_iam_ceddda9d.IRole,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b10f02cfdeaece2823930ff6ec66fa2a3fb45e59b9e05e0f4a3193250f3e3fd1(
    *,
    action_name: builtins.str,
    run_order: typing.Optional[jsii.Number] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    parameter_name: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    log_parameter: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa03c023475c8f6d0b01f06a1a4b1a4b173a566ef3196f25ddded8d712150b3(
    *,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eac801e191eec52fef8d933737323c4cfec5ca55b93d08917bdb4075d5f2eeb(
    *,
    action_name: builtins.str,
    run_order: typing.Optional[jsii.Number] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    parameter_name: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    log_parameter: typing.Optional[builtins.bool] = None,
    exact: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c455f546e9d8fb079b4d790adf324e2cce4017128035b693f73316a0f962d1ef(
    *,
    action_name: builtins.str,
    run_order: typing.Optional[jsii.Number] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    parameter_name: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    log_parameter: typing.Optional[builtins.bool] = None,
    reg_exp: typing.Optional[typing.Union[RegExp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__983e9f5850c8ce86bea7ae1453114f672708de88dd8533d1fa85cc13f7ee7783(
    *,
    action_name: builtins.str,
    run_order: typing.Optional[jsii.Number] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    parameter_name: builtins.str,
    cross_account_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    log_parameter: typing.Optional[builtins.bool] = None,
    exact: typing.Optional[builtins.bool] = None,
    strict: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
