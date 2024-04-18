'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-s3-antivirus

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-s3-antivirus)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-s3-antivirus/)

> Antivirus for Amazon S3

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-s3-antivirus
```

Python:

```bash
pip install cloudcomponents.cdk-s3-antivirus
```

## How to use

```python
import { Scanner } from '@cloudcomponents/cdk-s3-antivirus';
import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { SnsDestination } from 'aws-cdk-lib/aws-lambda-destinations';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { EmailSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';
import { Construct } from 'constructs';

export class S3AntivirusStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const bucket = new Bucket(this, 'Bucket', {
      autoDeleteObjects: true,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const topic = new Topic(this, 'Topic');
    if (process.env.DEVSECOPS_TEAM_EMAIL) {
      topic.addSubscription(new EmailSubscription(process.env.DEVSECOPS_TEAM_EMAIL));
    }

    const scanner = new Scanner(this, 'Scanner', {
      onResult: new SnsDestination(topic),
      onError: new SnsDestination(topic),
    });

    scanner.addSourceBucket(bucket);
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-s3-antivirus/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-s3-antivirus/LICENSE)
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
import aws_cdk.aws_efs as _aws_cdk_aws_efs_ceddda9d
import aws_cdk.aws_events as _aws_cdk_aws_events_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class ClamavLayer(
    _aws_cdk_aws_lambda_ceddda9d.LayerVersion,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-s3-antivirus.ClamavLayer",
):
    '''Clamav Lambda layer.'''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f0f20dd21b6bbfb25699e7fe0168d53dc6c8d9b5c4ef728d9c2a459868473b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])


