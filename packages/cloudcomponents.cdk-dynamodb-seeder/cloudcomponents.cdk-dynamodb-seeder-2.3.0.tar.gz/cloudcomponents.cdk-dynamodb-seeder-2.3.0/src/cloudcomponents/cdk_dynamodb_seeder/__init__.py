'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-dynamodb-seeder

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-dynamodb-seeder)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-dynamodb-seeder/)

> A seeder for dynamodb tables

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-dynamodb-seeder
```

Python:

```bash
pip install cloudcomponents.cdk-dynamodb-seeder
```

## How to use

```python
import * as path from 'path';
import { DynamoDBSeeder, Seeds } from '@cloudcomponents/cdk-dynamodb-seeder';
import { Stack, StackProps, RemovalPolicy } from 'aws-cdk-lib';
import { Table, AttributeType } from 'aws-cdk-lib/aws-dynamodb';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class DynamoDBSeederStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const table = new Table(this, 'Table', {
      partitionKey: {
        name: 'id',
        type: AttributeType.NUMBER,
      },
      removalPolicy: RemovalPolicy.DESTROY,
    });

    new DynamoDBSeeder(this, 'JsonFileSeeder', {
      table,
      seeds: Seeds.fromJsonFile(path.join(__dirname, '..', 'seeds.json')),
    });

    new DynamoDBSeeder(this, 'InlineSeeder', {
      table,
      seeds: Seeds.fromInline([
        {
          id: 3,
          column: 'foo',
        },
        {
          id: 4,
          column: 'bar',
        },
      ]),
    });

    const seedsBucket = Bucket.fromBucketName(
      this,
      'SeedsBucket',
      'my-seeds-bucket',
    );

    new DynamoDBSeeder(this, 'BucketSeeder', {
      table,
      seeds: Seeds.fromBucket(seedsBucket, 'seeds.json'),
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-dynamodb-seeder/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-dynamodb-seeder/LICENSE)
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
import aws_cdk.aws_dynamodb as _aws_cdk_aws_dynamodb_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import aws_cdk.aws_s3_assets as _aws_cdk_aws_s3_assets_ceddda9d
import constructs as _constructs_77d1e7e8


class DynamoDBSeeder(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.DynamoDBSeeder",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        seeds: "Seeds",
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param seeds: -
        :param table: -
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f3b1f11cd36ccbedac9625a73b8930cb0f025deec8a89f2d3d91726cf2acb45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DynamoDBSeederProps(seeds=seeds, table=table, timeout=timeout)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.DynamoDBSeederProps",
    jsii_struct_bases=[],
    name_mapping={"seeds": "seeds", "table": "table", "timeout": "timeout"},
)
class DynamoDBSeederProps:
    def __init__(
        self,
        *,
        seeds: "Seeds",
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ) -> None:
        '''
        :param seeds: -
        :param table: -
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b26f02909a1c9759af776ae18e1cdb34e4e221c896b11e50fdc78dbd33cefe6)
            check_type(argname="argument seeds", value=seeds, expected_type=type_hints["seeds"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "seeds": seeds,
            "table": table,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def seeds(self) -> "Seeds":
        result = self._values.get("seeds")
        assert result is not None, "Required property 'seeds' is missing"
        return typing.cast("Seeds", result)

    @builtins.property
    def table(self) -> _aws_cdk_aws_dynamodb_ceddda9d.ITable:
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(_aws_cdk_aws_dynamodb_ceddda9d.ITable, result)

    @builtins.property
    def timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.minutes(15)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDBSeederProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Seeds(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.Seeds",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "S3Seeds":
        '''
        :param bucket: The S3 bucket.
        :param key: The object key.
        :param object_version: Optional S3 object version.

        :return: ``S3Seeds`` associated with the specified S3 object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b72929c5f8ebcfb03acae7bfa730c4ff3641be03e0abd0517d691236305fcc9)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        return typing.cast("S3Seeds", jsii.sinvoke(cls, "fromBucket", [bucket, key, object_version]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(
        cls,
        seeds: typing.Sequence[typing.Mapping[builtins.str, typing.Any]],
    ) -> "InlineSeeds":
        '''
        :param seeds: The actual json code (limited to 4KiB).

        :return: ``InlineSeeds`` with inline seeds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__036e194dd0724d7ad8439f00c4578259212e3cd85f43f56f081fc7f27aae24d6)
            check_type(argname="argument seeds", value=seeds, expected_type=type_hints["seeds"])
        return typing.cast("InlineSeeds", jsii.sinvoke(cls, "fromInline", [seeds]))

    @jsii.member(jsii_name="fromJsonFile")
    @builtins.classmethod
    def from_json_file(
        cls,
        path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
    ) -> "JsonFileSeeds":
        '''Loads the seeds from a local disk path and uploads it to s3.

        :param path: Path to json seeds file.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :return: ``JsonFileSeeds`` associated with the specified S3 object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d066b1066c32d330342d55172d85557a3fdc7893f362e59c154a42f0efbbeb6c)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = _aws_cdk_aws_s3_assets_ceddda9d.AssetOptions(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("JsonFileSeeds", jsii.sinvoke(cls, "fromJsonFile", [path, options]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "SeedsConfig":
        '''Called when the seeder is initialized to allow this object to bind to the stack.

        :param scope: The binding scope.
        '''
        ...


class _SeedsProxy(Seeds):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "SeedsConfig":
        '''Called when the seeder is initialized to allow this object to bind to the stack.

        :param scope: The binding scope.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06672241fc43ca5f71f4ef9649c4ae3367cc3f9f88674226174bb0dbc1150518)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("SeedsConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Seeds).__jsii_proxy_class__ = lambda : _SeedsProxy


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.SeedsConfig",
    jsii_struct_bases=[],
    name_mapping={"inline_seeds": "inlineSeeds", "s3_location": "s3Location"},
)
class SeedsConfig:
    def __init__(
        self,
        *,
        inline_seeds: typing.Optional[builtins.str] = None,
        s3_location: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.Location, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param inline_seeds: Inline seeds.
        :param s3_location: The location of the seeds in S3.
        '''
        if isinstance(s3_location, dict):
            s3_location = _aws_cdk_aws_s3_ceddda9d.Location(**s3_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__740c436e3c17e6b1c99bf7c369e6ee70af358325167fa9674a3b63e68e58be6d)
            check_type(argname="argument inline_seeds", value=inline_seeds, expected_type=type_hints["inline_seeds"])
            check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inline_seeds is not None:
            self._values["inline_seeds"] = inline_seeds
        if s3_location is not None:
            self._values["s3_location"] = s3_location

    @builtins.property
    def inline_seeds(self) -> typing.Optional[builtins.str]:
        '''Inline seeds.'''
        result = self._values.get("inline_seeds")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_location(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Location]:
        '''The location of the seeds in S3.'''
        result = self._values.get("s3_location")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Location], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SeedsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InlineSeeds(
    Seeds,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.InlineSeeds",
):
    '''Seeds from an inline json object (limited to 4KiB).'''

    def __init__(self, seeds: builtins.str) -> None:
        '''
        :param seeds: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b13a4566e09c6b8b41014be8b7b11cbbf089bb75336b64d2a728c95a4f82e72b)
            check_type(argname="argument seeds", value=seeds, expected_type=type_hints["seeds"])
        jsii.create(self.__class__, self, [seeds])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _constructs_77d1e7e8.Construct) -> SeedsConfig:
        '''Called when the seeder is initialized to allow this object to bind to the stack.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d797c0942c833ee8a3efd5429a41982a073b45438d0121231ee912a8203cfc7)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(SeedsConfig, jsii.invoke(self, "bind", [_scope]))


class JsonFileSeeds(
    Seeds,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.JsonFileSeeds",
):
    '''Seeds from a local json file.'''

    def __init__(
        self,
        path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
    ) -> None:
        '''
        :param path: -
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527ee4b61270bc63b15eb65b60b654d9923a3a6cca10c39527e754caa496f84f)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = _aws_cdk_aws_s3_assets_ceddda9d.AssetOptions(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        jsii.create(self.__class__, self, [path, options])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> SeedsConfig:
        '''Called when the seeder is initialized to allow this object to bind to the stack.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82813fc88d8b0d4df60ddbf924aebd78cab8fd719d01d17b27fcb10a8f20e33)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(SeedsConfig, jsii.invoke(self, "bind", [scope]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))


class S3Seeds(
    Seeds,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-dynamodb-seeder.S3Seeds",
):
    '''Seeds from an S3 archive.'''

    def __init__(
        self,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param key: -
        :param object_version: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__386f76601e70f2aea1357fa296dfeead562b09c962c1df1f4fc7a7d4a204d348)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        jsii.create(self.__class__, self, [bucket, key, object_version])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _constructs_77d1e7e8.Construct) -> SeedsConfig:
        '''Called when the seeder is initialized to allow this object to bind to the stack.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e4dd956f2bd378fb0c5b58636d320b033852052da330560d89ef6ee50fc5c71)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(SeedsConfig, jsii.invoke(self, "bind", [_scope]))


__all__ = [
    "DynamoDBSeeder",
    "DynamoDBSeederProps",
    "InlineSeeds",
    "JsonFileSeeds",
    "S3Seeds",
    "Seeds",
    "SeedsConfig",
]

publication.publish()

def _typecheckingstub__7f3b1f11cd36ccbedac9625a73b8930cb0f025deec8a89f2d3d91726cf2acb45(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    seeds: Seeds,
    table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b26f02909a1c9759af776ae18e1cdb34e4e221c896b11e50fdc78dbd33cefe6(
    *,
    seeds: Seeds,
    table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b72929c5f8ebcfb03acae7bfa730c4ff3641be03e0abd0517d691236305fcc9(
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__036e194dd0724d7ad8439f00c4578259212e3cd85f43f56f081fc7f27aae24d6(
    seeds: typing.Sequence[typing.Mapping[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d066b1066c32d330342d55172d85557a3fdc7893f362e59c154a42f0efbbeb6c(
    path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
    bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
    ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06672241fc43ca5f71f4ef9649c4ae3367cc3f9f88674226174bb0dbc1150518(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740c436e3c17e6b1c99bf7c369e6ee70af358325167fa9674a3b63e68e58be6d(
    *,
    inline_seeds: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.Location, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13a4566e09c6b8b41014be8b7b11cbbf089bb75336b64d2a728c95a4f82e72b(
    seeds: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d797c0942c833ee8a3efd5429a41982a073b45438d0121231ee912a8203cfc7(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527ee4b61270bc63b15eb65b60b654d9923a3a6cca10c39527e754caa496f84f(
    path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
    bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
    ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82813fc88d8b0d4df60ddbf924aebd78cab8fd719d01d17b27fcb10a8f20e33(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386f76601e70f2aea1357fa296dfeead562b09c962c1df1f4fc7a7d4a204d348(
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e4dd956f2bd378fb0c5b58636d320b033852052da330560d89ef6ee50fc5c71(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass
