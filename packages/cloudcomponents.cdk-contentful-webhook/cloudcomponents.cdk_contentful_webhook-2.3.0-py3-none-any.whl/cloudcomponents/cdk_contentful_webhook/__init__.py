'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-contentful-webhook

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-contentful-webhook)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-contentful-webhook/)

> Create, update and delete contentful webhooks with your app deployment

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-contentful-webhook
```

Python:

```bash
pip install cloudcomponents.cdk-contentful-webhook
```

## How to use

```python
import { ContentfulWebhook } from '@cloudcomponents/cdk-contentful-webhook';
import { SecretKey } from '@cloudcomponents/cdk-secret-key';
import { Stack, StackProps, aws_apigateway } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class ContentfulWebhookStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const api = new aws_apigateway.RestApi(this, 'Endpoint');
    api.root.addMethod('POST');

    if (typeof process.env.ACCESS_TOKEN === 'undefined') {
      throw new Error('environment variable ACCESS_TOKEN undefined');
    }
    const accessToken = SecretKey.fromPlainText(process.env.ACCESS_TOKEN);

    if (typeof process.env.SPACE_ID === 'undefined') {
      throw new Error('environment variable SPACE_ID undefined');
    }
    const spaceId = process.env.SPACE_ID;

    const topics = ['Entry.create'];

    new ContentfulWebhook(this, 'ContentfulWebhook', {
      accessToken,
      spaceId,
      name: 'ExampleWebhook',
      url: api.url,
      topics,
      logLevel: 'debug',
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-contentful-webhook/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-contentful-webhook/LICENSE)
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

import cloudcomponents.cdk_secret_key as _cloudcomponents_cdk_secret_key_a12c7701
import constructs as _constructs_77d1e7e8


class ContentfulWebhook(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-contentful-webhook.ContentfulWebhook",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
        name: builtins.str,
        space_id: builtins.str,
        topics: typing.Sequence[builtins.str],
        url: builtins.str,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_token: -
        :param name: -
        :param space_id: -
        :param topics: -
        :param url: -
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2da197ece5d55fa4d2b779cde521295bd7dd33f7309a48ed83a7303a5a98056)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ContentfulWebhookProps(
            access_token=access_token,
            name=name,
            space_id=space_id,
            topics=topics,
            url=url,
            log_level=log_level,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-contentful-webhook.ContentfulWebhookProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "name": "name",
        "space_id": "spaceId",
        "topics": "topics",
        "url": "url",
        "log_level": "logLevel",
    },
)
class ContentfulWebhookProps:
    def __init__(
        self,
        *,
        access_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
        name: builtins.str,
        space_id: builtins.str,
        topics: typing.Sequence[builtins.str],
        url: builtins.str,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: -
        :param name: -
        :param space_id: -
        :param topics: -
        :param url: -
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f01bf5b9d2476f0acc9cd08ba5b1b45a19ab8f463f22c607b9799ce74a1746b)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument space_id", value=space_id, expected_type=type_hints["space_id"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_token": access_token,
            "name": name,
            "space_id": space_id,
            "topics": topics,
            "url": url,
        }
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def access_token(
        self,
    ) -> typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey]:
        result = self._values.get("access_token")
        assert result is not None, "Required property 'access_token' is missing"
        return typing.cast(typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey], result)

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def space_id(self) -> builtins.str:
        result = self._values.get("space_id")
        assert result is not None, "Required property 'space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topics(self) -> typing.List[builtins.str]:
        result = self._values.get("topics")
        assert result is not None, "Required property 'topics' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def url(self) -> builtins.str:
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContentfulWebhookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ContentfulWebhook",
    "ContentfulWebhookProps",
]

publication.publish()

def _typecheckingstub__f2da197ece5d55fa4d2b779cde521295bd7dd33f7309a48ed83a7303a5a98056(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
    name: builtins.str,
    space_id: builtins.str,
    topics: typing.Sequence[builtins.str],
    url: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f01bf5b9d2476f0acc9cd08ba5b1b45a19ab8f463f22c607b9799ce74a1746b(
    *,
    access_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
    name: builtins.str,
    space_id: builtins.str,
    topics: typing.Sequence[builtins.str],
    url: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
