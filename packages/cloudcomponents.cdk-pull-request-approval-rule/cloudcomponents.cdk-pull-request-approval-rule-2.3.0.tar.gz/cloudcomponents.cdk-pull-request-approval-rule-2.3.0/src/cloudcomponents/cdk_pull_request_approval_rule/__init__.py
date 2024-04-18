'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-pull-request-approval-rule

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-pull-request-approval-rule)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-pull-request-approval-rule/)

> CodeCommit pull request approval rules to enforcing your pull request workflow

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-pull-request-approval-rule
```

Python:

```bash
pip install cloudcomponents.cdk-pull-request-approval-rule
```

## How to use

```python
import { ApprovalRuleTemplate, ApprovalRuleTemplateRepositoryAssociation } from '@cloudcomponents/cdk-pull-request-approval-rule';
import { PullRequestCheck } from '@cloudcomponents/cdk-pull-request-check';
import { Stack, StackProps } from 'aws-cdk-lib';
import { BuildSpec } from 'aws-cdk-lib/aws-codebuild';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { Construct } from 'constructs';

export class PullRequestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const repository = new Repository(this, 'Repository', {
      repositoryName: 'pr-check-repository',
    });

    const { approvalRuleTemplateName } = new ApprovalRuleTemplate(this, 'ApprovalRuleTemplate', {
      approvalRuleTemplateName: 'template-name',
      template: {
        approvers: {
          numberOfApprovalsNeeded: 1,
        },
      },
    });

    new ApprovalRuleTemplateRepositoryAssociation(this, 'ApprovalRuleTemplateRepositoryAssociation', {
      approvalRuleTemplateName,
      repository,
    });

    new PullRequestCheck(this, 'PullRequestCheck', {
      repository,
      buildSpec: BuildSpec.fromSourceFilename('prcheck.yml'),
    });
  }
}
```

## ApprovalRuleOverridden notification

```python
import { ApprovalRuleTemplate, ApprovalRuleTemplateRepositoryAssociation } from '@cloudcomponents/cdk-pull-request-approval-rule';
import { PullRequestCheck } from '@cloudcomponents/cdk-pull-request-check';
import { Stack, StackProps } from 'aws-cdk-lib';
import { BuildSpec } from 'aws-cdk-lib/aws-codebuild';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { SnsTopic } from 'aws-cdk-lib/aws-events-targets';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { Construct } from 'constructs';

