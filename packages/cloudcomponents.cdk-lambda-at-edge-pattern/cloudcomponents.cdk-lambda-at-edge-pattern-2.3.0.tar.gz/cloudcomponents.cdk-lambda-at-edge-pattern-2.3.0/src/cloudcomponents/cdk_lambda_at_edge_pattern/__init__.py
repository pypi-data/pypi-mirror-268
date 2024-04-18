'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-lambda-at-edge-pattern

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-lambda-at-edge-pattern)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-lambda-at-edge-pattern/)

> CDK Constructs for Lambda@Edge pattern: HttpHeaders

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-lambda-at-edge-pattern
```

Python:

```bash
pip install cloudcomponents.cdk-lambda-at-edge-pattern
```

## How to use

```python
import { StaticWebsite } from '@cloudcomponents/cdk-static-website';
import { OriginMutation } from '@cloudcomponents/cdk-lambda-at-edge-pattern';
import { RemovalPolicy, Stack, StackProps, aws_route53 } from 'aws-cdk-lib';

import { Construct } from 'constructs';

export class StaticWebsiteStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const hostedZone = aws_route53.HostedZone.fromLookup(this, 'HostedZone', {
      domainName: 'cloudcomponents.org',
    });

    // Create a lambda at edge
    const originMutation = new OriginMutation(stack, 'OriginMutation');

    new StaticWebsite(this, 'StaticWebsite', {
      hostedZone,
      domainNames: ['cloudcomponents.org', 'www.cloudcomponents.org'],
      edgeLambdas: [originMutation],
      removalPolicy: RemovalPolicy.DESTROY,
    });
  }
}
```

### Cloudfront Distribution

```python
new cloudfront.Distribution(this, 'myDist', {
  defaultBehavior: {
    origin: new origins.S3Origin(myBucket),
    edgeLambdas: [httpHeaders],
  },
});
```

### HttpHeaders

```python
const httpHeaders = new HttpHeaders(this, 'HttpHeaders', {
  httpHeaders: {
    'Content-Security-Policy':
      "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; object-src 'none'; connect-src 'self'",
    'Strict-Transport-Security':
      'max-age=31536000; includeSubdomains; preload',
    'Referrer-Policy': 'same-origin',
    'X-XSS-Protection': '1; mode=block',
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
    'Cache-Control': 'no-cache',
  },
});
```

### OriginMutation

https://chrisschuld.com/2020/05/gatsby-hosting-on-cloudfront/

```python
const originMutation = new OriginMutation(stack, 'OriginMutation');
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-lambda-at-edge-pattern/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-lambda-at-edge-pattern/LICENSE)
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
import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import constructs as _constructs_77d1e7e8


