'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-stripe-webhook

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-stripe-webhook)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-stripe-webhook/)

> Create, update and delete stripe webhooks with your app deployment

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-stripe-webhook
```

Python:

```bash
pip install cloudcomponents.cdk-stripe-webhook
```

## How to use

### EventBus Producer

```python
import { SecretKey, SecretKeyStore } from '@cloudcomponents/cdk-secret-key';
import { StripeWebhook, StripeEventBusProducer } from '@cloudcomponents/cdk-stripe-webhook';
import { Stack, StackProps, aws_ssm } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class StripeWebhookEventBusStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    if (typeof process.env.SECRET_KEY === 'undefined') {
      throw new Error('environment variable SECRET_KEY undefined');
    }
    const secretKey = SecretKey.fromPlainText(process.env.SECRET_KEY);

    const endpointSecretParameter = aws_ssm.StringParameter.fromSecureStringParameterAttributes(this, 'Param', {
      parameterName: 'stripe',
      version: 1,
    });

    const producer = new StripeEventBusProducer(this, 'Producer', {
      secretKey,
      endpointSecret: SecretKey.fromSSMParameter(endpointSecretParameter),
    });

    const events = ['charge.failed', 'charge.succeeded'];

    const endpointSecretStore = SecretKeyStore.fromSSMParameter(endpointSecretParameter);

    new StripeWebhook(this, 'StripeWebhook', {
      secretKey,
      url: producer.url,
      events,
      logLevel: 'debug',
      endpointSecretStore,
    });
  }
}
```

### Custom Handler

```python
import { SecretKey } from '@cloudcomponents/cdk-secret-key';
import { StripeWebhook } from '@cloudcomponents/cdk-stripe-webhook';
import { Stack, StackProps, aws_apigateway } from 'aws-cdk-lib';
import { Construct } from 'constructs';
export class StripeWebhookStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const api = new aws_apigateway.RestApi(this, 'Endpoint');
    api.root.addMethod('POST');

    if (typeof process.env.SECRET_KEY === 'undefined') {
      throw new Error('environment variable SECRET_KEY undefined');
    }
    const secretKey = SecretKey.fromPlainText(process.env.SECRET_KEY);

    const events = ['charge.failed', 'charge.succeeded'];

    new StripeWebhook(this, 'StripeWebhook', {
      secretKey,
      url: api.url,
      events,
      logLevel: 'debug',
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-stripe-webhook/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-stripe-webhook/LICENSE)
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

import aws_cdk.aws_events as _aws_cdk_aws_events_ceddda9d
import cloudcomponents.cdk_secret_key as _cloudcomponents_cdk_secret_key_a12c7701
import constructs as _constructs_77d1e7e8


class StripeEventBusProducer(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-stripe-webhook.StripeEventBusProducer",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        endpoint_secret: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
        secret_key: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
        event_bus: typing.Optional[_aws_cdk_aws_events_ceddda9d.IEventBus] = None,
        source: typing.Optional[builtins.str] = None,
        throttling_burst_limit: typing.Optional[jsii.Number] = None,
        throttling_rate_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param endpoint_secret: -
        :param secret_key: -
        :param event_bus: -
        :param source: -
        :param throttling_burst_limit: -
        :param throttling_rate_limit: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3470879764bf0031cba3bfb9ff7046e7753f5ebb9c5d4c06117b20eca25f6755)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StripeEventBusProducerProps(
            endpoint_secret=endpoint_secret,
            secret_key=secret_key,
            event_bus=event_bus,
            source=source,
            throttling_burst_limit=throttling_burst_limit,
            throttling_rate_limit=throttling_rate_limit,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-stripe-webhook.StripeEventBusProducerProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_secret": "endpointSecret",
        "secret_key": "secretKey",
        "event_bus": "eventBus",
        "source": "source",
        "throttling_burst_limit": "throttlingBurstLimit",
        "throttling_rate_limit": "throttlingRateLimit",
    },
)
class StripeEventBusProducerProps:
    def __init__(
        self,
        *,
        endpoint_secret: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
        secret_key: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
        event_bus: typing.Optional[_aws_cdk_aws_events_ceddda9d.IEventBus] = None,
        source: typing.Optional[builtins.str] = None,
        throttling_burst_limit: typing.Optional[jsii.Number] = None,
        throttling_rate_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_secret: -
        :param secret_key: -
        :param event_bus: -
        :param source: -
        :param throttling_burst_limit: -
        :param throttling_rate_limit: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104bad6ee27439068284d1209b33b2cb7fba50ec49bddc5ae23f061dff5ca9b2)
            check_type(argname="argument endpoint_secret", value=endpoint_secret, expected_type=type_hints["endpoint_secret"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument throttling_burst_limit", value=throttling_burst_limit, expected_type=type_hints["throttling_burst_limit"])
            check_type(argname="argument throttling_rate_limit", value=throttling_rate_limit, expected_type=type_hints["throttling_rate_limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_secret": endpoint_secret,
            "secret_key": secret_key,
        }
        if event_bus is not None:
            self._values["event_bus"] = event_bus
        if source is not None:
            self._values["source"] = source
        if throttling_burst_limit is not None:
            self._values["throttling_burst_limit"] = throttling_burst_limit
        if throttling_rate_limit is not None:
            self._values["throttling_rate_limit"] = throttling_rate_limit

    @builtins.property
    def endpoint_secret(self) -> _cloudcomponents_cdk_secret_key_a12c7701.SecretKey:
        result = self._values.get("endpoint_secret")
        assert result is not None, "Required property 'endpoint_secret' is missing"
        return typing.cast(_cloudcomponents_cdk_secret_key_a12c7701.SecretKey, result)

    @builtins.property
    def secret_key(self) -> _cloudcomponents_cdk_secret_key_a12c7701.SecretKey:
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(_cloudcomponents_cdk_secret_key_a12c7701.SecretKey, result)

    @builtins.property
    def event_bus(self) -> typing.Optional[_aws_cdk_aws_events_ceddda9d.IEventBus]:
        result = self._values.get("event_bus")
        return typing.cast(typing.Optional[_aws_cdk_aws_events_ceddda9d.IEventBus], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("throttling_burst_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("throttling_rate_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StripeEventBusProducerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StripeWebhook(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-stripe-webhook.StripeWebhook",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        events: typing.Sequence[builtins.str],
        secret_key: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
        url: builtins.str,
        description: typing.Optional[builtins.str] = None,
        endpoint_secret_store: typing.Optional[_cloudcomponents_cdk_secret_key_a12c7701.SecretKeyStore] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param events: -
        :param secret_key: -
        :param url: -
        :param description: -
        :param endpoint_secret_store: -
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03824f0260cc289d9ad5280fc213dad01232b00d4ac7ba88e673868503c5871e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StripeWebhookProps(
            events=events,
            secret_key=secret_key,
            url=url,
            description=description,
            endpoint_secret_store=endpoint_secret_store,
            log_level=log_level,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-stripe-webhook.StripeWebhookProps",
    jsii_struct_bases=[],
    name_mapping={
        "events": "events",
        "secret_key": "secretKey",
        "url": "url",
        "description": "description",
        "endpoint_secret_store": "endpointSecretStore",
        "log_level": "logLevel",
    },
)
class StripeWebhookProps:
    def __init__(
        self,
        *,
        events: typing.Sequence[builtins.str],
        secret_key: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
        url: builtins.str,
        description: typing.Optional[builtins.str] = None,
        endpoint_secret_store: typing.Optional[_cloudcomponents_cdk_secret_key_a12c7701.SecretKeyStore] = None,
        log_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param events: -
        :param secret_key: -
        :param url: -
        :param description: -
        :param endpoint_secret_store: -
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a92d1219a62b0fa19f9e986a7c3fc0370984a4d00e7b903e259e41e4472fc46)
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument endpoint_secret_store", value=endpoint_secret_store, expected_type=type_hints["endpoint_secret_store"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "events": events,
            "secret_key": secret_key,
            "url": url,
        }
        if description is not None:
            self._values["description"] = description
        if endpoint_secret_store is not None:
            self._values["endpoint_secret_store"] = endpoint_secret_store
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def events(self) -> typing.List[builtins.str]:
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def secret_key(
        self,
    ) -> typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey]:
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey], result)

    @builtins.property
    def url(self) -> builtins.str:
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_secret_store(
        self,
    ) -> typing.Optional[_cloudcomponents_cdk_secret_key_a12c7701.SecretKeyStore]:
        result = self._values.get("endpoint_secret_store")
        return typing.cast(typing.Optional[_cloudcomponents_cdk_secret_key_a12c7701.SecretKeyStore], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StripeWebhookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StripeEventBusProducer",
    "StripeEventBusProducerProps",
    "StripeWebhook",
    "StripeWebhookProps",
]

publication.publish()

def _typecheckingstub__3470879764bf0031cba3bfb9ff7046e7753f5ebb9c5d4c06117b20eca25f6755(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    endpoint_secret: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
    secret_key: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
    event_bus: typing.Optional[_aws_cdk_aws_events_ceddda9d.IEventBus] = None,
    source: typing.Optional[builtins.str] = None,
    throttling_burst_limit: typing.Optional[jsii.Number] = None,
    throttling_rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104bad6ee27439068284d1209b33b2cb7fba50ec49bddc5ae23f061dff5ca9b2(
    *,
    endpoint_secret: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
    secret_key: _cloudcomponents_cdk_secret_key_a12c7701.SecretKey,
    event_bus: typing.Optional[_aws_cdk_aws_events_ceddda9d.IEventBus] = None,
    source: typing.Optional[builtins.str] = None,
    throttling_burst_limit: typing.Optional[jsii.Number] = None,
    throttling_rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03824f0260cc289d9ad5280fc213dad01232b00d4ac7ba88e673868503c5871e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    events: typing.Sequence[builtins.str],
    secret_key: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
    url: builtins.str,
    description: typing.Optional[builtins.str] = None,
    endpoint_secret_store: typing.Optional[_cloudcomponents_cdk_secret_key_a12c7701.SecretKeyStore] = None,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a92d1219a62b0fa19f9e986a7c3fc0370984a4d00e7b903e259e41e4472fc46(
    *,
    events: typing.Sequence[builtins.str],
    secret_key: typing.Union[builtins.str, _cloudcomponents_cdk_secret_key_a12c7701.SecretKey],
    url: builtins.str,
    description: typing.Optional[builtins.str] = None,
    endpoint_secret_store: typing.Optional[_cloudcomponents_cdk_secret_key_a12c7701.SecretKeyStore] = None,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