class DefinitionBucket(
    _aws_cdk_aws_s3_ceddda9d.Bucket,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-s3-antivirus.DefinitionBucket",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        vpc_endpoint: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc_endpoint: -
        :param bucket_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93468d6a31dd51fd538fdb783e5cc286aef8538f0a66eef2b8fd90a547bcaa95)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DefinitionBucketProps(
            vpc_endpoint=vpc_endpoint, bucket_name=bucket_name
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-s3-antivirus.DefinitionBucketProps",
    jsii_struct_bases=[],
    name_mapping={"vpc_endpoint": "vpcEndpoint", "bucket_name": "bucketName"},
)
class DefinitionBucketProps:
    def __init__(
        self,
        *,
        vpc_endpoint: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param vpc_endpoint: -
        :param bucket_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c26272e7df2e42ad47485f39c0beeb6889b6865c0b918e3b8927ef9ca80879c)
            check_type(argname="argument vpc_endpoint", value=vpc_endpoint, expected_type=type_hints["vpc_endpoint"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_endpoint": vpc_endpoint,
        }
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name

    @builtins.property
    def vpc_endpoint(self) -> builtins.str:
        result = self._values.get("vpc_endpoint")
        assert result is not None, "Required property 'vpc_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefinitionBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefinitionInitializer(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-s3-antivirus.DefinitionInitializer",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        fn: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param fn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__201914154bf8b8d4dc22a3c1f8acb5d5e6ff7eee06050abdffbc02128e4d29aa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DefinitionInitializerProps(fn=fn)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-s3-antivirus.DefinitionInitializerProps",
    jsii_struct_bases=[],
    name_mapping={"fn": "fn"},
)
class DefinitionInitializerProps:
    def __init__(self, *, fn: _aws_cdk_aws_lambda_ceddda9d.IFunction) -> None:
        '''
        :param fn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2a20b5e896cc86bb710f21077df2a61eda2470c56880ad1269be85c2395980)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fn": fn,
        }

    @builtins.property
    def fn(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        result = self._values.get("fn")
        assert result is not None, "Required property 'fn' is missing"
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefinitionInitializerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sandbox(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-s3-antivirus.Sandbox",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        encrypted_file_system: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param encrypted_file_system: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd909ff8b45755736128261a1cd0e016aa852a884206de574b9547637977302)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SandboxProps(encrypted_file_system=encrypted_file_system)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToS3EnpointPolicy")
    def add_to_s3_enpoint_policy(
        self,
        statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
    ) -> None:
        '''
        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302b2f7daf5bffab0c2eedff66e741f34a75a160eef3c28f4a4a0f5fe13ec0a4)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToS3EnpointPolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="definitionBucket")
    def definition_bucket(self) -> DefinitionBucket:
        return typing.cast(DefinitionBucket, jsii.get(self, "definitionBucket"))

    @builtins.property
    @jsii.member(jsii_name="lambdaAccessPoint")
    def lambda_access_point(self) -> _aws_cdk_aws_efs_ceddda9d.IAccessPoint:
        return typing.cast(_aws_cdk_aws_efs_ceddda9d.IAccessPoint, jsii.get(self, "lambdaAccessPoint"))

    @builtins.property
    @jsii.member(jsii_name="s3Endpoint")
    def s3_endpoint(self) -> _aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpoint:
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpoint, jsii.get(self, "s3Endpoint"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-s3-antivirus.SandboxProps",
    jsii_struct_bases=[],
    name_mapping={"encrypted_file_system": "encryptedFileSystem"},
)
class SandboxProps:
    def __init__(
        self,
        *,
        encrypted_file_system: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param encrypted_file_system: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c44df258ec6c46019ae6323fffe75e0483d45e87ccd2fa5c9889635f6a813ad2)
            check_type(argname="argument encrypted_file_system", value=encrypted_file_system, expected_type=type_hints["encrypted_file_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encrypted_file_system is not None:
            self._values["encrypted_file_system"] = encrypted_file_system

    @builtins.property
    def encrypted_file_system(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("encrypted_file_system")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SandboxProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Scanner(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-s3-antivirus.Scanner",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        buckets: typing.Optional[typing.Sequence[_aws_cdk_aws_s3_ceddda9d.Bucket]] = None,
        on_error: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        on_result: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        scan_status_tag_name: typing.Optional[builtins.str] = None,
        update_schedule: typing.Optional[_aws_cdk_aws_events_ceddda9d.Schedule] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param buckets: -
        :param on_error: -
        :param on_result: -
        :param scan_status_tag_name: Default: cc:scan-status
        :param update_schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb3aba7b4444385349d0c3231fb2e55b8793f29c76bfc18cc026e75ce8cad2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScannerProps(
            buckets=buckets,
            on_error=on_error,
            on_result=on_result,
            scan_status_tag_name=scan_status_tag_name,
            update_schedule=update_schedule,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addSourceBucket")
    def add_source_bucket(self, bucket: _aws_cdk_aws_s3_ceddda9d.Bucket) -> None:
        '''
        :param bucket: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36204b1adecc35d453f0a3becef8e8a8255da078cdebfe41d00845cc3a015072)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast(None, jsii.invoke(self, "addSourceBucket", [bucket]))

    @builtins.property
    @jsii.member(jsii_name="sandbox")
    def sandbox(self) -> Sandbox:
        return typing.cast(Sandbox, jsii.get(self, "sandbox"))

    @builtins.property
    @jsii.member(jsii_name="scanFunction")
    def scan_function(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, jsii.get(self, "scanFunction"))

    @builtins.property
    @jsii.member(jsii_name="scanStatusTagName")
    def scan_status_tag_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scanStatusTagName"))

    @builtins.property
    @jsii.member(jsii_name="updateFunction")
    def update_function(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, jsii.get(self, "updateFunction"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-s3-antivirus.ScannerProps",
    jsii_struct_bases=[],
    name_mapping={
        "buckets": "buckets",
        "on_error": "onError",
        "on_result": "onResult",
        "scan_status_tag_name": "scanStatusTagName",
        "update_schedule": "updateSchedule",
    },
)
class ScannerProps:
    def __init__(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[_aws_cdk_aws_s3_ceddda9d.Bucket]] = None,
        on_error: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        on_result: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        scan_status_tag_name: typing.Optional[builtins.str] = None,
        update_schedule: typing.Optional[_aws_cdk_aws_events_ceddda9d.Schedule] = None,
    ) -> None:
        '''
        :param buckets: -
        :param on_error: -
        :param on_result: -
        :param scan_status_tag_name: Default: cc:scan-status
        :param update_schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f269d920da8a40f867d64b9b9f45fb5ffbf21e2ca1e0e747bee0d667bd9b91e6)
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
            check_type(argname="argument on_error", value=on_error, expected_type=type_hints["on_error"])
            check_type(argname="argument on_result", value=on_result, expected_type=type_hints["on_result"])
            check_type(argname="argument scan_status_tag_name", value=scan_status_tag_name, expected_type=type_hints["scan_status_tag_name"])
            check_type(argname="argument update_schedule", value=update_schedule, expected_type=type_hints["update_schedule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buckets is not None:
            self._values["buckets"] = buckets
        if on_error is not None:
            self._values["on_error"] = on_error
        if on_result is not None:
            self._values["on_result"] = on_result
        if scan_status_tag_name is not None:
            self._values["scan_status_tag_name"] = scan_status_tag_name
        if update_schedule is not None:
            self._values["update_schedule"] = update_schedule

    @builtins.property
    def buckets(self) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.Bucket]]:
        result = self._values.get("buckets")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.Bucket]], result)

    @builtins.property
    def on_error(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination]:
        result = self._values.get("on_error")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination], result)

    @builtins.property
    def on_result(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination]:
        result = self._values.get("on_result")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination], result)

    @builtins.property
    def scan_status_tag_name(self) -> typing.Optional[builtins.str]:
        '''
        :default: cc:scan-status
        '''
        result = self._values.get("scan_status_tag_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_schedule(self) -> typing.Optional[_aws_cdk_aws_events_ceddda9d.Schedule]:
        result = self._values.get("update_schedule")
        return typing.cast(typing.Optional[_aws_cdk_aws_events_ceddda9d.Schedule], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScannerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClamavLayer",
    "DefinitionBucket",
    "DefinitionBucketProps",
    "DefinitionInitializer",
    "DefinitionInitializerProps",
    "Sandbox",
    "SandboxProps",
    "Scanner",
    "ScannerProps",
]

publication.publish()

def _typecheckingstub__8f0f20dd21b6bbfb25699e7fe0168d53dc6c8d9b5c4ef728d9c2a459868473b9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93468d6a31dd51fd538fdb783e5cc286aef8538f0a66eef2b8fd90a547bcaa95(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    vpc_endpoint: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c26272e7df2e42ad47485f39c0beeb6889b6865c0b918e3b8927ef9ca80879c(
    *,
    vpc_endpoint: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201914154bf8b8d4dc22a3c1f8acb5d5e6ff7eee06050abdffbc02128e4d29aa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    fn: _aws_cdk_aws_lambda_ceddda9d.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2a20b5e896cc86bb710f21077df2a61eda2470c56880ad1269be85c2395980(
    *,
    fn: _aws_cdk_aws_lambda_ceddda9d.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd909ff8b45755736128261a1cd0e016aa852a884206de574b9547637977302(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encrypted_file_system: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302b2f7daf5bffab0c2eedff66e741f34a75a160eef3c28f4a4a0f5fe13ec0a4(
    statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44df258ec6c46019ae6323fffe75e0483d45e87ccd2fa5c9889635f6a813ad2(
    *,
    encrypted_file_system: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb3aba7b4444385349d0c3231fb2e55b8793f29c76bfc18cc026e75ce8cad2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    buckets: typing.Optional[typing.Sequence[_aws_cdk_aws_s3_ceddda9d.Bucket]] = None,
    on_error: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    on_result: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    scan_status_tag_name: typing.Optional[builtins.str] = None,
    update_schedule: typing.Optional[_aws_cdk_aws_events_ceddda9d.Schedule] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36204b1adecc35d453f0a3becef8e8a8255da078cdebfe41d00845cc3a015072(
    bucket: _aws_cdk_aws_s3_ceddda9d.Bucket,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f269d920da8a40f867d64b9b9f45fb5ffbf21e2ca1e0e747bee0d667bd9b91e6(
    *,
    buckets: typing.Optional[typing.Sequence[_aws_cdk_aws_s3_ceddda9d.Bucket]] = None,
    on_error: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    on_result: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    scan_status_tag_name: typing.Optional[builtins.str] = None,
    update_schedule: typing.Optional[_aws_cdk_aws_events_ceddda9d.Schedule] = None,
) -> None:
    """Type checking stubs"""
    pass
