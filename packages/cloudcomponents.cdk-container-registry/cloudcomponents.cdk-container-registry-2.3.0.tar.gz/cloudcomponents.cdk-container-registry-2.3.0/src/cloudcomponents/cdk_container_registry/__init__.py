'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-container-registry

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-container-registry)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-container-registry/)

> Registry for container images

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-container-registry
```

Python:

```bash
pip install cloudcomponents.cdk-container-registry
```

## How to use

```python
import { ImageRepository, Severity } from '@cloudcomponents/cdk-container-registry';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { EmailSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';
import { Construct } from 'constructs';

export class ImageRepositoryStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const alarmTopic = new Topic(this, 'Topic');

    alarmTopic.addSubscription(
      new EmailSubscription(process.env.DEVSECOPS_TEAM_EMAIL as string),
    );

    const imageRepository = new ImageRepository(this, 'ImageRepository', {
      forceDelete: true, //Only for tests
      imageScanOnPush: true,
    });

    imageRepository.onFinding('finding', {
      severity: Severity.HIGH,
      alarmTopic,
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-container-registry/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-container-registry/LICENSE)
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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_ecr as _aws_cdk_aws_ecr_ceddda9d
import aws_cdk.aws_events as _aws_cdk_aws_events_ceddda9d
import aws_cdk.aws_kms as _aws_cdk_aws_kms_ceddda9d
import aws_cdk.aws_sns as _aws_cdk_aws_sns_ceddda9d
import constructs as _constructs_77d1e7e8


class ImageRepository(
    _aws_cdk_aws_ecr_ceddda9d.Repository,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-container-registry.ImageRepository",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        force_delete: typing.Optional[builtins.bool] = None,
        auto_delete_images: typing.Optional[builtins.bool] = None,
        empty_on_delete: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.RepositoryEncryption] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        image_scan_on_push: typing.Optional[builtins.bool] = None,
        image_tag_mutability: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.TagMutability] = None,
        lifecycle_registry_id: typing.Optional[builtins.str] = None,
        lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecr_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param force_delete: If a repository contains images, forces the deletion during stack deletion. Default: false
        :param auto_delete_images: (deprecated) Whether all images should be automatically deleted when the repository is removed from the stack or when the stack is deleted. Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``. Default: false
        :param empty_on_delete: If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it. Default: false
        :param encryption: The kind of server-side encryption to apply to this repository. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryptionKey is not specified, an AWS managed KMS key is used. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        :param encryption_key: External KMS key to use for repository encryption. The 'encryption' property must be either not specified or set to "KMS". An error will be emitted if encryption is set to "AES256". Default: - If encryption is set to ``KMS`` and this property is undefined, an AWS managed KMS key is used.
        :param image_scan_on_push: Enable the scan on push when creating the repository. Default: false
        :param image_tag_mutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten. Default: TagMutability.MUTABLE
        :param lifecycle_registry_id: The AWS account ID associated with the registry that contains the repository. Default: The default registry is assumed.
        :param lifecycle_rules: Life cycle rules to apply to this registry. Default: No life cycle rules
        :param removal_policy: Determine what happens to the repository when the resource/stack is deleted. Default: RemovalPolicy.Retain
        :param repository_name: Name for this repository. The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. Default: Automatically generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bff602dff410ce3816795da6ec3151ce273448863647957c3108ea192df0d56)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ImageRepositoryProps(
            force_delete=force_delete,
            auto_delete_images=auto_delete_images,
            empty_on_delete=empty_on_delete,
            encryption=encryption,
            encryption_key=encryption_key,
            image_scan_on_push=image_scan_on_push,
            image_tag_mutability=image_tag_mutability,
            lifecycle_registry_id=lifecycle_registry_id,
            lifecycle_rules=lifecycle_rules,
            removal_policy=removal_policy,
            repository_name=repository_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="onFinding")
    def on_finding(
        self,
        id: builtins.str,
        *,
        alarm_topic: _aws_cdk_aws_sns_ceddda9d.ITopic,
        severity: "Severity",
        image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> _aws_cdk_aws_events_ceddda9d.Rule:
        '''
        :param id: -
        :param alarm_topic: -
        :param severity: -
        :param image_tags: Only watch changes to the image tags specified. Leave it undefined to watch the full repository. Default: - Watch the changes to the repository with all image tags
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbf063d951c5690fbe8a347778bca0840ad83acaa9b37b263ceb681fa84c4bd9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnFindingOptions(
            alarm_topic=alarm_topic, severity=severity, image_tags=image_tags
        )

        return typing.cast(_aws_cdk_aws_events_ceddda9d.Rule, jsii.invoke(self, "onFinding", [id, options]))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-container-registry.ImageRepositoryProps",
    jsii_struct_bases=[_aws_cdk_aws_ecr_ceddda9d.RepositoryProps],
    name_mapping={
        "auto_delete_images": "autoDeleteImages",
        "empty_on_delete": "emptyOnDelete",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "image_scan_on_push": "imageScanOnPush",
        "image_tag_mutability": "imageTagMutability",
        "lifecycle_registry_id": "lifecycleRegistryId",
        "lifecycle_rules": "lifecycleRules",
        "removal_policy": "removalPolicy",
        "repository_name": "repositoryName",
        "force_delete": "forceDelete",
    },
)
class ImageRepositoryProps(_aws_cdk_aws_ecr_ceddda9d.RepositoryProps):
    def __init__(
        self,
        *,
        auto_delete_images: typing.Optional[builtins.bool] = None,
        empty_on_delete: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.RepositoryEncryption] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        image_scan_on_push: typing.Optional[builtins.bool] = None,
        image_tag_mutability: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.TagMutability] = None,
        lifecycle_registry_id: typing.Optional[builtins.str] = None,
        lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecr_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        repository_name: typing.Optional[builtins.str] = None,
        force_delete: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param auto_delete_images: (deprecated) Whether all images should be automatically deleted when the repository is removed from the stack or when the stack is deleted. Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``. Default: false
        :param empty_on_delete: If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it. Default: false
        :param encryption: The kind of server-side encryption to apply to this repository. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryptionKey is not specified, an AWS managed KMS key is used. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        :param encryption_key: External KMS key to use for repository encryption. The 'encryption' property must be either not specified or set to "KMS". An error will be emitted if encryption is set to "AES256". Default: - If encryption is set to ``KMS`` and this property is undefined, an AWS managed KMS key is used.
        :param image_scan_on_push: Enable the scan on push when creating the repository. Default: false
        :param image_tag_mutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten. Default: TagMutability.MUTABLE
        :param lifecycle_registry_id: The AWS account ID associated with the registry that contains the repository. Default: The default registry is assumed.
        :param lifecycle_rules: Life cycle rules to apply to this registry. Default: No life cycle rules
        :param removal_policy: Determine what happens to the repository when the resource/stack is deleted. Default: RemovalPolicy.Retain
        :param repository_name: Name for this repository. The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. Default: Automatically generated name.
        :param force_delete: If a repository contains images, forces the deletion during stack deletion. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9595661c2e9d422c6b1873d6fd49f23250005d739912fe2be57cfe163a69aabf)
            check_type(argname="argument auto_delete_images", value=auto_delete_images, expected_type=type_hints["auto_delete_images"])
            check_type(argname="argument empty_on_delete", value=empty_on_delete, expected_type=type_hints["empty_on_delete"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument image_scan_on_push", value=image_scan_on_push, expected_type=type_hints["image_scan_on_push"])
            check_type(argname="argument image_tag_mutability", value=image_tag_mutability, expected_type=type_hints["image_tag_mutability"])
            check_type(argname="argument lifecycle_registry_id", value=lifecycle_registry_id, expected_type=type_hints["lifecycle_registry_id"])
            check_type(argname="argument lifecycle_rules", value=lifecycle_rules, expected_type=type_hints["lifecycle_rules"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_delete_images is not None:
            self._values["auto_delete_images"] = auto_delete_images
        if empty_on_delete is not None:
            self._values["empty_on_delete"] = empty_on_delete
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if image_scan_on_push is not None:
            self._values["image_scan_on_push"] = image_scan_on_push
        if image_tag_mutability is not None:
            self._values["image_tag_mutability"] = image_tag_mutability
        if lifecycle_registry_id is not None:
            self._values["lifecycle_registry_id"] = lifecycle_registry_id
        if lifecycle_rules is not None:
            self._values["lifecycle_rules"] = lifecycle_rules
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if repository_name is not None:
            self._values["repository_name"] = repository_name
        if force_delete is not None:
            self._values["force_delete"] = force_delete

    @builtins.property
    def auto_delete_images(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether all images should be automatically deleted when the repository is removed from the stack or when the stack is deleted.

        Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``.

        :default: false

        :deprecated: Use ``emptyOnDelete`` instead.

        :stability: deprecated
        '''
        result = self._values.get("auto_delete_images")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def empty_on_delete(self) -> typing.Optional[builtins.bool]:
        '''If true, deleting the repository force deletes the contents of the repository.

        If false, the repository must be empty before attempting to delete it.

        :default: false
        '''
        result = self._values.get("empty_on_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecr_ceddda9d.RepositoryEncryption]:
        '''The kind of server-side encryption to apply to this repository.

        If you choose KMS, you can specify a KMS key via ``encryptionKey``. If
        encryptionKey is not specified, an AWS managed KMS key is used.

        :default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecr_ceddda9d.RepositoryEncryption], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey]:
        '''External KMS key to use for repository encryption.

        The 'encryption' property must be either not specified or set to "KMS".
        An error will be emitted if encryption is set to "AES256".

        :default:

        - If encryption is set to ``KMS`` and this property is undefined,
        an AWS managed KMS key is used.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey], result)

    @builtins.property
    def image_scan_on_push(self) -> typing.Optional[builtins.bool]:
        '''Enable the scan on push when creating the repository.

        :default: false
        '''
        result = self._values.get("image_scan_on_push")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image_tag_mutability(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecr_ceddda9d.TagMutability]:
        '''The tag mutability setting for the repository.

        If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten.

        :default: TagMutability.MUTABLE
        '''
        result = self._values.get("image_tag_mutability")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecr_ceddda9d.TagMutability], result)

    @builtins.property
    def lifecycle_registry_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID associated with the registry that contains the repository.

        :default: The default registry is assumed.

        :see: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutLifecyclePolicy.html
        '''
        result = self._values.get("lifecycle_registry_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_rules(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ecr_ceddda9d.LifecycleRule]]:
        '''Life cycle rules to apply to this registry.

        :default: No life cycle rules
        '''
        result = self._values.get("lifecycle_rules")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ecr_ceddda9d.LifecycleRule]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''Determine what happens to the repository when the resource/stack is deleted.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''Name for this repository.

        The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :default: Automatically generated name.
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_delete(self) -> typing.Optional[builtins.bool]:
        '''If a repository contains images, forces the deletion during stack deletion.

        :default: false
        '''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-container-registry.OnFindingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_topic": "alarmTopic",
        "severity": "severity",
        "image_tags": "imageTags",
    },
)
class OnFindingOptions:
    def __init__(
        self,
        *,
        alarm_topic: _aws_cdk_aws_sns_ceddda9d.ITopic,
        severity: "Severity",
        image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param alarm_topic: -
        :param severity: -
        :param image_tags: Only watch changes to the image tags specified. Leave it undefined to watch the full repository. Default: - Watch the changes to the repository with all image tags
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1395d13036d306905008034f859540280af7aa9c4927b4da641e1396d2b6689)
            check_type(argname="argument alarm_topic", value=alarm_topic, expected_type=type_hints["alarm_topic"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument image_tags", value=image_tags, expected_type=type_hints["image_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_topic": alarm_topic,
            "severity": severity,
        }
        if image_tags is not None:
            self._values["image_tags"] = image_tags

    @builtins.property
    def alarm_topic(self) -> _aws_cdk_aws_sns_ceddda9d.ITopic:
        result = self._values.get("alarm_topic")
        assert result is not None, "Required property 'alarm_topic' is missing"
        return typing.cast(_aws_cdk_aws_sns_ceddda9d.ITopic, result)

    @builtins.property
    def severity(self) -> "Severity":
        result = self._values.get("severity")
        assert result is not None, "Required property 'severity' is missing"
        return typing.cast("Severity", result)

    @builtins.property
    def image_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only watch changes to the image tags specified.

        Leave it undefined to watch the full repository.

        :default: - Watch the changes to the repository with all image tags
        '''
        result = self._values.get("image_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OnFindingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cloudcomponents/cdk-container-registry.Severity")
