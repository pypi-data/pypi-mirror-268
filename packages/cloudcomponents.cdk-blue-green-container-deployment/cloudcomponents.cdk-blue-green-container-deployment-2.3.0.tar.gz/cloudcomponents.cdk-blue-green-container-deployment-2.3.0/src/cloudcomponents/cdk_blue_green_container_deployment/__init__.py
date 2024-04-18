'''
[![cloudcomponents Logo](https://raw.githubusercontent.com/cloudcomponents/cdk-constructs/master/logo.png)](https://github.com/cloudcomponents/cdk-constructs)

# @cloudcomponents/cdk-blue-green-container-deployment

[![Build Status](https://github.com/cloudcomponents/cdk-constructs/workflows/Build/badge.svg)](https://github.com/cloudcomponents/cdk-constructs/actions?query=workflow=Build)
[![cdkdx](https://img.shields.io/badge/buildtool-cdkdx-blue.svg)](https://github.com/hupe1980/cdkdx)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/@cloudcomponents/cdk-blue-green-container-deployment)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cloudcomponents.cdk-blue-green-container-deployment/)
[![Mentioned in Awesome CDK](https://awesome.re/mentioned-badge.svg)](https://github.com/kolomied/awesome-cdk)

> Blue green container deployment with CodeDeploy

## Install

TypeScript/JavaScript:

```bash
npm i @cloudcomponents/cdk-blue-green-container-deployment
```

Python:

```bash
pip install cloudcomponents.cdk-blue-green-container-deployment
```

## How to use

```python
import { EcsService, DummyTaskDefinition, EcsDeploymentGroup, PushImageProject } from '@cloudcomponents/cdk-blue-green-container-deployment';
import { ImageRepository } from '@cloudcomponents/cdk-container-registry';
import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { Pipeline, Artifact } from 'aws-cdk-lib/aws-codepipeline';
import { CodeBuildAction, CodeCommitSourceAction, CodeDeployEcsDeployAction } from 'aws-cdk-lib/aws-codepipeline-actions';
import { Vpc, Port } from 'aws-cdk-lib/aws-ec2';
import { Cluster } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancer, ApplicationTargetGroup, TargetType } from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import { Construct } from 'constructs';

export class BlueGreenContainerDeploymentStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new Vpc(this, 'Vpc', {
      maxAzs: 2,
    });

    const cluster = new Cluster(this, 'Cluster', {
      vpc,
      clusterName: 'blue-green-cluster',
    });

    const loadBalancer = new ApplicationLoadBalancer(this, 'LoadBalancer', {
      vpc,
      internetFacing: true,
    });

    const prodListener = loadBalancer.addListener('ProfListener', {
      port: 80,
    });

    const testListener = loadBalancer.addListener('TestListener', {
      port: 8080,
    });

    const prodTargetGroup = new ApplicationTargetGroup(this, 'ProdTargetGroup', {
      port: 80,
      targetType: TargetType.IP,
      vpc,
    });

    prodListener.addTargetGroups('AddProdTg', {
      targetGroups: [prodTargetGroup],
    });

    const testTargetGroup = new ApplicationTargetGroup(this, 'TestTargetGroup', {
      port: 8080,
      targetType: TargetType.IP,
      vpc,
    });

    testListener.addTargetGroups('AddTestTg', {
      targetGroups: [testTargetGroup],
    });

    // Will be replaced by CodeDeploy in CodePipeline
    const taskDefinition = new DummyTaskDefinition(this, 'DummyTaskDefinition', {
      image: 'nginx',
      family: 'blue-green',
    });

    const ecsService = new EcsService(this, 'EcsService', {
      cluster,
      serviceName: 'blue-green-service',
      desiredCount: 2,
      taskDefinition,
      prodTargetGroup,
      testTargetGroup,
    });

    ecsService.connections.allowFrom(loadBalancer, Port.tcp(80));
    ecsService.connections.allowFrom(loadBalancer, Port.tcp(8080));

    const deploymentGroup = new EcsDeploymentGroup(this, 'DeploymentGroup', {
      applicationName: 'blue-green-application',
      deploymentGroupName: 'blue-green-deployment-group',
      ecsServices: [ecsService],
      targetGroups: [prodTargetGroup, testTargetGroup],
      prodTrafficListener: prodListener,
      testTrafficListener: testListener,
      terminationWaitTime: Duration.minutes(100),
    });

    // @see files: ./blue-green-repository for example content
    const repository = new Repository(this, 'CodeRepository', {
      repositoryName: 'blue-green-repository',
    });

    const imageRepository = new ImageRepository(this, 'ImageRepository', {
      forceDelete: true, //Only for tests
    });

    const sourceArtifact = new Artifact();

    const sourceAction = new CodeCommitSourceAction({
      actionName: 'CodeCommit',
      repository,
      output: sourceArtifact,
    });

    const imageArtifact = new Artifact('ImageArtifact');
    const manifestArtifact = new Artifact('ManifestArtifact');

    const pushImageProject = new PushImageProject(this, 'PushImageProject', {
      imageRepository,
      taskDefinition,
    });

    const buildAction = new CodeBuildAction({
      actionName: 'PushImage',
      project: pushImageProject,
      input: sourceArtifact,
      outputs: [imageArtifact, manifestArtifact],
    });

    const deployAction = new CodeDeployEcsDeployAction({
      actionName: 'CodeDeploy',
      taskDefinitionTemplateInput: manifestArtifact,
      appSpecTemplateInput: manifestArtifact,
      containerImageInputs: [
        {
          input: imageArtifact,
          taskDefinitionPlaceholder: 'IMAGE1_NAME',
        },
      ],
      deploymentGroup,
    });

    new Pipeline(this, 'Pipeline', {
      pipelineName: 'blue-green-pipeline',
      stages: [
        {
          stageName: 'Source',
          actions: [sourceAction],
        },
        {
          stageName: 'Build',
          actions: [buildAction],
        },
        {
          stageName: 'Deploy',
          actions: [deployAction],
        },
      ],
    });
  }
}
```

## API Reference

See [API.md](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-blue-green-container-deployment/API.md).

## Example

See more complete [examples](https://github.com/cloudcomponents/cdk-constructs/tree/master/examples).

## License

[MIT](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-blue-green-container-deployment//LICENSE)
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
import aws_cdk.aws_codebuild as _aws_cdk_aws_codebuild_ceddda9d
import aws_cdk.aws_codedeploy as _aws_cdk_aws_codedeploy_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_ecr as _aws_cdk_aws_ecr_ceddda9d
import aws_cdk.aws_ecs as _aws_cdk_aws_ecs_ceddda9d
import aws_cdk.aws_elasticloadbalancingv2 as _aws_cdk_aws_elasticloadbalancingv2_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.DummyTaskDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "container_name": "containerName",
        "container_port": "containerPort",
        "family": "family",
    },
)
class DummyTaskDefinitionProps:
    def __init__(
        self,
        *,
        image: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The image used to start a container.
        :param container_name: The name of the container. Default: ``sample-website``
        :param container_port: Default: 80
        :param family: The name of a family that this task definition is registered to. A family groups multiple versions of a task definition. Default: - Automatically generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cdda6af9beed04a908975bf1a83cd92b81f1f7462a344ae755f48943c546ff9)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image": image,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if container_port is not None:
            self._values["container_port"] = container_port
        if family is not None:
            self._values["family"] = family

    @builtins.property
    def image(self) -> builtins.str:
        '''The image used to start a container.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''The name of the container.

        :default: ``sample-website``
        '''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''
        :default: 80
        '''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def family(self) -> typing.Optional[builtins.str]:
        '''The name of a family that this task definition is registered to.

        A family groups multiple versions of a task definition.

        :default: - Automatically generated name.
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DummyTaskDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.EcsDeploymentConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_config_name": "deploymentConfigName",
        "minimum_healthy_hosts": "minimumHealthyHosts",
        "traffic_routing_config": "trafficRoutingConfig",
    },
)
class EcsDeploymentConfigurationProps:
    def __init__(
        self,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        traffic_routing_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    ) -> None:
        '''
        :param deployment_config_name: ``AWS::CodeDeploy::DeploymentConfig.DeploymentConfigName``.
        :param minimum_healthy_hosts: ``AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts``.
        :param traffic_routing_config: ``AWS::CodeDeploy::DeploymentConfig.TrafficRoutingConfig``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2e154a1d784f97e23a110c06b7758cc4de7a940c61038daa3fb539cd7bf4bb)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument minimum_healthy_hosts", value=minimum_healthy_hosts, expected_type=type_hints["minimum_healthy_hosts"])
            check_type(argname="argument traffic_routing_config", value=traffic_routing_config, expected_type=type_hints["traffic_routing_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if minimum_healthy_hosts is not None:
            self._values["minimum_healthy_hosts"] = minimum_healthy_hosts
        if traffic_routing_config is not None:
            self._values["traffic_routing_config"] = traffic_routing_config

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CodeDeploy::DeploymentConfig.DeploymentConfigName``.

        :external: true
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_healthy_hosts(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.MinimumHealthyHostsProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''``AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts``.

        :external: true
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts
        '''
        result = self._values.get("minimum_healthy_hosts")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.MinimumHealthyHostsProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def traffic_routing_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.TrafficRoutingConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''``AWS::CodeDeploy::DeploymentConfig.TrafficRoutingConfig``.

        :external: true
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig
        '''
        result = self._values.get("traffic_routing_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.TrafficRoutingConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsDeploymentConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.EcsDeploymentGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_group_name": "deploymentGroupName",
        "ecs_services": "ecsServices",
        "prod_traffic_listener": "prodTrafficListener",
        "target_groups": "targetGroups",
        "test_traffic_listener": "testTrafficListener",
        "application": "application",
        "application_name": "applicationName",
        "auto_rollback_on_events": "autoRollbackOnEvents",
        "deployment_config": "deploymentConfig",
        "termination_wait_time": "terminationWaitTime",
    },
)
class EcsDeploymentGroupProps:
    def __init__(
        self,
        *,
        deployment_group_name: builtins.str,
        ecs_services: typing.Sequence["IEcsService"],
        prod_traffic_listener: typing.Union["TrafficListener", typing.Dict[builtins.str, typing.Any]],
        target_groups: typing.Sequence[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationTargetGroup],
        test_traffic_listener: typing.Union["TrafficListener", typing.Dict[builtins.str, typing.Any]],
        application: typing.Optional[_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication] = None,
        application_name: typing.Optional[builtins.str] = None,
        auto_rollback_on_events: typing.Optional[typing.Sequence["RollbackEvent"]] = None,
        deployment_config: typing.Optional["IEcsDeploymentConfig"] = None,
        termination_wait_time: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ) -> None:
        '''
        :param deployment_group_name: -
        :param ecs_services: -
        :param prod_traffic_listener: -
        :param target_groups: -
        :param test_traffic_listener: -
        :param application: The CodeDeploy Application to associate to the DeploymentGroup. Default: - create a new CodeDeploy Application.
        :param application_name: (deprecated) The name to use for the implicitly created CodeDeploy Application. Default: - uses auto-generated name
        :param auto_rollback_on_events: The event type or types that trigger a rollback.
        :param deployment_config: -
        :param termination_wait_time: the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set. The maximum setting is 2880 minutes (2 days). Default: 60 minutes
        '''
        if isinstance(prod_traffic_listener, dict):
            prod_traffic_listener = TrafficListener(**prod_traffic_listener)
        if isinstance(test_traffic_listener, dict):
            test_traffic_listener = TrafficListener(**test_traffic_listener)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c8e3cf458a49bf400dcceca3416d1e809978fb50bccc294c763f18c9a78176)
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument ecs_services", value=ecs_services, expected_type=type_hints["ecs_services"])
            check_type(argname="argument prod_traffic_listener", value=prod_traffic_listener, expected_type=type_hints["prod_traffic_listener"])
            check_type(argname="argument target_groups", value=target_groups, expected_type=type_hints["target_groups"])
            check_type(argname="argument test_traffic_listener", value=test_traffic_listener, expected_type=type_hints["test_traffic_listener"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument auto_rollback_on_events", value=auto_rollback_on_events, expected_type=type_hints["auto_rollback_on_events"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
            check_type(argname="argument termination_wait_time", value=termination_wait_time, expected_type=type_hints["termination_wait_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_group_name": deployment_group_name,
            "ecs_services": ecs_services,
            "prod_traffic_listener": prod_traffic_listener,
            "target_groups": target_groups,
            "test_traffic_listener": test_traffic_listener,
        }
        if application is not None:
            self._values["application"] = application
        if application_name is not None:
            self._values["application_name"] = application_name
        if auto_rollback_on_events is not None:
            self._values["auto_rollback_on_events"] = auto_rollback_on_events
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if termination_wait_time is not None:
            self._values["termination_wait_time"] = termination_wait_time

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ecs_services(self) -> typing.List["IEcsService"]:
        result = self._values.get("ecs_services")
        assert result is not None, "Required property 'ecs_services' is missing"
        return typing.cast(typing.List["IEcsService"], result)

    @builtins.property
    def prod_traffic_listener(self) -> "TrafficListener":
        result = self._values.get("prod_traffic_listener")
        assert result is not None, "Required property 'prod_traffic_listener' is missing"
        return typing.cast("TrafficListener", result)

    @builtins.property
    def target_groups(
        self,
    ) -> typing.List[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationTargetGroup]:
        result = self._values.get("target_groups")
        assert result is not None, "Required property 'target_groups' is missing"
        return typing.cast(typing.List[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationTargetGroup], result)

    @builtins.property
    def test_traffic_listener(self) -> "TrafficListener":
        result = self._values.get("test_traffic_listener")
        assert result is not None, "Required property 'test_traffic_listener' is missing"
        return typing.cast("TrafficListener", result)

    @builtins.property
    def application(
        self,
    ) -> typing.Optional[_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication]:
        '''The CodeDeploy Application to associate to the DeploymentGroup.

        :default: - create a new CodeDeploy Application.
        '''
        result = self._values.get("application")
        return typing.cast(typing.Optional[_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication], result)

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name to use for the implicitly created CodeDeploy Application.

        :default: - uses auto-generated name

        :deprecated: Use {@link application} instead to create a custom CodeDeploy Application.

        :stability: deprecated
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_rollback_on_events(self) -> typing.Optional[typing.List["RollbackEvent"]]:
        '''The event type or types that trigger a rollback.'''
        result = self._values.get("auto_rollback_on_events")
        return typing.cast(typing.Optional[typing.List["RollbackEvent"]], result)

    @builtins.property
    def deployment_config(self) -> typing.Optional["IEcsDeploymentConfig"]:
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional["IEcsDeploymentConfig"], result)

    @builtins.property
    def termination_wait_time(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''the number of minutes before deleting the original (blue) task set.

        During an Amazon ECS deployment, CodeDeploy shifts traffic from the
        original (blue) task set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

        :default: 60 minutes
        '''
        result = self._values.get("termination_wait_time")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsDeploymentGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.EcsServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "prod_target_group": "prodTargetGroup",
        "service_name": "serviceName",
        "task_definition": "taskDefinition",
        "test_target_group": "testTargetGroup",
        "circuit_breaker": "circuitBreaker",
        "container_port": "containerPort",
        "desired_count": "desiredCount",
        "health_check_grace_period": "healthCheckGracePeriod",
        "launch_type": "launchType",
        "max_healthy_percent": "maxHealthyPercent",
        "min_healthy_percent": "minHealthyPercent",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "security_groups": "securityGroups",
    },
)
class EcsServiceProps:
    def __init__(
        self,
        *,
        cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
        prod_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
        service_name: builtins.str,
        task_definition: "DummyTaskDefinition",
        test_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
        circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
        container_port: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        launch_type: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.LaunchType] = None,
        max_healthy_percent: typing.Optional[jsii.Number] = None,
        min_healthy_percent: typing.Optional[jsii.Number] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional["PropagateTags"] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup]] = None,
    ) -> None:
        '''
        :param cluster: -
        :param prod_target_group: -
        :param service_name: -
        :param task_definition: -
        :param test_target_group: -
        :param circuit_breaker: Whether to enable the deployment circuit breaker. If this property is defined, circuit breaker will be implicitly enabled. Default: - disabled
        :param container_port: -
        :param desired_count: -
        :param health_check_grace_period: The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. Default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
        :param launch_type: -
        :param max_healthy_percent: The maximum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that can run in a service during a deployment. Default: - 100 if daemon, otherwise 200
        :param min_healthy_percent: The minimum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that must continue to run and remain healthy during a deployment. Default: - 0 if daemon, otherwise 50
        :param platform_version: -
        :param propagate_tags: Specifies whether to propagate the tags from the task definition or the service to the tasks in the service. If no value is specified, the tags aren't propagated. Default: - no propagate
        :param security_groups: -
        '''
        if isinstance(circuit_breaker, dict):
            circuit_breaker = _aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker(**circuit_breaker)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e25ddaacd098fee9380e8adea6f7a93c6bc49b3c22cfe483ec49967e5501f903)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument prod_target_group", value=prod_target_group, expected_type=type_hints["prod_target_group"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument test_target_group", value=test_target_group, expected_type=type_hints["test_target_group"])
            check_type(argname="argument circuit_breaker", value=circuit_breaker, expected_type=type_hints["circuit_breaker"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument max_healthy_percent", value=max_healthy_percent, expected_type=type_hints["max_healthy_percent"])
            check_type(argname="argument min_healthy_percent", value=min_healthy_percent, expected_type=type_hints["min_healthy_percent"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "prod_target_group": prod_target_group,
            "service_name": service_name,
            "task_definition": task_definition,
            "test_target_group": test_target_group,
        }
        if circuit_breaker is not None:
            self._values["circuit_breaker"] = circuit_breaker
        if container_port is not None:
            self._values["container_port"] = container_port
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if max_healthy_percent is not None:
            self._values["max_healthy_percent"] = max_healthy_percent
        if min_healthy_percent is not None:
            self._values["min_healthy_percent"] = min_healthy_percent
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def cluster(self) -> _aws_cdk_aws_ecs_ceddda9d.ICluster:
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.ICluster, result)

    @builtins.property
    def prod_target_group(
        self,
    ) -> _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup:
        result = self._values.get("prod_target_group")
        assert result is not None, "Required property 'prod_target_group' is missing"
        return typing.cast(_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_definition(self) -> "DummyTaskDefinition":
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast("DummyTaskDefinition", result)

    @builtins.property
    def test_target_group(
        self,
    ) -> _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup:
        result = self._values.get("test_target_group")
        assert result is not None, "Required property 'test_target_group' is missing"
        return typing.cast(_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup, result)

    @builtins.property
    def circuit_breaker(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker]:
        '''Whether to enable the deployment circuit breaker.

        If this property is defined, circuit breaker will be implicitly
        enabled.

        :default: - disabled
        '''
        result = self._values.get("circuit_breaker")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.

        :default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
        '''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.LaunchType]:
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.LaunchType], result)

    @builtins.property
    def max_healthy_percent(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that can run in a service during a deployment.

        :default: - 100 if daemon, otherwise 200
        '''
        result = self._values.get("max_healthy_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_healthy_percent(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that must continue to run and remain healthy during a deployment.

        :default: - 0 if daemon, otherwise 50
        '''
        result = self._values.get("min_healthy_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional["PropagateTags"]:
        '''Specifies whether to propagate the tags from the task definition or the service to the tasks in the service.

        If no value is specified, the tags aren't propagated.

        :default: - no propagate
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional["PropagateTags"], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup]]:
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.IDummyTaskDefinition"
)
class IDummyTaskDefinition(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        ...

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> _aws_cdk_aws_iam_ceddda9d.IRole:
        ...

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArn")
    def task_definition_arn(self) -> builtins.str:
        ...


class _IDummyTaskDefinitionProxy:
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-blue-green-container-deployment.IDummyTaskDefinition"

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> _aws_cdk_aws_iam_ceddda9d.IRole:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IRole, jsii.get(self, "executionRole"))

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArn")
    def task_definition_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinitionArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDummyTaskDefinition).__jsii_proxy_class__ = lambda : _IDummyTaskDefinitionProxy


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.IEcsDeploymentConfig"
)
class IEcsDeploymentConfig(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        ...


class _IEcsDeploymentConfigProxy:
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-blue-green-container-deployment.IEcsDeploymentConfig"

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEcsDeploymentConfig).__jsii_proxy_class__ = lambda : _IEcsDeploymentConfigProxy


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.IEcsDeploymentGroup"
)
class IEcsDeploymentGroup(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    '''Interface for an ECS deployment group.'''

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> _aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IEcsDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.'''
        ...


class _IEcsDeploymentGroupProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    '''Interface for an ECS deployment group.'''

    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-blue-green-container-deployment.IEcsDeploymentGroup"

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> _aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        return typing.cast(_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IEcsDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        return typing.cast(IEcsDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEcsDeploymentGroup).__jsii_proxy_class__ = lambda : _IEcsDeploymentGroupProxy


@jsii.interface(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.IEcsService"
)
class IEcsService(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        ...


class _IEcsServiceProxy:
    __jsii_type__: typing.ClassVar[str] = "@cloudcomponents/cdk-blue-green-container-deployment.IEcsService"

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEcsService).__jsii_proxy_class__ = lambda : _IEcsServiceProxy


@jsii.enum(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.PropagateTags"
)
class PropagateTags(enum.Enum):
    TASK_DEFINITION = "TASK_DEFINITION"
    SERVICE = "SERVICE"


class PushImageProject(
    _aws_cdk_aws_codebuild_ceddda9d.PipelineProject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.PushImageProject",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        image_repository: _aws_cdk_aws_ecr_ceddda9d.IRepository,
        task_definition: IDummyTaskDefinition,
        build_spec: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.BuildSpec] = None,
        cache: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.Cache] = None,
        compute_type: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.ComputeType] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_codebuild_ceddda9d.BuildEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]] = None,
        project_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param image_repository: -
        :param task_definition: -
        :param build_spec: -
        :param cache: -
        :param compute_type: -
        :param environment_variables: -
        :param project_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__583427900c4d8d9b4029ac1e3d834d575484540f24ff6af1a581ba86da07bf19)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PushImageProjectProps(
            image_repository=image_repository,
            task_definition=task_definition,
            build_spec=build_spec,
            cache=cache,
            compute_type=compute_type,
            environment_variables=environment_variables,
            project_name=project_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.PushImageProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "image_repository": "imageRepository",
        "task_definition": "taskDefinition",
        "build_spec": "buildSpec",
        "cache": "cache",
        "compute_type": "computeType",
        "environment_variables": "environmentVariables",
        "project_name": "projectName",
    },
)
class PushImageProjectProps:
    def __init__(
        self,
        *,
        image_repository: _aws_cdk_aws_ecr_ceddda9d.IRepository,
        task_definition: IDummyTaskDefinition,
        build_spec: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.BuildSpec] = None,
        cache: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.Cache] = None,
        compute_type: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.ComputeType] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_codebuild_ceddda9d.BuildEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]] = None,
        project_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_repository: -
        :param task_definition: -
        :param build_spec: -
        :param cache: -
        :param compute_type: -
        :param environment_variables: -
        :param project_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a98ecf4520bf3b5188f22abc82bc6fe452185dc43d6b813fed53490051589d)
            check_type(argname="argument image_repository", value=image_repository, expected_type=type_hints["image_repository"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument build_spec", value=build_spec, expected_type=type_hints["build_spec"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_repository": image_repository,
            "task_definition": task_definition,
        }
        if build_spec is not None:
            self._values["build_spec"] = build_spec
        if cache is not None:
            self._values["cache"] = cache
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if project_name is not None:
            self._values["project_name"] = project_name

    @builtins.property
    def image_repository(self) -> _aws_cdk_aws_ecr_ceddda9d.IRepository:
        result = self._values.get("image_repository")
        assert result is not None, "Required property 'image_repository' is missing"
        return typing.cast(_aws_cdk_aws_ecr_ceddda9d.IRepository, result)

    @builtins.property
    def task_definition(self) -> IDummyTaskDefinition:
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(IDummyTaskDefinition, result)

    @builtins.property
    def build_spec(self) -> typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.BuildSpec]:
        result = self._values.get("build_spec")
        return typing.cast(typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.BuildSpec], result)

    @builtins.property
    def cache(self) -> typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.Cache]:
        result = self._values.get("cache")
        return typing.cast(typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.Cache], result)

    @builtins.property
    def compute_type(
        self,
    ) -> typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.ComputeType]:
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.ComputeType], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_codebuild_ceddda9d.BuildEnvironmentVariable]]:
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_codebuild_ceddda9d.BuildEnvironmentVariable]], result)

    @builtins.property
    def project_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("project_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PushImageProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.RollbackEvent"
)
class RollbackEvent(enum.Enum):
    DEPLOYMENT_FAILURE = "DEPLOYMENT_FAILURE"
    DEPLOYMENT_STOP_ON_ALARM = "DEPLOYMENT_STOP_ON_ALARM"
    DEPLOYMENT_STOP_ON_REQUEST = "DEPLOYMENT_STOP_ON_REQUEST"


