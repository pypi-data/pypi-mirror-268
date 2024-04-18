'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-cloudfront-authorization

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-cloudfront-authorization)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-cloudfront-authorization/)
[![Mentioned in Awesome CDK](https://awesome.re/mentioned-badge.svg)](https://github.com/kolomied/awesome-cdk)

> CloudFront with Cognito authentication using Lambda@Edge

This construct is based on https://github.com/aws-samples/cloudfront-authorization-at-edge.

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-cloudfront-authorization
```

Python:

```bash
pip install cloudcomponents.cdk-cloudfront-authorization
```

## How to use SPA

```python
import { SpaAuthorization, SpaDistribution } from '@cloudcomponents/cdk-cloudfront-authorization';
import { Stack, StackProps, aws_cognito } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class CloudFrontAuthorizationStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const userPool = new aws_cognito.UserPool(this, 'UserPool', {
      selfSignUpEnabled: false,
      userPoolName: 'cloudfront-authorization-userpool',
    });

    // UserPool must have a domain!
    userPool.addDomain('Domain', {
      cognitoDomain: {
        domainPrefix: 'cloudcomponents',
      },
    });

    const authorization = new SpaAuthorization(this, 'Authorization', {
      userPool,
    });

    new SpaDistribution(this, 'Distribution', {
      authorization,
    });
  }
}
```

## How to use StaticSite

```python
import { SpaAuthorization, SpaDistribution } from '@cloudcomponents/cdk-cloudfront-authorization';
import { Stack, StackProps, aws_cognito } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class CloudFrontAuthorizationStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const userPool = new aws_cognito.UserPool(this, 'UserPool', {
      selfSignUpEnabled: false,
      userPoolName: 'cloudfront-authorization-userpool',
    });

    // UserPool must have a domain!
    userPool.addDomain('Domain', {
      cognitoDomain: {
        domainPrefix: 'cloudcomponents',
      },
    });

    const authorization = new StaticSiteAuthorization(this, 'Authorization', {
      userPool,
    });

    new StaticSiteDistribution(this, 'Distribution', {
      authorization,
    });
  }
}
```

## Identity Providers

Identity providers can be specified in the authorization object. To make sure that the user pool client is created after the identity provider, please specify a dependency using "addDependency".

```python
const identityProvider = UserPoolIdentityProviderAmazon(this, "IdentityProvider", {
  // ...
})
const authorization = new SpaAuthorization(this, 'Authorization_SPA', {
  // ...
  identityProviders: [cognito.UserPoolClientIdentityProvider.AMAZON],
};
authorization.userPoolClient.node.addDependency(identityProvider);
```

## SPA mode vs. Static Site mode

### SPA

* User Pool client does not use a client secret
* The cookies with JWT's are not "http only", so that they can be read and used by the SPA (e.g. to display the user name, or to refresh tokens)
* 404's (page not found on S3) will return index.html, to enable SPA-routing

### Static Site

* Enforce use of a client secret
* Set cookies to be http only by default (unless you've provided other cookie settings explicitly)
* No special error handling

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-cloudfront-authorization/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-cloudfront-authorization/LICENSE)
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
import aws_cdk.aws_certificatemanager as _aws_cdk_aws_certificatemanager_ceddda9d
import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_ceddda9d
import aws_cdk.aws_cognito as _aws_cdk_aws_cognito_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import cloudcomponents.cdk_lambda_at_edge_pattern as _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101
import constructs as _constructs_77d1e7e8


class AuthFlow(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.AuthFlow",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cognito_auth_domain: builtins.str,
        cookie_settings: typing.Mapping[builtins.str, builtins.str],
        log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
        nonce_signing_secret: builtins.str,
        oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
        redirect_paths: typing.Union["RedirectPaths", typing.Dict[builtins.str, typing.Any]],
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
        client_secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cognito_auth_domain: -
        :param cookie_settings: -
        :param log_level: -
        :param nonce_signing_secret: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param user_pool: -
        :param user_pool_client: -
        :param client_secret: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ee32de3f57deb4b774ba7debdcd7fc50616e8dc156d0bbdcf29510bc2d2c84)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AuthFlowProps(
            cognito_auth_domain=cognito_auth_domain,
            cookie_settings=cookie_settings,
            log_level=log_level,
            nonce_signing_secret=nonce_signing_secret,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            user_pool=user_pool,
            user_pool_client=user_pool_client,
            client_secret=client_secret,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="checkAuth")
    def check_auth(
        self,
    ) -> _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction:
        return typing.cast(_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction, jsii.get(self, "checkAuth"))

    @builtins.property
    @jsii.member(jsii_name="parseAuth")
    def parse_auth(
        self,
    ) -> _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction:
        return typing.cast(_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction, jsii.get(self, "parseAuth"))

    @builtins.property
    @jsii.member(jsii_name="refreshAuth")
    def refresh_auth(
        self,
    ) -> _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction:
        return typing.cast(_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction, jsii.get(self, "refreshAuth"))

    @builtins.property
    @jsii.member(jsii_name="signOut")
    def sign_out(
        self,
    ) -> _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction:
        return typing.cast(_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.EdgeFunction, jsii.get(self, "signOut"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.AuthFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "cognito_auth_domain": "cognitoAuthDomain",
        "cookie_settings": "cookieSettings",
        "log_level": "logLevel",
        "nonce_signing_secret": "nonceSigningSecret",
        "oauth_scopes": "oauthScopes",
        "redirect_paths": "redirectPaths",
        "user_pool": "userPool",
        "user_pool_client": "userPoolClient",
        "client_secret": "clientSecret",
    },
)
class AuthFlowProps:
    def __init__(
        self,
        *,
        cognito_auth_domain: builtins.str,
        cookie_settings: typing.Mapping[builtins.str, builtins.str],
        log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
        nonce_signing_secret: builtins.str,
        oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
        redirect_paths: typing.Union["RedirectPaths", typing.Dict[builtins.str, typing.Any]],
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
        client_secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cognito_auth_domain: -
        :param cookie_settings: -
        :param log_level: -
        :param nonce_signing_secret: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param user_pool: -
        :param user_pool_client: -
        :param client_secret: -
        '''
        if isinstance(redirect_paths, dict):
            redirect_paths = RedirectPaths(**redirect_paths)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1002aaae28fe87a2e0c53bb479cbed9bef9257d6af80171919f9ebcebd0d328a)
            check_type(argname="argument cognito_auth_domain", value=cognito_auth_domain, expected_type=type_hints["cognito_auth_domain"])
            check_type(argname="argument cookie_settings", value=cookie_settings, expected_type=type_hints["cookie_settings"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument nonce_signing_secret", value=nonce_signing_secret, expected_type=type_hints["nonce_signing_secret"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument redirect_paths", value=redirect_paths, expected_type=type_hints["redirect_paths"])
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument user_pool_client", value=user_pool_client, expected_type=type_hints["user_pool_client"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cognito_auth_domain": cognito_auth_domain,
            "cookie_settings": cookie_settings,
            "log_level": log_level,
            "nonce_signing_secret": nonce_signing_secret,
            "oauth_scopes": oauth_scopes,
            "redirect_paths": redirect_paths,
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret

    @builtins.property
    def cognito_auth_domain(self) -> builtins.str:
        result = self._values.get("cognito_auth_domain")
        assert result is not None, "Required property 'cognito_auth_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cookie_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        result = self._values.get("cookie_settings")
        assert result is not None, "Required property 'cookie_settings' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def log_level(
        self,
    ) -> _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel:
        result = self._values.get("log_level")
        assert result is not None, "Required property 'log_level' is missing"
        return typing.cast(_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel, result)

    @builtins.property
    def nonce_signing_secret(self) -> builtins.str:
        result = self._values.get("nonce_signing_secret")
        assert result is not None, "Required property 'nonce_signing_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_scopes(self) -> typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]:
        result = self._values.get("oauth_scopes")
        assert result is not None, "Required property 'oauth_scopes' is missing"
        return typing.cast(typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope], result)

    @builtins.property
    def redirect_paths(self) -> "RedirectPaths":
        result = self._values.get("redirect_paths")
        assert result is not None, "Required property 'redirect_paths' is missing"
        return typing.cast("RedirectPaths", result)

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, result)

    @builtins.property
    def user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        result = self._values.get("user_pool_client")
        assert result is not None, "Required property 'user_pool_client' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Authorization(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.Authorization",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
        log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
        oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
        redirect_paths: typing.Optional[typing.Union["RedirectPaths", typing.Dict[builtins.str, typing.Any]]] = None,
        security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
        sign_out_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param user_pool: -
        :param cookie_settings: -
        :param custom_headers: -
        :param identity_providers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param security_headers_behavior: -
        :param sign_out_url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7077620d622b3d4c8ab6e8a3140f5822f254c95899b11a0a7e7c2ff153a9812)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AuthorizationProps(
            user_pool=user_pool,
            cookie_settings=cookie_settings,
            custom_headers=custom_headers,
            identity_providers=identity_providers,
            log_level=log_level,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            security_headers_behavior=security_headers_behavior,
            sign_out_url=sign_out_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createAdditionalBehaviors")
    def create_additional_behaviors(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        *,
        allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
        cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
        cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
        function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
        origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
        realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
        response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
    ) -> typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]:
        '''
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param realtime_log_config: The real-time log configuration to be attached to this cache behavior. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64c663f49bd9c434f939a70a9de23520f14ab2e12021ae28168a0f7020c8f9bd)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        options = _aws_cdk_aws_cloudfront_ceddda9d.AddBehaviorOptions(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            cache_policy=cache_policy,
            compress=compress,
            edge_lambdas=edge_lambdas,
            function_associations=function_associations,
            origin_request_policy=origin_request_policy,
            realtime_log_config=realtime_log_config,
            response_headers_policy=response_headers_policy,
            smooth_streaming=smooth_streaming,
            trusted_key_groups=trusted_key_groups,
            viewer_protocol_policy=viewer_protocol_policy,
        )

        return typing.cast(typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions], jsii.invoke(self, "createAdditionalBehaviors", [origin, options]))

    @jsii.member(jsii_name="createAuthFlow")
    @abc.abstractmethod
    def _create_auth_flow(
        self,
        log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
    ) -> AuthFlow:
        '''
        :param log_level: -
        '''
        ...

    @jsii.member(jsii_name="createDefaultBehavior")
    def create_default_behavior(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        *,
        allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
        cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
        cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
        function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
        origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
        realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
        response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions:
        '''
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param realtime_log_config: The real-time log configuration to be attached to this cache behavior. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__201a9f962e826e921d390810b38a79a53b68bcbbe0c697b0258950c0cdf1e5e8)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        options = _aws_cdk_aws_cloudfront_ceddda9d.AddBehaviorOptions(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            cache_policy=cache_policy,
            compress=compress,
            edge_lambdas=edge_lambdas,
            function_associations=function_associations,
            origin_request_policy=origin_request_policy,
            realtime_log_config=realtime_log_config,
            response_headers_policy=response_headers_policy,
            smooth_streaming=smooth_streaming,
            trusted_key_groups=trusted_key_groups,
            viewer_protocol_policy=viewer_protocol_policy,
        )

        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, jsii.invoke(self, "createDefaultBehavior", [origin, options]))

    @jsii.member(jsii_name="createUserPoolClient")
    @abc.abstractmethod
    def _create_user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        ...

    @jsii.member(jsii_name="updateUserPoolClientCallbacks")
    def update_user_pool_client_callbacks(
        self,
        *,
        callback_urls: typing.Sequence[builtins.str],
        logout_urls: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        '''
        redirects = UserPoolClientCallbackUrls(
            callback_urls=callback_urls, logout_urls=logout_urls
        )

        return typing.cast(None, jsii.invoke(self, "updateUserPoolClientCallbacks", [redirects]))

    @builtins.property
    @jsii.member(jsii_name="authFlow")
    def auth_flow(self) -> AuthFlow:
        return typing.cast(AuthFlow, jsii.get(self, "authFlow"))

    @builtins.property
    @jsii.member(jsii_name="cognitoAuthDomain")
    def _cognito_auth_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cognitoAuthDomain"))

    @builtins.property
    @jsii.member(jsii_name="identityProviders")
    def _identity_providers(
        self,
    ) -> typing.List[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]:
        return typing.cast(typing.List[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider], jsii.get(self, "identityProviders"))

    @builtins.property
    @jsii.member(jsii_name="nonceSigningSecret")
    def _nonce_signing_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nonceSigningSecret"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def _oauth_scopes(self) -> typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]:
        return typing.cast(typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope], jsii.get(self, "oauthScopes"))

    @builtins.property
    @jsii.member(jsii_name="redirectPaths")
    def redirect_paths(self) -> "RedirectPaths":
        return typing.cast("RedirectPaths", jsii.get(self, "redirectPaths"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderPolicy")
    def _response_header_policy(
        self,
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy:
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy, jsii.get(self, "responseHeaderPolicy"))

    @builtins.property
    @jsii.member(jsii_name="signOutUrlPath")
    def sign_out_url_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signOutUrlPath"))

    @builtins.property
    @jsii.member(jsii_name="userPool")
    def _user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, jsii.get(self, "userPool"))

    @builtins.property
    @jsii.member(jsii_name="userPoolClient")
    def user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, jsii.get(self, "userPoolClient"))

    @builtins.property
    @jsii.member(jsii_name="cookieSettings")
    def _cookie_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "cookieSettings"))


class _AuthorizationProxy(Authorization):
    @jsii.member(jsii_name="createAuthFlow")
    def _create_auth_flow(
        self,
        log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
    ) -> AuthFlow:
        '''
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38795deefd7e892c326266825115bb98ae0a4e4de91d2748b3ee30d6b8e0fb7e)
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        return typing.cast(AuthFlow, jsii.invoke(self, "createAuthFlow", [log_level]))

    @jsii.member(jsii_name="createUserPoolClient")
    def _create_user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, jsii.invoke(self, "createUserPoolClient", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Authorization).__jsii_proxy_class__ = lambda : _AuthorizationProxy


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.AuthorizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "cookie_settings": "cookieSettings",
        "custom_headers": "customHeaders",
        "identity_providers": "identityProviders",
        "log_level": "logLevel",
        "oauth_scopes": "oauthScopes",
        "redirect_paths": "redirectPaths",
        "security_headers_behavior": "securityHeadersBehavior",
        "sign_out_url": "signOutUrl",
    },
)
class AuthorizationProps:
    def __init__(
        self,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
        log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
        oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
        redirect_paths: typing.Optional[typing.Union["RedirectPaths", typing.Dict[builtins.str, typing.Any]]] = None,
        security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
        sign_out_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param user_pool: -
        :param cookie_settings: -
        :param custom_headers: -
        :param identity_providers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param security_headers_behavior: -
        :param sign_out_url: -
        '''
        if isinstance(redirect_paths, dict):
            redirect_paths = RedirectPaths(**redirect_paths)
        if isinstance(security_headers_behavior, dict):
            security_headers_behavior = _aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior(**security_headers_behavior)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__500e8b2a19a6fa2f75fda2970001830c69473a22d165472c7e93598666261fbf)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument cookie_settings", value=cookie_settings, expected_type=type_hints["cookie_settings"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument identity_providers", value=identity_providers, expected_type=type_hints["identity_providers"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument redirect_paths", value=redirect_paths, expected_type=type_hints["redirect_paths"])
            check_type(argname="argument security_headers_behavior", value=security_headers_behavior, expected_type=type_hints["security_headers_behavior"])
            check_type(argname="argument sign_out_url", value=sign_out_url, expected_type=type_hints["sign_out_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool": user_pool,
        }
        if cookie_settings is not None:
            self._values["cookie_settings"] = cookie_settings
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if identity_providers is not None:
            self._values["identity_providers"] = identity_providers
        if log_level is not None:
            self._values["log_level"] = log_level
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if redirect_paths is not None:
            self._values["redirect_paths"] = redirect_paths
        if security_headers_behavior is not None:
            self._values["security_headers_behavior"] = security_headers_behavior
        if sign_out_url is not None:
            self._values["sign_out_url"] = sign_out_url

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, result)

    @builtins.property
    def cookie_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        result = self._values.get("cookie_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader]]:
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader]], result)

    @builtins.property
    def identity_providers(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]]:
        result = self._values.get("identity_providers")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]], result)

    @builtins.property
    def log_level(
        self,
    ) -> typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel]:
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel], result)

    @builtins.property
    def oauth_scopes(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]]:
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]], result)

    @builtins.property
    def redirect_paths(self) -> typing.Optional["RedirectPaths"]:
        result = self._values.get("redirect_paths")
        return typing.cast(typing.Optional["RedirectPaths"], result)

    @builtins.property
    def security_headers_behavior(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior]:
        result = self._values.get("security_headers_behavior")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior], result)

    @builtins.property
    def sign_out_url(self) -> typing.Optional[builtins.str]:
        result = self._values.get("sign_out_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_aws_cloudfront_ceddda9d.IDistribution)
class BaseDistribution(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.BaseDistribution",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorization: "IAuthorization",
        error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param authorization: -
        :param error_responses: -
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9af47237b87881f9e25920aac49bf4e9ced82b33a82789247906269a2b9afb64)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseDistributionProps(
            authorization=authorization,
            error_responses=error_responses,
            certificate=certificate,
            comment=comment,
            default_root_object=default_root_object,
            domain_names=domain_names,
            enabled=enabled,
            enable_ipv6=enable_ipv6,
            enable_logging=enable_logging,
            geo_restriction=geo_restriction,
            http_version=http_version,
            log_bucket=log_bucket,
            log_file_prefix=log_file_prefix,
            log_includes_cookies=log_includes_cookies,
            minimum_protocol_version=minimum_protocol_version,
            origin=origin,
            price_class=price_class,
            removal_policy=removal_policy,
            web_acl_id=web_acl_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="applyRemovalPolicy")
    def apply_removal_policy(self, policy: _aws_cdk_ceddda9d.RemovalPolicy) -> None:
        '''Apply the given removal policy to this resource.

        The Removal Policy controls what happens to this resource when it stops
        being managed by CloudFormation, either because you've removed it from the
        CDK application or because you've made a change that requires the resource
        to be replaced.

        The resource can be deleted (``RemovalPolicy.DESTROY``), or left in your AWS
        account for data recovery and cleanup later (``RemovalPolicy.RETAIN``).

        :param policy: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eaf152379a7e68a4fed275da8ee866f956447859d9492e0a732a3d3162e872f)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "applyRemovalPolicy", [policy]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        identity: _aws_cdk_aws_iam_ceddda9d.IGrantable,
        *actions: builtins.str,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''Adds an IAM policy statement associated with this distribution to an IAM principal's policy.

        :param identity: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5148c617a3cfa268364e52c0a3f592a02c678db4e6d1caad8dda743d8d74a6e7)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grant", [identity, *actions]))

    @jsii.member(jsii_name="grantCreateInvalidation")
    def grant_create_invalidation(
        self,
        identity: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''Grant to create invalidations for this bucket to an IAM principal (Role/Group/User).

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3488abcb2678b9a8b8f818e63bbd6be14050e1ec4eeba1f450a3988284f983)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grantCreateInvalidation", [identity]))

    @jsii.member(jsii_name="renderAdditionalBehaviors")
    def _render_additional_behaviors(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        authorization: "IAuthorization",
    ) -> typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]:
        '''
        :param origin: -
        :param authorization: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b735364cae2cf49671028114f0acc77565ef4d22e9aed823a0013f8a60cadb7f)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
        return typing.cast(typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions], jsii.invoke(self, "renderAdditionalBehaviors", [origin, authorization]))

    @jsii.member(jsii_name="renderDefaultBehaviour")
    def _render_default_behaviour(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        authorization: "IAuthorization",
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions:
        '''
        :param origin: -
        :param authorization: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6842593e0df22944aa745717da66252de73f6dabfdfba9202fc550bfc626d1)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, jsii.invoke(self, "renderDefaultBehaviour", [origin, authorization]))

    @builtins.property
    @jsii.member(jsii_name="distributionDomainName")
    def distribution_domain_name(self) -> builtins.str:
        '''The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.'''
        return typing.cast(builtins.str, jsii.get(self, "distributionDomainName"))

    @builtins.property
    @jsii.member(jsii_name="distributionId")
    def distribution_id(self) -> builtins.str:
        '''The distribution ID for this distribution.'''
        return typing.cast(builtins.str, jsii.get(self, "distributionId"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> _aws_cdk_ceddda9d.ResourceEnvironment:
        '''The environment this resource belongs to.

        For resources that are created and managed by the CDK
        (generally, those created by creating new class instances like Role, Bucket, etc.),
        this is always the same as the environment of the stack they belong to;
        however, for imported resources
        (those obtained from static methods like fromRoleArn, fromBucketName, etc.),
        that might be different than the stack they were imported into.
        '''
        return typing.cast(_aws_cdk_ceddda9d.ResourceEnvironment, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="stack")
    def stack(self) -> _aws_cdk_ceddda9d.Stack:
        '''The stack in which this resource is defined.'''
        return typing.cast(_aws_cdk_ceddda9d.Stack, jsii.get(self, "stack"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.CommonDistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "comment": "comment",
        "default_root_object": "defaultRootObject",
        "domain_names": "domainNames",
        "enabled": "enabled",
        "enable_ipv6": "enableIpv6",
        "enable_logging": "enableLogging",
        "geo_restriction": "geoRestriction",
        "http_version": "httpVersion",
        "log_bucket": "logBucket",
        "log_file_prefix": "logFilePrefix",
        "log_includes_cookies": "logIncludesCookies",
        "minimum_protocol_version": "minimumProtocolVersion",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "web_acl_id": "webAclId",
    },
)
class CommonDistributionProps:
    def __init__(
        self,
        *,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d2d4211da7c2a4365ee54147c7d1a0a368b498865e1ab0cb78cc910f6dc122e)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_root_object", value=default_root_object, expected_type=type_hints["default_root_object"])
            check_type(argname="argument domain_names", value=domain_names, expected_type=type_hints["domain_names"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument geo_restriction", value=geo_restriction, expected_type=type_hints["geo_restriction"])
            check_type(argname="argument http_version", value=http_version, expected_type=type_hints["http_version"])
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_file_prefix", value=log_file_prefix, expected_type=type_hints["log_file_prefix"])
            check_type(argname="argument log_includes_cookies", value=log_includes_cookies, expected_type=type_hints["log_includes_cookies"])
            check_type(argname="argument minimum_protocol_version", value=minimum_protocol_version, expected_type=type_hints["minimum_protocol_version"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument price_class", value=price_class, expected_type=type_hints["price_class"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate is not None:
            self._values["certificate"] = certificate
        if comment is not None:
            self._values["comment"] = comment
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if domain_names is not None:
            self._values["domain_names"] = domain_names
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if geo_restriction is not None:
            self._values["geo_restriction"] = geo_restriction
        if http_version is not None:
            self._values["http_version"] = http_version
        if log_bucket is not None:
            self._values["log_bucket"] = log_bucket
        if log_file_prefix is not None:
            self._values["log_file_prefix"] = log_file_prefix
        if log_includes_cookies is not None:
            self._values["log_includes_cookies"] = log_includes_cookies
        if minimum_protocol_version is not None:
            self._values["minimum_protocol_version"] = minimum_protocol_version
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate]:
        '''A certificate to associate with the distribution.

        The certificate must be located in N. Virginia (us-east-1).

        :default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments you want to include about the distribution.

        :default: - no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_object(self) -> typing.Optional[builtins.str]:
        '''The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/).

        :default: - index.html
        '''
        result = self._values.get("default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names for this distribution.

        If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name,
        you can add an alternate domain name to your distribution. If you attach a certificate to the distribution,
        you must add (at least one of) the domain names of the certificate to this list.

        :default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        '''
        result = self._values.get("domain_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable the distribution.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address.

        If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses.
        This allows viewers to submit a second request, for an IPv4 address for your distribution.

        :default: true
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_logging(self) -> typing.Optional[builtins.bool]:
        '''Enable access logging for the distribution.

        :default: - false, unless ``logBucket`` is specified.
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_restriction(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction]:
        '''Controls the countries in which your content is distributed.

        :default: - No geographic restrictions
        '''
        result = self._values.get("geo_restriction")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction], result)

    @builtins.property
    def http_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion]:
        '''Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront.

        For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI).

        :default: HttpVersion.HTTP2
        '''
        result = self._values.get("http_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion], result)

    @builtins.property
    def log_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''The Amazon S3 bucket to store the access logs in.

        :default: - A bucket is created if ``enableLogging`` is true
        '''
        result = self._values.get("log_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def log_file_prefix(self) -> typing.Optional[builtins.str]:
        '''An optional string that you want CloudFront to prefix to the access log filenames for this distribution.

        :default: - no prefix
        '''
        result = self._values.get("log_file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_includes_cookies(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether you want CloudFront to include cookies in access logs.

        :default: false
        '''
        result = self._values.get("log_includes_cookies")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimum_protocol_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol]:
        '''The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        :default: SecurityPolicyProtocol.TLS_V1_2_2019
        '''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol], result)

    @builtins.property
    def origin(self) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin]:
        '''The origin that you want CloudFront to route requests.'''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin], result)

    @builtins.property
    def price_class(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass]:
        '''The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        :default: PriceClass.PRICE_CLASS_100
        '''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''
        :default: Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def web_acl_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution.

        To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example
        ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``.
        To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``.

        :default: - No AWS Web Application Firewall web access control list (web ACL).

        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html#API_CreateDistribution_RequestParameters.
        '''
        result = self._values.get("web_acl_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.IAuthorization"
)
class IAuthorization(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="redirectPaths")
    def redirect_paths(self) -> "RedirectPaths":
        ...

    @builtins.property
    @jsii.member(jsii_name="signOutUrlPath")
    def sign_out_url_path(self) -> builtins.str:
        ...

    @jsii.member(jsii_name="createAdditionalBehaviors")
    def create_additional_behaviors(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        *,
        allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
        cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
        cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
        function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
        origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
        realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
        response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
    ) -> typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]:
        '''
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param realtime_log_config: The real-time log configuration to be attached to this cache behavior. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        ...

    @jsii.member(jsii_name="createDefaultBehavior")
    def create_default_behavior(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        *,
        allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
        cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
        cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
        function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
        origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
        realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
        response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions:
        '''
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param realtime_log_config: The real-time log configuration to be attached to this cache behavior. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        ...

    @jsii.member(jsii_name="updateUserPoolClientCallbacks")
    def update_user_pool_client_callbacks(
        self,
        *,
        callback_urls: typing.Sequence[builtins.str],
        logout_urls: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        '''
        ...


class _IAuthorizationProxy:
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-cloudfront-authorization.IAuthorization"

    @builtins.property
    @jsii.member(jsii_name="redirectPaths")
    def redirect_paths(self) -> "RedirectPaths":
        return typing.cast("RedirectPaths", jsii.get(self, "redirectPaths"))

    @builtins.property
    @jsii.member(jsii_name="signOutUrlPath")
    def sign_out_url_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signOutUrlPath"))

    @jsii.member(jsii_name="createAdditionalBehaviors")
    def create_additional_behaviors(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        *,
        allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
        cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
        cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
        function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
        origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
        realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
        response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
    ) -> typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]:
        '''
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param realtime_log_config: The real-time log configuration to be attached to this cache behavior. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd6e340d7380deb166246717ce51aae4d72535d1c4b1af8f856a90a544cfaba)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        options = _aws_cdk_aws_cloudfront_ceddda9d.AddBehaviorOptions(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            cache_policy=cache_policy,
            compress=compress,
            edge_lambdas=edge_lambdas,
            function_associations=function_associations,
            origin_request_policy=origin_request_policy,
            realtime_log_config=realtime_log_config,
            response_headers_policy=response_headers_policy,
            smooth_streaming=smooth_streaming,
            trusted_key_groups=trusted_key_groups,
            viewer_protocol_policy=viewer_protocol_policy,
        )

        return typing.cast(typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions], jsii.invoke(self, "createAdditionalBehaviors", [origin, options]))

    @jsii.member(jsii_name="createDefaultBehavior")
    def create_default_behavior(
        self,
        origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
        *,
        allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
        cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
        cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
        compress: typing.Optional[builtins.bool] = None,
        edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
        function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
        origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
        realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
        response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
        smooth_streaming: typing.Optional[builtins.bool] = None,
        trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
        viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions:
        '''
        :param origin: -
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param cache_policy: The cache policy for this behavior. The cache policy determines what values are included in the cache key, and the time-to-live (TTL) values for the cache. Default: CachePolicy.CACHING_OPTIMIZED
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: true
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param function_associations: The CloudFront functions to invoke before serving the contents. Default: - no functions will be invoked
        :param origin_request_policy: The origin request policy for this behavior. The origin request policy determines which values (e.g., headers, cookies) are included in requests that CloudFront sends to the origin. Default: - none
        :param realtime_log_config: The real-time log configuration to be attached to this cache behavior. Default: - none
        :param response_headers_policy: The response headers policy for this behavior. The response headers policy determines which headers are included in responses Default: - none
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param trusted_key_groups: A list of Key Groups that CloudFront can use to validate signed URLs or signed cookies. Default: - no KeyGroups are associated with cache behavior
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d24f79512286a186b1a282bd9bef52ed8f14ae0eb64b254832b0441a0338a280)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        options = _aws_cdk_aws_cloudfront_ceddda9d.AddBehaviorOptions(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            cache_policy=cache_policy,
            compress=compress,
            edge_lambdas=edge_lambdas,
            function_associations=function_associations,
            origin_request_policy=origin_request_policy,
            realtime_log_config=realtime_log_config,
            response_headers_policy=response_headers_policy,
            smooth_streaming=smooth_streaming,
            trusted_key_groups=trusted_key_groups,
            viewer_protocol_policy=viewer_protocol_policy,
        )

        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, jsii.invoke(self, "createDefaultBehavior", [origin, options]))

    @jsii.member(jsii_name="updateUserPoolClientCallbacks")
    def update_user_pool_client_callbacks(
        self,
        *,
        callback_urls: typing.Sequence[builtins.str],
        logout_urls: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        '''
        redirects = UserPoolClientCallbackUrls(
            callback_urls=callback_urls, logout_urls=logout_urls
        )

        return typing.cast(None, jsii.invoke(self, "updateUserPoolClientCallbacks", [redirects]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorization).__jsii_proxy_class__ = lambda : _IAuthorizationProxy


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.ISpaAuthorization"
)
class ISpaAuthorization(IAuthorization, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        ...


class _ISpaAuthorizationProxy(
    jsii.proxy_for(IAuthorization), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-cloudfront-authorization.ISpaAuthorization"

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        return typing.cast("Mode", jsii.get(self, "mode"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISpaAuthorization).__jsii_proxy_class__ = lambda : _ISpaAuthorizationProxy


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.IStaticSiteAuthorization"
)
class IStaticSiteAuthorization(IAuthorization, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        ...


class _IStaticSiteAuthorizationProxy(
    jsii.proxy_for(IAuthorization), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-cloudfront-authorization.IStaticSiteAuthorization"

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "Mode":
        return typing.cast("Mode", jsii.get(self, "mode"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStaticSiteAuthorization).__jsii_proxy_class__ = lambda : _IStaticSiteAuthorizationProxy


@jsii.enum(jsii_type="@cloudcomponents/cdk-cloudfront-authorization.Mode")
class Mode(enum.Enum):
    SPA = "SPA"
    STATIC_SITE = "STATIC_SITE"


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.RedirectPaths",
    jsii_struct_bases=[],
    name_mapping={
        "auth_refresh": "authRefresh",
        "sign_in": "signIn",
        "sign_out": "signOut",
    },
)
class RedirectPaths:
    def __init__(
        self,
        *,
        auth_refresh: builtins.str,
        sign_in: builtins.str,
        sign_out: builtins.str,
    ) -> None:
        '''
        :param auth_refresh: -
        :param sign_in: -
        :param sign_out: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f63907758ab50698a779728a546d1c91b7f5349800a9a88ac7660a584bbb3c)
            check_type(argname="argument auth_refresh", value=auth_refresh, expected_type=type_hints["auth_refresh"])
            check_type(argname="argument sign_in", value=sign_in, expected_type=type_hints["sign_in"])
            check_type(argname="argument sign_out", value=sign_out, expected_type=type_hints["sign_out"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_refresh": auth_refresh,
            "sign_in": sign_in,
            "sign_out": sign_out,
        }

    @builtins.property
    def auth_refresh(self) -> builtins.str:
        result = self._values.get("auth_refresh")
        assert result is not None, "Required property 'auth_refresh' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sign_in(self) -> builtins.str:
        result = self._values.get("sign_in")
        assert result is not None, "Required property 'sign_in' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sign_out(self) -> builtins.str:
        result = self._values.get("sign_out")
        assert result is not None, "Required property 'sign_out' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedirectPaths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RetrieveUserPoolClientSecret(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.RetrieveUserPoolClientSecret",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param user_pool: -
        :param user_pool_client: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__170d807b252d82b1b9b32d4f831b3477bbdbe72dca1f79451f59419a4cfcb2df)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RetrieveUserPoolClientSecretProps(
            user_pool=user_pool, user_pool_client=user_pool_client
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97830b045d238d0b8d131ab167575d8d0f2d8826c91f48cbddf9f3e7246c0cc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.RetrieveUserPoolClientSecretProps",
    jsii_struct_bases=[],
    name_mapping={"user_pool": "userPool", "user_pool_client": "userPoolClient"},
)
class RetrieveUserPoolClientSecretProps:
    def __init__(
        self,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
    ) -> None:
        '''
        :param user_pool: -
        :param user_pool_client: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb3ceaa6da908543d0a9def8ca4352880f31088af631c862c816717e7a936f2)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument user_pool_client", value=user_pool_client, expected_type=type_hints["user_pool_client"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
        }

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, result)

    @builtins.property
    def user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        result = self._values.get("user_pool_client")
        assert result is not None, "Required property 'user_pool_client' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RetrieveUserPoolClientSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretGenerator(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SecretGenerator",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        allowed_characters: typing.Optional[builtins.str] = None,
        length: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allowed_characters: -
        :param length: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__896a5ca8bbc3b7d8b94abb8b9f94ca4bcdb9a6a2c522ac7a202e172e0ffcacec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SecretGeneratorProps(
            allowed_characters=allowed_characters, length=length
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SecretGeneratorProps",
    jsii_struct_bases=[],
    name_mapping={"allowed_characters": "allowedCharacters", "length": "length"},
)
class SecretGeneratorProps:
    def __init__(
        self,
        *,
        allowed_characters: typing.Optional[builtins.str] = None,
        length: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allowed_characters: -
        :param length: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc4b1455fc78cfc610c85420cf64186223aae30560816f9f944b0f1f83bbbee8)
            check_type(argname="argument allowed_characters", value=allowed_characters, expected_type=type_hints["allowed_characters"])
            check_type(argname="argument length", value=length, expected_type=type_hints["length"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_characters is not None:
            self._values["allowed_characters"] = allowed_characters
        if length is not None:
            self._values["length"] = length

    @builtins.property
    def allowed_characters(self) -> typing.Optional[builtins.str]:
        result = self._values.get("allowed_characters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def length(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("length")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretGeneratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISpaAuthorization)
class SpaAuthorization(
    Authorization,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SpaAuthorization",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
        log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
        oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
        redirect_paths: typing.Optional[typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]]] = None,
        security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
        sign_out_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param user_pool: -
        :param cookie_settings: -
        :param custom_headers: -
        :param identity_providers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param security_headers_behavior: -
        :param sign_out_url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d7d404060a09a65f73fd33694e859d9dd781df10f45dafaba01780db0ec396)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AuthorizationProps(
            user_pool=user_pool,
            cookie_settings=cookie_settings,
            custom_headers=custom_headers,
            identity_providers=identity_providers,
            log_level=log_level,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            security_headers_behavior=security_headers_behavior,
            sign_out_url=sign_out_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createAuthFlow")
    def _create_auth_flow(
        self,
        log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
    ) -> AuthFlow:
        '''
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__610c4da44720c57febe62b8eeb0f79f53522bc3e7705affcc998fd6d1a8cc0bf)
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        return typing.cast(AuthFlow, jsii.invoke(self, "createAuthFlow", [log_level]))

    @jsii.member(jsii_name="createUserPoolClient")
    def _create_user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, jsii.invoke(self, "createUserPoolClient", []))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> Mode:
        return typing.cast(Mode, jsii.get(self, "mode"))


class SpaDistribution(
    BaseDistribution,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SpaDistribution",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorization: ISpaAuthorization,
        ttl: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param authorization: -
        :param ttl: The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode. Default: 300 seconds
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e241ddf633750acd88125d1e5601ba48d5596b5f903193d4392fed59ffba9a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SpaDistributionProps(
            authorization=authorization,
            ttl=ttl,
            certificate=certificate,
            comment=comment,
            default_root_object=default_root_object,
            domain_names=domain_names,
            enabled=enabled,
            enable_ipv6=enable_ipv6,
            enable_logging=enable_logging,
            geo_restriction=geo_restriction,
            http_version=http_version,
            log_bucket=log_bucket,
            log_file_prefix=log_file_prefix,
            log_includes_cookies=log_includes_cookies,
            minimum_protocol_version=minimum_protocol_version,
            origin=origin,
            price_class=price_class,
            removal_policy=removal_policy,
            web_acl_id=web_acl_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.SpaDistributionProps",
    jsii_struct_bases=[CommonDistributionProps],
    name_mapping={
        "certificate": "certificate",
        "comment": "comment",
        "default_root_object": "defaultRootObject",
        "domain_names": "domainNames",
        "enabled": "enabled",
        "enable_ipv6": "enableIpv6",
        "enable_logging": "enableLogging",
        "geo_restriction": "geoRestriction",
        "http_version": "httpVersion",
        "log_bucket": "logBucket",
        "log_file_prefix": "logFilePrefix",
        "log_includes_cookies": "logIncludesCookies",
        "minimum_protocol_version": "minimumProtocolVersion",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "web_acl_id": "webAclId",
        "authorization": "authorization",
        "ttl": "ttl",
    },
)
class SpaDistributionProps(CommonDistributionProps):
    def __init__(
        self,
        *,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
        authorization: ISpaAuthorization,
        ttl: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ) -> None:
        '''
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        :param authorization: -
        :param ttl: The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode. Default: 300 seconds
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f9064ef0fc8e2acdb5387c77835361e50d477c8dbdb2dfcf7d01baae67a6ded)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_root_object", value=default_root_object, expected_type=type_hints["default_root_object"])
            check_type(argname="argument domain_names", value=domain_names, expected_type=type_hints["domain_names"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument geo_restriction", value=geo_restriction, expected_type=type_hints["geo_restriction"])
            check_type(argname="argument http_version", value=http_version, expected_type=type_hints["http_version"])
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_file_prefix", value=log_file_prefix, expected_type=type_hints["log_file_prefix"])
            check_type(argname="argument log_includes_cookies", value=log_includes_cookies, expected_type=type_hints["log_includes_cookies"])
            check_type(argname="argument minimum_protocol_version", value=minimum_protocol_version, expected_type=type_hints["minimum_protocol_version"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument price_class", value=price_class, expected_type=type_hints["price_class"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization": authorization,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if comment is not None:
            self._values["comment"] = comment
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if domain_names is not None:
            self._values["domain_names"] = domain_names
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if geo_restriction is not None:
            self._values["geo_restriction"] = geo_restriction
        if http_version is not None:
            self._values["http_version"] = http_version
        if log_bucket is not None:
            self._values["log_bucket"] = log_bucket
        if log_file_prefix is not None:
            self._values["log_file_prefix"] = log_file_prefix
        if log_includes_cookies is not None:
            self._values["log_includes_cookies"] = log_includes_cookies
        if minimum_protocol_version is not None:
            self._values["minimum_protocol_version"] = minimum_protocol_version
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate]:
        '''A certificate to associate with the distribution.

        The certificate must be located in N. Virginia (us-east-1).

        :default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments you want to include about the distribution.

        :default: - no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_object(self) -> typing.Optional[builtins.str]:
        '''The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/).

        :default: - index.html
        '''
        result = self._values.get("default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names for this distribution.

        If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name,
        you can add an alternate domain name to your distribution. If you attach a certificate to the distribution,
        you must add (at least one of) the domain names of the certificate to this list.

        :default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        '''
        result = self._values.get("domain_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable the distribution.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address.

        If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses.
        This allows viewers to submit a second request, for an IPv4 address for your distribution.

        :default: true
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_logging(self) -> typing.Optional[builtins.bool]:
        '''Enable access logging for the distribution.

        :default: - false, unless ``logBucket`` is specified.
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_restriction(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction]:
        '''Controls the countries in which your content is distributed.

        :default: - No geographic restrictions
        '''
        result = self._values.get("geo_restriction")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction], result)

    @builtins.property
    def http_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion]:
        '''Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront.

        For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI).

        :default: HttpVersion.HTTP2
        '''
        result = self._values.get("http_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion], result)

    @builtins.property
    def log_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''The Amazon S3 bucket to store the access logs in.

        :default: - A bucket is created if ``enableLogging`` is true
        '''
        result = self._values.get("log_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def log_file_prefix(self) -> typing.Optional[builtins.str]:
        '''An optional string that you want CloudFront to prefix to the access log filenames for this distribution.

        :default: - no prefix
        '''
        result = self._values.get("log_file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_includes_cookies(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether you want CloudFront to include cookies in access logs.

        :default: false
        '''
        result = self._values.get("log_includes_cookies")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimum_protocol_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol]:
        '''The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        :default: SecurityPolicyProtocol.TLS_V1_2_2019
        '''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol], result)

    @builtins.property
    def origin(self) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin]:
        '''The origin that you want CloudFront to route requests.'''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin], result)

    @builtins.property
    def price_class(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass]:
        '''The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        :default: PriceClass.PRICE_CLASS_100
        '''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''
        :default: Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def web_acl_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution.

        To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example
        ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``.
        To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``.

        :default: - No AWS Web Application Firewall web access control list (web ACL).

        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html#API_CreateDistribution_RequestParameters.
        '''
        result = self._values.get("web_acl_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorization(self) -> ISpaAuthorization:
        result = self._values.get("authorization")
        assert result is not None, "Required property 'authorization' is missing"
        return typing.cast(ISpaAuthorization, result)

    @builtins.property
    def ttl(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode.

        :default: 300 seconds
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpaDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStaticSiteAuthorization)
class StaticSiteAuthorization(
    Authorization,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.StaticSiteAuthorization",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
        log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
        oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
        redirect_paths: typing.Optional[typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]]] = None,
        security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
        sign_out_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param user_pool: -
        :param cookie_settings: -
        :param custom_headers: -
        :param identity_providers: -
        :param log_level: -
        :param oauth_scopes: -
        :param redirect_paths: -
        :param security_headers_behavior: -
        :param sign_out_url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d404ed40edee2aae263b7107fe9c8182cf5b8f59de5dec2994c5a2a49b5974)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AuthorizationProps(
            user_pool=user_pool,
            cookie_settings=cookie_settings,
            custom_headers=custom_headers,
            identity_providers=identity_providers,
            log_level=log_level,
            oauth_scopes=oauth_scopes,
            redirect_paths=redirect_paths,
            security_headers_behavior=security_headers_behavior,
            sign_out_url=sign_out_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createAuthFlow")
    def _create_auth_flow(
        self,
        log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
    ) -> AuthFlow:
        '''
        :param log_level: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d38bd88ce93edf4d7f9696bdd32e538851a103fbbcc852151f5d93b26ba876)
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
        return typing.cast(AuthFlow, jsii.invoke(self, "createAuthFlow", [log_level]))

    @jsii.member(jsii_name="createUserPoolClient")
    def _create_user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, jsii.invoke(self, "createUserPoolClient", []))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> Mode:
        return typing.cast(Mode, jsii.get(self, "mode"))


class StaticSiteDistribution(
    BaseDistribution,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.StaticSiteDistribution",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorization: IStaticSiteAuthorization,
        error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param authorization: -
        :param error_responses: -
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c52404d6cd363e8ec929d36d264abb1ed9dd25e10f99559ae3c432fb8ae88c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StaticSiteDistributionProps(
            authorization=authorization,
            error_responses=error_responses,
            certificate=certificate,
            comment=comment,
            default_root_object=default_root_object,
            domain_names=domain_names,
            enabled=enabled,
            enable_ipv6=enable_ipv6,
            enable_logging=enable_logging,
            geo_restriction=geo_restriction,
            http_version=http_version,
            log_bucket=log_bucket,
            log_file_prefix=log_file_prefix,
            log_includes_cookies=log_includes_cookies,
            minimum_protocol_version=minimum_protocol_version,
            origin=origin,
            price_class=price_class,
            removal_policy=removal_policy,
            web_acl_id=web_acl_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.StaticSiteDistributionProps",
    jsii_struct_bases=[CommonDistributionProps],
    name_mapping={
        "certificate": "certificate",
        "comment": "comment",
        "default_root_object": "defaultRootObject",
        "domain_names": "domainNames",
        "enabled": "enabled",
        "enable_ipv6": "enableIpv6",
        "enable_logging": "enableLogging",
        "geo_restriction": "geoRestriction",
        "http_version": "httpVersion",
        "log_bucket": "logBucket",
        "log_file_prefix": "logFilePrefix",
        "log_includes_cookies": "logIncludesCookies",
        "minimum_protocol_version": "minimumProtocolVersion",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "web_acl_id": "webAclId",
        "authorization": "authorization",
        "error_responses": "errorResponses",
    },
)
class StaticSiteDistributionProps(CommonDistributionProps):
    def __init__(
        self,
        *,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
        authorization: IStaticSiteAuthorization,
        error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        :param authorization: -
        :param error_responses: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5202e16cdcc711fbfddb991d7f5f345254b76a15f659e0f12cd135a2e3be4c9)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_root_object", value=default_root_object, expected_type=type_hints["default_root_object"])
            check_type(argname="argument domain_names", value=domain_names, expected_type=type_hints["domain_names"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument geo_restriction", value=geo_restriction, expected_type=type_hints["geo_restriction"])
            check_type(argname="argument http_version", value=http_version, expected_type=type_hints["http_version"])
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_file_prefix", value=log_file_prefix, expected_type=type_hints["log_file_prefix"])
            check_type(argname="argument log_includes_cookies", value=log_includes_cookies, expected_type=type_hints["log_includes_cookies"])
            check_type(argname="argument minimum_protocol_version", value=minimum_protocol_version, expected_type=type_hints["minimum_protocol_version"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument price_class", value=price_class, expected_type=type_hints["price_class"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument error_responses", value=error_responses, expected_type=type_hints["error_responses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization": authorization,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if comment is not None:
            self._values["comment"] = comment
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if domain_names is not None:
            self._values["domain_names"] = domain_names
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if geo_restriction is not None:
            self._values["geo_restriction"] = geo_restriction
        if http_version is not None:
            self._values["http_version"] = http_version
        if log_bucket is not None:
            self._values["log_bucket"] = log_bucket
        if log_file_prefix is not None:
            self._values["log_file_prefix"] = log_file_prefix
        if log_includes_cookies is not None:
            self._values["log_includes_cookies"] = log_includes_cookies
        if minimum_protocol_version is not None:
            self._values["minimum_protocol_version"] = minimum_protocol_version
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id
        if error_responses is not None:
            self._values["error_responses"] = error_responses

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate]:
        '''A certificate to associate with the distribution.

        The certificate must be located in N. Virginia (us-east-1).

        :default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments you want to include about the distribution.

        :default: - no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_object(self) -> typing.Optional[builtins.str]:
        '''The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/).

        :default: - index.html
        '''
        result = self._values.get("default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names for this distribution.

        If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name,
        you can add an alternate domain name to your distribution. If you attach a certificate to the distribution,
        you must add (at least one of) the domain names of the certificate to this list.

        :default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        '''
        result = self._values.get("domain_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable the distribution.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address.

        If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses.
        This allows viewers to submit a second request, for an IPv4 address for your distribution.

        :default: true
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_logging(self) -> typing.Optional[builtins.bool]:
        '''Enable access logging for the distribution.

        :default: - false, unless ``logBucket`` is specified.
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_restriction(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction]:
        '''Controls the countries in which your content is distributed.

        :default: - No geographic restrictions
        '''
        result = self._values.get("geo_restriction")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction], result)

    @builtins.property
    def http_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion]:
        '''Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront.

        For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI).

        :default: HttpVersion.HTTP2
        '''
        result = self._values.get("http_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion], result)

    @builtins.property
    def log_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''The Amazon S3 bucket to store the access logs in.

        :default: - A bucket is created if ``enableLogging`` is true
        '''
        result = self._values.get("log_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def log_file_prefix(self) -> typing.Optional[builtins.str]:
        '''An optional string that you want CloudFront to prefix to the access log filenames for this distribution.

        :default: - no prefix
        '''
        result = self._values.get("log_file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_includes_cookies(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether you want CloudFront to include cookies in access logs.

        :default: false
        '''
        result = self._values.get("log_includes_cookies")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimum_protocol_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol]:
        '''The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        :default: SecurityPolicyProtocol.TLS_V1_2_2019
        '''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol], result)

    @builtins.property
    def origin(self) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin]:
        '''The origin that you want CloudFront to route requests.'''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin], result)

    @builtins.property
    def price_class(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass]:
        '''The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        :default: PriceClass.PRICE_CLASS_100
        '''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''
        :default: Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def web_acl_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution.

        To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example
        ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``.
        To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``.

        :default: - No AWS Web Application Firewall web access control list (web ACL).

        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html#API_CreateDistribution_RequestParameters.
        '''
        result = self._values.get("web_acl_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorization(self) -> IStaticSiteAuthorization:
        result = self._values.get("authorization")
        assert result is not None, "Required property 'authorization' is missing"
        return typing.cast(IStaticSiteAuthorization, result)

    @builtins.property
    def error_responses(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse]]:
        result = self._values.get("error_responses")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaticSiteDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.UserPoolClientCallbackUrls",
    jsii_struct_bases=[],
    name_mapping={"callback_urls": "callbackUrls", "logout_urls": "logoutUrls"},
)
class UserPoolClientCallbackUrls:
    def __init__(
        self,
        *,
        callback_urls: typing.Sequence[builtins.str],
        logout_urls: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param callback_urls: A list of allowed redirect (callback) URLs for the identity providers.
        :param logout_urls: A list of allowed logout URLs for the identity providers.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c917dd323f8c9dd6d21b692c6a170fadf195696bdd1787f50ce6b03915c5b3cf)
            check_type(argname="argument callback_urls", value=callback_urls, expected_type=type_hints["callback_urls"])
            check_type(argname="argument logout_urls", value=logout_urls, expected_type=type_hints["logout_urls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "callback_urls": callback_urls,
            "logout_urls": logout_urls,
        }

    @builtins.property
    def callback_urls(self) -> typing.List[builtins.str]:
        '''A list of allowed redirect (callback) URLs for the identity providers.'''
        result = self._values.get("callback_urls")
        assert result is not None, "Required property 'callback_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def logout_urls(self) -> typing.List[builtins.str]:
        '''A list of allowed logout URLs for the identity providers.'''
        result = self._values.get("logout_urls")
        assert result is not None, "Required property 'logout_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolClientCallbackUrls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserPoolClientRedirects(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.UserPoolClientRedirects",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        callback_urls: typing.Sequence[builtins.str],
        identity_providers: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider],
        logout_urls: typing.Sequence[builtins.str],
        oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param callback_urls: -
        :param identity_providers: -
        :param logout_urls: -
        :param oauth_scopes: -
        :param user_pool: -
        :param user_pool_client: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bbad32d1f28a960fdff821cb2ab4f6b16a2745d8ba3f6f9679af43c8d57ca87)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = UserPoolClientRedirectsProps(
            callback_urls=callback_urls,
            identity_providers=identity_providers,
            logout_urls=logout_urls,
            oauth_scopes=oauth_scopes,
            user_pool=user_pool,
            user_pool_client=user_pool_client,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.UserPoolClientRedirectsProps",
    jsii_struct_bases=[],
    name_mapping={
        "callback_urls": "callbackUrls",
        "identity_providers": "identityProviders",
        "logout_urls": "logoutUrls",
        "oauth_scopes": "oauthScopes",
        "user_pool": "userPool",
        "user_pool_client": "userPoolClient",
    },
)
class UserPoolClientRedirectsProps:
    def __init__(
        self,
        *,
        callback_urls: typing.Sequence[builtins.str],
        identity_providers: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider],
        logout_urls: typing.Sequence[builtins.str],
        oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
    ) -> None:
        '''
        :param callback_urls: -
        :param identity_providers: -
        :param logout_urls: -
        :param oauth_scopes: -
        :param user_pool: -
        :param user_pool_client: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f80524222ee747484f32ae51b81bf1253fa9d67c400f31876cc94770679fa0)
            check_type(argname="argument callback_urls", value=callback_urls, expected_type=type_hints["callback_urls"])
            check_type(argname="argument identity_providers", value=identity_providers, expected_type=type_hints["identity_providers"])
            check_type(argname="argument logout_urls", value=logout_urls, expected_type=type_hints["logout_urls"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument user_pool_client", value=user_pool_client, expected_type=type_hints["user_pool_client"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "callback_urls": callback_urls,
            "identity_providers": identity_providers,
            "logout_urls": logout_urls,
            "oauth_scopes": oauth_scopes,
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
        }

    @builtins.property
    def callback_urls(self) -> typing.List[builtins.str]:
        result = self._values.get("callback_urls")
        assert result is not None, "Required property 'callback_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def identity_providers(
        self,
    ) -> typing.List[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]:
        result = self._values.get("identity_providers")
        assert result is not None, "Required property 'identity_providers' is missing"
        return typing.cast(typing.List[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider], result)

    @builtins.property
    def logout_urls(self) -> typing.List[builtins.str]:
        result = self._values.get("logout_urls")
        assert result is not None, "Required property 'logout_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]:
        result = self._values.get("oauth_scopes")
        assert result is not None, "Required property 'oauth_scopes' is missing"
        return typing.cast(typing.List[_aws_cdk_aws_cognito_ceddda9d.OAuthScope], result)

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, result)

    @builtins.property
    def user_pool_client(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient:
        result = self._values.get("user_pool_client")
        assert result is not None, "Required property 'user_pool_client' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPoolClient, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolClientRedirectsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-cloudfront-authorization.BaseDistributionProps",
    jsii_struct_bases=[CommonDistributionProps],
    name_mapping={
        "certificate": "certificate",
        "comment": "comment",
        "default_root_object": "defaultRootObject",
        "domain_names": "domainNames",
        "enabled": "enabled",
        "enable_ipv6": "enableIpv6",
        "enable_logging": "enableLogging",
        "geo_restriction": "geoRestriction",
        "http_version": "httpVersion",
        "log_bucket": "logBucket",
        "log_file_prefix": "logFilePrefix",
        "log_includes_cookies": "logIncludesCookies",
        "minimum_protocol_version": "minimumProtocolVersion",
        "origin": "origin",
        "price_class": "priceClass",
        "removal_policy": "removalPolicy",
        "web_acl_id": "webAclId",
        "authorization": "authorization",
        "error_responses": "errorResponses",
    },
)
class BaseDistributionProps(CommonDistributionProps):
    def __init__(
        self,
        *,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
        authorization: IAuthorization,
        error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - index.html
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: SecurityPolicyProtocol.TLS_V1_2_2019
        :param origin: The origin that you want CloudFront to route requests.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_100
        :param removal_policy: Default: Destroy
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        :param authorization: -
        :param error_responses: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f058c58bca699c44c339a580b6ad5ace3c595e45d67277ace583aa6f34b993c9)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_root_object", value=default_root_object, expected_type=type_hints["default_root_object"])
            check_type(argname="argument domain_names", value=domain_names, expected_type=type_hints["domain_names"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument geo_restriction", value=geo_restriction, expected_type=type_hints["geo_restriction"])
            check_type(argname="argument http_version", value=http_version, expected_type=type_hints["http_version"])
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_file_prefix", value=log_file_prefix, expected_type=type_hints["log_file_prefix"])
            check_type(argname="argument log_includes_cookies", value=log_includes_cookies, expected_type=type_hints["log_includes_cookies"])
            check_type(argname="argument minimum_protocol_version", value=minimum_protocol_version, expected_type=type_hints["minimum_protocol_version"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument price_class", value=price_class, expected_type=type_hints["price_class"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument error_responses", value=error_responses, expected_type=type_hints["error_responses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization": authorization,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if comment is not None:
            self._values["comment"] = comment
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if domain_names is not None:
            self._values["domain_names"] = domain_names
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if geo_restriction is not None:
            self._values["geo_restriction"] = geo_restriction
        if http_version is not None:
            self._values["http_version"] = http_version
        if log_bucket is not None:
            self._values["log_bucket"] = log_bucket
        if log_file_prefix is not None:
            self._values["log_file_prefix"] = log_file_prefix
        if log_includes_cookies is not None:
            self._values["log_includes_cookies"] = log_includes_cookies
        if minimum_protocol_version is not None:
            self._values["minimum_protocol_version"] = minimum_protocol_version
        if origin is not None:
            self._values["origin"] = origin
        if price_class is not None:
            self._values["price_class"] = price_class
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id
        if error_responses is not None:
            self._values["error_responses"] = error_responses

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate]:
        '''A certificate to associate with the distribution.

        The certificate must be located in N. Virginia (us-east-1).

        :default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments you want to include about the distribution.

        :default: - no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_object(self) -> typing.Optional[builtins.str]:
        '''The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/).

        :default: - index.html
        '''
        result = self._values.get("default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names for this distribution.

        If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name,
        you can add an alternate domain name to your distribution. If you attach a certificate to the distribution,
        you must add (at least one of) the domain names of the certificate to this list.

        :default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        '''
        result = self._values.get("domain_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable the distribution.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address.

        If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses.
        This allows viewers to submit a second request, for an IPv4 address for your distribution.

        :default: true
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_logging(self) -> typing.Optional[builtins.bool]:
        '''Enable access logging for the distribution.

        :default: - false, unless ``logBucket`` is specified.
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_restriction(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction]:
        '''Controls the countries in which your content is distributed.

        :default: - No geographic restrictions
        '''
        result = self._values.get("geo_restriction")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction], result)

    @builtins.property
    def http_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion]:
        '''Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront.

        For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI).

        :default: HttpVersion.HTTP2
        '''
        result = self._values.get("http_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion], result)

    @builtins.property
    def log_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''The Amazon S3 bucket to store the access logs in.

        :default: - A bucket is created if ``enableLogging`` is true
        '''
        result = self._values.get("log_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def log_file_prefix(self) -> typing.Optional[builtins.str]:
        '''An optional string that you want CloudFront to prefix to the access log filenames for this distribution.

        :default: - no prefix
        '''
        result = self._values.get("log_file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_includes_cookies(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether you want CloudFront to include cookies in access logs.

        :default: false
        '''
        result = self._values.get("log_includes_cookies")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimum_protocol_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol]:
        '''The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        :default: SecurityPolicyProtocol.TLS_V1_2_2019
        '''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol], result)

    @builtins.property
    def origin(self) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin]:
        '''The origin that you want CloudFront to route requests.'''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin], result)

    @builtins.property
    def price_class(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass]:
        '''The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        :default: PriceClass.PRICE_CLASS_100
        '''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''
        :default: Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def web_acl_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution.

        To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example
        ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``.
        To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``.

        :default: - No AWS Web Application Firewall web access control list (web ACL).

        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html#API_CreateDistribution_RequestParameters.
        '''
        result = self._values.get("web_acl_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorization(self) -> IAuthorization:
        result = self._values.get("authorization")
        assert result is not None, "Required property 'authorization' is missing"
        return typing.cast(IAuthorization, result)

    @builtins.property
    def error_responses(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse]]:
        result = self._values.get("error_responses")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthFlow",
    "AuthFlowProps",
    "Authorization",
    "AuthorizationProps",
    "BaseDistribution",
    "BaseDistributionProps",
    "CommonDistributionProps",
    "IAuthorization",
    "ISpaAuthorization",
    "IStaticSiteAuthorization",
    "Mode",
    "RedirectPaths",
    "RetrieveUserPoolClientSecret",
    "RetrieveUserPoolClientSecretProps",
    "SecretGenerator",
    "SecretGeneratorProps",
    "SpaAuthorization",
    "SpaDistribution",
    "SpaDistributionProps",
    "StaticSiteAuthorization",
    "StaticSiteDistribution",
    "StaticSiteDistributionProps",
    "UserPoolClientCallbackUrls",
    "UserPoolClientRedirects",
    "UserPoolClientRedirectsProps",
]

publication.publish()

def _typecheckingstub__28ee32de3f57deb4b774ba7debdcd7fc50616e8dc156d0bbdcf29510bc2d2c84(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cognito_auth_domain: builtins.str,
    cookie_settings: typing.Mapping[builtins.str, builtins.str],
    log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
    nonce_signing_secret: builtins.str,
    oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
    redirect_paths: typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]],
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
    client_secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1002aaae28fe87a2e0c53bb479cbed9bef9257d6af80171919f9ebcebd0d328a(
    *,
    cognito_auth_domain: builtins.str,
    cookie_settings: typing.Mapping[builtins.str, builtins.str],
    log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
    nonce_signing_secret: builtins.str,
    oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
    redirect_paths: typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]],
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
    client_secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7077620d622b3d4c8ab6e8a3140f5822f254c95899b11a0a7e7c2ff153a9812(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
    log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
    oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
    redirect_paths: typing.Optional[typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]]] = None,
    security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    sign_out_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64c663f49bd9c434f939a70a9de23520f14ab2e12021ae28168a0f7020c8f9bd(
    origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
    *,
    allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
    cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
    cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
    compress: typing.Optional[builtins.bool] = None,
    edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
    function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
    origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
    realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
    response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
    smooth_streaming: typing.Optional[builtins.bool] = None,
    trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
    viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201a9f962e826e921d390810b38a79a53b68bcbbe0c697b0258950c0cdf1e5e8(
    origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
    *,
    allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
    cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
    cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
    compress: typing.Optional[builtins.bool] = None,
    edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
    function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
    origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
    realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
    response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
    smooth_streaming: typing.Optional[builtins.bool] = None,
    trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
    viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38795deefd7e892c326266825115bb98ae0a4e4de91d2748b3ee30d6b8e0fb7e(
    log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500e8b2a19a6fa2f75fda2970001830c69473a22d165472c7e93598666261fbf(
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
    log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
    oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
    redirect_paths: typing.Optional[typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]]] = None,
    security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    sign_out_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9af47237b87881f9e25920aac49bf4e9ced82b33a82789247906269a2b9afb64(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorization: IAuthorization,
    error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eaf152379a7e68a4fed275da8ee866f956447859d9492e0a732a3d3162e872f(
    policy: _aws_cdk_ceddda9d.RemovalPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5148c617a3cfa268364e52c0a3f592a02c678db4e6d1caad8dda743d8d74a6e7(
    identity: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3488abcb2678b9a8b8f818e63bbd6be14050e1ec4eeba1f450a3988284f983(
    identity: _aws_cdk_aws_iam_ceddda9d.IGrantable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b735364cae2cf49671028114f0acc77565ef4d22e9aed823a0013f8a60cadb7f(
    origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
    authorization: IAuthorization,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6842593e0df22944aa745717da66252de73f6dabfdfba9202fc550bfc626d1(
    origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
    authorization: IAuthorization,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d2d4211da7c2a4365ee54147c7d1a0a368b498865e1ab0cb78cc910f6dc122e(
    *,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd6e340d7380deb166246717ce51aae4d72535d1c4b1af8f856a90a544cfaba(
    origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
    *,
    allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
    cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
    cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
    compress: typing.Optional[builtins.bool] = None,
    edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
    function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
    origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
    realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
    response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
    smooth_streaming: typing.Optional[builtins.bool] = None,
    trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
    viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24f79512286a186b1a282bd9bef52ed8f14ae0eb64b254832b0441a0338a280(
    origin: _aws_cdk_aws_cloudfront_ceddda9d.IOrigin,
    *,
    allowed_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.AllowedMethods] = None,
    cached_methods: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.CachedMethods] = None,
    cache_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ICachePolicy] = None,
    compress: typing.Optional[builtins.bool] = None,
    edge_lambdas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.EdgeLambda, typing.Dict[builtins.str, typing.Any]]]] = None,
    function_associations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.FunctionAssociation, typing.Dict[builtins.str, typing.Any]]]] = None,
    origin_request_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOriginRequestPolicy] = None,
    realtime_log_config: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IRealtimeLogConfig] = None,
    response_headers_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IResponseHeadersPolicy] = None,
    smooth_streaming: typing.Optional[builtins.bool] = None,
    trusted_key_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_ceddda9d.IKeyGroup]] = None,
    viewer_protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.ViewerProtocolPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f63907758ab50698a779728a546d1c91b7f5349800a9a88ac7660a584bbb3c(
    *,
    auth_refresh: builtins.str,
    sign_in: builtins.str,
    sign_out: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170d807b252d82b1b9b32d4f831b3477bbdbe72dca1f79451f59419a4cfcb2df(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97830b045d238d0b8d131ab167575d8d0f2d8826c91f48cbddf9f3e7246c0cc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb3ceaa6da908543d0a9def8ca4352880f31088af631c862c816717e7a936f2(
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__896a5ca8bbc3b7d8b94abb8b9f94ca4bcdb9a6a2c522ac7a202e172e0ffcacec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allowed_characters: typing.Optional[builtins.str] = None,
    length: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc4b1455fc78cfc610c85420cf64186223aae30560816f9f944b0f1f83bbbee8(
    *,
    allowed_characters: typing.Optional[builtins.str] = None,
    length: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d7d404060a09a65f73fd33694e859d9dd781df10f45dafaba01780db0ec396(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
    log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
    oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
    redirect_paths: typing.Optional[typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]]] = None,
    security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    sign_out_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610c4da44720c57febe62b8eeb0f79f53522bc3e7705affcc998fd6d1a8cc0bf(
    log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e241ddf633750acd88125d1e5601ba48d5596b5f903193d4392fed59ffba9a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorization: ISpaAuthorization,
    ttl: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f9064ef0fc8e2acdb5387c77835361e50d477c8dbdb2dfcf7d01baae67a6ded(
    *,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
    authorization: ISpaAuthorization,
    ttl: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d404ed40edee2aae263b7107fe9c8182cf5b8f59de5dec2994c5a2a49b5974(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    cookie_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    custom_headers: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseCustomHeader, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_providers: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider]] = None,
    log_level: typing.Optional[_cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel] = None,
    oauth_scopes: typing.Optional[typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope]] = None,
    redirect_paths: typing.Optional[typing.Union[RedirectPaths, typing.Dict[builtins.str, typing.Any]]] = None,
    security_headers_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ResponseSecurityHeadersBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    sign_out_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d38bd88ce93edf4d7f9696bdd32e538851a103fbbcc852151f5d93b26ba876(
    log_level: _cloudcomponents_cdk_lambda_at_edge_pattern_71cb1101.LogLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c52404d6cd363e8ec929d36d264abb1ed9dd25e10f99559ae3c432fb8ae88c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorization: IStaticSiteAuthorization,
    error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5202e16cdcc711fbfddb991d7f5f345254b76a15f659e0f12cd135a2e3be4c9(
    *,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
    authorization: IStaticSiteAuthorization,
    error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c917dd323f8c9dd6d21b692c6a170fadf195696bdd1787f50ce6b03915c5b3cf(
    *,
    callback_urls: typing.Sequence[builtins.str],
    logout_urls: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbad32d1f28a960fdff821cb2ab4f6b16a2745d8ba3f6f9679af43c8d57ca87(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    callback_urls: typing.Sequence[builtins.str],
    identity_providers: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider],
    logout_urls: typing.Sequence[builtins.str],
    oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f80524222ee747484f32ae51b81bf1253fa9d67c400f31876cc94770679fa0(
    *,
    callback_urls: typing.Sequence[builtins.str],
    identity_providers: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.UserPoolClientIdentityProvider],
    logout_urls: typing.Sequence[builtins.str],
    oauth_scopes: typing.Sequence[_aws_cdk_aws_cognito_ceddda9d.OAuthScope],
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_ceddda9d.IUserPoolClient,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f058c58bca699c44c339a580b6ad5ace3c595e45d67277ace583aa6f34b993c9(
    *,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    origin: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.IOrigin] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
    authorization: IAuthorization,
    error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