class Severity(enum.Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNDEFINED = "UNDEFINED"


__all__ = [
    "ImageRepository",
    "ImageRepositoryProps",
    "OnFindingOptions",
    "Severity",
]

publication.publish()

def _typecheckingstub__0bff602dff410ce3816795da6ec3151ce273448863647957c3108ea192df0d56(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    force_delete: typing.Optional[builtins.bool] = None,
    auto_delete_images: typing.Optional[builtins.bool] = None,
    empty_on_delete: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.RepositoryEncryption] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    image_scan_on_push: typing.Optional[builtins.bool] = None,
    image_tag_mutability: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.TagMutability] = None,
    lifecycle_registry_id: typing.Optional[builtins.str] = None,
    lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecr_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbf063d951c5690fbe8a347778bca0840ad83acaa9b37b263ceb681fa84c4bd9(
    id: builtins.str,
    *,
    alarm_topic: _aws_cdk_aws_sns_ceddda9d.ITopic,
    severity: Severity,
    image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9595661c2e9d422c6b1873d6fd49f23250005d739912fe2be57cfe163a69aabf(
    *,
    auto_delete_images: typing.Optional[builtins.bool] = None,
    empty_on_delete: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.RepositoryEncryption] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    image_scan_on_push: typing.Optional[builtins.bool] = None,
    image_tag_mutability: typing.Optional[_aws_cdk_aws_ecr_ceddda9d.TagMutability] = None,
    lifecycle_registry_id: typing.Optional[builtins.str] = None,
    lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecr_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    repository_name: typing.Optional[builtins.str] = None,
    force_delete: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1395d13036d306905008034f859540280af7aa9c4927b4da641e1396d2b6689(
    *,
    alarm_topic: _aws_cdk_aws_sns_ceddda9d.ITopic,
    severity: Severity,
    image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