@jsii.enum(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.SchedulingStrategy"
)
class SchedulingStrategy(enum.Enum):
    REPLICA = "REPLICA"
    DAEMON = "DAEMON"


@jsii.data_type(
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.TrafficListener",
    jsii_struct_bases=[],
    name_mapping={"listener_arn": "listenerArn"},
)
class TrafficListener:
    def __init__(self, *, listener_arn: builtins.str) -> None:
        '''
        :param listener_arn: ARN of the listener.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba4d3dd74c72a164e6b84164928da295871a509033d5b03337e6f6798aabe276)
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_arn": listener_arn,
        }

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''ARN of the listener.

        :attribute: true
        '''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IDummyTaskDefinition, _aws_cdk_ceddda9d.ITaggable)
class DummyTaskDefinition(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.DummyTaskDefinition",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        image: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        family: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param image: The image used to start a container.
        :param container_name: The name of the container. Default: ``sample-website``
        :param container_port: Default: 80
        :param family: The name of a family that this task definition is registered to. A family groups multiple versions of a task definition. Default: - Automatically generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9278f594ec9ad9cc04181b24d1175392ff2895526d8cdde7d6caff84a0918f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DummyTaskDefinitionProps(
            image=image,
            container_name=container_name,
            container_port=container_port,
            family=family,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToExecutionRolePolicy")
    def add_to_execution_role_policy(
        self,
        statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
    ) -> None:
        '''Adds a policy statement to the task execution IAM role.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0340d1921b3cc5580dffdab2b84dc17cdad7763d9345264aa45def8d48027954)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToExecutionRolePolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> _aws_cdk_aws_iam_ceddda9d.IRole:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IRole, jsii.get(self, "executionRole"))

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_ceddda9d.TagManager:
        '''TagManager to set, remove and format tags.'''
        return typing.cast(_aws_cdk_ceddda9d.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArn")
    def task_definition_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinitionArn"))


@jsii.implements(IEcsDeploymentConfig)
class EcsDeploymentConfig(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.EcsDeploymentConfig",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        traffic_routing_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param deployment_config_name: ``AWS::CodeDeploy::DeploymentConfig.DeploymentConfigName``.
        :param minimum_healthy_hosts: ``AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts``.
        :param traffic_routing_config: ``AWS::CodeDeploy::DeploymentConfig.TrafficRoutingConfig``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd92719e890cea3d3cec9b86303a9b27c8d1bdfc44b64720751c06d08cd49b62)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsDeploymentConfigurationProps(
            deployment_config_name=deployment_config_name,
            minimum_healthy_hosts=minimum_healthy_hosts,
            traffic_routing_config=traffic_routing_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEcsDeploymentConfigName")
    @builtins.classmethod
    def from_ecs_deployment_config_name(
        cls,
        _scope: _constructs_77d1e7e8.Construct,
        _id: builtins.str,
        ecs_deployment_config_name: builtins.str,
    ) -> IEcsDeploymentConfig:
        '''Import a custom Deployment Configuration for an ECS Deployment Group defined outside the CDK.

        :param _scope: the parent Construct for this new Construct.
        :param _id: the logical ID of this new Construct.
        :param ecs_deployment_config_name: the name of the referenced custom Deployment Configuration.

        :return: a Construct representing a reference to an existing custom Deployment Configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c09ab642ac5a13d37f43654ac7b8d11c6ca71b3dcdd94b7ea4de3f43e62c67a5)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
            check_type(argname="argument ecs_deployment_config_name", value=ecs_deployment_config_name, expected_type=type_hints["ecs_deployment_config_name"])
        return typing.cast(IEcsDeploymentConfig, jsii.sinvoke(cls, "fromEcsDeploymentConfigName", [_scope, _id, ecs_deployment_config_name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> IEcsDeploymentConfig:
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "ALL_AT_ONCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_15MINUTES")
    def CANARY_10_PERCENT_15_MINUTES(cls) -> IEcsDeploymentConfig:
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_15MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_5MINUTES")
    def CANARY_10_PERCENT_5_MINUTES(cls) -> IEcsDeploymentConfig:
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_5MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_1MINUTE")
    def LINEAR_10_PERCENT_EVERY_1_MINUTE(cls) -> IEcsDeploymentConfig:
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_1MINUTE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_3MINUTES")
    def LINEAR_10_PERCENT_EVERY_3_MINUTES(cls) -> IEcsDeploymentConfig:
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_3MINUTES"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))


@jsii.implements(IEcsDeploymentGroup, _aws_cdk_ceddda9d.ITaggable)
class EcsDeploymentGroup(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.EcsDeploymentGroup",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        deployment_group_name: builtins.str,
        ecs_services: typing.Sequence[IEcsService],
        prod_traffic_listener: typing.Union[TrafficListener, typing.Dict[builtins.str, typing.Any]],
        target_groups: typing.Sequence[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationTargetGroup],
        test_traffic_listener: typing.Union[TrafficListener, typing.Dict[builtins.str, typing.Any]],
        application: typing.Optional[_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication] = None,
        application_name: typing.Optional[builtins.str] = None,
        auto_rollback_on_events: typing.Optional[typing.Sequence[RollbackEvent]] = None,
        deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
        termination_wait_time: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param deployment_group_name: -
        :param ecs_services: -
        :param prod_traffic_listener: -
        :param target_groups: -
        :param test_traffic_listener: -
        :param application: The CodeDeploy Application to associate to the DeploymentGroup. Default: - create a new CodeDeploy Application.
        :param application_name: (deprecated) The name to use for the implicitly created CodeDeploy Application. Default: - uses auto-generated name
        :param auto_rollback_on_events: The event type or types that trigger a rollback.
        :param deployment_config: -
        :param termination_wait_time: the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set. The maximum setting is 2880 minutes (2 days). Default: 60 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6171456bd6372667b6ff958acb34ed1e93971cbfa7f7206e5081dfc46bb0540d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsDeploymentGroupProps(
            deployment_group_name=deployment_group_name,
            ecs_services=ecs_services,
            prod_traffic_listener=prod_traffic_listener,
            target_groups=target_groups,
            test_traffic_listener=test_traffic_listener,
            application=application,
            application_name=application_name,
            auto_rollback_on_events=auto_rollback_on_events,
            deployment_config=deployment_config,
            termination_wait_time=termination_wait_time,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> _aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        return typing.cast(_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IEcsDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        return typing.cast(IEcsDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_ceddda9d.TagManager:
        '''TagManager to set, remove and format tags.'''
        return typing.cast(_aws_cdk_ceddda9d.TagManager, jsii.get(self, "tags"))


@jsii.implements(_aws_cdk_aws_ec2_ceddda9d.IConnectable, IEcsService, _aws_cdk_ceddda9d.ITaggable)
class EcsService(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudcomponents/cdk-blue-green-container-deployment.EcsService",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
        prod_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
        service_name: builtins.str,
        task_definition: DummyTaskDefinition,
        test_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
        circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
        container_port: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        launch_type: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.LaunchType] = None,
        max_healthy_percent: typing.Optional[jsii.Number] = None,
        min_healthy_percent: typing.Optional[jsii.Number] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[PropagateTags] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: -
        :param prod_target_group: -
        :param service_name: -
        :param task_definition: -
        :param test_target_group: -
        :param circuit_breaker: Whether to enable the deployment circuit breaker. If this property is defined, circuit breaker will be implicitly enabled. Default: - disabled
        :param container_port: -
        :param desired_count: -
        :param health_check_grace_period: The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. Default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
        :param launch_type: -
        :param max_healthy_percent: The maximum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that can run in a service during a deployment. Default: - 100 if daemon, otherwise 200
        :param min_healthy_percent: The minimum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that must continue to run and remain healthy during a deployment. Default: - 0 if daemon, otherwise 50
        :param platform_version: -
        :param propagate_tags: Specifies whether to propagate the tags from the task definition or the service to the tasks in the service. If no value is specified, the tags aren't propagated. Default: - no propagate
        :param security_groups: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__708b2d896671b6871b936d61ecbc383c82efa7f9113cffbd9781fb8e7172dba0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsServiceProps(
            cluster=cluster,
            prod_target_group=prod_target_group,
            service_name=service_name,
            task_definition=task_definition,
            test_target_group=test_target_group,
            circuit_breaker=circuit_breaker,
            container_port=container_port,
            desired_count=desired_count,
            health_check_grace_period=health_check_grace_period,
            launch_type=launch_type,
            max_healthy_percent=max_healthy_percent,
            min_healthy_percent=min_healthy_percent,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            security_groups=security_groups,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _aws_cdk_aws_ec2_ceddda9d.Connections:
        '''The network connections associated with this resource.'''
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_ceddda9d.TagManager:
        '''TagManager to set, remove and format tags.'''
        return typing.cast(_aws_cdk_ceddda9d.TagManager, jsii.get(self, "tags"))


__all__ = [
    "DummyTaskDefinition",
    "DummyTaskDefinitionProps",
    "EcsDeploymentConfig",
    "EcsDeploymentConfigurationProps",
    "EcsDeploymentGroup",
    "EcsDeploymentGroupProps",
    "EcsService",
    "EcsServiceProps",
    "IDummyTaskDefinition",
    "IEcsDeploymentConfig",
    "IEcsDeploymentGroup",
    "IEcsService",
    "PropagateTags",
    "PushImageProject",
    "PushImageProjectProps",
    "RollbackEvent",
    "SchedulingStrategy",
    "TrafficListener",
]

publication.publish()

def _typecheckingstub__6cdda6af9beed04a908975bf1a83cd92b81f1f7462a344ae755f48943c546ff9(
    *,
    image: builtins.str,
    container_name: typing.Optional[builtins.str] = None,
    container_port: typing.Optional[jsii.Number] = None,
    family: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2e154a1d784f97e23a110c06b7758cc4de7a940c61038daa3fb539cd7bf4bb(
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
    minimum_healthy_hosts: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    traffic_routing_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c8e3cf458a49bf400dcceca3416d1e809978fb50bccc294c763f18c9a78176(
    *,
    deployment_group_name: builtins.str,
    ecs_services: typing.Sequence[IEcsService],
    prod_traffic_listener: typing.Union[TrafficListener, typing.Dict[builtins.str, typing.Any]],
    target_groups: typing.Sequence[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationTargetGroup],
    test_traffic_listener: typing.Union[TrafficListener, typing.Dict[builtins.str, typing.Any]],
    application: typing.Optional[_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication] = None,
    application_name: typing.Optional[builtins.str] = None,
    auto_rollback_on_events: typing.Optional[typing.Sequence[RollbackEvent]] = None,
    deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
    termination_wait_time: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e25ddaacd098fee9380e8adea6f7a93c6bc49b3c22cfe483ec49967e5501f903(
    *,
    cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
    prod_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
    service_name: builtins.str,
    task_definition: DummyTaskDefinition,
    test_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
    circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
    container_port: typing.Optional[jsii.Number] = None,
    desired_count: typing.Optional[jsii.Number] = None,
    health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    launch_type: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.LaunchType] = None,
    max_healthy_percent: typing.Optional[jsii.Number] = None,
    min_healthy_percent: typing.Optional[jsii.Number] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[PropagateTags] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__583427900c4d8d9b4029ac1e3d834d575484540f24ff6af1a581ba86da07bf19(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    image_repository: _aws_cdk_aws_ecr_ceddda9d.IRepository,
    task_definition: IDummyTaskDefinition,
    build_spec: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.BuildSpec] = None,
    cache: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.Cache] = None,
    compute_type: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.ComputeType] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_codebuild_ceddda9d.BuildEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]] = None,
    project_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a98ecf4520bf3b5188f22abc82bc6fe452185dc43d6b813fed53490051589d(
    *,
    image_repository: _aws_cdk_aws_ecr_ceddda9d.IRepository,
    task_definition: IDummyTaskDefinition,
    build_spec: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.BuildSpec] = None,
    cache: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.Cache] = None,
    compute_type: typing.Optional[_aws_cdk_aws_codebuild_ceddda9d.ComputeType] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_codebuild_ceddda9d.BuildEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]] = None,
    project_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4d3dd74c72a164e6b84164928da295871a509033d5b03337e6f6798aabe276(
    *,
    listener_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9278f594ec9ad9cc04181b24d1175392ff2895526d8cdde7d6caff84a0918f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    image: builtins.str,
    container_name: typing.Optional[builtins.str] = None,
    container_port: typing.Optional[jsii.Number] = None,
    family: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0340d1921b3cc5580dffdab2b84dc17cdad7763d9345264aa45def8d48027954(
    statement: _aws_cdk_aws_iam_ceddda9d.PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd92719e890cea3d3cec9b86303a9b27c8d1bdfc44b64720751c06d08cd49b62(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
    minimum_healthy_hosts: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    traffic_routing_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_codedeploy_ceddda9d.CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09ab642ac5a13d37f43654ac7b8d11c6ca71b3dcdd94b7ea4de3f43e62c67a5(
    _scope: _constructs_77d1e7e8.Construct,
    _id: builtins.str,
    ecs_deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6171456bd6372667b6ff958acb34ed1e93971cbfa7f7206e5081dfc46bb0540d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_group_name: builtins.str,
    ecs_services: typing.Sequence[IEcsService],
    prod_traffic_listener: typing.Union[TrafficListener, typing.Dict[builtins.str, typing.Any]],
    target_groups: typing.Sequence[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationTargetGroup],
    test_traffic_listener: typing.Union[TrafficListener, typing.Dict[builtins.str, typing.Any]],
    application: typing.Optional[_aws_cdk_aws_codedeploy_ceddda9d.IEcsApplication] = None,
    application_name: typing.Optional[builtins.str] = None,
    auto_rollback_on_events: typing.Optional[typing.Sequence[RollbackEvent]] = None,
    deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
    termination_wait_time: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708b2d896671b6871b936d61ecbc383c82efa7f9113cffbd9781fb8e7172dba0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
    prod_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
    service_name: builtins.str,
    task_definition: DummyTaskDefinition,
    test_target_group: _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ITargetGroup,
    circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
    container_port: typing.Optional[jsii.Number] = None,
    desired_count: typing.Optional[jsii.Number] = None,
    health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    launch_type: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.LaunchType] = None,
    max_healthy_percent: typing.Optional[jsii.Number] = None,
    min_healthy_percent: typing.Optional[jsii.Number] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[PropagateTags] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup]] = None,
) -> None:
    """Type checking stubs"""
    pass
