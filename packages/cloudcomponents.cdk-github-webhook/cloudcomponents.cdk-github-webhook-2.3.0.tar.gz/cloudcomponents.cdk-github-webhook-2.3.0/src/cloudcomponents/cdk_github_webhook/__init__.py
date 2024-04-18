'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-github-webhook

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-github-webhook)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-github-webhook/)
[![Mentioned in Awesome CDK](https://awesome.re/mentioned-badge.svg)](https://github.com/kolomied/awesome-cdk)

> Create, update and delete github webhooks with your app deployment

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-github-webhook
```

Python:

```bash
pip install cloudcomponents.cdk-github-webhook
```

## How to use

```python
import { GithubWebhook } from '@cloudcomponents/cdk-github-webhook';
import { SecretKey } from '@cloudcomponents/cdk-secret-key';
import { Stack, StackProps, aws_apigateway } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class GithubWebhookStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const api = new aws_apigateway.RestApi(this, 'github-webhook');
    api.root.addMethod('POST');

    if (typeof process.env.API_TOKEN === 'undefined') {
      throw new Error('environment variable API_TOKEN undefined');
    }
    const githubApiToken = SecretKey.fromPlainText(process.env.API_TOKEN);

    // @example https://github.com/cloudcomponents/cdk-constructs
    if (typeof process.env.REPO_URL === 'undefined') {
      throw new Error('environment variable REPO_URL undefined');
    }
    const githubRepoUrl = process.env.REPO_URL;

    // @see https://developer.github.com/v3/activity/events/types/
    const events = ['*'];

    new GithubWebhook(this, 'GithubWebhook', {
      githubApiToken,
      githubRepoUrl,
      payloadUrl: api.url,
      events,
      logLevel: 'debug',
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-github-webhook/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-github-webhook/LICENSE)
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


class GithubWebhook(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-github-webhook.GithubWebhook",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        events: typing.Sequence[builtins.str],
        github_api_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
        github_repo_url: builtins.str,
        payload_url: builtins.str,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param events: Determines what events the hook is triggered for.
        :param github_api_token: The OAuth access token.
        :param github_repo_url: The Github repo url.
        :param payload_url: The URL to which the payloads will be delivered.
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fea15c4d53a91e8ff98163c995dadfd911357466ce9365a13fe0b4a6caafadb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GithubWebhookProps(
            events=events,
            github_api_token=github_api_token,
            github_repo_url=github_repo_url,
            payload_url=payload_url,
            log_level=log_level,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-github-webhook.GithubWebhookProps",
    jsii_struct_bases=[],
    name_mapping={
        "events": "events",
        "github_api_token": "githubApiToken",
        "github_repo_url": "githubRepoUrl",
        "payload_url": "payloadUrl",
        "log_level": "logLevel",
    },
)
class GithubWebhookProps:
    def __init__(
        self,
        *,
        events: typing.Sequence[builtins.str],
        github_api_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
        github_repo_url: builtins.str,
        payload_url: builtins.str,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param events: Determines what events the hook is triggered for.
        :param github_api_token: The OAuth access token.
        :param github_repo_url: The Github repo url.
        :param payload_url: The URL to which the payloads will be delivered.
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4764619dba203fad2b8bc2903124d361eacb9addb3213354c5e0463a047171a4)
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument github_api_token", value=github_api_token, expected_type=type_hints["github_api_token"])
            check_type(argname="argument github_repo_url", value=github_repo_url, expected_type=type_hints["github_repo_url"])
            check_type(argname="argument payload_url", value=payload_url, expected_type=type_hints["payload_url"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "events": events,
            "github_api_token": github_api_token,
            "github_repo_url": github_repo_url,
            "payload_url": payload_url,
        }
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def events(self) -> typing.List[builtins.str]:
        '''Determines what events the hook is triggered for.

        :see: https://developer.github.com/v3/activity/events/types/
        '''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def github_api_token(
        self,
    ) -> typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey]:
        '''The OAuth access token.'''
        result = self._values.get("github_api_token")
        assert result is not None, "Required property 'github_api_token' is missing"
        return typing.cast(typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey], result)

    @builtins.property
    def github_repo_url(self) -> builtins.str:
        '''The Github repo url.'''
        result = self._values.get("github_repo_url")
        assert result is not None, "Required property 'github_repo_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def payload_url(self) -> builtins.str:
        '''The URL to which the payloads will be delivered.'''
        result = self._values.get("payload_url")
        assert result is not None, "Required property 'payload_url' is missing"
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
        return "GithubWebhookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GithubWebhook",
    "GithubWebhookProps",
]

publication.publish()

def _typecheckingstub__9fea15c4d53a91e8ff98163c995dadfd911357466ce9365a13fe0b4a6caafadb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    events: typing.Sequence[builtins.str],
    github_api_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
    github_repo_url: builtins.str,
    payload_url: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4764619dba203fad2b8bc2903124d361eacb9addb3213354c5e0463a047171a4(
    *,
    events: typing.Sequence[builtins.str],
    github_api_token: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
    github_repo_url: builtins.str,
    payload_url: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