class BaseEdgeConstruct(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.BaseEdgeConstruct",
):
    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e897633093046b31f10c449b1c989e12717049e7a8b35678bd473d2aa8933a32)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @builtins.property
    @jsii.member(jsii_name="edgeStack")
    def _edge_stack(self) -> _aws_cdk_ceddda9d.Stack:
        return typing.cast(_aws_cdk_ceddda9d.Stack, jsii.get(self, "edgeStack"))

    @builtins.property
    @jsii.member(jsii_name="stack")
    def _stack(self) -> _aws_cdk_ceddda9d.Stack:
        return typing.cast(_aws_cdk_ceddda9d.Stack, jsii.get(self, "stack"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.CommonEdgeFunctionProps",
    jsii_struct_bases=[],
    name_mapping={"edge_role": "edgeRole", "parameter_name": "parameterName"},
)
class CommonEdgeFunctionProps:
    def __init__(
        self,
        *,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a11bcba1b3fb4f90ac388bdf2240c3429b6b3652f75a0d74066c48056b02ba45)
            check_type(argname="argument edge_role", value=edge_role, expected_type=type_hints["edge_role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if edge_role is not None:
            self._values["edge_role"] = edge_role
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name

    @builtins.property
    def edge_role(self) -> typing.Optional["IEdgeRole"]:
        result = self._values.get("edge_role")
        return typing.cast(typing.Optional["IEdgeRole"], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonEdgeFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.Configuration",
    jsii_struct_bases=[],
    name_mapping={"log_level": "logLevel"},
)
class Configuration:
    def __init__(self, *, log_level: "LogLevel") -> None:
        '''
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d715db8efd192c2cb4d618089f3c5c51d706aacf1b36df8e22a040777d067230)
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_level": log_level,
        }

    @builtins.property
    def log_level(self) -> "LogLevel":
        result = self._values.get("log_level")
        assert result is not None, "Required property 'log_level' is missing"
        return typing.cast("LogLevel", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeFunctionProps",
    jsii_struct_bases=[CommonEdgeFunctionProps],
    name_mapping={
        "edge_role": "edgeRole",
        "parameter_name": "parameterName",
        "code": "code",
        "configuration": "configuration",
        "event_type": "eventType",
        "name": "name",
    },
)
class EdgeFunctionProps(CommonEdgeFunctionProps):
    def __init__(
        self,
        *,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        code: _aws_cdk_aws_lambda_ceddda9d.Code,
        configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
        event_type: _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType,
        name: builtins.str,
    ) -> None:
        '''
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        :param code: -
        :param configuration: -
        :param event_type: -
        :param name: -
        '''
        if isinstance(configuration, dict):
            configuration = Configuration(**configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ebf0cc10d99339aea13b2ef002f1f29c41d055319600a8c34c99f37390b6039)
            check_type(argname="argument edge_role", value=edge_role, expected_type=type_hints["edge_role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code": code,
            "configuration": configuration,
            "event_type": event_type,
            "name": name,
        }
        if edge_role is not None:
            self._values["edge_role"] = edge_role
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name

    @builtins.property
    def edge_role(self) -> typing.Optional["IEdgeRole"]:
        result = self._values.get("edge_role")
        return typing.cast(typing.Optional["IEdgeRole"], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code(self) -> _aws_cdk_aws_lambda_ceddda9d.Code:
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.Code, result)

    @builtins.property
    def configuration(self) -> Configuration:
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(Configuration, result)

    @builtins.property
    def event_type(self) -> _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType:
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType, result)

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeRoleProps",
    jsii_struct_bases=[],
    name_mapping={"role_name": "roleName"},
)
class EdgeRoleProps:
    def __init__(self, *, role_name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param role_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__159e1595a39de1730ac4cc6f928d0b44a45b9fe1adeec67c4e9b106c91c70456)
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.HttpHeadersProps",
    jsii_struct_bases=[CommonEdgeFunctionProps],
    name_mapping={
        "edge_role": "edgeRole",
        "parameter_name": "parameterName",
        "http_headers": "httpHeaders",
        "log_level": "logLevel",
    },
)
class HttpHeadersProps(CommonEdgeFunctionProps):
    def __init__(
        self,
        *,
        edge_role: typing.Optional["IEdgeRole"] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        http_headers: typing.Mapping[builtins.str, builtins.str],
        log_level: typing.Optional["LogLevel"] = None,
    ) -> None:
        '''
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        :param http_headers: -
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20afa5cc819176ed71252f6eadecde451587c277961225a86f21006e9a783694)
            check_type(argname="argument edge_role", value=edge_role, expected_type=type_hints["edge_role"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_headers": http_headers,
        }
        if edge_role is not None:
            self._values["edge_role"] = edge_role
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if log_level is not None:
            self._values["log_level"] = log_level

    @builtins.property
    def edge_role(self) -> typing.Optional["IEdgeRole"]:
        result = self._values.get("edge_role")
        return typing.cast(typing.Optional["IEdgeRole"], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.'''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        result = self._values.get("http_headers")
        assert result is not None, "Required property 'http_headers' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional["LogLevel"]:
        result = self._values.get("log_level")
        return typing.cast(typing.Optional["LogLevel"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpHeadersProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeLambda")
class IEdgeLambda(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType:
        ...

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> _aws_cdk_aws_lambda_ceddda9d.IVersion:
        ...


class _IEdgeLambdaProxy:
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeLambda"

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType:
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType, jsii.get(self, "eventType"))

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> _aws_cdk_aws_lambda_ceddda9d.IVersion:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IVersion, jsii.get(self, "functionVersion"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEdgeLambda).__jsii_proxy_class__ = lambda : _IEdgeLambdaProxy


@jsii.interface(jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeRole")
class IEdgeRole(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _aws_cdk_aws_iam_ceddda9d.Role:
        ...

    @jsii.member(jsii_name="addToEdgeRolePolicy")
    def add_to_edge_role_policy(
        self,
        statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
    ) -> None:
        '''
        :param statement: -
        '''
        ...


class _IEdgeRoleProxy:
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-lambda-at-edge-pattern.IEdgeRole"

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _aws_cdk_aws_iam_ceddda9d.Role:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Role, jsii.get(self, "role"))

    @jsii.member(jsii_name="addToEdgeRolePolicy")
    def add_to_edge_role_policy(
        self,
        statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
    ) -> None:
        '''
        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9a763bfae0041e9ade24c7d580dd52fb0cfbad9064760a10a9e54c966c7ad0)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToEdgeRolePolicy", [statement]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEdgeRole).__jsii_proxy_class__ = lambda : _IEdgeRoleProxy


@jsii.enum(jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.LogLevel")
class LogLevel(enum.Enum):
    NONE = "NONE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"


class WithConfiguration(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.WithConfiguration",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
        function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param configuration: -
        :param function: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d855882f3f86f88d0b60a9f7f9872881a94a646e732611eb2688adc267d90e07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WithConfigurationProps(configuration=configuration, function=function)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> _aws_cdk_aws_lambda_ceddda9d.IVersion:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IVersion, jsii.get(self, "functionVersion"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.WithConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"configuration": "configuration", "function": "function"},
)
class WithConfigurationProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
        function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    ) -> None:
        '''
        :param configuration: -
        :param function: -
        '''
        if isinstance(configuration, dict):
            configuration = Configuration(**configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5c3edcb92f6dabdeaa62c04afe4e9bcb45fd1c8173f4f2fd50ddfc91581836)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "function": function,
        }

    @builtins.property
    def configuration(self) -> Configuration:
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(Configuration, result)

    @builtins.property
    def function(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        result = self._values.get("function")
        assert result is not None, "Required property 'function' is missing"
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WithConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEdgeLambda)
class EdgeFunction(
    BaseEdgeConstruct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeFunction",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        code: _aws_cdk_aws_lambda_ceddda9d.Code,
        configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
        event_type: _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType,
        name: builtins.str,
        edge_role: typing.Optional[IEdgeRole] = None,
        parameter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param code: -
        :param configuration: -
        :param event_type: -
        :param name: -
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a8fd532338064a740bea50e7f32222360e741806dd415cef6c1b1afe495dd7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EdgeFunctionProps(
            code=code,
            configuration=configuration,
            event_type=event_type,
            name=name,
            edge_role=edge_role,
            parameter_name=parameter_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="edgeRole")
    def edge_role(self) -> IEdgeRole:
        return typing.cast(IEdgeRole, jsii.get(self, "edgeRole"))

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType:
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType, jsii.get(self, "eventType"))

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> _aws_cdk_aws_lambda_ceddda9d.IVersion:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IVersion, jsii.get(self, "functionVersion"))


@jsii.implements(IEdgeRole)
class EdgeRole(
    BaseEdgeConstruct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.EdgeRole",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param role_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e806a868526580220d3e0a28891a354c224e2b9bbd8edd25b50ee0799dfa765)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EdgeRoleProps(role_name=role_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToEdgeRolePolicy")
    def add_to_edge_role_policy(
        self,
        statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
    ) -> None:
        '''
        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c12ce860b5204aa7070ba1b8c56616c7c0a2efbdb0b6bfdb62e5c61ce64ae4e3)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToEdgeRolePolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _aws_cdk_aws_iam_ceddda9d.Role:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Role, jsii.get(self, "role"))


class HttpHeaders(
    EdgeFunction,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-lambda-at-edge-pattern.HttpHeaders",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        http_headers: typing.Mapping[builtins.str, builtins.str],
        log_level: typing.Optional[LogLevel] = None,
        edge_role: typing.Optional[IEdgeRole] = None,
        parameter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param http_headers: -
        :param log_level: -
        :param edge_role: -
        :param parameter_name: The name of the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72388fb1515e89f27ef1c9278cab7dcfb75884659f209b84816eec9cc3ac4213)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HttpHeadersProps(
            http_headers=http_headers,
            log_level=log_level,
            edge_role=edge_role,
            parameter_name=parameter_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


__all__ = [
    "BaseEdgeConstruct",
    "CommonEdgeFunctionProps",
    "Configuration",
    "EdgeFunction",
    "EdgeFunctionProps",
    "EdgeRole",
    "EdgeRoleProps",
    "HttpHeaders",
    "HttpHeadersProps",
    "IEdgeLambda",
    "IEdgeRole",
    "LogLevel",
    "WithConfiguration",
    "WithConfigurationProps",
]

publication.publish()

def _typecheckingstub__e897633093046b31f10c449b1c989e12717049e7a8b35678bd473d2aa8933a32(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a11bcba1b3fb4f90ac388bdf2240c3429b6b3652f75a0d74066c48056b02ba45(
    *,
    edge_role: typing.Optional[IEdgeRole] = None,
    parameter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d715db8efd192c2cb4d618089f3c5c51d706aacf1b36df8e22a040777d067230(
    *,
    log_level: LogLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ebf0cc10d99339aea13b2ef002f1f29c41d055319600a8c34c99f37390b6039(
    *,
    edge_role: typing.Optional[IEdgeRole] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    code: _aws_cdk_aws_lambda_ceddda9d.Code,
    configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
    event_type: _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159e1595a39de1730ac4cc6f928d0b44a45b9fe1adeec67c4e9b106c91c70456(
    *,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20afa5cc819176ed71252f6eadecde451587c277961225a86f21006e9a783694(
    *,
    edge_role: typing.Optional[IEdgeRole] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    http_headers: typing.Mapping[builtins.str, builtins.str],
    log_level: typing.Optional[LogLevel] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9a763bfae0041e9ade24c7d580dd52fb0cfbad9064760a10a9e54c966c7ad0(
    statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d855882f3f86f88d0b60a9f7f9872881a94a646e732611eb2688adc267d90e07(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
    function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5c3edcb92f6dabdeaa62c04afe4e9bcb45fd1c8173f4f2fd50ddfc91581836(
    *,
    configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
    function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a8fd532338064a740bea50e7f32222360e741806dd415cef6c1b1afe495dd7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    code: _aws_cdk_aws_lambda_ceddda9d.Code,
    configuration: typing.Union[Configuration, typing.Dict[builtins.str, typing.Any]],
    event_type: _aws_cdk_aws_cloudfront_ceddda9d.LambdaEdgeEventType,
    name: builtins.str,
    edge_role: typing.Optional[IEdgeRole] = None,
    parameter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e806a868526580220d3e0a28891a354c224e2b9bbd8edd25b50ee0799dfa765(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c12ce860b5204aa7070ba1b8c56616c7c0a2efbdb0b6bfdb62e5c61ce64ae4e3(
    statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72388fb1515e89f27ef1c9278cab7dcfb75884659f209b84816eec9cc3ac4213(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    http_headers: typing.Mapping[builtins.str, builtins.str],
    log_level: typing.Optional[LogLevel] = None,
    edge_role: typing.Optional[IEdgeRole] = None,
    parameter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