export class PullRequestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const repository = new Repository(this, 'Repository', {
      repositoryName: 'pr-check-repository',
    });

    const { approvalRuleTemplateName } = new ApprovalRuleTemplate(
      this,
      'ApprovalRuleTemplate',
      {
        approvalRuleTemplateName: 'template-name',
        template: {
          approvers: {
            numberOfApprovalsNeeded: 1,
          },
        },
      },
    );

    const ruleAsscociation = new ApprovalRuleTemplateRepositoryAssociation(
      stack,
      'ApprovalRuleTemplateRepositoryAssociation',
      {
          approvalRuleTemplateName,
          repository,
      },
    );

    const topic = new Topic(stack, 'Topic');

    ruleAsscociation.onOverridden('overridden', {
        target: new SnsTopic(topic),
    });

    // Approves the pull request
    new PullRequestCheck(this, 'PullRequestCheck', {
        repository,
        buildSpec: BuildSpec.fromSourceFilename('prcheck.yml'),
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-pull-request-approval-rule/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-pull-request-approval-rule/LICENSE)
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
import aws_cdk.aws_events as _aws_cdk_aws_events_ceddda9d
import constructs as _constructs_77d1e7e8


class ApprovalRuleTemplate(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-pull-request-approval-rule.ApprovalRuleTemplate",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        approval_rule_template_name: builtins.str,
        template: typing.Union["Template", typing.Dict[builtins.str, typing.Any]],
        approval_rule_template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param approval_rule_template_name: The name of the approval rule template.
        :param template: The content of the approval rule that is created on pull requests in associated repositories.
        :param approval_rule_template_description: The description of the approval rule template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd2095102f94db9942699964390df48f6b61d3ffaccde0c96c6cc2af9a9e1097)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ApprovalRuleTemplateProps(
            approval_rule_template_name=approval_rule_template_name,
            template=template,
            approval_rule_template_description=approval_rule_template_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="approvalRuleTemplateName")
    def approval_rule_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approvalRuleTemplateName"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-pull-request-approval-rule.ApprovalRuleTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "approval_rule_template_name": "approvalRuleTemplateName",
        "template": "template",
        "approval_rule_template_description": "approvalRuleTemplateDescription",
    },
)
class ApprovalRuleTemplateProps:
    def __init__(
        self,
        *,
        approval_rule_template_name: builtins.str,
        template: typing.Union["Template", typing.Dict[builtins.str, typing.Any]],
        approval_rule_template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param approval_rule_template_name: The name of the approval rule template.
        :param template: The content of the approval rule that is created on pull requests in associated repositories.
        :param approval_rule_template_description: The description of the approval rule template.
        '''
        if isinstance(template, dict):
            template = Template(**template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f77ec0b57a50215ec0c04e82a2847214bb82ddb9ad42563c944bc9d11b62de4)
            check_type(argname="argument approval_rule_template_name", value=approval_rule_template_name, expected_type=type_hints["approval_rule_template_name"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument approval_rule_template_description", value=approval_rule_template_description, expected_type=type_hints["approval_rule_template_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "approval_rule_template_name": approval_rule_template_name,
            "template": template,
        }
        if approval_rule_template_description is not None:
            self._values["approval_rule_template_description"] = approval_rule_template_description

    @builtins.property
    def approval_rule_template_name(self) -> builtins.str:
        '''The name of the approval rule template.'''
        result = self._values.get("approval_rule_template_name")
        assert result is not None, "Required property 'approval_rule_template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template(self) -> "Template":
        '''The content of the approval rule that is created on pull requests in associated repositories.'''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast("Template", result)

    @builtins.property
    def approval_rule_template_description(self) -> typing.Optional[builtins.str]:
        '''The description of the approval rule template.'''
        result = self._values.get("approval_rule_template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprovalRuleTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApprovalRuleTemplateRepositoryAssociation(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-pull-request-approval-rule.ApprovalRuleTemplateRepositoryAssociation",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        approval_rule_template_name: builtins.str,
        repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param approval_rule_template_name: The name of the template you want to associate with one or more repositories.
        :param repository: The repository you want to associate with the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__263a807043d1d1848f4e138aa8ac5ccc9f2786caaeb3e55e7f1f6ae0609551b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ApprovalRuleTemplateRepositoryAssociationProps(
            approval_rule_template_name=approval_rule_template_name,
            repository=repository,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="onOverridden")
    def on_overridden(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_aws_cdk_aws_events_ceddda9d.IRuleTarget] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_ceddda9d.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _aws_cdk_aws_events_ceddda9d.Rule:
        '''
        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5445fab644f49c045d17c45efdb85cd15a9638acb9d540d2401d3e6d179c92a3)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_ceddda9d.OnEventOptions(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_aws_cdk_aws_events_ceddda9d.Rule, jsii.invoke(self, "onOverridden", [id, options]))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-pull-request-approval-rule.ApprovalRuleTemplateRepositoryAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "approval_rule_template_name": "approvalRuleTemplateName",
        "repository": "repository",
    },
)
class ApprovalRuleTemplateRepositoryAssociationProps:
    def __init__(
        self,
        *,
        approval_rule_template_name: builtins.str,
        repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
    ) -> None:
        '''
        :param approval_rule_template_name: The name of the template you want to associate with one or more repositories.
        :param repository: The repository you want to associate with the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d8c801535dde9ce3da6ed44e4aeb7f0122e15b4ff74c4261be3956a001a165e)
            check_type(argname="argument approval_rule_template_name", value=approval_rule_template_name, expected_type=type_hints["approval_rule_template_name"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "approval_rule_template_name": approval_rule_template_name,
            "repository": repository,
        }

    @builtins.property
    def approval_rule_template_name(self) -> builtins.str:
        '''The name of the template you want to associate with one or more repositories.'''
        result = self._values.get("approval_rule_template_name")
        assert result is not None, "Required property 'approval_rule_template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> _aws_cdk_aws_codecommit_ceddda9d.IRepository:
        '''The repository you want to associate with the template.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(_aws_cdk_aws_codecommit_ceddda9d.IRepository, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprovalRuleTemplateRepositoryAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-pull-request-approval-rule.Approvers",
    jsii_struct_bases=[],
    name_mapping={
        "number_of_approvals_needed": "numberOfApprovalsNeeded",
        "approval_pool_members": "approvalPoolMembers",
    },
)
class Approvers:
    def __init__(
        self,
        *,
        number_of_approvals_needed: jsii.Number,
        approval_pool_members: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param number_of_approvals_needed: -
        :param approval_pool_members: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef3f0228b0497b3f5f1ecabf9c7e6929ae90a0fe84caef9a0fb39c51d678cb3c)
            check_type(argname="argument number_of_approvals_needed", value=number_of_approvals_needed, expected_type=type_hints["number_of_approvals_needed"])
            check_type(argname="argument approval_pool_members", value=approval_pool_members, expected_type=type_hints["approval_pool_members"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "number_of_approvals_needed": number_of_approvals_needed,
        }
        if approval_pool_members is not None:
            self._values["approval_pool_members"] = approval_pool_members

    @builtins.property
    def number_of_approvals_needed(self) -> jsii.Number:
        result = self._values.get("number_of_approvals_needed")
        assert result is not None, "Required property 'number_of_approvals_needed' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def approval_pool_members(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("approval_pool_members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Approvers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-pull-request-approval-rule.Template",
    jsii_struct_bases=[],
    name_mapping={"approvers": "approvers", "branches": "branches"},
)
class Template:
    def __init__(
        self,
        *,
        approvers: typing.Union[Approvers, typing.Dict[builtins.str, typing.Any]],
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param approvers: -
        :param branches: -
        '''
        if isinstance(approvers, dict):
            approvers = Approvers(**approvers)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f6ebb0bed24a6de95ff615762037995556f166ea7d933e55f0d100fff10311f)
            check_type(argname="argument approvers", value=approvers, expected_type=type_hints["approvers"])
            check_type(argname="argument branches", value=branches, expected_type=type_hints["branches"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "approvers": approvers,
        }
        if branches is not None:
            self._values["branches"] = branches

    @builtins.property
    def approvers(self) -> Approvers:
        result = self._values.get("approvers")
        assert result is not None, "Required property 'approvers' is missing"
        return typing.cast(Approvers, result)

    @builtins.property
    def branches(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("branches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Template(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApprovalRuleTemplate",
    "ApprovalRuleTemplateProps",
    "ApprovalRuleTemplateRepositoryAssociation",
    "ApprovalRuleTemplateRepositoryAssociationProps",
    "Approvers",
    "Template",
]

publication.publish()

def _typecheckingstub__cd2095102f94db9942699964390df48f6b61d3ffaccde0c96c6cc2af9a9e1097(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    approval_rule_template_name: builtins.str,
    template: typing.Union[Template, typing.Dict[builtins.str, typing.Any]],
    approval_rule_template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f77ec0b57a50215ec0c04e82a2847214bb82ddb9ad42563c944bc9d11b62de4(
    *,
    approval_rule_template_name: builtins.str,
    template: typing.Union[Template, typing.Dict[builtins.str, typing.Any]],
    approval_rule_template_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263a807043d1d1848f4e138aa8ac5ccc9f2786caaeb3e55e7f1f6ae0609551b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    approval_rule_template_name: builtins.str,
    repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5445fab644f49c045d17c45efdb85cd15a9638acb9d540d2401d3e6d179c92a3(
    id: builtins.str,
    *,
    target: typing.Optional[_aws_cdk_aws_events_ceddda9d.IRuleTarget] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_ceddda9d.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d8c801535dde9ce3da6ed44e4aeb7f0122e15b4ff74c4261be3956a001a165e(
    *,
    approval_rule_template_name: builtins.str,
    repository: _aws_cdk_aws_codecommit_ceddda9d.IRepository,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef3f0228b0497b3f5f1ecabf9c7e6929ae90a0fe84caef9a0fb39c51d678cb3c(
    *,
    number_of_approvals_needed: jsii.Number,
    approval_pool_members: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f6ebb0bed24a6de95ff615762037995556f166ea7d933e55f0d100fff10311f(
    *,
    approvers: typing.Union[Approvers, typing.Dict[builtins.str, typing.Any]],
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
