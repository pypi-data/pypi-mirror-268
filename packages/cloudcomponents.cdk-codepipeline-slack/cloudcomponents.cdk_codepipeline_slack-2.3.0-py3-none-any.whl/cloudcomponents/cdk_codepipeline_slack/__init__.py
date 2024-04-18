'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-codepipeline-slack

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-codepipeline-slack)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-codepipeline-slack/)
[![Mentioned in Awesome CDK](https://awesome.re/mentioned-badge.svg)](https://github.com/kolomied/awesome-cdk)

> Cdk component that provisions a #slack approval workflow and notification messages on codepipeline state changes

![Approval Workflow](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/packages/cdk-codepipeline-slack/assets/approval_workflow.png)

![Review Dialog](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/packages/cdk-codepipeline-slack/assets/review_dialog.png)

## Install

TypeScript/JavaScript:

```bash
npm install --save @cloudcomponents/cdk-codepipeline-slack
```

Python:

```bash
pip install cloudcomponents.cdk-codepipeline-slack
```

## How to use

```python
import { SlackApprovalAction, SlackNotifier } from '@cloudcomponents/cdk-codepipeline-slack';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { Pipeline, Artifact } from 'aws-cdk-lib/aws-codepipeline';
import { CodeCommitSourceAction } from 'aws-cdk-lib/aws-codepipeline-actions';
import { Construct } from 'constructs';

export class CodePipelineSlackApprovalStack extends Stack {
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
    });

    if (typeof process.env.SLACK_BOT_TOKEN === 'undefined') {
      throw new Error('environment variable SLACK_BOT_TOKEN undefined');
    }
    const slackBotToken = process.env.SLACK_BOT_TOKEN;

    if (typeof process.env.SLACK_SIGNING_SECRET === 'undefined') {
      throw new Error('environment variable SLACK_SIGNING_SECRET undefined');
    }
    const slackSigningSecret = process.env.SLACK_SIGNING_SECRET;

    if (typeof process.env.SLACK_CHANNEL_NAME === 'undefined') {
      throw new Error('environment variable SLACK_CHANNEL_NAME undefined');
    }
    const slackChannel = process.env.SLACK_CHANNEL_NAME;

    const approvalAction = new SlackApprovalAction({
      actionName: 'SlackApproval',
      slackBotToken,
      slackSigningSecret,
      slackChannel,
      externalEntityLink: 'http://cloudcomponents.org',
      additionalInformation: 'Would you like to promote the build to production?',
    });

    const pipeline = new Pipeline(this, 'MyPipeline', {
      pipelineName: 'MyPipeline',
      stages: [
        {
          stageName: 'Source',
          actions: [sourceAction],
        },
        {
          stageName: 'Approval',
          actions: [approvalAction],
        },
      ],
    });

    new SlackNotifier(this, 'SlackNotifier', {
      pipeline,
      slackBotToken,
      slackSigningSecret,
      slackChannel,
    });
  }
}
```

## Slack App Settings

Create an app that’s just for your workspace

### OAuth & Permissions

Grant the `channels::history`-Scope to the Bot in your app and Add the Bot to the configured Slack-Channel

Select Permission Scopes:

![OAuth Scopes](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/packages/cdk-codepipeline-slack/assets/oauth_scope.png)

### Interactive Components

Enter the url of your api from the AWS Api Gateway and append `/slack/actions`:

![Interactive Components](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/packages/cdk-codepipeline-slack/assets/interactive_components.png)

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-slack/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-codepipeline-slack/LICENSE)
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
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.enum(jsii_type="@cloudcomponents/cdk-codepipeline-slack.ChannelTypes")
class ChannelTypes(enum.Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class SlackApprovalAction(
    _aws_cdk_aws_codepipeline_actions_ceddda9d.Action,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-slack.SlackApprovalAction",
):
    def __init__(
        self,
        *,
        slack_bot_token: builtins.str,
        slack_signing_secret: builtins.str,
        additional_information: typing.Optional[builtins.str] = None,
        external_entity_link: typing.Optional[builtins.str] = None,
        slack_bot_icon: typing.Optional[builtins.str] = None,
        slack_bot_name: typing.Optional[builtins.str] = None,
        slack_channel: typing.Optional[builtins.str] = None,
        slack_channel_id: typing.Optional[builtins.str] = None,
        slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param slack_bot_token: -
        :param slack_signing_secret: -
        :param additional_information: -
        :param external_entity_link: -
        :param slack_bot_icon: -
        :param slack_bot_name: -
        :param slack_channel: -
        :param slack_channel_id: -
        :param slack_channel_types: -
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        '''
        props = SlackApprovalActionProps(
            slack_bot_token=slack_bot_token,
            slack_signing_secret=slack_signing_secret,
            additional_information=additional_information,
            external_entity_link=external_entity_link,
            slack_bot_icon=slack_bot_icon,
            slack_bot_name=slack_bot_name,
            slack_channel=slack_channel,
            slack_channel_id=slack_channel_id,
            slack_channel_types=slack_channel_types,
            action_name=action_name,
            run_order=run_order,
            variables_namespace=variables_namespace,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(
        self,
        scope: _constructs_77d1e7e8.Construct,
        stage: _aws_cdk_aws_codepipeline_ceddda9d.IStage,
        *,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        role: _aws_cdk_aws_iam_ceddda9d.IRole,
    ) -> _aws_cdk_aws_codepipeline_ceddda9d.ActionConfig:
        '''This is a renamed version of the ``IAction.bind`` method.

        :param scope: -
        :param stage: -
        :param bucket: 
        :param role: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83217fcc7e78270fd355da7ae14ee490fedb9d199241ae3bb3dfce655980b343)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        options = _aws_cdk_aws_codepipeline_ceddda9d.ActionBindOptions(
            bucket=bucket, role=role
        )

        return typing.cast(_aws_cdk_aws_codepipeline_ceddda9d.ActionConfig, jsii.invoke(self, "bound", [scope, stage, options]))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-slack.SlackApprovalActionProps",
    jsii_struct_bases=[_aws_cdk_aws_codepipeline_ceddda9d.CommonActionProps],
    name_mapping={
        "action_name": "actionName",
        "run_order": "runOrder",
        "variables_namespace": "variablesNamespace",
        "slack_bot_token": "slackBotToken",
        "slack_signing_secret": "slackSigningSecret",
        "additional_information": "additionalInformation",
        "external_entity_link": "externalEntityLink",
        "slack_bot_icon": "slackBotIcon",
        "slack_bot_name": "slackBotName",
        "slack_channel": "slackChannel",
        "slack_channel_id": "slackChannelId",
        "slack_channel_types": "slackChannelTypes",
    },
)
class SlackApprovalActionProps(_aws_cdk_aws_codepipeline_ceddda9d.CommonActionProps):
    def __init__(
        self,
        *,
        action_name: builtins.str,
        run_order: typing.Optional[jsii.Number] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
        slack_bot_token: builtins.str,
        slack_signing_secret: builtins.str,
        additional_information: typing.Optional[builtins.str] = None,
        external_entity_link: typing.Optional[builtins.str] = None,
        slack_bot_icon: typing.Optional[builtins.str] = None,
        slack_bot_name: typing.Optional[builtins.str] = None,
        slack_channel: typing.Optional[builtins.str] = None,
        slack_channel_id: typing.Optional[builtins.str] = None,
        slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
    ) -> None:
        '''
        :param action_name: The physical, human-readable name of the Action. Note that Action names must be unique within a single Stage.
        :param run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1
        :param variables_namespace: The name of the namespace to use for variables emitted by this action. Default: - a name will be generated, based on the stage and action names, if any of the action's variables were referenced - otherwise, no namespace will be set
        :param slack_bot_token: -
        :param slack_signing_secret: -
        :param additional_information: -
        :param external_entity_link: -
        :param slack_bot_icon: -
        :param slack_bot_name: -
        :param slack_channel: -
        :param slack_channel_id: -
        :param slack_channel_types: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1000848885c3ccc2923385c05580a7c1da59ef4f2d17e57f8e915e1941439f9)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
            check_type(argname="argument slack_bot_token", value=slack_bot_token, expected_type=type_hints["slack_bot_token"])
            check_type(argname="argument slack_signing_secret", value=slack_signing_secret, expected_type=type_hints["slack_signing_secret"])
            check_type(argname="argument additional_information", value=additional_information, expected_type=type_hints["additional_information"])
            check_type(argname="argument external_entity_link", value=external_entity_link, expected_type=type_hints["external_entity_link"])
            check_type(argname="argument slack_bot_icon", value=slack_bot_icon, expected_type=type_hints["slack_bot_icon"])
            check_type(argname="argument slack_bot_name", value=slack_bot_name, expected_type=type_hints["slack_bot_name"])
            check_type(argname="argument slack_channel", value=slack_channel, expected_type=type_hints["slack_channel"])
            check_type(argname="argument slack_channel_id", value=slack_channel_id, expected_type=type_hints["slack_channel_id"])
            check_type(argname="argument slack_channel_types", value=slack_channel_types, expected_type=type_hints["slack_channel_types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "slack_bot_token": slack_bot_token,
            "slack_signing_secret": slack_signing_secret,
        }
        if run_order is not None:
            self._values["run_order"] = run_order
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace
        if additional_information is not None:
            self._values["additional_information"] = additional_information
        if external_entity_link is not None:
            self._values["external_entity_link"] = external_entity_link
        if slack_bot_icon is not None:
            self._values["slack_bot_icon"] = slack_bot_icon
        if slack_bot_name is not None:
            self._values["slack_bot_name"] = slack_bot_name
        if slack_channel is not None:
            self._values["slack_channel"] = slack_channel
        if slack_channel_id is not None:
            self._values["slack_channel_id"] = slack_channel_id
        if slack_channel_types is not None:
            self._values["slack_channel_types"] = slack_channel_types

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
    def slack_bot_token(self) -> builtins.str:
        result = self._values.get("slack_bot_token")
        assert result is not None, "Required property 'slack_bot_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_signing_secret(self) -> builtins.str:
        result = self._values.get("slack_signing_secret")
        assert result is not None, "Required property 'slack_signing_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_information(self) -> typing.Optional[builtins.str]:
        result = self._values.get("additional_information")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_entity_link(self) -> typing.Optional[builtins.str]:
        result = self._values.get("external_entity_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_bot_icon(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_bot_icon")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_bot_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_bot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_channel(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_channel_id(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_channel_types(self) -> typing.Optional[typing.List[ChannelTypes]]:
        result = self._values.get("slack_channel_types")
        return typing.cast(typing.Optional[typing.List[ChannelTypes]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SlackApprovalActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SlackNotifier(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-codepipeline-slack.SlackNotifier",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        pipeline: _aws_cdk_aws_codepipeline_ceddda9d.IPipeline,
        slack_bot_token: builtins.str,
        slack_signing_secret: builtins.str,
        slack_bot_icon: typing.Optional[builtins.str] = None,
        slack_bot_name: typing.Optional[builtins.str] = None,
        slack_channel: typing.Optional[builtins.str] = None,
        slack_channel_id: typing.Optional[builtins.str] = None,
        slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
        stage_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param pipeline: -
        :param slack_bot_token: -
        :param slack_signing_secret: -
        :param slack_bot_icon: -
        :param slack_bot_name: -
        :param slack_channel: -
        :param slack_channel_id: -
        :param slack_channel_types: -
        :param stage_names: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524bb5d9a1058a9f5bb3ffe0846ab04aafe77a67834c8f32a555fc441d267455)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SlackNotifierProps(
            pipeline=pipeline,
            slack_bot_token=slack_bot_token,
            slack_signing_secret=slack_signing_secret,
            slack_bot_icon=slack_bot_icon,
            slack_bot_name=slack_bot_name,
            slack_channel=slack_channel,
            slack_channel_id=slack_channel_id,
            slack_channel_types=slack_channel_types,
            stage_names=stage_names,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def _environment(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environment"))

    @_environment.setter
    def _environment(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a13ce342615495d23c51f1a1c053c972c191001ab48714c365afee46b285e2b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-codepipeline-slack.SlackNotifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline": "pipeline",
        "slack_bot_token": "slackBotToken",
        "slack_signing_secret": "slackSigningSecret",
        "slack_bot_icon": "slackBotIcon",
        "slack_bot_name": "slackBotName",
        "slack_channel": "slackChannel",
        "slack_channel_id": "slackChannelId",
        "slack_channel_types": "slackChannelTypes",
        "stage_names": "stageNames",
    },
)
class SlackNotifierProps:
    def __init__(
        self,
        *,
        pipeline: _aws_cdk_aws_codepipeline_ceddda9d.IPipeline,
        slack_bot_token: builtins.str,
        slack_signing_secret: builtins.str,
        slack_bot_icon: typing.Optional[builtins.str] = None,
        slack_bot_name: typing.Optional[builtins.str] = None,
        slack_channel: typing.Optional[builtins.str] = None,
        slack_channel_id: typing.Optional[builtins.str] = None,
        slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
        stage_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param pipeline: -
        :param slack_bot_token: -
        :param slack_signing_secret: -
        :param slack_bot_icon: -
        :param slack_bot_name: -
        :param slack_channel: -
        :param slack_channel_id: -
        :param slack_channel_types: -
        :param stage_names: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ddfd28166f6c2a2c20de60a34069d986f3539b74e448e0f177433fac5835f7)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
            check_type(argname="argument slack_bot_token", value=slack_bot_token, expected_type=type_hints["slack_bot_token"])
            check_type(argname="argument slack_signing_secret", value=slack_signing_secret, expected_type=type_hints["slack_signing_secret"])
            check_type(argname="argument slack_bot_icon", value=slack_bot_icon, expected_type=type_hints["slack_bot_icon"])
            check_type(argname="argument slack_bot_name", value=slack_bot_name, expected_type=type_hints["slack_bot_name"])
            check_type(argname="argument slack_channel", value=slack_channel, expected_type=type_hints["slack_channel"])
            check_type(argname="argument slack_channel_id", value=slack_channel_id, expected_type=type_hints["slack_channel_id"])
            check_type(argname="argument slack_channel_types", value=slack_channel_types, expected_type=type_hints["slack_channel_types"])
            check_type(argname="argument stage_names", value=stage_names, expected_type=type_hints["stage_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline": pipeline,
            "slack_bot_token": slack_bot_token,
            "slack_signing_secret": slack_signing_secret,
        }
        if slack_bot_icon is not None:
            self._values["slack_bot_icon"] = slack_bot_icon
        if slack_bot_name is not None:
            self._values["slack_bot_name"] = slack_bot_name
        if slack_channel is not None:
            self._values["slack_channel"] = slack_channel
        if slack_channel_id is not None:
            self._values["slack_channel_id"] = slack_channel_id
        if slack_channel_types is not None:
            self._values["slack_channel_types"] = slack_channel_types
        if stage_names is not None:
            self._values["stage_names"] = stage_names

    @builtins.property
    def pipeline(self) -> _aws_cdk_aws_codepipeline_ceddda9d.IPipeline:
        result = self._values.get("pipeline")
        assert result is not None, "Required property 'pipeline' is missing"
        return typing.cast(_aws_cdk_aws_codepipeline_ceddda9d.IPipeline, result)

    @builtins.property
    def slack_bot_token(self) -> builtins.str:
        result = self._values.get("slack_bot_token")
        assert result is not None, "Required property 'slack_bot_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_signing_secret(self) -> builtins.str:
        result = self._values.get("slack_signing_secret")
        assert result is not None, "Required property 'slack_signing_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_bot_icon(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_bot_icon")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_bot_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_bot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_channel(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_channel_id(self) -> typing.Optional[builtins.str]:
        result = self._values.get("slack_channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack_channel_types(self) -> typing.Optional[typing.List[ChannelTypes]]:
        result = self._values.get("slack_channel_types")
        return typing.cast(typing.Optional[typing.List[ChannelTypes]], result)

    @builtins.property
    def stage_names(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("stage_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SlackNotifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelTypes",
    "SlackApprovalAction",
    "SlackApprovalActionProps",
    "SlackNotifier",
    "SlackNotifierProps",
]

publication.publish()

def _typecheckingstub__83217fcc7e78270fd355da7ae14ee490fedb9d199241ae3bb3dfce655980b343(
    scope: _constructs_77d1e7e8.Construct,
    stage: _aws_cdk_aws_codepipeline_ceddda9d.IStage,
    *,
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    role: _aws_cdk_aws_iam_ceddda9d.IRole,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1000848885c3ccc2923385c05580a7c1da59ef4f2d17e57f8e915e1941439f9(
    *,
    action_name: builtins.str,
    run_order: typing.Optional[jsii.Number] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
    slack_bot_token: builtins.str,
    slack_signing_secret: builtins.str,
    additional_information: typing.Optional[builtins.str] = None,
    external_entity_link: typing.Optional[builtins.str] = None,
    slack_bot_icon: typing.Optional[builtins.str] = None,
    slack_bot_name: typing.Optional[builtins.str] = None,
    slack_channel: typing.Optional[builtins.str] = None,
    slack_channel_id: typing.Optional[builtins.str] = None,
    slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524bb5d9a1058a9f5bb3ffe0846ab04aafe77a67834c8f32a555fc441d267455(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    pipeline: _aws_cdk_aws_codepipeline_ceddda9d.IPipeline,
    slack_bot_token: builtins.str,
    slack_signing_secret: builtins.str,
    slack_bot_icon: typing.Optional[builtins.str] = None,
    slack_bot_name: typing.Optional[builtins.str] = None,
    slack_channel: typing.Optional[builtins.str] = None,
    slack_channel_id: typing.Optional[builtins.str] = None,
    slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
    stage_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a13ce342615495d23c51f1a1c053c972c191001ab48714c365afee46b285e2b4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ddfd28166f6c2a2c20de60a34069d986f3539b74e448e0f177433fac5835f7(
    *,
    pipeline: _aws_cdk_aws_codepipeline_ceddda9d.IPipeline,
    slack_bot_token: builtins.str,
    slack_signing_secret: builtins.str,
    slack_bot_icon: typing.Optional[builtins.str] = None,
    slack_bot_name: typing.Optional[builtins.str] = None,
    slack_channel: typing.Optional[builtins.str] = None,
    slack_channel_id: typing.Optional[builtins.str] = None,
    slack_channel_types: typing.Optional[typing.Sequence[ChannelTypes]] = None,
    stage_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
