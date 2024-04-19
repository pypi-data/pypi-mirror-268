'''
# About CloudKitect

[CloudKitect](https://cloudkitect.com) revolutionizes the way technology organizations adopt cloud computing by providing innovative, secure,
and cost-effective turnkey solution that fast-tracks the AWS Adoption.
Think of CloudKitect as Cloud Architect as a Service.

# About CloudKitect Patterns.

CloudKitect Patterns offer turnkey architecture using pre-built patterns for
frequently used infrastructures such as website hosting, REST APIs, and container based applications, etc.
Premium version of CloudKitect Patterns utilized enhanced components, that offer out of the box compliance and monitoring at every
level of your infrastructure. In addition to the freemium patterns, enterprise patterns offer virous other patterns
such as serverless virus scanner, event sourcing pattern, GenAI pipelines etc. You can view details and demos by visiting our
website [cloudkitect.com](https://cloudkitect.com)

## Developer Workstation Setup

Primarily, CloudKitect prioritizes enhancing the developer experience,
thus all our products are designed with the developer community at the forefront.
Consequently, to utilize the product, developers need to initially set up their workstations
with the necessary development tools.
You can either follow the steps below or watch this [Video](https://youtu.be/EoF-_U-Cyrg)

### Step 1: Install NPM

NPM is a package manager for javascript and typescript based projects.
Depending on your OS, install NPM.

#### Step 1a: Mac Users

Mac users can use homebrew to install node which will also install npm

```shell
brew upgrade
brew install node
```

#### Step 1b: Windows Users

Windows users can download the installer from [Here](https://nodejs.org/en/download/)

After the download of the installer package, follow these steps.

* Double-click on the downloaded file (.msi file).
* During installation, make sure to check the option "Add Node.js to Path". This will allow you to access npm commands from any directory in your command prompt.
* Make sure you choose npm package manager , not the default of Node.js runtime.
* This way, we can install Node and NPM simultaneously. Finally, click on install

Windows users can also use Chocolatey package manager, and install using the following command

```shell
chco install nodejs
```

For other Operating Systems follow the instructions [Here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

#### Step 1c: Verify Installation

Open a new terminal on your workstation and run the following commands to verify the installation:

```shell
node -v
npm -v
```

### Step 2: Install NVM (Optional)

It is recommended to install nvm, for managing various versions of nodejs.
For Mac

```shell
brew install nvm
```

For other OS

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
OR
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

#### Step 2a: Install Node via nvm

Install node version 18 or later, using nvm

```shell
nvm install 18
nvm use 18
```

### Step 3: Install AWS CLI

Install AWS cli to interact with your AWS account using terminal

#### Step 3a: Mac Users

Mac users can use homebrew to install node which will also install npm

```shell
brew upgrade
brew install awscli
```

#### Step 3b: Windows Users

* Visit the AWS CLI to download the installer [Download Page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* Double-click the downloaded .msi file and follow the instructions.

Follow other OS follow instructions [Here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

#### Step 3c: Verify Installation

Open a new terminal on your workstation and run the following commands to verify the installation:

```shell
aws --version
```

### Step 4: Install AWS CDK

#### Step 4a: Mac and Windows Users

Run the following command in your terminal.

```shell
npm install -g aws-cdk
```

#### Step 4b: Verify Installation

Open a new terminal on your workstation and run the following commands to verify the installation:

```shell
cdk --version
```

### Step 5: Install typescript

#### Step 5a: Mac and Windows Users

Run the following command in your terminal.

```shell
npm -g install typescript
```

#### Step 5b: Verify Installation

Open a new terminal on your workstation and run the following commands to verify the installation:

```shell
tsc --version
```

## Step 6: AWS Account Setup

Your AWS account needs to be setup and bootstrapped for CDK deployment

#### Step 6a: Create a user with Admin privileges

Create a user named "deployer" (you can give it any name) with Admin permissions in the AWS account where
application will be deployed.

#### 6b: Create Access key

Create Access Keys for the deployer user.

#### 6c: Configure AWS CLI

Run the following command and follow the instructions by providing your access key and secret key

```shell
aws configure --profile deployer
```

#### 6d: Route53 Hosted Zone

These components assume that there is a Route53 Hosted zone present in the AWS account
where the application is deployed. So create a hosted zone for a domain you own.
e.g. example.com and update the nameservers to point to this hosted zone.

#### 6e: Bootstrap AWS Account for CDK Deployment

```shell
cdk bootstrap aws://ACCOUNT_ID/us-east-1 --profile deployer
```

## Step 7: Create CDK project

NOTE: DEPLOYING THESE APPLICATIONS IN YOUR AWS ACCOUNT WILL INCUR COST THAT YOU WILL BE RESPONSIBLE FOR, SO MAKE SURE YOU
SHUT DOWN YOUR APPLICATION ONCE YOU ARE DONE.

### Step 7a: Create and initialize CDK project

Run the following commands to scaffold a CDK project

```shell
mkdir my-project
cd my-project
cdk init app --language typescript
```

### Step 7b: Open Project in IDE of your choice

For example Visual Studio or IntelliJ etc.

### Step 7c: Add CloudKitect Dependencies

Open package.json file in your project and under dependencies add the following two dependencies, check for the current released
version and use that version instead of "0.0.0"

```json
{
  "dependencies": {
    "@cloudkitect/components": "0.0.0",
    "@cloudkitect/patterns": "0.0.0",
    ...
  }
}
```

### Step 7d: Install dependencies

```shell
npm install
```

## Step 8: Build Your App

### Step 8a:

Open the my-project.ts file under lib directory, and add the following lines to it, replace 'AWS_ACCOUNT_ID' with your AWS
account Id. You can also change the 'ckApplication' and 'ckCompany' names.

```python
#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { MyProjectStack } from '../lib/my-project-stack';
import {CkAccountType} from "@cloudkitect/components";

const app = new cdk.App();

const devEnv = { account: "AWS_ACCOUNT_ID", region: "us-east-1" };

const stackProps = {
    ckAccountType: CkAccountType.DEVELOPMENT,
    ckApplication: "TestApp",
    ckCompany: "CloudKitect",
};

new MyProjectStack(app, 'MyProjectStack', {
    ...stackProps,
    env: devEnv
});
```

## Step 8b: Create Website Infrastructure

Under lib directory, open the  file named. my-project-stack.ts. Then copy and paste the following code
Change 'ckDomainName' to match the domain name that is currently setup in Route53.
.

```python
import { Construct } from 'constructs';
import {CkStack, CkStackProps} from "@cloudkitect/components";
import {CkServerlessWebsite} from "@cloudkitect/patterns"

export class MyProjectStack extends CkStack {
    constructor(scope: Construct, id: string, props: CkStackProps) {
        super(scope, id, props);

        new CkServerlessWebsite(this, 'TestSite', {
            ckDomainName: 'socalstartups.net',
            ckPathToContent: './site-content',
        });

    }
}
```

### Step 8c: Create website code.

Create a directory site-content under the directory my-project and add index.html. In real project this directory
will contain your angular, reactjs etc. app. You can also change 'ckPathToContent' to point to the location where
your existing web application artifacts are present, such as react/angular app dist folder

```shell
cd my-project
mkdir site-content
cd site-content
echo "CloudKitect is Awesome" >> index.html
```

### Step 8d: Deploy the stack.

Let's deploy the stack to our AWS account.

```shell
cdk deploy --require-approval never --profile deployer
```

### Step 8e: Verify Deployment

Once the deployment completes it will output the url for your website, copy and paste it in your browser. The website
should display the message "CloudKitect is Awesome".

## Step 9: Container App Deployment

Next we will deploy a containerized app.

### Step 9a: Create an ECR Repository

Login to your AWS account, goto ECR repository and create a new repository. You can name anything but in this example
we are using name "addressbook"

### Step 9b: Push your docker image to ecr

Login to ecr repository, replace AWS_ACCOUNT_ID with your aws account id.

```shell
aws ecr get-login-password --region us-east-1 --profile deployer | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
```

### Step9c: Build your docker images

```shell
docker build -t APP_NAME .
```

Tag your image and give it a version 1.0

```shell
docker tag APP_NAME:latest AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/APP_NAME:1.0
```

Push your image

```shell
docker push AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/APP_NAME:1.0
```

### Step 9d: Update your stack

Add the following code to your stack. Change the 'ckDomainName' to match your Route53 Hosted zone

```python
import { Construct } from 'constructs';
import {CkStack, CkStackProps} from "@cloudkitect/components";
import {CkServerlessContainerApps, CkServerlessWebsite} from "@cloudkitect/patterns"
import {Repository} from "aws-cdk-lib/aws-ecr";
import {Aws} from "aws-cdk-lib";
import {ContainerImage} from "aws-cdk-lib/aws-ecs";

export class MyProjectStack extends CkStack {
    constructor(scope: Construct, id: string, props: CkStackProps) {
        super(scope, id, props);

        new CkServerlessWebsite(this, 'TestSite', {
            ckDomainName: 'socalstartups.net',
            ckSubdomain: 'test',
            ckPathToContent: './site-content',
        });

        const repo = Repository.fromRepositoryAttributes(this, 'Repo', {
            repositoryArn: `arn:aws:ecr:${Aws.REGION}:${Aws.ACCOUNT_ID}:repository/addressbook`,
            repositoryName: 'addressbook',
        });

        const container = new CkServerlessContainerApps(this, 'NodeApp', {
            ckDomainName: 'socalstartups.net',
            ckSubDomain: 'app',
        });

        container.addService({
            ckServiceName: 'NodeAppService',
            ckImage: ContainerImage.fromEcrRepository(repo, '1.0'),
            ckContainerPort: 8080,
        });

    }
}
```

### Step 9e: Deploy our updated stack

Let's deploy the updated stack to our AWS account.

```shell
cdk deploy --require-approval never --profile deployer
```

### Step 9f: Verify Application

Once deployed it will output the endpoint of your application. Copy and paste it in your browser.

## Step 10: Destroy Application

Once you have verified clean up resources by destroying your stack and avoid further cost.

```shell
cdk destroy --profile deployer
```
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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

import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_ecs as _aws_cdk_aws_ecs_ceddda9d
import aws_cdk.aws_elasticloadbalancingv2 as _aws_cdk_aws_elasticloadbalancingv2_ceddda9d
import aws_cdk.aws_route53 as _aws_cdk_aws_route53_ceddda9d
import aws_cdk.aws_s3_deployment as _aws_cdk_aws_s3_deployment_ceddda9d
import cloudkitect.components as _cloudkitect_components_f1c376de
import constructs as _constructs_77d1e7e8


class CkServerlessContainerApps(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/patterns.CkServerlessContainerApps",
):
    '''CloudKitect Serverless Container App.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ck_domain_name: builtins.str,
        ck_sub_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ck_domain_name: Domain name.
        :param ck_sub_domain: Subdomain is usually the name of the microservice application such as user-app, account-app etc. Default: app
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c4cde542275507033d0e18ddecae8a5ddc89685cfff9383b6011bbe24e298f5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkServerlessContainerAppsProps(
            ck_domain_name=ck_domain_name, ck_sub_domain=ck_sub_domain
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addService")
    def add_service(
        self,
        *,
        ck_image: _aws_cdk_aws_ecs_ceddda9d.ContainerImage,
        ck_service_name: builtins.str,
        ck_container_port: typing.Optional[jsii.Number] = None,
        ck_health_check_path: typing.Optional[builtins.str] = None,
        ck_path_pattern: typing.Optional[builtins.str] = None,
        ck_service_priority: typing.Optional[jsii.Number] = None,
    ) -> "ServiceConfig":
        '''Adds a Microservice as a new ECS Service to the cluster It will have its own TaskDefinition and will run as a task managed by ECS Service.

        :param ck_image: Container image used for the task definition.
        :param ck_service_name: Service name e.g. UserService, FileService etc.
        :param ck_container_port: Port at which container listens for requests. Default: 80
        :param ck_health_check_path: Health check path. Default: /
        :param ck_path_pattern: Service Path e.g /user or /account. Default: /
        :param ck_service_priority: Priority of the service within the load balancer routing. Default: 1
        '''
        props = CkServiceProps(
            ck_image=ck_image,
            ck_service_name=ck_service_name,
            ck_container_port=ck_container_port,
            ck_health_check_path=ck_health_check_path,
            ck_path_pattern=ck_path_pattern,
            ck_service_priority=ck_service_priority,
        )

        return typing.cast("ServiceConfig", jsii.invoke(self, "addService", [props]))

    @builtins.property
    @jsii.member(jsii_name="cloudFront")
    def cloud_front(self) -> _cloudkitect_components_f1c376de.CkDistribution:
        '''CloudFront distribution created for sending traffic to load balancer.'''
        return typing.cast(_cloudkitect_components_f1c376de.CkDistribution, jsii.get(self, "cloudFront"))

    @builtins.property
    @jsii.member(jsii_name="fargateCluster")
    def fargate_cluster(self) -> _cloudkitect_components_f1c376de.CkFargateCluster:
        '''ECS fargate cluster.'''
        return typing.cast(_cloudkitect_components_f1c376de.CkFargateCluster, jsii.get(self, "fargateCluster"))

    @builtins.property
    @jsii.member(jsii_name="publicAlb")
    def public_alb(
        self,
    ) -> _cloudkitect_components_f1c376de.CkPublicApplicationLoadbalancer:
        '''Publicly accessible Application Load Balancer.'''
        return typing.cast(_cloudkitect_components_f1c376de.CkPublicApplicationLoadbalancer, jsii.get(self, "publicAlb"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> _cloudkitect_components_f1c376de.CkVpc:
        '''VPC where ECS cluster is launched.'''
        return typing.cast(_cloudkitect_components_f1c376de.CkVpc, jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="httpsListener")
    def https_listener(
        self,
    ) -> typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationListener]:
        '''Https Listener configured for the public ALB.'''
        return typing.cast(typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationListener], jsii.get(self, "httpsListener"))


@jsii.data_type(
    jsii_type="@cloudkitect/patterns.CkServerlessContainerAppsProps",
    jsii_struct_bases=[],
    name_mapping={"ck_domain_name": "ckDomainName", "ck_sub_domain": "ckSubDomain"},
)
class CkServerlessContainerAppsProps:
    def __init__(
        self,
        *,
        ck_domain_name: builtins.str,
        ck_sub_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Serverless container app properties.

        :param ck_domain_name: Domain name.
        :param ck_sub_domain: Subdomain is usually the name of the microservice application such as user-app, account-app etc. Default: app
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20ba5f59546a719d96e6d49943c7feef5f93dfb1880adcabadec577e2cef56a6)
            check_type(argname="argument ck_domain_name", value=ck_domain_name, expected_type=type_hints["ck_domain_name"])
            check_type(argname="argument ck_sub_domain", value=ck_sub_domain, expected_type=type_hints["ck_sub_domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ck_domain_name": ck_domain_name,
        }
        if ck_sub_domain is not None:
            self._values["ck_sub_domain"] = ck_sub_domain

    @builtins.property
    def ck_domain_name(self) -> builtins.str:
        '''Domain name.

        Example::

            cloudkitect.com
        '''
        result = self._values.get("ck_domain_name")
        assert result is not None, "Required property 'ck_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ck_sub_domain(self) -> typing.Optional[builtins.str]:
        '''Subdomain is usually the name of the microservice application such as user-app, account-app etc.

        :default: app
        '''
        result = self._values.get("ck_sub_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkServerlessContainerAppsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkServerlessWebsite(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/patterns.CkServerlessWebsite",
):
    '''CloudKitect Serverless Website Pattern Properties.



    Infrastructure Diagram



    Default Configuration

    Validated public certificate for the API domain
    Cloudfront Distribution

    Note: This construct expects a HostedZone present in the same AWS account


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Default Usage, if HostedZone is in the same account Example::

       new CkServerlessWebsite(this, "LogicalId", {
            ckDomainName: 'example.com',
            ckSubdomain: "www",
            ckPathToContent: './site-content'
       });


    Compliance

    It addresses the following compliance requirements

    1. Blocks public access
       .. epigraph::

          - Risk Level: Medium
          - Compliance: PCI, HIPAA, GDPR, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    2. Block S3 Bucket Public 'READ' Access
       .. epigraph::

          - Risk Level: Very High
          - Compliance: PCI, GDPR, ARPA, MAS, NIST4
          - Well Architected Pillar: Security

    3. Only allow secure transport protocols
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    4. Server side encryption
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, HIPAA, GDPR, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    5. S3 Bucket Block ACLs
       .. epigraph::

          - Risk Level: Very High
          - Compliance: PCI, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    6. Cloudfront origin should not use insecure protocols
       .. epigraph::

          - Risk Level: Medium
          - Compliance: PCI, HIPAA, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    7. Cloudfront uses enhanced security policy min TLS1.2
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, HIPAA, MAS, NIST4
          - Well Architected Pillar: Security

    8. Cloudfront uses only secure protocol to communicate with origin
       .. epigraph::

          - Risk Level: Medium
          - Compliance: PCI, HIPAA, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    9. Cloudfront uses only secure protocol to communicate with end users
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, HIPAA, NIST4
          - Well Architected Pillar: Security

    10. Enable origin access identify for S3 origins

    .. epigraph::

       - Risk Level: Medium
       - Compliance: NA
       - Well Architected Pillar: Security
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        name: builtins.str,
        *,
        ck_domain_name: builtins.str,
        ck_path_to_content: builtins.str,
        ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_default_root_object: typing.Optional[builtins.str] = None,
        ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
        ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
        ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
        ck_subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param name: -
        :param ck_domain_name: Domain name.
        :param ck_path_to_content: Location of website content.
        :param ck_bucket_policy_actions: Additional bucket policy actions. Default: s3:GetObject
        :param ck_bucket_props: Bucket properties to override defaults.
        :param ck_cloud_front_distribution_default_behavior: Override default CloudFront Distribution behavior.
        :param ck_default_root_object: Root object of the website, e.g. index.html. Default: index.html
        :param ck_enable_cloud_front_logging: Flag to enable or disable CloudFront logging. Default: false
        :param ck_hosted_zone: Hosted zone properties.
        :param ck_origin_access_identity: Origin Access Identity to override defaults. Default: A new one is created
        :param ck_subdomain: Subdomain name e.g. www. Default: www
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df46eade2f965a18ae612a14b78a1a6ab005428a64257ac72b2adcea0af1b0f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        props = CkServerlessWebsiteProps(
            ck_domain_name=ck_domain_name,
            ck_path_to_content=ck_path_to_content,
            ck_bucket_policy_actions=ck_bucket_policy_actions,
            ck_bucket_props=ck_bucket_props,
            ck_cloud_front_distribution_default_behavior=ck_cloud_front_distribution_default_behavior,
            ck_default_root_object=ck_default_root_object,
            ck_enable_cloud_front_logging=ck_enable_cloud_front_logging,
            ck_hosted_zone=ck_hosted_zone,
            ck_origin_access_identity=ck_origin_access_identity,
            ck_subdomain=ck_subdomain,
        )

        jsii.create(self.__class__, self, [scope, name, props])

    @jsii.member(jsii_name="getDistributionDomains")
    def get_distribution_domains(
        self,
        *,
        ck_domain_name: builtins.str,
        ck_path_to_content: builtins.str,
        ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_default_root_object: typing.Optional[builtins.str] = None,
        ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
        ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
        ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
        ck_subdomain: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''
        :param ck_domain_name: Domain name.
        :param ck_path_to_content: Location of website content.
        :param ck_bucket_policy_actions: Additional bucket policy actions. Default: s3:GetObject
        :param ck_bucket_props: Bucket properties to override defaults.
        :param ck_cloud_front_distribution_default_behavior: Override default CloudFront Distribution behavior.
        :param ck_default_root_object: Root object of the website, e.g. index.html. Default: index.html
        :param ck_enable_cloud_front_logging: Flag to enable or disable CloudFront logging. Default: false
        :param ck_hosted_zone: Hosted zone properties.
        :param ck_origin_access_identity: Origin Access Identity to override defaults. Default: A new one is created
        :param ck_subdomain: Subdomain name e.g. www. Default: www
        '''
        props = CkServerlessWebsiteProps(
            ck_domain_name=ck_domain_name,
            ck_path_to_content=ck_path_to_content,
            ck_bucket_policy_actions=ck_bucket_policy_actions,
            ck_bucket_props=ck_bucket_props,
            ck_cloud_front_distribution_default_behavior=ck_cloud_front_distribution_default_behavior,
            ck_default_root_object=ck_default_root_object,
            ck_enable_cloud_front_logging=ck_enable_cloud_front_logging,
            ck_hosted_zone=ck_hosted_zone,
            ck_origin_access_identity=ck_origin_access_identity,
            ck_subdomain=ck_subdomain,
        )

        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getDistributionDomains", [props]))

    @jsii.member(jsii_name="getSanCertificateDomains")
    def get_san_certificate_domains(
        self,
        *,
        ck_domain_name: builtins.str,
        ck_path_to_content: builtins.str,
        ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_default_root_object: typing.Optional[builtins.str] = None,
        ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
        ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
        ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
        ck_subdomain: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''
        :param ck_domain_name: Domain name.
        :param ck_path_to_content: Location of website content.
        :param ck_bucket_policy_actions: Additional bucket policy actions. Default: s3:GetObject
        :param ck_bucket_props: Bucket properties to override defaults.
        :param ck_cloud_front_distribution_default_behavior: Override default CloudFront Distribution behavior.
        :param ck_default_root_object: Root object of the website, e.g. index.html. Default: index.html
        :param ck_enable_cloud_front_logging: Flag to enable or disable CloudFront logging. Default: false
        :param ck_hosted_zone: Hosted zone properties.
        :param ck_origin_access_identity: Origin Access Identity to override defaults. Default: A new one is created
        :param ck_subdomain: Subdomain name e.g. www. Default: www
        '''
        props = CkServerlessWebsiteProps(
            ck_domain_name=ck_domain_name,
            ck_path_to_content=ck_path_to_content,
            ck_bucket_policy_actions=ck_bucket_policy_actions,
            ck_bucket_props=ck_bucket_props,
            ck_cloud_front_distribution_default_behavior=ck_cloud_front_distribution_default_behavior,
            ck_default_root_object=ck_default_root_object,
            ck_enable_cloud_front_logging=ck_enable_cloud_front_logging,
            ck_hosted_zone=ck_hosted_zone,
            ck_origin_access_identity=ck_origin_access_identity,
            ck_subdomain=ck_subdomain,
        )

        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getSanCertificateDomains", [props]))

    @jsii.member(jsii_name="getSiteDomain")
    def get_site_domain(
        self,
        *,
        ck_domain_name: builtins.str,
        ck_path_to_content: builtins.str,
        ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_default_root_object: typing.Optional[builtins.str] = None,
        ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
        ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
        ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
        ck_subdomain: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''
        :param ck_domain_name: Domain name.
        :param ck_path_to_content: Location of website content.
        :param ck_bucket_policy_actions: Additional bucket policy actions. Default: s3:GetObject
        :param ck_bucket_props: Bucket properties to override defaults.
        :param ck_cloud_front_distribution_default_behavior: Override default CloudFront Distribution behavior.
        :param ck_default_root_object: Root object of the website, e.g. index.html. Default: index.html
        :param ck_enable_cloud_front_logging: Flag to enable or disable CloudFront logging. Default: false
        :param ck_hosted_zone: Hosted zone properties.
        :param ck_origin_access_identity: Origin Access Identity to override defaults. Default: A new one is created
        :param ck_subdomain: Subdomain name e.g. www. Default: www
        '''
        props = CkServerlessWebsiteProps(
            ck_domain_name=ck_domain_name,
            ck_path_to_content=ck_path_to_content,
            ck_bucket_policy_actions=ck_bucket_policy_actions,
            ck_bucket_props=ck_bucket_props,
            ck_cloud_front_distribution_default_behavior=ck_cloud_front_distribution_default_behavior,
            ck_default_root_object=ck_default_root_object,
            ck_enable_cloud_front_logging=ck_enable_cloud_front_logging,
            ck_hosted_zone=ck_hosted_zone,
            ck_origin_access_identity=ck_origin_access_identity,
            ck_subdomain=ck_subdomain,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "getSiteDomain", [props]))

    @builtins.property
    @jsii.member(jsii_name="bucketDeployment")
    def bucket_deployment(self) -> _aws_cdk_aws_s3_deployment_ceddda9d.BucketDeployment:
        '''Bucket deployment.'''
        return typing.cast(_aws_cdk_aws_s3_deployment_ceddda9d.BucketDeployment, jsii.get(self, "bucketDeployment"))

    @builtins.property
    @jsii.member(jsii_name="cdn")
    def cdn(self) -> _cloudkitect_components_f1c376de.CkDistribution:
        '''CloudFront distribution used in this construct.'''
        return typing.cast(_cloudkitect_components_f1c376de.CkDistribution, jsii.get(self, "cdn"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontOAI")
    def cloudfront_oai(self) -> _aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity:
        '''Origin Access Identity.'''
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity, jsii.get(self, "cloudfrontOAI"))

    @builtins.property
    @jsii.member(jsii_name="websiteBucket")
    def website_bucket(self) -> _cloudkitect_components_f1c376de.CkBucket:
        '''Bucket hosting website content.'''
        return typing.cast(_cloudkitect_components_f1c376de.CkBucket, jsii.get(self, "websiteBucket"))


@jsii.data_type(
    jsii_type="@cloudkitect/patterns.CkServerlessWebsiteProps",
    jsii_struct_bases=[],
    name_mapping={
        "ck_domain_name": "ckDomainName",
        "ck_path_to_content": "ckPathToContent",
        "ck_bucket_policy_actions": "ckBucketPolicyActions",
        "ck_bucket_props": "ckBucketProps",
        "ck_cloud_front_distribution_default_behavior": "ckCloudFrontDistributionDefaultBehavior",
        "ck_default_root_object": "ckDefaultRootObject",
        "ck_enable_cloud_front_logging": "ckEnableCloudFrontLogging",
        "ck_hosted_zone": "ckHostedZone",
        "ck_origin_access_identity": "ckOriginAccessIdentity",
        "ck_subdomain": "ckSubdomain",
    },
)
class CkServerlessWebsiteProps:
    def __init__(
        self,
        *,
        ck_domain_name: builtins.str,
        ck_path_to_content: builtins.str,
        ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        ck_default_root_object: typing.Optional[builtins.str] = None,
        ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
        ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
        ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
        ck_subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CloudKitect Serverless Website Pattern Properties.

        :param ck_domain_name: Domain name.
        :param ck_path_to_content: Location of website content.
        :param ck_bucket_policy_actions: Additional bucket policy actions. Default: s3:GetObject
        :param ck_bucket_props: Bucket properties to override defaults.
        :param ck_cloud_front_distribution_default_behavior: Override default CloudFront Distribution behavior.
        :param ck_default_root_object: Root object of the website, e.g. index.html. Default: index.html
        :param ck_enable_cloud_front_logging: Flag to enable or disable CloudFront logging. Default: false
        :param ck_hosted_zone: Hosted zone properties.
        :param ck_origin_access_identity: Origin Access Identity to override defaults. Default: A new one is created
        :param ck_subdomain: Subdomain name e.g. www. Default: www
        '''
        if isinstance(ck_bucket_props, dict):
            ck_bucket_props = _cloudkitect_components_f1c376de.CkBucketProps(**ck_bucket_props)
        if isinstance(ck_cloud_front_distribution_default_behavior, dict):
            ck_cloud_front_distribution_default_behavior = _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions(**ck_cloud_front_distribution_default_behavior)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95cf5dd5288d073fc94b6e7ecdfe8fc3337f4923161522b6ec7f669e757a76c6)
            check_type(argname="argument ck_domain_name", value=ck_domain_name, expected_type=type_hints["ck_domain_name"])
            check_type(argname="argument ck_path_to_content", value=ck_path_to_content, expected_type=type_hints["ck_path_to_content"])
            check_type(argname="argument ck_bucket_policy_actions", value=ck_bucket_policy_actions, expected_type=type_hints["ck_bucket_policy_actions"])
            check_type(argname="argument ck_bucket_props", value=ck_bucket_props, expected_type=type_hints["ck_bucket_props"])
            check_type(argname="argument ck_cloud_front_distribution_default_behavior", value=ck_cloud_front_distribution_default_behavior, expected_type=type_hints["ck_cloud_front_distribution_default_behavior"])
            check_type(argname="argument ck_default_root_object", value=ck_default_root_object, expected_type=type_hints["ck_default_root_object"])
            check_type(argname="argument ck_enable_cloud_front_logging", value=ck_enable_cloud_front_logging, expected_type=type_hints["ck_enable_cloud_front_logging"])
            check_type(argname="argument ck_hosted_zone", value=ck_hosted_zone, expected_type=type_hints["ck_hosted_zone"])
            check_type(argname="argument ck_origin_access_identity", value=ck_origin_access_identity, expected_type=type_hints["ck_origin_access_identity"])
            check_type(argname="argument ck_subdomain", value=ck_subdomain, expected_type=type_hints["ck_subdomain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ck_domain_name": ck_domain_name,
            "ck_path_to_content": ck_path_to_content,
        }
        if ck_bucket_policy_actions is not None:
            self._values["ck_bucket_policy_actions"] = ck_bucket_policy_actions
        if ck_bucket_props is not None:
            self._values["ck_bucket_props"] = ck_bucket_props
        if ck_cloud_front_distribution_default_behavior is not None:
            self._values["ck_cloud_front_distribution_default_behavior"] = ck_cloud_front_distribution_default_behavior
        if ck_default_root_object is not None:
            self._values["ck_default_root_object"] = ck_default_root_object
        if ck_enable_cloud_front_logging is not None:
            self._values["ck_enable_cloud_front_logging"] = ck_enable_cloud_front_logging
        if ck_hosted_zone is not None:
            self._values["ck_hosted_zone"] = ck_hosted_zone
        if ck_origin_access_identity is not None:
            self._values["ck_origin_access_identity"] = ck_origin_access_identity
        if ck_subdomain is not None:
            self._values["ck_subdomain"] = ck_subdomain

    @builtins.property
    def ck_domain_name(self) -> builtins.str:
        '''Domain name.'''
        result = self._values.get("ck_domain_name")
        assert result is not None, "Required property 'ck_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ck_path_to_content(self) -> builtins.str:
        '''Location of website content.'''
        result = self._values.get("ck_path_to_content")
        assert result is not None, "Required property 'ck_path_to_content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ck_bucket_policy_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional bucket policy actions.

        :default: s3:GetObject
        '''
        result = self._values.get("ck_bucket_policy_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ck_bucket_props(
        self,
    ) -> typing.Optional[_cloudkitect_components_f1c376de.CkBucketProps]:
        '''Bucket properties to override defaults.'''
        result = self._values.get("ck_bucket_props")
        return typing.cast(typing.Optional[_cloudkitect_components_f1c376de.CkBucketProps], result)

    @builtins.property
    def ck_cloud_front_distribution_default_behavior(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]:
        '''Override default CloudFront Distribution behavior.'''
        result = self._values.get("ck_cloud_front_distribution_default_behavior")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions], result)

    @builtins.property
    def ck_default_root_object(self) -> typing.Optional[builtins.str]:
        '''Root object of the website, e.g. index.html.

        :default: index.html
        '''
        result = self._values.get("ck_default_root_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ck_enable_cloud_front_logging(self) -> typing.Optional[builtins.bool]:
        '''Flag to enable or disable CloudFront logging.

        :default: false
        '''
        result = self._values.get("ck_enable_cloud_front_logging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ck_hosted_zone(
        self,
    ) -> typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone]:
        '''Hosted zone properties.'''
        result = self._values.get("ck_hosted_zone")
        return typing.cast(typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone], result)

    @builtins.property
    def ck_origin_access_identity(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity]:
        '''Origin Access Identity to override defaults.

        :default: A new one is created
        '''
        result = self._values.get("ck_origin_access_identity")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity], result)

    @builtins.property
    def ck_subdomain(self) -> typing.Optional[builtins.str]:
        '''Subdomain name e.g. www.

        :default: www
        '''
        result = self._values.get("ck_subdomain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkServerlessWebsiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudkitect/patterns.CkServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "ck_image": "ckImage",
        "ck_service_name": "ckServiceName",
        "ck_container_port": "ckContainerPort",
        "ck_health_check_path": "ckHealthCheckPath",
        "ck_path_pattern": "ckPathPattern",
        "ck_service_priority": "ckServicePriority",
    },
)
class CkServiceProps:
    def __init__(
        self,
        *,
        ck_image: _aws_cdk_aws_ecs_ceddda9d.ContainerImage,
        ck_service_name: builtins.str,
        ck_container_port: typing.Optional[jsii.Number] = None,
        ck_health_check_path: typing.Optional[builtins.str] = None,
        ck_path_pattern: typing.Optional[builtins.str] = None,
        ck_service_priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties that are used to customize the service.

        You can add multiple services behind the load balancer using addService() method
        and passing these properties for customization.

        :param ck_image: Container image used for the task definition.
        :param ck_service_name: Service name e.g. UserService, FileService etc.
        :param ck_container_port: Port at which container listens for requests. Default: 80
        :param ck_health_check_path: Health check path. Default: /
        :param ck_path_pattern: Service Path e.g /user or /account. Default: /
        :param ck_service_priority: Priority of the service within the load balancer routing. Default: 1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d98a04d8a449c6ca5674b2ef8580b0715e77104a62921d47721a34aa5b983fb)
            check_type(argname="argument ck_image", value=ck_image, expected_type=type_hints["ck_image"])
            check_type(argname="argument ck_service_name", value=ck_service_name, expected_type=type_hints["ck_service_name"])
            check_type(argname="argument ck_container_port", value=ck_container_port, expected_type=type_hints["ck_container_port"])
            check_type(argname="argument ck_health_check_path", value=ck_health_check_path, expected_type=type_hints["ck_health_check_path"])
            check_type(argname="argument ck_path_pattern", value=ck_path_pattern, expected_type=type_hints["ck_path_pattern"])
            check_type(argname="argument ck_service_priority", value=ck_service_priority, expected_type=type_hints["ck_service_priority"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ck_image": ck_image,
            "ck_service_name": ck_service_name,
        }
        if ck_container_port is not None:
            self._values["ck_container_port"] = ck_container_port
        if ck_health_check_path is not None:
            self._values["ck_health_check_path"] = ck_health_check_path
        if ck_path_pattern is not None:
            self._values["ck_path_pattern"] = ck_path_pattern
        if ck_service_priority is not None:
            self._values["ck_service_priority"] = ck_service_priority

    @builtins.property
    def ck_image(self) -> _aws_cdk_aws_ecs_ceddda9d.ContainerImage:
        '''Container image used for the task definition.'''
        result = self._values.get("ck_image")
        assert result is not None, "Required property 'ck_image' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.ContainerImage, result)

    @builtins.property
    def ck_service_name(self) -> builtins.str:
        '''Service name e.g. UserService, FileService etc.'''
        result = self._values.get("ck_service_name")
        assert result is not None, "Required property 'ck_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ck_container_port(self) -> typing.Optional[jsii.Number]:
        '''Port at which container listens for requests.

        :default: 80
        '''
        result = self._values.get("ck_container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ck_health_check_path(self) -> typing.Optional[builtins.str]:
        '''Health check path.

        :default: /
        '''
        result = self._values.get("ck_health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ck_path_pattern(self) -> typing.Optional[builtins.str]:
        '''Service Path e.g /user or /account.

        :default: /
        '''
        result = self._values.get("ck_path_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ck_service_priority(self) -> typing.Optional[jsii.Number]:
        '''Priority of the service within the load balancer routing.

        :default: 1
        '''
        result = self._values.get("ck_service_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudkitect/patterns.ServiceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "container_def": "containerDef",
        "ecs_service": "ecsService",
        "fargate_security_group": "fargateSecurityGroup",
        "fargate_task_definition": "fargateTaskDefinition",
    },
)
class ServiceConfig:
    def __init__(
        self,
        *,
        container_def: _aws_cdk_aws_ecs_ceddda9d.ContainerDefinition,
        ecs_service: _cloudkitect_components_f1c376de.CkFargateService,
        fargate_security_group: _aws_cdk_aws_ec2_ceddda9d.SecurityGroup,
        fargate_task_definition: _cloudkitect_components_f1c376de.CkFargateTaskDefinition,
    ) -> None:
        '''Information regarding how the service is configured, can be used to customize certain aspects of the service.

        :param container_def: Container Definition.
        :param ecs_service: Fargate ECS Service.
        :param fargate_security_group: Fargate security group.
        :param fargate_task_definition: Fargate task definition.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d9476caa95770be0fbc67098df0356e17ffc2027e05d3d20ad9cb10638f9a13)
            check_type(argname="argument container_def", value=container_def, expected_type=type_hints["container_def"])
            check_type(argname="argument ecs_service", value=ecs_service, expected_type=type_hints["ecs_service"])
            check_type(argname="argument fargate_security_group", value=fargate_security_group, expected_type=type_hints["fargate_security_group"])
            check_type(argname="argument fargate_task_definition", value=fargate_task_definition, expected_type=type_hints["fargate_task_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_def": container_def,
            "ecs_service": ecs_service,
            "fargate_security_group": fargate_security_group,
            "fargate_task_definition": fargate_task_definition,
        }

    @builtins.property
    def container_def(self) -> _aws_cdk_aws_ecs_ceddda9d.ContainerDefinition:
        '''Container Definition.'''
        result = self._values.get("container_def")
        assert result is not None, "Required property 'container_def' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.ContainerDefinition, result)

    @builtins.property
    def ecs_service(self) -> _cloudkitect_components_f1c376de.CkFargateService:
        '''Fargate ECS Service.'''
        result = self._values.get("ecs_service")
        assert result is not None, "Required property 'ecs_service' is missing"
        return typing.cast(_cloudkitect_components_f1c376de.CkFargateService, result)

    @builtins.property
    def fargate_security_group(self) -> _aws_cdk_aws_ec2_ceddda9d.SecurityGroup:
        '''Fargate security group.'''
        result = self._values.get("fargate_security_group")
        assert result is not None, "Required property 'fargate_security_group' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.SecurityGroup, result)

    @builtins.property
    def fargate_task_definition(
        self,
    ) -> _cloudkitect_components_f1c376de.CkFargateTaskDefinition:
        '''Fargate task definition.'''
        result = self._values.get("fargate_task_definition")
        assert result is not None, "Required property 'fargate_task_definition' is missing"
        return typing.cast(_cloudkitect_components_f1c376de.CkFargateTaskDefinition, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CkServerlessContainerApps",
    "CkServerlessContainerAppsProps",
    "CkServerlessWebsite",
    "CkServerlessWebsiteProps",
    "CkServiceProps",
    "ServiceConfig",
]

publication.publish()

def _typecheckingstub__9c4cde542275507033d0e18ddecae8a5ddc89685cfff9383b6011bbe24e298f5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ck_domain_name: builtins.str,
    ck_sub_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ba5f59546a719d96e6d49943c7feef5f93dfb1880adcabadec577e2cef56a6(
    *,
    ck_domain_name: builtins.str,
    ck_sub_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df46eade2f965a18ae612a14b78a1a6ab005428a64257ac72b2adcea0af1b0f0(
    scope: _constructs_77d1e7e8.Construct,
    name: builtins.str,
    *,
    ck_domain_name: builtins.str,
    ck_path_to_content: builtins.str,
    ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ck_default_root_object: typing.Optional[builtins.str] = None,
    ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
    ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
    ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
    ck_subdomain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95cf5dd5288d073fc94b6e7ecdfe8fc3337f4923161522b6ec7f669e757a76c6(
    *,
    ck_domain_name: builtins.str,
    ck_path_to_content: builtins.str,
    ck_bucket_policy_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ck_bucket_props: typing.Optional[typing.Union[_cloudkitect_components_f1c376de.CkBucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ck_cloud_front_distribution_default_behavior: typing.Optional[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ck_default_root_object: typing.Optional[builtins.str] = None,
    ck_enable_cloud_front_logging: typing.Optional[builtins.bool] = None,
    ck_hosted_zone: typing.Optional[_aws_cdk_aws_route53_ceddda9d.IHostedZone] = None,
    ck_origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.OriginAccessIdentity] = None,
    ck_subdomain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d98a04d8a449c6ca5674b2ef8580b0715e77104a62921d47721a34aa5b983fb(
    *,
    ck_image: _aws_cdk_aws_ecs_ceddda9d.ContainerImage,
    ck_service_name: builtins.str,
    ck_container_port: typing.Optional[jsii.Number] = None,
    ck_health_check_path: typing.Optional[builtins.str] = None,
    ck_path_pattern: typing.Optional[builtins.str] = None,
    ck_service_priority: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9476caa95770be0fbc67098df0356e17ffc2027e05d3d20ad9cb10638f9a13(
    *,
    container_def: _aws_cdk_aws_ecs_ceddda9d.ContainerDefinition,
    ecs_service: _cloudkitect_components_f1c376de.CkFargateService,
    fargate_security_group: _aws_cdk_aws_ec2_ceddda9d.SecurityGroup,
    fargate_task_definition: _cloudkitect_components_f1c376de.CkFargateTaskDefinition,
) -> None:
    """Type checking stubs"""
    pass
