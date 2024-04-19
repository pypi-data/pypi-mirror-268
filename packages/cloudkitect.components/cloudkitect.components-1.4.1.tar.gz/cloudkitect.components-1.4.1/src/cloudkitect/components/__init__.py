'''
# About CloudKitect

CloudKitect revolutionizes the way technology organizations adopt cloud computing by providing innovative, secure,
and cost-effective turnkey solution that fast-tracks the AWS Adoption.
Think of CloudKitect as Cloud Architect as a Service.

# About CloudKitect Components.

This repository includes freemium version of CloudKitect components.
They are available under a freemium model and meet a subset of compliance requirements in
contrast to CloudKitect Enhanced components, which conform to a broader range of compliance
standards including CIS, PCI, MAS, NIST-800, ARP, GDPR, and others.

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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_certificatemanager as _aws_cdk_aws_certificatemanager_ceddda9d
import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_ceddda9d
import aws_cdk.aws_dynamodb as _aws_cdk_aws_dynamodb_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_ecr as _aws_cdk_aws_ecr_ceddda9d
import aws_cdk.aws_ecs as _aws_cdk_aws_ecs_ceddda9d
import aws_cdk.aws_elasticloadbalancingv2 as _aws_cdk_aws_elasticloadbalancingv2_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_kinesis as _aws_cdk_aws_kinesis_ceddda9d
import aws_cdk.aws_kms as _aws_cdk_aws_kms_ceddda9d
import aws_cdk.aws_route53 as _aws_cdk_aws_route53_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.enum(jsii_type="@cloudkitect/components.CkAccountType")
class CkAccountType(enum.Enum):
    '''Well Architected Stack supports the following environments.'''

    DEVELOPMENT = "DEVELOPMENT"
    TEST = "TEST"
    UAT = "UAT"
    PRODUCTION = "PRODUCTION"


class CkBucket(
    _aws_cdk_aws_s3_ceddda9d.Bucket,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkBucket",
):
    '''CloudKitect S3 Bucket component.



    Default Configuration

    Encryption: S3 Managed
    Versioned: True
    Removal Policy: Retain in Production


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components

    Note that the default alarm uses the CcAlarm construct, which sets up an alarm
    action to notify the SNS Topic *AlarmEventsTopic* by default.


    Examples

    Default Usage Example::

       new CkBucket(this, "LogicalId", {
       });

    Custom Configuration Example::

       new CkBucket(this, "LogicalId", {
          enforceSSL: false
       });


    Compliance

    It addresses the following compliance requirements

    1. Blocks public access
       .. epigraph::

          - Risk Level: Medium
          - Compliance: PCI, HIPAA, GDPR, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    2. Bucket versioning enabled in Production Environment
       .. epigraph::

          - Risk Level: Low
          - Compliance: PCI, APRA, MAS, NIST4
          - Well Architected Pillar: Reliability

    3. Block S3 Bucket Public 'READ' Access
       .. epigraph::

          - Risk Level: Very High
          - Compliance: PCI, GDPR, ARPA, MAS, NIST4
          - Well Architected Pillar: Security

    4. Only allow secure transport protocols
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    5. Server side encryption
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, HIPAA, GDPR, APRA, MAS, NIST4
          - Well Architected Pillar: Security
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_control: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketAccessControl] = None,
        auto_delete_objects: typing.Optional[builtins.bool] = None,
        block_public_access: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BlockPublicAccess] = None,
        bucket_key_enabled: typing.Optional[builtins.bool] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        cors: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.CorsRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        encryption: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketEncryption] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        enforce_ssl: typing.Optional[builtins.bool] = None,
        event_bridge_enabled: typing.Optional[builtins.bool] = None,
        intelligent_tiering_configurations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.IntelligentTieringConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
        inventories: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.Inventory, typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        metrics: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketMetrics, typing.Dict[builtins.str, typing.Any]]]] = None,
        minimum_tls_version: typing.Optional[jsii.Number] = None,
        notifications_handler_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        object_lock_default_retention: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectLockRetention] = None,
        object_lock_enabled: typing.Optional[builtins.bool] = None,
        object_ownership: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectOwnership] = None,
        public_read_access: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        server_access_logs_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        server_access_logs_prefix: typing.Optional[builtins.str] = None,
        target_object_key_format: typing.Optional[_aws_cdk_aws_s3_ceddda9d.TargetObjectKeyFormat] = None,
        transfer_acceleration: typing.Optional[builtins.bool] = None,
        versioned: typing.Optional[builtins.bool] = None,
        website_error_document: typing.Optional[builtins.str] = None,
        website_index_document: typing.Optional[builtins.str] = None,
        website_redirect: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.RedirectTarget, typing.Dict[builtins.str, typing.Any]]] = None,
        website_routing_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.RoutingRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_control: Specifies a canned ACL that grants predefined permissions to the bucket. Default: BucketAccessControl.PRIVATE
        :param auto_delete_objects: Whether all objects should be automatically deleted when the bucket is removed from the stack or when the stack is deleted. Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``. **Warning** if you have deployed a bucket with ``autoDeleteObjects: true``, switching this to ``false`` in a CDK version *before* ``1.126.0`` will lead to all objects in the bucket being deleted. Be sure to update your bucket resources by deploying with CDK version ``1.126.0`` or later **before** switching this value to ``false``. Default: false
        :param block_public_access: The block public access configuration of this bucket. Default: - CloudFormation defaults will apply. New buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access
        :param bucket_key_enabled: Whether Amazon S3 should use its own intermediary key to generate data keys. Only relevant when using KMS for encryption. - If not enabled, every object GET and PUT will cause an API call to KMS (with the attendant cost implications of that). - If enabled, S3 will use its own time-limited key instead. Only relevant, when Encryption is set to ``BucketEncryption.KMS`` or ``BucketEncryption.KMS_MANAGED``. Default: - false
        :param bucket_name: Physical name of this bucket. Default: - Assigned by CloudFormation (recommended).
        :param cors: The CORS configuration of this bucket. Default: - No CORS configuration.
        :param encryption: The kind of server-side encryption to apply to this bucket. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``UNENCRYPTED`` otherwise. But if ``UNENCRYPTED`` is specified, the bucket will be encrypted as ``S3_MANAGED`` automatically.
        :param encryption_key: External KMS key to use for bucket encryption. The ``encryption`` property must be either not specified or set to ``KMS`` or ``DSSE``. An error will be emitted if ``encryption`` is set to ``UNENCRYPTED`` or ``S3_MANAGED``. Default: - If ``encryption`` is set to ``KMS`` and this property is undefined, a new KMS key will be created and associated with this bucket.
        :param enforce_ssl: Enforces SSL for requests. S3.5 of the AWS Foundational Security Best Practices Regarding S3. Default: false
        :param event_bridge_enabled: Whether this bucket should send notifications to Amazon EventBridge or not. Default: false
        :param intelligent_tiering_configurations: Inteligent Tiering Configurations. Default: No Intelligent Tiiering Configurations.
        :param inventories: The inventory configuration of the bucket. Default: - No inventory configuration
        :param lifecycle_rules: Rules that define how Amazon S3 manages objects during their lifetime. Default: - No lifecycle rules.
        :param metrics: The metrics configuration of this bucket. Default: - No metrics configuration.
        :param minimum_tls_version: Enforces minimum TLS version for requests. Requires ``enforceSSL`` to be enabled. Default: No minimum TLS version is enforced.
        :param notifications_handler_role: The role to be used by the notifications handler. Default: - a new role will be created.
        :param object_lock_default_retention: The default retention mode and rules for S3 Object Lock. Default retention can be configured after a bucket is created if the bucket already has object lock enabled. Enabling object lock for existing buckets is not supported. Default: no default retention period
        :param object_lock_enabled: Enable object lock on the bucket. Enabling object lock for existing buckets is not supported. Object lock must be enabled when the bucket is created. Default: false, unless objectLockDefaultRetention is set (then, true)
        :param object_ownership: The objectOwnership of the bucket. Default: - No ObjectOwnership configuration, uploading account will own the object.
        :param public_read_access: Grants public read access to all objects in the bucket. Similar to calling ``bucket.grantPublicAccess()`` Default: false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param server_access_logs_bucket: Destination bucket for the server access logs. Default: - If "serverAccessLogsPrefix" undefined - access logs disabled, otherwise - log to current bucket.
        :param server_access_logs_prefix: Optional log file prefix to use for the bucket's access logs. If defined without "serverAccessLogsBucket", enables access logs to current bucket with this prefix. Default: - No log file prefix
        :param target_object_key_format: Optional key format for log objects. Default: - the default key format is: [DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
        :param transfer_acceleration: Whether this bucket should have transfer acceleration turned on or not. Default: false
        :param versioned: Whether this bucket should have versioning turned on or not. Default: false (unless object lock is enabled, then true)
        :param website_error_document: The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set. Default: - No error document.
        :param website_index_document: The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket. Default: - No index document.
        :param website_redirect: Specifies the redirect behavior of all requests to a website endpoint of a bucket. If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules". Default: - No redirection.
        :param website_routing_rules: Rules that define when a redirect is applied and the redirect behavior. Default: - No redirection rules.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__305950b3a114851fa68ea7e16c0814b62283c5e5d995e7d52f848f00a1490c2a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkBucketProps(
            access_control=access_control,
            auto_delete_objects=auto_delete_objects,
            block_public_access=block_public_access,
            bucket_key_enabled=bucket_key_enabled,
            bucket_name=bucket_name,
            cors=cors,
            encryption=encryption,
            encryption_key=encryption_key,
            enforce_ssl=enforce_ssl,
            event_bridge_enabled=event_bridge_enabled,
            intelligent_tiering_configurations=intelligent_tiering_configurations,
            inventories=inventories,
            lifecycle_rules=lifecycle_rules,
            metrics=metrics,
            minimum_tls_version=minimum_tls_version,
            notifications_handler_role=notifications_handler_role,
            object_lock_default_retention=object_lock_default_retention,
            object_lock_enabled=object_lock_enabled,
            object_ownership=object_ownership,
            public_read_access=public_read_access,
            removal_policy=removal_policy,
            server_access_logs_bucket=server_access_logs_bucket,
            server_access_logs_prefix=server_access_logs_prefix,
            target_object_key_format=target_object_key_format,
            transfer_acceleration=transfer_acceleration,
            versioned=versioned,
            website_error_document=website_error_document,
            website_index_document=website_index_document,
            website_redirect=website_redirect,
            website_routing_rules=website_routing_rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkBucketProps",
    jsii_struct_bases=[_aws_cdk_aws_s3_ceddda9d.BucketProps],
    name_mapping={
        "access_control": "accessControl",
        "auto_delete_objects": "autoDeleteObjects",
        "block_public_access": "blockPublicAccess",
        "bucket_key_enabled": "bucketKeyEnabled",
        "bucket_name": "bucketName",
        "cors": "cors",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "enforce_ssl": "enforceSSL",
        "event_bridge_enabled": "eventBridgeEnabled",
        "intelligent_tiering_configurations": "intelligentTieringConfigurations",
        "inventories": "inventories",
        "lifecycle_rules": "lifecycleRules",
        "metrics": "metrics",
        "minimum_tls_version": "minimumTLSVersion",
        "notifications_handler_role": "notificationsHandlerRole",
        "object_lock_default_retention": "objectLockDefaultRetention",
        "object_lock_enabled": "objectLockEnabled",
        "object_ownership": "objectOwnership",
        "public_read_access": "publicReadAccess",
        "removal_policy": "removalPolicy",
        "server_access_logs_bucket": "serverAccessLogsBucket",
        "server_access_logs_prefix": "serverAccessLogsPrefix",
        "target_object_key_format": "targetObjectKeyFormat",
        "transfer_acceleration": "transferAcceleration",
        "versioned": "versioned",
        "website_error_document": "websiteErrorDocument",
        "website_index_document": "websiteIndexDocument",
        "website_redirect": "websiteRedirect",
        "website_routing_rules": "websiteRoutingRules",
    },
)
class CkBucketProps(_aws_cdk_aws_s3_ceddda9d.BucketProps):
    def __init__(
        self,
        *,
        access_control: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketAccessControl] = None,
        auto_delete_objects: typing.Optional[builtins.bool] = None,
        block_public_access: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BlockPublicAccess] = None,
        bucket_key_enabled: typing.Optional[builtins.bool] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        cors: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.CorsRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        encryption: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketEncryption] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        enforce_ssl: typing.Optional[builtins.bool] = None,
        event_bridge_enabled: typing.Optional[builtins.bool] = None,
        intelligent_tiering_configurations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.IntelligentTieringConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
        inventories: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.Inventory, typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        metrics: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketMetrics, typing.Dict[builtins.str, typing.Any]]]] = None,
        minimum_tls_version: typing.Optional[jsii.Number] = None,
        notifications_handler_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        object_lock_default_retention: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectLockRetention] = None,
        object_lock_enabled: typing.Optional[builtins.bool] = None,
        object_ownership: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectOwnership] = None,
        public_read_access: typing.Optional[builtins.bool] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        server_access_logs_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        server_access_logs_prefix: typing.Optional[builtins.str] = None,
        target_object_key_format: typing.Optional[_aws_cdk_aws_s3_ceddda9d.TargetObjectKeyFormat] = None,
        transfer_acceleration: typing.Optional[builtins.bool] = None,
        versioned: typing.Optional[builtins.bool] = None,
        website_error_document: typing.Optional[builtins.str] = None,
        website_index_document: typing.Optional[builtins.str] = None,
        website_redirect: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.RedirectTarget, typing.Dict[builtins.str, typing.Any]]] = None,
        website_routing_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.RoutingRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''CloudKitect Bucket component properties.

        :param access_control: Specifies a canned ACL that grants predefined permissions to the bucket. Default: BucketAccessControl.PRIVATE
        :param auto_delete_objects: Whether all objects should be automatically deleted when the bucket is removed from the stack or when the stack is deleted. Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``. **Warning** if you have deployed a bucket with ``autoDeleteObjects: true``, switching this to ``false`` in a CDK version *before* ``1.126.0`` will lead to all objects in the bucket being deleted. Be sure to update your bucket resources by deploying with CDK version ``1.126.0`` or later **before** switching this value to ``false``. Default: false
        :param block_public_access: The block public access configuration of this bucket. Default: - CloudFormation defaults will apply. New buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access
        :param bucket_key_enabled: Whether Amazon S3 should use its own intermediary key to generate data keys. Only relevant when using KMS for encryption. - If not enabled, every object GET and PUT will cause an API call to KMS (with the attendant cost implications of that). - If enabled, S3 will use its own time-limited key instead. Only relevant, when Encryption is set to ``BucketEncryption.KMS`` or ``BucketEncryption.KMS_MANAGED``. Default: - false
        :param bucket_name: Physical name of this bucket. Default: - Assigned by CloudFormation (recommended).
        :param cors: The CORS configuration of this bucket. Default: - No CORS configuration.
        :param encryption: The kind of server-side encryption to apply to this bucket. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``UNENCRYPTED`` otherwise. But if ``UNENCRYPTED`` is specified, the bucket will be encrypted as ``S3_MANAGED`` automatically.
        :param encryption_key: External KMS key to use for bucket encryption. The ``encryption`` property must be either not specified or set to ``KMS`` or ``DSSE``. An error will be emitted if ``encryption`` is set to ``UNENCRYPTED`` or ``S3_MANAGED``. Default: - If ``encryption`` is set to ``KMS`` and this property is undefined, a new KMS key will be created and associated with this bucket.
        :param enforce_ssl: Enforces SSL for requests. S3.5 of the AWS Foundational Security Best Practices Regarding S3. Default: false
        :param event_bridge_enabled: Whether this bucket should send notifications to Amazon EventBridge or not. Default: false
        :param intelligent_tiering_configurations: Inteligent Tiering Configurations. Default: No Intelligent Tiiering Configurations.
        :param inventories: The inventory configuration of the bucket. Default: - No inventory configuration
        :param lifecycle_rules: Rules that define how Amazon S3 manages objects during their lifetime. Default: - No lifecycle rules.
        :param metrics: The metrics configuration of this bucket. Default: - No metrics configuration.
        :param minimum_tls_version: Enforces minimum TLS version for requests. Requires ``enforceSSL`` to be enabled. Default: No minimum TLS version is enforced.
        :param notifications_handler_role: The role to be used by the notifications handler. Default: - a new role will be created.
        :param object_lock_default_retention: The default retention mode and rules for S3 Object Lock. Default retention can be configured after a bucket is created if the bucket already has object lock enabled. Enabling object lock for existing buckets is not supported. Default: no default retention period
        :param object_lock_enabled: Enable object lock on the bucket. Enabling object lock for existing buckets is not supported. Object lock must be enabled when the bucket is created. Default: false, unless objectLockDefaultRetention is set (then, true)
        :param object_ownership: The objectOwnership of the bucket. Default: - No ObjectOwnership configuration, uploading account will own the object.
        :param public_read_access: Grants public read access to all objects in the bucket. Similar to calling ``bucket.grantPublicAccess()`` Default: false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param server_access_logs_bucket: Destination bucket for the server access logs. Default: - If "serverAccessLogsPrefix" undefined - access logs disabled, otherwise - log to current bucket.
        :param server_access_logs_prefix: Optional log file prefix to use for the bucket's access logs. If defined without "serverAccessLogsBucket", enables access logs to current bucket with this prefix. Default: - No log file prefix
        :param target_object_key_format: Optional key format for log objects. Default: - the default key format is: [DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
        :param transfer_acceleration: Whether this bucket should have transfer acceleration turned on or not. Default: false
        :param versioned: Whether this bucket should have versioning turned on or not. Default: false (unless object lock is enabled, then true)
        :param website_error_document: The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set. Default: - No error document.
        :param website_index_document: The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket. Default: - No index document.
        :param website_redirect: Specifies the redirect behavior of all requests to a website endpoint of a bucket. If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules". Default: - No redirection.
        :param website_routing_rules: Rules that define when a redirect is applied and the redirect behavior. Default: - No redirection rules.
        '''
        if isinstance(website_redirect, dict):
            website_redirect = _aws_cdk_aws_s3_ceddda9d.RedirectTarget(**website_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0ad6ea5dc0bc9f7228cd62f328eac77acd69d77ada3adaf155c2be557a785c)
            check_type(argname="argument access_control", value=access_control, expected_type=type_hints["access_control"])
            check_type(argname="argument auto_delete_objects", value=auto_delete_objects, expected_type=type_hints["auto_delete_objects"])
            check_type(argname="argument block_public_access", value=block_public_access, expected_type=type_hints["block_public_access"])
            check_type(argname="argument bucket_key_enabled", value=bucket_key_enabled, expected_type=type_hints["bucket_key_enabled"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument enforce_ssl", value=enforce_ssl, expected_type=type_hints["enforce_ssl"])
            check_type(argname="argument event_bridge_enabled", value=event_bridge_enabled, expected_type=type_hints["event_bridge_enabled"])
            check_type(argname="argument intelligent_tiering_configurations", value=intelligent_tiering_configurations, expected_type=type_hints["intelligent_tiering_configurations"])
            check_type(argname="argument inventories", value=inventories, expected_type=type_hints["inventories"])
            check_type(argname="argument lifecycle_rules", value=lifecycle_rules, expected_type=type_hints["lifecycle_rules"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument notifications_handler_role", value=notifications_handler_role, expected_type=type_hints["notifications_handler_role"])
            check_type(argname="argument object_lock_default_retention", value=object_lock_default_retention, expected_type=type_hints["object_lock_default_retention"])
            check_type(argname="argument object_lock_enabled", value=object_lock_enabled, expected_type=type_hints["object_lock_enabled"])
            check_type(argname="argument object_ownership", value=object_ownership, expected_type=type_hints["object_ownership"])
            check_type(argname="argument public_read_access", value=public_read_access, expected_type=type_hints["public_read_access"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument server_access_logs_bucket", value=server_access_logs_bucket, expected_type=type_hints["server_access_logs_bucket"])
            check_type(argname="argument server_access_logs_prefix", value=server_access_logs_prefix, expected_type=type_hints["server_access_logs_prefix"])
            check_type(argname="argument target_object_key_format", value=target_object_key_format, expected_type=type_hints["target_object_key_format"])
            check_type(argname="argument transfer_acceleration", value=transfer_acceleration, expected_type=type_hints["transfer_acceleration"])
            check_type(argname="argument versioned", value=versioned, expected_type=type_hints["versioned"])
            check_type(argname="argument website_error_document", value=website_error_document, expected_type=type_hints["website_error_document"])
            check_type(argname="argument website_index_document", value=website_index_document, expected_type=type_hints["website_index_document"])
            check_type(argname="argument website_redirect", value=website_redirect, expected_type=type_hints["website_redirect"])
            check_type(argname="argument website_routing_rules", value=website_routing_rules, expected_type=type_hints["website_routing_rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_control is not None:
            self._values["access_control"] = access_control
        if auto_delete_objects is not None:
            self._values["auto_delete_objects"] = auto_delete_objects
        if block_public_access is not None:
            self._values["block_public_access"] = block_public_access
        if bucket_key_enabled is not None:
            self._values["bucket_key_enabled"] = bucket_key_enabled
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if cors is not None:
            self._values["cors"] = cors
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if enforce_ssl is not None:
            self._values["enforce_ssl"] = enforce_ssl
        if event_bridge_enabled is not None:
            self._values["event_bridge_enabled"] = event_bridge_enabled
        if intelligent_tiering_configurations is not None:
            self._values["intelligent_tiering_configurations"] = intelligent_tiering_configurations
        if inventories is not None:
            self._values["inventories"] = inventories
        if lifecycle_rules is not None:
            self._values["lifecycle_rules"] = lifecycle_rules
        if metrics is not None:
            self._values["metrics"] = metrics
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if notifications_handler_role is not None:
            self._values["notifications_handler_role"] = notifications_handler_role
        if object_lock_default_retention is not None:
            self._values["object_lock_default_retention"] = object_lock_default_retention
        if object_lock_enabled is not None:
            self._values["object_lock_enabled"] = object_lock_enabled
        if object_ownership is not None:
            self._values["object_ownership"] = object_ownership
        if public_read_access is not None:
            self._values["public_read_access"] = public_read_access
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if server_access_logs_bucket is not None:
            self._values["server_access_logs_bucket"] = server_access_logs_bucket
        if server_access_logs_prefix is not None:
            self._values["server_access_logs_prefix"] = server_access_logs_prefix
        if target_object_key_format is not None:
            self._values["target_object_key_format"] = target_object_key_format
        if transfer_acceleration is not None:
            self._values["transfer_acceleration"] = transfer_acceleration
        if versioned is not None:
            self._values["versioned"] = versioned
        if website_error_document is not None:
            self._values["website_error_document"] = website_error_document
        if website_index_document is not None:
            self._values["website_index_document"] = website_index_document
        if website_redirect is not None:
            self._values["website_redirect"] = website_redirect
        if website_routing_rules is not None:
            self._values["website_routing_rules"] = website_routing_rules

    @builtins.property
    def access_control(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketAccessControl]:
        '''Specifies a canned ACL that grants predefined permissions to the bucket.

        :default: BucketAccessControl.PRIVATE
        '''
        result = self._values.get("access_control")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketAccessControl], result)

    @builtins.property
    def auto_delete_objects(self) -> typing.Optional[builtins.bool]:
        '''Whether all objects should be automatically deleted when the bucket is removed from the stack or when the stack is deleted.

        Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``.

        **Warning** if you have deployed a bucket with ``autoDeleteObjects: true``,
        switching this to ``false`` in a CDK version *before* ``1.126.0`` will lead to
        all objects in the bucket being deleted. Be sure to update your bucket resources
        by deploying with CDK version ``1.126.0`` or later **before** switching this value to ``false``.

        :default: false
        '''
        result = self._values.get("auto_delete_objects")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def block_public_access(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BlockPublicAccess]:
        '''The block public access configuration of this bucket.

        :default: - CloudFormation defaults will apply. New buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html
        '''
        result = self._values.get("block_public_access")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BlockPublicAccess], result)

    @builtins.property
    def bucket_key_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether Amazon S3 should use its own intermediary key to generate data keys.

        Only relevant when using KMS for encryption.

        - If not enabled, every object GET and PUT will cause an API call to KMS (with the
          attendant cost implications of that).
        - If enabled, S3 will use its own time-limited key instead.

        Only relevant, when Encryption is set to ``BucketEncryption.KMS`` or ``BucketEncryption.KMS_MANAGED``.

        :default: - false
        '''
        result = self._values.get("bucket_key_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Physical name of this bucket.

        :default: - Assigned by CloudFormation (recommended).
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cors(self) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.CorsRule]]:
        '''The CORS configuration of this bucket.

        :default: - No CORS configuration.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.CorsRule]], result)

    @builtins.property
    def encryption(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketEncryption]:
        '''The kind of server-side encryption to apply to this bucket.

        If you choose KMS, you can specify a KMS key via ``encryptionKey``. If
        encryption key is not specified, a key will automatically be created.

        :default:

        - ``KMS`` if ``encryptionKey`` is specified, or ``UNENCRYPTED`` otherwise.
        But if ``UNENCRYPTED`` is specified, the bucket will be encrypted as ``S3_MANAGED`` automatically.
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketEncryption], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey]:
        '''External KMS key to use for bucket encryption.

        The ``encryption`` property must be either not specified or set to ``KMS`` or ``DSSE``.
        An error will be emitted if ``encryption`` is set to ``UNENCRYPTED`` or ``S3_MANAGED``.

        :default:

        - If ``encryption`` is set to ``KMS`` and this property is undefined,
        a new KMS key will be created and associated with this bucket.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey], result)

    @builtins.property
    def enforce_ssl(self) -> typing.Optional[builtins.bool]:
        '''Enforces SSL for requests.

        S3.5 of the AWS Foundational Security Best Practices Regarding S3.

        :default: false

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-ssl-requests-only.html
        '''
        result = self._values.get("enforce_ssl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_bridge_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether this bucket should send notifications to Amazon EventBridge or not.

        :default: false
        '''
        result = self._values.get("event_bridge_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intelligent_tiering_configurations(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.IntelligentTieringConfiguration]]:
        '''Inteligent Tiering Configurations.

        :default: No Intelligent Tiiering Configurations.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html
        '''
        result = self._values.get("intelligent_tiering_configurations")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.IntelligentTieringConfiguration]], result)

    @builtins.property
    def inventories(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.Inventory]]:
        '''The inventory configuration of the bucket.

        :default: - No inventory configuration

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html
        '''
        result = self._values.get("inventories")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.Inventory]], result)

    @builtins.property
    def lifecycle_rules(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.LifecycleRule]]:
        '''Rules that define how Amazon S3 manages objects during their lifetime.

        :default: - No lifecycle rules.
        '''
        result = self._values.get("lifecycle_rules")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.LifecycleRule]], result)

    @builtins.property
    def metrics(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.BucketMetrics]]:
        '''The metrics configuration of this bucket.

        :default: - No metrics configuration.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.BucketMetrics]], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[jsii.Number]:
        '''Enforces minimum TLS version for requests.

        Requires ``enforceSSL`` to be enabled.

        :default: No minimum TLS version is enforced.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-object-tls-version
        '''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notifications_handler_role(
        self,
    ) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''The role to be used by the notifications handler.

        :default: - a new role will be created.
        '''
        result = self._values.get("notifications_handler_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def object_lock_default_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectLockRetention]:
        '''The default retention mode and rules for S3 Object Lock.

        Default retention can be configured after a bucket is created if the bucket already
        has object lock enabled. Enabling object lock for existing buckets is not supported.

        :default: no default retention period

        :see: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-bucket-config-enable
        '''
        result = self._values.get("object_lock_default_retention")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectLockRetention], result)

    @builtins.property
    def object_lock_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable object lock on the bucket.

        Enabling object lock for existing buckets is not supported. Object lock must be
        enabled when the bucket is created.

        :default: false, unless objectLockDefaultRetention is set (then, true)

        :see: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-bucket-config-enable
        '''
        result = self._values.get("object_lock_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def object_ownership(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectOwnership]:
        '''The objectOwnership of the bucket.

        :default: - No ObjectOwnership configuration, uploading account will own the object.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html
        '''
        result = self._values.get("object_ownership")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectOwnership], result)

    @builtins.property
    def public_read_access(self) -> typing.Optional[builtins.bool]:
        '''Grants public read access to all objects in the bucket.

        Similar to calling ``bucket.grantPublicAccess()``

        :default: false
        '''
        result = self._values.get("public_read_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''Policy to apply when the bucket is removed from this stack.

        :default: - The bucket will be orphaned.
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def server_access_logs_bucket(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''Destination bucket for the server access logs.

        :default: - If "serverAccessLogsPrefix" undefined - access logs disabled, otherwise - log to current bucket.
        '''
        result = self._values.get("server_access_logs_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def server_access_logs_prefix(self) -> typing.Optional[builtins.str]:
        '''Optional log file prefix to use for the bucket's access logs.

        If defined without "serverAccessLogsBucket", enables access logs to current bucket with this prefix.

        :default: - No log file prefix
        '''
        result = self._values.get("server_access_logs_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_object_key_format(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.TargetObjectKeyFormat]:
        '''Optional key format for log objects.

        :default: - the default key format is: [DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
        '''
        result = self._values.get("target_object_key_format")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.TargetObjectKeyFormat], result)

    @builtins.property
    def transfer_acceleration(self) -> typing.Optional[builtins.bool]:
        '''Whether this bucket should have transfer acceleration turned on or not.

        :default: false
        '''
        result = self._values.get("transfer_acceleration")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def versioned(self) -> typing.Optional[builtins.bool]:
        '''Whether this bucket should have versioning turned on or not.

        :default: false (unless object lock is enabled, then true)
        '''
        result = self._values.get("versioned")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def website_error_document(self) -> typing.Optional[builtins.str]:
        '''The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set.

        :default: - No error document.
        '''
        result = self._values.get("website_error_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def website_index_document(self) -> typing.Optional[builtins.str]:
        '''The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket.

        :default: - No index document.
        '''
        result = self._values.get("website_index_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def website_redirect(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.RedirectTarget]:
        '''Specifies the redirect behavior of all requests to a website endpoint of a bucket.

        If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules".

        :default: - No redirection.
        '''
        result = self._values.get("website_redirect")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.RedirectTarget], result)

    @builtins.property
    def website_routing_rules(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.RoutingRule]]:
        '''Rules that define when a redirect is applied and the redirect behavior.

        :default: - No redirection rules.
        '''
        result = self._values.get("website_routing_rules")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.RoutingRule]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkCluster(
    _aws_cdk_aws_ecs_ceddda9d.Cluster,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkCluster",
):
    '''CloudKitect ECS cluster component is a regional grouping of one or more container instances on which you can run tasks and services and enables container insights,  ### Default Configuration New VPC is created by default.



    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkCluster(this, "LogicalId", {});

    Custom Configuration Example::

       new CkCluster(this, "LogicalId", {
          containerInsights: false
       });


    Compliance

    It addresses the following compliance requirements
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        container_insights: typing.Optional[builtins.bool] = None,
        default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
        execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param capacity: The ec2 capacity to add to the cluster. Default: - no EC2 capacity will be added, you can use ``addCapacity`` to add capacity later.
        :param cluster_name: The name for the cluster. Default: CloudFormation-generated name
        :param container_insights: If true CloudWatch Container Insights will be enabled for the cluster. Default: - Container Insights will be disabled for this cluster.
        :param default_cloud_map_namespace: The service discovery namespace created in this cluster. Default: - no service discovery namespace created, you can use ``addDefaultCloudMapNamespace`` to add a default service discovery namespace later.
        :param enable_fargate_capacity_providers: Whether to enable Fargate Capacity Providers. Default: false
        :param execute_command_configuration: The execute command configuration for the cluster. Default: - no configuration will be provided.
        :param vpc: The VPC where your ECS instances will be running or your ENIs will be deployed. Default: - creates a new VPC with two AZs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0c1b1000bca3bfc90f4a2f2f762c754fc5f4a24071b976a5caa8e08af4d81d8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkClusterProps(
            capacity=capacity,
            cluster_name=cluster_name,
            container_insights=container_insights,
            default_cloud_map_namespace=default_cloud_map_namespace,
            enable_fargate_capacity_providers=enable_fargate_capacity_providers,
            execute_command_configuration=execute_command_configuration,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkClusterProps",
    jsii_struct_bases=[_aws_cdk_aws_ecs_ceddda9d.ClusterProps],
    name_mapping={
        "capacity": "capacity",
        "cluster_name": "clusterName",
        "container_insights": "containerInsights",
        "default_cloud_map_namespace": "defaultCloudMapNamespace",
        "enable_fargate_capacity_providers": "enableFargateCapacityProviders",
        "execute_command_configuration": "executeCommandConfiguration",
        "vpc": "vpc",
    },
)
class CkClusterProps(_aws_cdk_aws_ecs_ceddda9d.ClusterProps):
    def __init__(
        self,
        *,
        capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        container_insights: typing.Optional[builtins.bool] = None,
        default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
        execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''CloudKitect Cluster component properties.

        :param capacity: The ec2 capacity to add to the cluster. Default: - no EC2 capacity will be added, you can use ``addCapacity`` to add capacity later.
        :param cluster_name: The name for the cluster. Default: CloudFormation-generated name
        :param container_insights: If true CloudWatch Container Insights will be enabled for the cluster. Default: - Container Insights will be disabled for this cluster.
        :param default_cloud_map_namespace: The service discovery namespace created in this cluster. Default: - no service discovery namespace created, you can use ``addDefaultCloudMapNamespace`` to add a default service discovery namespace later.
        :param enable_fargate_capacity_providers: Whether to enable Fargate Capacity Providers. Default: false
        :param execute_command_configuration: The execute command configuration for the cluster. Default: - no configuration will be provided.
        :param vpc: The VPC where your ECS instances will be running or your ENIs will be deployed. Default: - creates a new VPC with two AZs
        '''
        if isinstance(capacity, dict):
            capacity = _aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions(**capacity)
        if isinstance(default_cloud_map_namespace, dict):
            default_cloud_map_namespace = _aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions(**default_cloud_map_namespace)
        if isinstance(execute_command_configuration, dict):
            execute_command_configuration = _aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration(**execute_command_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0fd78b1b4eb803922b57b83831556117fa86638eb7175748b9da4a2690fc318)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument container_insights", value=container_insights, expected_type=type_hints["container_insights"])
            check_type(argname="argument default_cloud_map_namespace", value=default_cloud_map_namespace, expected_type=type_hints["default_cloud_map_namespace"])
            check_type(argname="argument enable_fargate_capacity_providers", value=enable_fargate_capacity_providers, expected_type=type_hints["enable_fargate_capacity_providers"])
            check_type(argname="argument execute_command_configuration", value=execute_command_configuration, expected_type=type_hints["execute_command_configuration"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity is not None:
            self._values["capacity"] = capacity
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if container_insights is not None:
            self._values["container_insights"] = container_insights
        if default_cloud_map_namespace is not None:
            self._values["default_cloud_map_namespace"] = default_cloud_map_namespace
        if enable_fargate_capacity_providers is not None:
            self._values["enable_fargate_capacity_providers"] = enable_fargate_capacity_providers
        if execute_command_configuration is not None:
            self._values["execute_command_configuration"] = execute_command_configuration
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def capacity(self) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions]:
        '''The ec2 capacity to add to the cluster.

        :default: - no EC2 capacity will be added, you can use ``addCapacity`` to add capacity later.
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name for the cluster.

        :default: CloudFormation-generated name
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_insights(self) -> typing.Optional[builtins.bool]:
        '''If true CloudWatch Container Insights will be enabled for the cluster.

        :default: - Container Insights will be disabled for this cluster.
        '''
        result = self._values.get("container_insights")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_cloud_map_namespace(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions]:
        '''The service discovery namespace created in this cluster.

        :default:

        - no service discovery namespace created, you can use ``addDefaultCloudMapNamespace`` to add a
        default service discovery namespace later.
        '''
        result = self._values.get("default_cloud_map_namespace")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions], result)

    @builtins.property
    def enable_fargate_capacity_providers(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable Fargate Capacity Providers.

        :default: false
        '''
        result = self._values.get("enable_fargate_capacity_providers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def execute_command_configuration(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration]:
        '''The execute command configuration for the cluster.

        :default: - no configuration will be provided.
        '''
        result = self._values.get("execute_command_configuration")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''The VPC where your ECS instances will be running or your ENIs will be deployed.

        :default: - creates a new VPC with two AZs
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkDistribution(
    _aws_cdk_aws_cloudfront_ceddda9d.Distribution,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkDistribution",
):
    '''CloudKitect CloudFront Distribution Component.



    Default Configuration

    Http Protocol: Redirect to Https
    Protocol Version: SecurityPolicyProtocol.TLS_V1_2_2021


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkDistribution(this, "LogicalId", {});


    Compliance

    It addresses the following compliance requirements

    1. Cloudfront origin should not use insecure protocols
       .. epigraph::

          - Risk Level: Medium
          - Compliance: PCI, HIPAA, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    2. Cloudfront uses enhanced security policy min TLS1.2
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, HIPAA, MAS, NIST4
          - Well Architected Pillar: Security

    3. Cloudfront uses only secure protocol to communicate with origin
       .. epigraph::

          - Risk Level: Medium
          - Compliance: PCI, HIPAA, APRA, MAS, NIST4
          - Well Architected Pillar: Security

    4. Cloudfront uses only secure protocol to communicate with end users
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, HIPAA, NIST4
          - Well Architected Pillar: Security

    5. Use appropriate class for each environment to save cost
       .. epigraph::

          - Risk Level: Low
          - Compliance: NA
          - Well Architected Pillar: Cost Optimization
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        default_behavior: typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]],
        additional_behaviors: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        publish_additional_metrics: typing.Optional[builtins.bool] = None,
        ssl_support_method: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SSLMethod] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param default_behavior: The default behavior for the distribution.
        :param additional_behaviors: Additional behaviors for the distribution, mapped by the pathPattern that specifies which requests to apply the behavior to. Default: - no additional behaviors are added.
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - no default root object
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param error_responses: How CloudFront should handle requests that are not successful (e.g., PageNotFound). Default: - No custom error responses.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Make sure to set ``objectOwnership`` to ``s3.ObjectOwnership.OBJECT_WRITER`` in your custom bucket. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SecurityPolicyProtocol.TLS_V1_2_2021 if the '@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021' feature flag is set; otherwise, SecurityPolicyProtocol.TLS_V1_2_2019.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_ALL
        :param publish_additional_metrics: Whether to enable additional CloudWatch metrics. Default: false
        :param ssl_support_method: The SSL method CloudFront will use for your distribution. Server Name Indication (SNI) - is an extension to the TLS computer networking protocol by which a client indicates which hostname it is attempting to connect to at the start of the handshaking process. This allows a server to present multiple certificates on the same IP address and TCP port number and hence allows multiple secure (HTTPS) websites (or any other service over TLS) to be served by the same IP address without requiring all those sites to use the same certificate. CloudFront can use SNI to host multiple distributions on the same IP - which a large majority of clients will support. If your clients cannot support SNI however - CloudFront can use dedicated IPs for your distribution - but there is a prorated monthly charge for using this feature. By default, we use SNI - but you can optionally enable dedicated IPs (VIP). See the CloudFront SSL for more details about pricing : https://aws.amazon.com/cloudfront/custom-ssl-domains/ Default: SSLMethod.SNI
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ac339f76bd4d2ce81454703e11e442363cdd4fd95a6c2a1b2732f6bf44cf3b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkDistributionProps(
            default_behavior=default_behavior,
            additional_behaviors=additional_behaviors,
            certificate=certificate,
            comment=comment,
            default_root_object=default_root_object,
            domain_names=domain_names,
            enabled=enabled,
            enable_ipv6=enable_ipv6,
            enable_logging=enable_logging,
            error_responses=error_responses,
            geo_restriction=geo_restriction,
            http_version=http_version,
            log_bucket=log_bucket,
            log_file_prefix=log_file_prefix,
            log_includes_cookies=log_includes_cookies,
            minimum_protocol_version=minimum_protocol_version,
            price_class=price_class,
            publish_additional_metrics=publish_additional_metrics,
            ssl_support_method=ssl_support_method,
            web_acl_id=web_acl_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkDistributionProps",
    jsii_struct_bases=[_aws_cdk_aws_cloudfront_ceddda9d.DistributionProps],
    name_mapping={
        "default_behavior": "defaultBehavior",
        "additional_behaviors": "additionalBehaviors",
        "certificate": "certificate",
        "comment": "comment",
        "default_root_object": "defaultRootObject",
        "domain_names": "domainNames",
        "enabled": "enabled",
        "enable_ipv6": "enableIpv6",
        "enable_logging": "enableLogging",
        "error_responses": "errorResponses",
        "geo_restriction": "geoRestriction",
        "http_version": "httpVersion",
        "log_bucket": "logBucket",
        "log_file_prefix": "logFilePrefix",
        "log_includes_cookies": "logIncludesCookies",
        "minimum_protocol_version": "minimumProtocolVersion",
        "price_class": "priceClass",
        "publish_additional_metrics": "publishAdditionalMetrics",
        "ssl_support_method": "sslSupportMethod",
        "web_acl_id": "webAclId",
    },
)
class CkDistributionProps(_aws_cdk_aws_cloudfront_ceddda9d.DistributionProps):
    def __init__(
        self,
        *,
        default_behavior: typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]],
        additional_behaviors: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
        comment: typing.Optional[builtins.str] = None,
        default_root_object: typing.Optional[builtins.str] = None,
        domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_logging: typing.Optional[builtins.bool] = None,
        error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
        geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
        http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
        log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        log_file_prefix: typing.Optional[builtins.str] = None,
        log_includes_cookies: typing.Optional[builtins.bool] = None,
        minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
        price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
        publish_additional_metrics: typing.Optional[builtins.bool] = None,
        ssl_support_method: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SSLMethod] = None,
        web_acl_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CloudKitect Cloudfront Distribution Component Properties.

        :param default_behavior: The default behavior for the distribution.
        :param additional_behaviors: Additional behaviors for the distribution, mapped by the pathPattern that specifies which requests to apply the behavior to. Default: - no additional behaviors are added.
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param comment: Any comments you want to include about the distribution. Default: - no comment
        :param default_root_object: The object that you want CloudFront to request from your origin (for example, index.html) when a viewer requests the root URL for your distribution. If no default object is set, the request goes to the origin's root (e.g., example.com/). Default: - no default root object
        :param domain_names: Alternative domain names for this distribution. If you want to use your own domain name, such as www.example.com, instead of the cloudfront.net domain name, you can add an alternate domain name to your distribution. If you attach a certificate to the distribution, you must add (at least one of) the domain names of the certificate to this list. Default: - The distribution will only support the default generated name (e.g., d111111abcdef8.cloudfront.net)
        :param enabled: Enable or disable the distribution. Default: true
        :param enable_ipv6: Whether CloudFront will respond to IPv6 DNS requests with an IPv6 address. If you specify false, CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. Default: true
        :param enable_logging: Enable access logging for the distribution. Default: - false, unless ``logBucket`` is specified.
        :param error_responses: How CloudFront should handle requests that are not successful (e.g., PageNotFound). Default: - No custom error responses.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: - No geographic restrictions
        :param http_version: Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support server name identification (SNI). Default: HttpVersion.HTTP2
        :param log_bucket: The Amazon S3 bucket to store the access logs in. Make sure to set ``objectOwnership`` to ``s3.ObjectOwnership.OBJECT_WRITER`` in your custom bucket. Default: - A bucket is created if ``enableLogging`` is true
        :param log_file_prefix: An optional string that you want CloudFront to prefix to the access log filenames for this distribution. Default: - no prefix
        :param log_includes_cookies: Specifies whether you want CloudFront to include cookies in access logs. Default: false
        :param minimum_protocol_version: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SecurityPolicyProtocol.TLS_V1_2_2021 if the '@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021' feature flag is set; otherwise, SecurityPolicyProtocol.TLS_V1_2_2019.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_ALL
        :param publish_additional_metrics: Whether to enable additional CloudWatch metrics. Default: false
        :param ssl_support_method: The SSL method CloudFront will use for your distribution. Server Name Indication (SNI) - is an extension to the TLS computer networking protocol by which a client indicates which hostname it is attempting to connect to at the start of the handshaking process. This allows a server to present multiple certificates on the same IP address and TCP port number and hence allows multiple secure (HTTPS) websites (or any other service over TLS) to be served by the same IP address without requiring all those sites to use the same certificate. CloudFront can use SNI to host multiple distributions on the same IP - which a large majority of clients will support. If your clients cannot support SNI however - CloudFront can use dedicated IPs for your distribution - but there is a prorated monthly charge for using this feature. By default, we use SNI - but you can optionally enable dedicated IPs (VIP). See the CloudFront SSL for more details about pricing : https://aws.amazon.com/cloudfront/custom-ssl-domains/ Default: SSLMethod.SNI
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example ``arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a``. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example ``473e64fd-f30b-4765-81a0-62ad96dd167a``. Default: - No AWS Web Application Firewall web access control list (web ACL).
        '''
        if isinstance(default_behavior, dict):
            default_behavior = _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions(**default_behavior)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57704f62d36a0c5e8e2b6683208dba882021cdfddabbe489cab9a442e6076ec)
            check_type(argname="argument default_behavior", value=default_behavior, expected_type=type_hints["default_behavior"])
            check_type(argname="argument additional_behaviors", value=additional_behaviors, expected_type=type_hints["additional_behaviors"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_root_object", value=default_root_object, expected_type=type_hints["default_root_object"])
            check_type(argname="argument domain_names", value=domain_names, expected_type=type_hints["domain_names"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument error_responses", value=error_responses, expected_type=type_hints["error_responses"])
            check_type(argname="argument geo_restriction", value=geo_restriction, expected_type=type_hints["geo_restriction"])
            check_type(argname="argument http_version", value=http_version, expected_type=type_hints["http_version"])
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_file_prefix", value=log_file_prefix, expected_type=type_hints["log_file_prefix"])
            check_type(argname="argument log_includes_cookies", value=log_includes_cookies, expected_type=type_hints["log_includes_cookies"])
            check_type(argname="argument minimum_protocol_version", value=minimum_protocol_version, expected_type=type_hints["minimum_protocol_version"])
            check_type(argname="argument price_class", value=price_class, expected_type=type_hints["price_class"])
            check_type(argname="argument publish_additional_metrics", value=publish_additional_metrics, expected_type=type_hints["publish_additional_metrics"])
            check_type(argname="argument ssl_support_method", value=ssl_support_method, expected_type=type_hints["ssl_support_method"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_behavior": default_behavior,
        }
        if additional_behaviors is not None:
            self._values["additional_behaviors"] = additional_behaviors
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
        if error_responses is not None:
            self._values["error_responses"] = error_responses
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
        if price_class is not None:
            self._values["price_class"] = price_class
        if publish_additional_metrics is not None:
            self._values["publish_additional_metrics"] = publish_additional_metrics
        if ssl_support_method is not None:
            self._values["ssl_support_method"] = ssl_support_method
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id

    @builtins.property
    def default_behavior(self) -> _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions:
        '''The default behavior for the distribution.'''
        result = self._values.get("default_behavior")
        assert result is not None, "Required property 'default_behavior' is missing"
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, result)

    @builtins.property
    def additional_behaviors(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]]:
        '''Additional behaviors for the distribution, mapped by the pathPattern that specifies which requests to apply the behavior to.

        :default: - no additional behaviors are added.
        '''
        result = self._values.get("additional_behaviors")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions]], result)

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

        :default: - no default root object
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
    def error_responses(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse]]:
        '''How CloudFront should handle requests that are not successful (e.g., PageNotFound).

        :default: - No custom error responses.
        '''
        result = self._values.get("error_responses")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse]], result)

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

        Make sure to set ``objectOwnership`` to ``s3.ObjectOwnership.OBJECT_WRITER`` in your custom bucket.

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

        :default: - SecurityPolicyProtocol.TLS_V1_2_2021 if the '@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021' feature flag is set; otherwise, SecurityPolicyProtocol.TLS_V1_2_2019.
        '''
        result = self._values.get("minimum_protocol_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol], result)

    @builtins.property
    def price_class(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass]:
        '''The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        :default: PriceClass.PRICE_CLASS_ALL
        '''
        result = self._values.get("price_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass], result)

    @builtins.property
    def publish_additional_metrics(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable additional CloudWatch metrics.

        :default: false

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html
        '''
        result = self._values.get("publish_additional_metrics")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ssl_support_method(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SSLMethod]:
        '''The SSL method CloudFront will use for your distribution.

        Server Name Indication (SNI) - is an extension to the TLS computer networking protocol by which a client indicates
        which hostname it is attempting to connect to at the start of the handshaking process. This allows a server to present
        multiple certificates on the same IP address and TCP port number and hence allows multiple secure (HTTPS) websites
        (or any other service over TLS) to be served by the same IP address without requiring all those sites to use the same certificate.

        CloudFront can use SNI to host multiple distributions on the same IP - which a large majority of clients will support.

        If your clients cannot support SNI however - CloudFront can use dedicated IPs for your distribution - but there is a prorated monthly charge for
        using this feature. By default, we use SNI - but you can optionally enable dedicated IPs (VIP).

        See the CloudFront SSL for more details about pricing : https://aws.amazon.com/cloudfront/custom-ssl-domains/

        :default: SSLMethod.SNI
        '''
        result = self._values.get("ssl_support_method")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SSLMethod], result)

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
        return "CkDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkDnsValidatedCertificate(
    _aws_cdk_aws_certificatemanager_ceddda9d.Certificate,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkDnsValidatedCertificate",
):
    '''CloudKitect DnsValidatedCertificate Component.



    Default Configuration



    Default Alarms

    Available in Enhanced components only


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkDnsValidatedCertificate(this, "LogicalId", {
           domainName: "cloudkitect.com"
       });


    Compliance

    None
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ck_hosted_zone: _aws_cdk_aws_route53_ceddda9d.IHostedZone,
        domain_name: builtins.str,
        certificate_name: typing.Optional[builtins.str] = None,
        key_algorithm: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.KeyAlgorithm] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        transparency_logging_enabled: typing.Optional[builtins.bool] = None,
        validation: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateValidation] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ck_hosted_zone: Hosted zone.
        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param certificate_name: The Certificate name. Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: the full, absolute path of this construct
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param transparency_logging_enabled: Enable or disable transparency logging for this certificate. Once a certificate has been logged, it cannot be removed from the log. Opting out at that point will have no effect. If you opt out of logging when you request a certificate and then choose later to opt back in, your certificate will not be logged until it is renewed. If you want the certificate to be logged immediately, we recommend that you issue a new one. Default: true
        :param validation: How to validate this certificate. Default: CertificateValidation.fromEmail()
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e74f7843180c4ab8b56ce954ce39086d980f97493103f4d7f89a79fde269b42)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkDnsValidatedCertificateProps(
            ck_hosted_zone=ck_hosted_zone,
            domain_name=domain_name,
            certificate_name=certificate_name,
            key_algorithm=key_algorithm,
            subject_alternative_names=subject_alternative_names,
            transparency_logging_enabled=transparency_logging_enabled,
            validation=validation,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkDnsValidatedCertificateProps",
    jsii_struct_bases=[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateProps],
    name_mapping={
        "domain_name": "domainName",
        "certificate_name": "certificateName",
        "key_algorithm": "keyAlgorithm",
        "subject_alternative_names": "subjectAlternativeNames",
        "transparency_logging_enabled": "transparencyLoggingEnabled",
        "validation": "validation",
        "ck_hosted_zone": "ckHostedZone",
    },
)
class CkDnsValidatedCertificateProps(
    _aws_cdk_aws_certificatemanager_ceddda9d.CertificateProps,
):
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        certificate_name: typing.Optional[builtins.str] = None,
        key_algorithm: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.KeyAlgorithm] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        transparency_logging_enabled: typing.Optional[builtins.bool] = None,
        validation: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateValidation] = None,
        ck_hosted_zone: _aws_cdk_aws_route53_ceddda9d.IHostedZone,
    ) -> None:
        '''CloudKitect DnsValidatedCertificate Component Properties.

        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param certificate_name: The Certificate name. Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: the full, absolute path of this construct
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param transparency_logging_enabled: Enable or disable transparency logging for this certificate. Once a certificate has been logged, it cannot be removed from the log. Opting out at that point will have no effect. If you opt out of logging when you request a certificate and then choose later to opt back in, your certificate will not be logged until it is renewed. If you want the certificate to be logged immediately, we recommend that you issue a new one. Default: true
        :param validation: How to validate this certificate. Default: CertificateValidation.fromEmail()
        :param ck_hosted_zone: Hosted zone.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dcfc5fe917e31c299483725456c97c8f26932742e88c675e0223b87c5a61a6f)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
            check_type(argname="argument transparency_logging_enabled", value=transparency_logging_enabled, expected_type=type_hints["transparency_logging_enabled"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
            check_type(argname="argument ck_hosted_zone", value=ck_hosted_zone, expected_type=type_hints["ck_hosted_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "ck_hosted_zone": ck_hosted_zone,
        }
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if key_algorithm is not None:
            self._values["key_algorithm"] = key_algorithm
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if transparency_logging_enabled is not None:
            self._values["transparency_logging_enabled"] = transparency_logging_enabled
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Fully-qualified domain name to request a certificate for.

        May contain wildcards, such as ``*.domain.com``.
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''The Certificate name.

        Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag

        :default: the full, absolute path of this construct
        '''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_algorithm(
        self,
    ) -> typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.KeyAlgorithm]:
        '''Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data.

        :default: KeyAlgorithm.RSA_2048

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms.title
        '''
        result = self._values.get("key_algorithm")
        return typing.cast(typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.KeyAlgorithm], result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names on your certificate.

        Use this to register alternative domain names that represent the same site.

        :default: - No additional FQDNs will be included as alternative domain names.
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def transparency_logging_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable transparency logging for this certificate.

        Once a certificate has been logged, it cannot be removed from the log.
        Opting out at that point will have no effect. If you opt out of logging
        when you request a certificate and then choose later to opt back in,
        your certificate will not be logged until it is renewed.
        If you want the certificate to be logged immediately, we recommend that you issue a new one.

        :default: true

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency
        '''
        result = self._values.get("transparency_logging_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validation(
        self,
    ) -> typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateValidation]:
        '''How to validate this certificate.

        :default: CertificateValidation.fromEmail()
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateValidation], result)

    @builtins.property
    def ck_hosted_zone(self) -> _aws_cdk_aws_route53_ceddda9d.IHostedZone:
        '''Hosted zone.'''
        result = self._values.get("ck_hosted_zone")
        assert result is not None, "Required property 'ck_hosted_zone' is missing"
        return typing.cast(_aws_cdk_aws_route53_ceddda9d.IHostedZone, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkDnsValidatedCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkFargateCluster(
    CkCluster,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkFargateCluster",
):
    '''CloudKitect ECS cluster component backed by Fargate capacity provider is a regional grouping of one or more container instances on which you can run tasks and services and enables container insights,  ### Default Alarms  ### Examples Default Usage ```ts new CcFargateCluster(this, "LogicalId", {});

    Example::


       Custom Configuration
       ```ts
       new CcFargateCluster(this, "LogicalId", {
          containerInsights: false
       });


    Compliance

    It addresses the following compliance requirements

    1. Cluster insights enabled
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NA
          - Well Architected Pillar: Operational Excellence
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        container_insights: typing.Optional[builtins.bool] = None,
        default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
        execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param capacity: The ec2 capacity to add to the cluster. Default: - no EC2 capacity will be added, you can use ``addCapacity`` to add capacity later.
        :param cluster_name: The name for the cluster. Default: CloudFormation-generated name
        :param container_insights: If true CloudWatch Container Insights will be enabled for the cluster. Default: - Container Insights will be disabled for this cluster.
        :param default_cloud_map_namespace: The service discovery namespace created in this cluster. Default: - no service discovery namespace created, you can use ``addDefaultCloudMapNamespace`` to add a default service discovery namespace later.
        :param enable_fargate_capacity_providers: Whether to enable Fargate Capacity Providers. Default: false
        :param execute_command_configuration: The execute command configuration for the cluster. Default: - no configuration will be provided.
        :param vpc: The VPC where your ECS instances will be running or your ENIs will be deployed. Default: - creates a new VPC with two AZs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff4e09e2212846a88aef20544f866acc4f948a06534e4af9f9249ff380eb350)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkFargateClusterProps(
            capacity=capacity,
            cluster_name=cluster_name,
            container_insights=container_insights,
            default_cloud_map_namespace=default_cloud_map_namespace,
            enable_fargate_capacity_providers=enable_fargate_capacity_providers,
            execute_command_configuration=execute_command_configuration,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkFargateClusterProps",
    jsii_struct_bases=[CkClusterProps],
    name_mapping={
        "capacity": "capacity",
        "cluster_name": "clusterName",
        "container_insights": "containerInsights",
        "default_cloud_map_namespace": "defaultCloudMapNamespace",
        "enable_fargate_capacity_providers": "enableFargateCapacityProviders",
        "execute_command_configuration": "executeCommandConfiguration",
        "vpc": "vpc",
    },
)
class CkFargateClusterProps(CkClusterProps):
    def __init__(
        self,
        *,
        capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        container_insights: typing.Optional[builtins.bool] = None,
        default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
        execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''CloudKitect Fargate Cluster component properties.

        :param capacity: The ec2 capacity to add to the cluster. Default: - no EC2 capacity will be added, you can use ``addCapacity`` to add capacity later.
        :param cluster_name: The name for the cluster. Default: CloudFormation-generated name
        :param container_insights: If true CloudWatch Container Insights will be enabled for the cluster. Default: - Container Insights will be disabled for this cluster.
        :param default_cloud_map_namespace: The service discovery namespace created in this cluster. Default: - no service discovery namespace created, you can use ``addDefaultCloudMapNamespace`` to add a default service discovery namespace later.
        :param enable_fargate_capacity_providers: Whether to enable Fargate Capacity Providers. Default: false
        :param execute_command_configuration: The execute command configuration for the cluster. Default: - no configuration will be provided.
        :param vpc: The VPC where your ECS instances will be running or your ENIs will be deployed. Default: - creates a new VPC with two AZs
        '''
        if isinstance(capacity, dict):
            capacity = _aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions(**capacity)
        if isinstance(default_cloud_map_namespace, dict):
            default_cloud_map_namespace = _aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions(**default_cloud_map_namespace)
        if isinstance(execute_command_configuration, dict):
            execute_command_configuration = _aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration(**execute_command_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb6ff015b18506d60c0f6a9fd254596ec2ea75948af9d88831a604babc5a441)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument container_insights", value=container_insights, expected_type=type_hints["container_insights"])
            check_type(argname="argument default_cloud_map_namespace", value=default_cloud_map_namespace, expected_type=type_hints["default_cloud_map_namespace"])
            check_type(argname="argument enable_fargate_capacity_providers", value=enable_fargate_capacity_providers, expected_type=type_hints["enable_fargate_capacity_providers"])
            check_type(argname="argument execute_command_configuration", value=execute_command_configuration, expected_type=type_hints["execute_command_configuration"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if capacity is not None:
            self._values["capacity"] = capacity
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if container_insights is not None:
            self._values["container_insights"] = container_insights
        if default_cloud_map_namespace is not None:
            self._values["default_cloud_map_namespace"] = default_cloud_map_namespace
        if enable_fargate_capacity_providers is not None:
            self._values["enable_fargate_capacity_providers"] = enable_fargate_capacity_providers
        if execute_command_configuration is not None:
            self._values["execute_command_configuration"] = execute_command_configuration
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def capacity(self) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions]:
        '''The ec2 capacity to add to the cluster.

        :default: - no EC2 capacity will be added, you can use ``addCapacity`` to add capacity later.
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name for the cluster.

        :default: CloudFormation-generated name
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_insights(self) -> typing.Optional[builtins.bool]:
        '''If true CloudWatch Container Insights will be enabled for the cluster.

        :default: - Container Insights will be disabled for this cluster.
        '''
        result = self._values.get("container_insights")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_cloud_map_namespace(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions]:
        '''The service discovery namespace created in this cluster.

        :default:

        - no service discovery namespace created, you can use ``addDefaultCloudMapNamespace`` to add a
        default service discovery namespace later.
        '''
        result = self._values.get("default_cloud_map_namespace")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions], result)

    @builtins.property
    def enable_fargate_capacity_providers(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable Fargate Capacity Providers.

        :default: false
        '''
        result = self._values.get("enable_fargate_capacity_providers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def execute_command_configuration(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration]:
        '''The execute command configuration for the cluster.

        :default: - no configuration will be provided.
        '''
        result = self._values.get("execute_command_configuration")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''The VPC where your ECS instances will be running or your ENIs will be deployed.

        :default: - creates a new VPC with two AZs
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkFargateClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkFargateService(
    _aws_cdk_aws_ecs_ceddda9d.FargateService,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkFargateService",
):
    '''CloudKitect Fargate Service component to run tasks.



    Default Configuration

    VPC Subnet: Private


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Example::

       new CkFargateService(this, "LogicalId", {});

    Custom Configuration Example::

       new CkFargateService(this, "LogicalId", {
          assignPublicIp: true
       });


    Compliance

    It addresses the following compliance requirements

    1. Do not assign public IP
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NIST4
          - Well Architected Pillar:  Security
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        task_definition: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        platform_version: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.FargatePlatformVersion] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]] = None,
        circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_map_options: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_alarms: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentController, typing.Dict[builtins.str, typing.Any]]] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        max_healthy_percent: typing.Optional[jsii.Number] = None,
        min_healthy_percent: typing.Optional[jsii.Number] = None,
        propagate_tags: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.PropagatedTagSource] = None,
        service_connect_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps, typing.Dict[builtins.str, typing.Any]]] = None,
        service_name: typing.Optional[builtins.str] = None,
        task_definition_revision: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.TaskDefinitionRevision] = None,
        volume_configurations: typing.Optional[typing.Sequence[_aws_cdk_aws_ecs_ceddda9d.ServiceManagedVolume]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param task_definition: The task definition to use for tasks in the service. [disable-awslint:ref-via-interface]
        :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. If true, each task will receive a public IP address. Default: false
        :param platform_version: The platform version on which to run your service. If one is not specified, the LATEST platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the Amazon Elastic Container Service Developer Guide. Default: Latest
        :param security_groups: The security groups to associate with the service. If you do not specify a security group, a new security group is created. Default: - A new security group is created.
        :param vpc_subnets: The subnets to associate with the service. Default: - Public subnets if ``assignPublicIp`` is set, otherwise the first available one of Private, Isolated, Public, in that order.
        :param cluster: The name of the cluster that hosts the service.
        :param capacity_provider_strategies: A list of Capacity Provider strategies used to place a service. Default: - undefined
        :param circuit_breaker: Whether to enable the deployment circuit breaker. If this property is defined, circuit breaker will be implicitly enabled. Default: - disabled
        :param cloud_map_options: The options for configuring an Amazon ECS service to use service discovery. Default: - AWS Cloud Map service discovery is not enabled.
        :param deployment_alarms: The alarm(s) to monitor during deployment, and behavior to apply if at least one enters a state of alarm during the deployment or bake time. Default: - No alarms will be monitored during deployment.
        :param deployment_controller: Specifies which deployment controller to use for the service. For more information, see `Amazon ECS Deployment Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`_ Default: - Rolling update (ECS)
        :param desired_count: The desired number of instantiations of the task definition to keep running on the service. Default: - When creating the service, default is 1; when updating the service, default uses the current task number.
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the tasks within the service. For more information, see `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_ Default: false
        :param enable_execute_command: Whether to enable the ability to execute into a container. Default: - undefined
        :param health_check_grace_period: The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. Default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
        :param max_healthy_percent: The maximum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that can run in a service during a deployment. Default: - 100 if daemon, otherwise 200
        :param min_healthy_percent: The minimum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that must continue to run and remain healthy during a deployment. Default: - 0 if daemon, otherwise 50
        :param propagate_tags: Specifies whether to propagate the tags from the task definition or the service to the tasks in the service. Valid values are: PropagatedTagSource.SERVICE, PropagatedTagSource.TASK_DEFINITION or PropagatedTagSource.NONE Default: PropagatedTagSource.NONE
        :param service_connect_configuration: Configuration for Service Connect. Default: No ports are advertised via Service Connect on this service, and the service cannot make requests to other services via Service Connect.
        :param service_name: The name of the service. Default: - CloudFormation-generated name.
        :param task_definition_revision: Revision number for the task definition or ``latest`` to use the latest active task revision. Default: - Uses the revision of the passed task definition deployed by CloudFormation
        :param volume_configurations: Configuration details for a volume used by the service. This allows you to specify details about the EBS volume that can be attched to ECS tasks. Default: - undefined
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e12b1694d522e22e1ee4af1e81d5ce1981bdbafbc6b90c2e774f06adf08440)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkFargateServiceProps(
            task_definition=task_definition,
            assign_public_ip=assign_public_ip,
            platform_version=platform_version,
            security_groups=security_groups,
            vpc_subnets=vpc_subnets,
            cluster=cluster,
            capacity_provider_strategies=capacity_provider_strategies,
            circuit_breaker=circuit_breaker,
            cloud_map_options=cloud_map_options,
            deployment_alarms=deployment_alarms,
            deployment_controller=deployment_controller,
            desired_count=desired_count,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            health_check_grace_period=health_check_grace_period,
            max_healthy_percent=max_healthy_percent,
            min_healthy_percent=min_healthy_percent,
            propagate_tags=propagate_tags,
            service_connect_configuration=service_connect_configuration,
            service_name=service_name,
            task_definition_revision=task_definition_revision,
            volume_configurations=volume_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkFargateServiceProps",
    jsii_struct_bases=[_aws_cdk_aws_ecs_ceddda9d.FargateServiceProps],
    name_mapping={
        "cluster": "cluster",
        "capacity_provider_strategies": "capacityProviderStrategies",
        "circuit_breaker": "circuitBreaker",
        "cloud_map_options": "cloudMapOptions",
        "deployment_alarms": "deploymentAlarms",
        "deployment_controller": "deploymentController",
        "desired_count": "desiredCount",
        "enable_ecs_managed_tags": "enableECSManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "health_check_grace_period": "healthCheckGracePeriod",
        "max_healthy_percent": "maxHealthyPercent",
        "min_healthy_percent": "minHealthyPercent",
        "propagate_tags": "propagateTags",
        "service_connect_configuration": "serviceConnectConfiguration",
        "service_name": "serviceName",
        "task_definition_revision": "taskDefinitionRevision",
        "volume_configurations": "volumeConfigurations",
        "task_definition": "taskDefinition",
        "assign_public_ip": "assignPublicIp",
        "platform_version": "platformVersion",
        "security_groups": "securityGroups",
        "vpc_subnets": "vpcSubnets",
    },
)
class CkFargateServiceProps(_aws_cdk_aws_ecs_ceddda9d.FargateServiceProps):
    def __init__(
        self,
        *,
        cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]] = None,
        circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_map_options: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_alarms: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentController, typing.Dict[builtins.str, typing.Any]]] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        max_healthy_percent: typing.Optional[jsii.Number] = None,
        min_healthy_percent: typing.Optional[jsii.Number] = None,
        propagate_tags: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.PropagatedTagSource] = None,
        service_connect_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps, typing.Dict[builtins.str, typing.Any]]] = None,
        service_name: typing.Optional[builtins.str] = None,
        task_definition_revision: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.TaskDefinitionRevision] = None,
        volume_configurations: typing.Optional[typing.Sequence[_aws_cdk_aws_ecs_ceddda9d.ServiceManagedVolume]] = None,
        task_definition: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        platform_version: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.FargatePlatformVersion] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''CloudKitect Fargate Service component properties.

        :param cluster: The name of the cluster that hosts the service.
        :param capacity_provider_strategies: A list of Capacity Provider strategies used to place a service. Default: - undefined
        :param circuit_breaker: Whether to enable the deployment circuit breaker. If this property is defined, circuit breaker will be implicitly enabled. Default: - disabled
        :param cloud_map_options: The options for configuring an Amazon ECS service to use service discovery. Default: - AWS Cloud Map service discovery is not enabled.
        :param deployment_alarms: The alarm(s) to monitor during deployment, and behavior to apply if at least one enters a state of alarm during the deployment or bake time. Default: - No alarms will be monitored during deployment.
        :param deployment_controller: Specifies which deployment controller to use for the service. For more information, see `Amazon ECS Deployment Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`_ Default: - Rolling update (ECS)
        :param desired_count: The desired number of instantiations of the task definition to keep running on the service. Default: - When creating the service, default is 1; when updating the service, default uses the current task number.
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the tasks within the service. For more information, see `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_ Default: false
        :param enable_execute_command: Whether to enable the ability to execute into a container. Default: - undefined
        :param health_check_grace_period: The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. Default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
        :param max_healthy_percent: The maximum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that can run in a service during a deployment. Default: - 100 if daemon, otherwise 200
        :param min_healthy_percent: The minimum number of tasks, specified as a percentage of the Amazon ECS service's DesiredCount value, that must continue to run and remain healthy during a deployment. Default: - 0 if daemon, otherwise 50
        :param propagate_tags: Specifies whether to propagate the tags from the task definition or the service to the tasks in the service. Valid values are: PropagatedTagSource.SERVICE, PropagatedTagSource.TASK_DEFINITION or PropagatedTagSource.NONE Default: PropagatedTagSource.NONE
        :param service_connect_configuration: Configuration for Service Connect. Default: No ports are advertised via Service Connect on this service, and the service cannot make requests to other services via Service Connect.
        :param service_name: The name of the service. Default: - CloudFormation-generated name.
        :param task_definition_revision: Revision number for the task definition or ``latest`` to use the latest active task revision. Default: - Uses the revision of the passed task definition deployed by CloudFormation
        :param volume_configurations: Configuration details for a volume used by the service. This allows you to specify details about the EBS volume that can be attched to ECS tasks. Default: - undefined
        :param task_definition: The task definition to use for tasks in the service. [disable-awslint:ref-via-interface]
        :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. If true, each task will receive a public IP address. Default: false
        :param platform_version: The platform version on which to run your service. If one is not specified, the LATEST platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the Amazon Elastic Container Service Developer Guide. Default: Latest
        :param security_groups: The security groups to associate with the service. If you do not specify a security group, a new security group is created. Default: - A new security group is created.
        :param vpc_subnets: The subnets to associate with the service. Default: - Public subnets if ``assignPublicIp`` is set, otherwise the first available one of Private, Isolated, Public, in that order.
        '''
        if isinstance(circuit_breaker, dict):
            circuit_breaker = _aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker(**circuit_breaker)
        if isinstance(cloud_map_options, dict):
            cloud_map_options = _aws_cdk_aws_ecs_ceddda9d.CloudMapOptions(**cloud_map_options)
        if isinstance(deployment_alarms, dict):
            deployment_alarms = _aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig(**deployment_alarms)
        if isinstance(deployment_controller, dict):
            deployment_controller = _aws_cdk_aws_ecs_ceddda9d.DeploymentController(**deployment_controller)
        if isinstance(service_connect_configuration, dict):
            service_connect_configuration = _aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps(**service_connect_configuration)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce46173ac88c02abf267864dbd28c447cb4709c7710be240a43dd34036e313b)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument capacity_provider_strategies", value=capacity_provider_strategies, expected_type=type_hints["capacity_provider_strategies"])
            check_type(argname="argument circuit_breaker", value=circuit_breaker, expected_type=type_hints["circuit_breaker"])
            check_type(argname="argument cloud_map_options", value=cloud_map_options, expected_type=type_hints["cloud_map_options"])
            check_type(argname="argument deployment_alarms", value=deployment_alarms, expected_type=type_hints["deployment_alarms"])
            check_type(argname="argument deployment_controller", value=deployment_controller, expected_type=type_hints["deployment_controller"])
            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
            check_type(argname="argument max_healthy_percent", value=max_healthy_percent, expected_type=type_hints["max_healthy_percent"])
            check_type(argname="argument min_healthy_percent", value=min_healthy_percent, expected_type=type_hints["min_healthy_percent"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument service_connect_configuration", value=service_connect_configuration, expected_type=type_hints["service_connect_configuration"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument task_definition_revision", value=task_definition_revision, expected_type=type_hints["task_definition_revision"])
            check_type(argname="argument volume_configurations", value=volume_configurations, expected_type=type_hints["volume_configurations"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "task_definition": task_definition,
        }
        if capacity_provider_strategies is not None:
            self._values["capacity_provider_strategies"] = capacity_provider_strategies
        if circuit_breaker is not None:
            self._values["circuit_breaker"] = circuit_breaker
        if cloud_map_options is not None:
            self._values["cloud_map_options"] = cloud_map_options
        if deployment_alarms is not None:
            self._values["deployment_alarms"] = deployment_alarms
        if deployment_controller is not None:
            self._values["deployment_controller"] = deployment_controller
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if max_healthy_percent is not None:
            self._values["max_healthy_percent"] = max_healthy_percent
        if min_healthy_percent is not None:
            self._values["min_healthy_percent"] = min_healthy_percent
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if service_connect_configuration is not None:
            self._values["service_connect_configuration"] = service_connect_configuration
        if service_name is not None:
            self._values["service_name"] = service_name
        if task_definition_revision is not None:
            self._values["task_definition_revision"] = task_definition_revision
        if volume_configurations is not None:
            self._values["volume_configurations"] = volume_configurations
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def cluster(self) -> _aws_cdk_aws_ecs_ceddda9d.ICluster:
        '''The name of the cluster that hosts the service.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.ICluster, result)

    @builtins.property
    def capacity_provider_strategies(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ecs_ceddda9d.CapacityProviderStrategy]]:
        '''A list of Capacity Provider strategies used to place a service.

        :default: - undefined
        '''
        result = self._values.get("capacity_provider_strategies")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ecs_ceddda9d.CapacityProviderStrategy]], result)

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
    def cloud_map_options(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.CloudMapOptions]:
        '''The options for configuring an Amazon ECS service to use service discovery.

        :default: - AWS Cloud Map service discovery is not enabled.
        '''
        result = self._values.get("cloud_map_options")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.CloudMapOptions], result)

    @builtins.property
    def deployment_alarms(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig]:
        '''The alarm(s) to monitor during deployment, and behavior to apply if at least one enters a state of alarm during the deployment or bake time.

        :default: - No alarms will be monitored during deployment.
        '''
        result = self._values.get("deployment_alarms")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig], result)

    @builtins.property
    def deployment_controller(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.DeploymentController]:
        '''Specifies which deployment controller to use for the service.

        For more information, see
        `Amazon ECS Deployment Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`_

        :default: - Rolling update (ECS)
        '''
        result = self._values.get("deployment_controller")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.DeploymentController], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        '''The desired number of instantiations of the task definition to keep running on the service.

        :default:

        - When creating the service, default is 1; when updating the service, default uses
        the current task number.
        '''
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_ecs_managed_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to enable Amazon ECS managed tags for the tasks within the service.

        For more information, see
        `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_

        :default: false
        '''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_execute_command(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable the ability to execute into a container.

        :default: - undefined
        '''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.

        :default: - defaults to 60 seconds if at least one load balancer is in-use and it is not already set
        '''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

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
    def propagate_tags(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.PropagatedTagSource]:
        '''Specifies whether to propagate the tags from the task definition or the service to the tasks in the service.

        Valid values are: PropagatedTagSource.SERVICE, PropagatedTagSource.TASK_DEFINITION or PropagatedTagSource.NONE

        :default: PropagatedTagSource.NONE
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.PropagatedTagSource], result)

    @builtins.property
    def service_connect_configuration(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps]:
        '''Configuration for Service Connect.

        :default:

        No ports are advertised via Service Connect on this service, and the service
        cannot make requests to other services via Service Connect.
        '''
        result = self._values.get("service_connect_configuration")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''The name of the service.

        :default: - CloudFormation-generated name.
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_definition_revision(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.TaskDefinitionRevision]:
        '''Revision number for the task definition or ``latest`` to use the latest active task revision.

        :default: - Uses the revision of the passed task definition deployed by CloudFormation
        '''
        result = self._values.get("task_definition_revision")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.TaskDefinitionRevision], result)

    @builtins.property
    def volume_configurations(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ecs_ceddda9d.ServiceManagedVolume]]:
        '''Configuration details for a volume used by the service.

        This allows you to specify
        details about the EBS volume that can be attched to ECS tasks.

        :default: - undefined
        '''
        result = self._values.get("volume_configurations")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ecs_ceddda9d.ServiceManagedVolume]], result)

    @builtins.property
    def task_definition(self) -> _aws_cdk_aws_ecs_ceddda9d.TaskDefinition:
        '''The task definition to use for tasks in the service.

        [disable-awslint:ref-via-interface]
        '''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.TaskDefinition, result)

    @builtins.property
    def assign_public_ip(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the task's elastic network interface receives a public IP address.

        If true, each task will receive a public IP address.

        :default: false
        '''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def platform_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.FargatePlatformVersion]:
        '''The platform version on which to run your service.

        If one is not specified, the LATEST platform version is used by default. For more information, see
        `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_
        in the Amazon Elastic Container Service Developer Guide.

        :default: Latest
        '''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.FargatePlatformVersion], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]]:
        '''The security groups to associate with the service.

        If you do not specify a security group, a new security group is created.

        :default: - A new security group is created.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''The subnets to associate with the service.

        :default: - Public subnets if ``assignPublicIp`` is set, otherwise the first available one of Private, Isolated, Public, in that order.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkFargateServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkFargateTaskDefinition(
    _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkFargateTaskDefinition",
):
    '''Well Architected Fargate Task Definition component.



    Default Configuration

    CPU: 2048 (2vCPU) for Production
    Memory: 4096 GB for Production
    Storage: 50 GB for Production


    Default Alarms

    None

    Note that the default alarm uses the CcAlarm construct, which sets up an alarm
    action to notify the SNS Topic *AlarmEventsTopic* by default.


    Examples

    Default Usage Example::

       new CcFargateTaskDefinition(this, "LogicalId", {});

    Custom Configuration Example::

       new CcFargateTaskDefinition(this, "LogicalId", {
          cpu: 2048
       });


    Compliance

    It addresses the following compliance requirements

    1. Encrypted storage
       .. epigraph::

          - Risk Level: High
          - Compliance: NIST4
          - Well Architected Pillar: Security

    2. Cost Optimization
       .. epigraph::

          - Risk Level: Low
          - Compliance: NA
          - Well Architected Pillar: Cost Optimization
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
        runtime_platform: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.RuntimePlatform, typing.Dict[builtins.str, typing.Any]]] = None,
        execution_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        family: typing.Optional[builtins.str] = None,
        proxy_configuration: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ProxyConfiguration] = None,
        task_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.Volume, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cpu: The number of cpu units used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 8192 (8 vCPU) - Available memory values: Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) 16384 (16 vCPU) - Available memory values: Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) Default: 256
        :param ephemeral_storage_gib: The amount (in GiB) of ephemeral storage to be allocated to the task. The maximum supported value is 200 GiB. NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later. Default: 20
        :param memory_limit_mib: The amount (in MiB) of memory used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) - Available cpu values: 8192 (8 vCPU) Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) - Available cpu values: 16384 (16 vCPU) Default: 512
        :param runtime_platform: The operating system that your task definitions are running on. A runtimePlatform is supported only for tasks using the Fargate launch type. Default: - Undefined.
        :param execution_role: The name of the IAM task execution role that grants the ECS agent permission to call AWS APIs on your behalf. The role will be used to retrieve container images from ECR and create CloudWatch log groups. Default: - An execution role will be automatically created if you use ECR images in your task definition.
        :param family: The name of a family that this task definition is registered to. A family groups multiple versions of a task definition. Default: - Automatically generated name.
        :param proxy_configuration: The configuration details for the App Mesh proxy. Default: - No proxy configuration.
        :param task_role: The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf. Default: - A task role is automatically created for you.
        :param volumes: The list of volume definitions for the task. For more information, see `Task Definition Parameter Volumes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide//task_definition_parameters.html#volumes>`_. Default: - No volumes are passed to the Docker daemon on a container instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd42aad99202dee86e6119525894709c82f4f5f00011f17d4c156bee4052b04e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkFargateTaskDefinitionProps(
            cpu=cpu,
            ephemeral_storage_gib=ephemeral_storage_gib,
            memory_limit_mib=memory_limit_mib,
            runtime_platform=runtime_platform,
            execution_role=execution_role,
            family=family,
            proxy_configuration=proxy_configuration,
            task_role=task_role,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkFargateTaskDefinitionProps",
    jsii_struct_bases=[_aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinitionProps],
    name_mapping={
        "execution_role": "executionRole",
        "family": "family",
        "proxy_configuration": "proxyConfiguration",
        "task_role": "taskRole",
        "volumes": "volumes",
        "cpu": "cpu",
        "ephemeral_storage_gib": "ephemeralStorageGiB",
        "memory_limit_mib": "memoryLimitMiB",
        "runtime_platform": "runtimePlatform",
    },
)
class CkFargateTaskDefinitionProps(
    _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinitionProps,
):
    def __init__(
        self,
        *,
        execution_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        family: typing.Optional[builtins.str] = None,
        proxy_configuration: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ProxyConfiguration] = None,
        task_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.Volume, typing.Dict[builtins.str, typing.Any]]]] = None,
        cpu: typing.Optional[jsii.Number] = None,
        ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
        runtime_platform: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.RuntimePlatform, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Well Architected Fargate Task Definition properties.

        :param execution_role: The name of the IAM task execution role that grants the ECS agent permission to call AWS APIs on your behalf. The role will be used to retrieve container images from ECR and create CloudWatch log groups. Default: - An execution role will be automatically created if you use ECR images in your task definition.
        :param family: The name of a family that this task definition is registered to. A family groups multiple versions of a task definition. Default: - Automatically generated name.
        :param proxy_configuration: The configuration details for the App Mesh proxy. Default: - No proxy configuration.
        :param task_role: The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf. Default: - A task role is automatically created for you.
        :param volumes: The list of volume definitions for the task. For more information, see `Task Definition Parameter Volumes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide//task_definition_parameters.html#volumes>`_. Default: - No volumes are passed to the Docker daemon on a container instance.
        :param cpu: The number of cpu units used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 8192 (8 vCPU) - Available memory values: Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) 16384 (16 vCPU) - Available memory values: Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) Default: 256
        :param ephemeral_storage_gib: The amount (in GiB) of ephemeral storage to be allocated to the task. The maximum supported value is 200 GiB. NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later. Default: 20
        :param memory_limit_mib: The amount (in MiB) of memory used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) - Available cpu values: 8192 (8 vCPU) Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) - Available cpu values: 16384 (16 vCPU) Default: 512
        :param runtime_platform: The operating system that your task definitions are running on. A runtimePlatform is supported only for tasks using the Fargate launch type. Default: - Undefined.
        '''
        if isinstance(runtime_platform, dict):
            runtime_platform = _aws_cdk_aws_ecs_ceddda9d.RuntimePlatform(**runtime_platform)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__361f07a5bc0b8cd028d29946211aa877c11ec722d36e62ea253c80e86dbe3f74)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument proxy_configuration", value=proxy_configuration, expected_type=type_hints["proxy_configuration"])
            check_type(argname="argument task_role", value=task_role, expected_type=type_hints["task_role"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument ephemeral_storage_gib", value=ephemeral_storage_gib, expected_type=type_hints["ephemeral_storage_gib"])
            check_type(argname="argument memory_limit_mib", value=memory_limit_mib, expected_type=type_hints["memory_limit_mib"])
            check_type(argname="argument runtime_platform", value=runtime_platform, expected_type=type_hints["runtime_platform"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if execution_role is not None:
            self._values["execution_role"] = execution_role
        if family is not None:
            self._values["family"] = family
        if proxy_configuration is not None:
            self._values["proxy_configuration"] = proxy_configuration
        if task_role is not None:
            self._values["task_role"] = task_role
        if volumes is not None:
            self._values["volumes"] = volumes
        if cpu is not None:
            self._values["cpu"] = cpu
        if ephemeral_storage_gib is not None:
            self._values["ephemeral_storage_gib"] = ephemeral_storage_gib
        if memory_limit_mib is not None:
            self._values["memory_limit_mib"] = memory_limit_mib
        if runtime_platform is not None:
            self._values["runtime_platform"] = runtime_platform

    @builtins.property
    def execution_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''The name of the IAM task execution role that grants the ECS agent permission to call AWS APIs on your behalf.

        The role will be used to retrieve container images from ECR and create CloudWatch log groups.

        :default: - An execution role will be automatically created if you use ECR images in your task definition.
        '''
        result = self._values.get("execution_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def family(self) -> typing.Optional[builtins.str]:
        '''The name of a family that this task definition is registered to.

        A family groups multiple versions of a task definition.

        :default: - Automatically generated name.
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_configuration(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ProxyConfiguration]:
        '''The configuration details for the App Mesh proxy.

        :default: - No proxy configuration.
        '''
        result = self._values.get("proxy_configuration")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ProxyConfiguration], result)

    @builtins.property
    def task_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf.

        :default: - A task role is automatically created for you.
        '''
        result = self._values.get("task_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[_aws_cdk_aws_ecs_ceddda9d.Volume]]:
        '''The list of volume definitions for the task.

        For more information, see
        `Task Definition Parameter Volumes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide//task_definition_parameters.html#volumes>`_.

        :default: - No volumes are passed to the Docker daemon on a container instance.
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ecs_ceddda9d.Volume]], result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''The number of cpu units used by the task.

        For tasks using the Fargate launch type,
        this field is required and you must use one of the following values,
        which determines your range of valid values for the memory parameter:

        256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)

        512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)

        1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

        2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

        4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)

        8192 (8 vCPU) - Available memory values: Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB)

        16384 (16 vCPU) - Available memory values: Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB)

        :default: 256
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ephemeral_storage_gib(self) -> typing.Optional[jsii.Number]:
        '''The amount (in GiB) of ephemeral storage to be allocated to the task.

        The maximum supported value is 200 GiB.

        NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later.

        :default: 20
        '''
        result = self._values.get("ephemeral_storage_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_limit_mib(self) -> typing.Optional[jsii.Number]:
        '''The amount (in MiB) of memory used by the task.

        For tasks using the Fargate launch type,
        this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter:

        512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU)

        1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU)

        2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU)

        Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU)

        Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU)

        Between 16384 (16 GB) and 61440 (60 GB) in increments of 4096 (4 GB) - Available cpu values: 8192 (8 vCPU)

        Between 32768 (32 GB) and 122880 (120 GB) in increments of 8192 (8 GB) - Available cpu values: 16384 (16 vCPU)

        :default: 512
        '''
        result = self._values.get("memory_limit_mib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def runtime_platform(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ecs_ceddda9d.RuntimePlatform]:
        '''The operating system that your task definitions are running on.

        A runtimePlatform is supported only for tasks using the Fargate launch type.

        :default: - Undefined.
        '''
        result = self._values.get("runtime_platform")
        return typing.cast(typing.Optional[_aws_cdk_aws_ecs_ceddda9d.RuntimePlatform], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkFargateTaskDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkPublicApplicationLoadBalancerProps",
    jsii_struct_bases=[
        _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationLoadBalancerProps
    ],
    name_mapping={
        "vpc": "vpc",
        "cross_zone_enabled": "crossZoneEnabled",
        "deletion_protection": "deletionProtection",
        "deny_all_igw_traffic": "denyAllIgwTraffic",
        "internet_facing": "internetFacing",
        "load_balancer_name": "loadBalancerName",
        "vpc_subnets": "vpcSubnets",
        "client_keep_alive": "clientKeepAlive",
        "desync_mitigation_mode": "desyncMitigationMode",
        "drop_invalid_header_fields": "dropInvalidHeaderFields",
        "http2_enabled": "http2Enabled",
        "idle_timeout": "idleTimeout",
        "ip_address_type": "ipAddressType",
        "preserve_host_header": "preserveHostHeader",
        "preserve_xff_client_port": "preserveXffClientPort",
        "security_group": "securityGroup",
        "waf_fail_open": "wafFailOpen",
        "x_amzn_tls_version_and_cipher_suite_headers": "xAmznTlsVersionAndCipherSuiteHeaders",
        "xff_header_processing_mode": "xffHeaderProcessingMode",
    },
)
class CkPublicApplicationLoadBalancerProps(
    _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationLoadBalancerProps,
):
    def __init__(
        self,
        *,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        cross_zone_enabled: typing.Optional[builtins.bool] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        deny_all_igw_traffic: typing.Optional[builtins.bool] = None,
        internet_facing: typing.Optional[builtins.bool] = None,
        load_balancer_name: typing.Optional[builtins.str] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        client_keep_alive: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        desync_mitigation_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.DesyncMitigationMode] = None,
        drop_invalid_header_fields: typing.Optional[builtins.bool] = None,
        http2_enabled: typing.Optional[builtins.bool] = None,
        idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        ip_address_type: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.IpAddressType] = None,
        preserve_host_header: typing.Optional[builtins.bool] = None,
        preserve_xff_client_port: typing.Optional[builtins.bool] = None,
        security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
        waf_fail_open: typing.Optional[builtins.bool] = None,
        x_amzn_tls_version_and_cipher_suite_headers: typing.Optional[builtins.bool] = None,
        xff_header_processing_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.XffHeaderProcessingMode] = None,
    ) -> None:
        '''CloudKitect  Public Application Load Balancer component properties.

        :param vpc: The VPC network to place the load balancer in.
        :param cross_zone_enabled: Indicates whether cross-zone load balancing is enabled. Default: - false for Network Load Balancers and true for Application Load Balancers.
        :param deletion_protection: Indicates whether deletion protection is enabled. Default: false
        :param deny_all_igw_traffic: Indicates whether the load balancer blocks traffic through the Internet Gateway (IGW). Default: - false for internet-facing load balancers and true for internal load balancers
        :param internet_facing: Whether the load balancer has an internet-routable address. Default: false
        :param load_balancer_name: Name of the load balancer. Default: - Automatically generated name.
        :param vpc_subnets: Which subnets place the load balancer in. Default: - the Vpc default strategy.
        :param client_keep_alive: The client keep alive duration. The valid range is 60 to 604800 seconds (1 minute to 7 days). Default: - Duration.seconds(3600)
        :param desync_mitigation_mode: Determines how the load balancer handles requests that might pose a security risk to your application. Default: DesyncMitigationMode.DEFENSIVE
        :param drop_invalid_header_fields: Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true) or routed to targets (false). Default: false
        :param http2_enabled: Indicates whether HTTP/2 is enabled. Default: true
        :param idle_timeout: The load balancer idle timeout, in seconds. Default: 60
        :param ip_address_type: The type of IP addresses to use. Default: IpAddressType.IPV4
        :param preserve_host_header: Indicates whether the Application Load Balancer should preserve the host header in the HTTP request and send it to the target without any change. Default: false
        :param preserve_xff_client_port: Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer. Default: false
        :param security_group: Security group to associate with this load balancer. Default: A security group is created
        :param waf_fail_open: Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF. Default: false
        :param x_amzn_tls_version_and_cipher_suite_headers: Indicates whether the two headers (x-amzn-tls-version and x-amzn-tls-cipher-suite), which contain information about the negotiated TLS version and cipher suite, are added to the client request before sending it to the target. The x-amzn-tls-version header has information about the TLS protocol version negotiated with the client, and the x-amzn-tls-cipher-suite header has information about the cipher suite negotiated with the client. Both headers are in OpenSSL format. Default: false
        :param xff_header_processing_mode: Enables you to modify, preserve, or remove the X-Forwarded-For header in the HTTP request before the Application Load Balancer sends the request to the target. Default: XffHeaderProcessingMode.APPEND
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e087734a19fa17ee4c5f05e24a59d0eed8a597cbbcb90e7afb1a1a3ffd841de)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument cross_zone_enabled", value=cross_zone_enabled, expected_type=type_hints["cross_zone_enabled"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument deny_all_igw_traffic", value=deny_all_igw_traffic, expected_type=type_hints["deny_all_igw_traffic"])
            check_type(argname="argument internet_facing", value=internet_facing, expected_type=type_hints["internet_facing"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument client_keep_alive", value=client_keep_alive, expected_type=type_hints["client_keep_alive"])
            check_type(argname="argument desync_mitigation_mode", value=desync_mitigation_mode, expected_type=type_hints["desync_mitigation_mode"])
            check_type(argname="argument drop_invalid_header_fields", value=drop_invalid_header_fields, expected_type=type_hints["drop_invalid_header_fields"])
            check_type(argname="argument http2_enabled", value=http2_enabled, expected_type=type_hints["http2_enabled"])
            check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument preserve_host_header", value=preserve_host_header, expected_type=type_hints["preserve_host_header"])
            check_type(argname="argument preserve_xff_client_port", value=preserve_xff_client_port, expected_type=type_hints["preserve_xff_client_port"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument waf_fail_open", value=waf_fail_open, expected_type=type_hints["waf_fail_open"])
            check_type(argname="argument x_amzn_tls_version_and_cipher_suite_headers", value=x_amzn_tls_version_and_cipher_suite_headers, expected_type=type_hints["x_amzn_tls_version_and_cipher_suite_headers"])
            check_type(argname="argument xff_header_processing_mode", value=xff_header_processing_mode, expected_type=type_hints["xff_header_processing_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
        }
        if cross_zone_enabled is not None:
            self._values["cross_zone_enabled"] = cross_zone_enabled
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if deny_all_igw_traffic is not None:
            self._values["deny_all_igw_traffic"] = deny_all_igw_traffic
        if internet_facing is not None:
            self._values["internet_facing"] = internet_facing
        if load_balancer_name is not None:
            self._values["load_balancer_name"] = load_balancer_name
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if client_keep_alive is not None:
            self._values["client_keep_alive"] = client_keep_alive
        if desync_mitigation_mode is not None:
            self._values["desync_mitigation_mode"] = desync_mitigation_mode
        if drop_invalid_header_fields is not None:
            self._values["drop_invalid_header_fields"] = drop_invalid_header_fields
        if http2_enabled is not None:
            self._values["http2_enabled"] = http2_enabled
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if preserve_host_header is not None:
            self._values["preserve_host_header"] = preserve_host_header
        if preserve_xff_client_port is not None:
            self._values["preserve_xff_client_port"] = preserve_xff_client_port
        if security_group is not None:
            self._values["security_group"] = security_group
        if waf_fail_open is not None:
            self._values["waf_fail_open"] = waf_fail_open
        if x_amzn_tls_version_and_cipher_suite_headers is not None:
            self._values["x_amzn_tls_version_and_cipher_suite_headers"] = x_amzn_tls_version_and_cipher_suite_headers
        if xff_header_processing_mode is not None:
            self._values["xff_header_processing_mode"] = xff_header_processing_mode

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The VPC network to place the load balancer in.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def cross_zone_enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether cross-zone load balancing is enabled.

        :default: - false for Network Load Balancers and true for Application Load Balancers.
        '''
        result = self._values.get("cross_zone_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether deletion protection is enabled.

        :default: false
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deny_all_igw_traffic(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the load balancer blocks traffic through the Internet Gateway (IGW).

        :default: - false for internet-facing load balancers and true for internal load balancers
        '''
        result = self._values.get("deny_all_igw_traffic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def internet_facing(self) -> typing.Optional[builtins.bool]:
        '''Whether the load balancer has an internet-routable address.

        :default: false
        '''
        result = self._values.get("internet_facing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def load_balancer_name(self) -> typing.Optional[builtins.str]:
        '''Name of the load balancer.

        :default: - Automatically generated name.
        '''
        result = self._values.get("load_balancer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''Which subnets place the load balancer in.

        :default: - the Vpc default strategy.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def client_keep_alive(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The client keep alive duration.

        The valid range is 60 to 604800 seconds (1 minute to 7 days).

        :default: - Duration.seconds(3600)
        '''
        result = self._values.get("client_keep_alive")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def desync_mitigation_mode(
        self,
    ) -> typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.DesyncMitigationMode]:
        '''Determines how the load balancer handles requests that might pose a security risk to your application.

        :default: DesyncMitigationMode.DEFENSIVE
        '''
        result = self._values.get("desync_mitigation_mode")
        return typing.cast(typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.DesyncMitigationMode], result)

    @builtins.property
    def drop_invalid_header_fields(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true) or routed to targets (false).

        :default: false
        '''
        result = self._values.get("drop_invalid_header_fields")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def http2_enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether HTTP/2 is enabled.

        :default: true
        '''
        result = self._values.get("http2_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The load balancer idle timeout, in seconds.

        :default: 60
        '''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def ip_address_type(
        self,
    ) -> typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.IpAddressType]:
        '''The type of IP addresses to use.

        :default: IpAddressType.IPV4
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.IpAddressType], result)

    @builtins.property
    def preserve_host_header(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the Application Load Balancer should preserve the host header in the HTTP request and send it to the target without any change.

        :default: false
        '''
        result = self._values.get("preserve_host_header")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def preserve_xff_client_port(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer.

        :default: false
        '''
        result = self._values.get("preserve_xff_client_port")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def security_group(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]:
        '''Security group to associate with this load balancer.

        :default: A security group is created
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup], result)

    @builtins.property
    def waf_fail_open(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF.

        :default: false
        '''
        result = self._values.get("waf_fail_open")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def x_amzn_tls_version_and_cipher_suite_headers(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether the two headers (x-amzn-tls-version and x-amzn-tls-cipher-suite), which contain information about the negotiated TLS version and cipher suite, are added to the client request before sending it to the target.

        The x-amzn-tls-version header has information about the TLS protocol version negotiated with the client,
        and the x-amzn-tls-cipher-suite header has information about the cipher suite negotiated with the client.

        Both headers are in OpenSSL format.

        :default: false
        '''
        result = self._values.get("x_amzn_tls_version_and_cipher_suite_headers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def xff_header_processing_mode(
        self,
    ) -> typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.XffHeaderProcessingMode]:
        '''Enables you to modify, preserve, or remove the X-Forwarded-For header in the HTTP request before the Application Load Balancer sends the request to the target.

        :default: XffHeaderProcessingMode.APPEND
        '''
        result = self._values.get("xff_header_processing_mode")
        return typing.cast(typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.XffHeaderProcessingMode], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkPublicApplicationLoadBalancerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkPublicApplicationLoadbalancer(
    _aws_cdk_aws_elasticloadbalancingv2_ceddda9d.ApplicationLoadBalancer,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkPublicApplicationLoadbalancer",
):
    '''CloudKitect Public Application Load Balancer component. This load balancer is created in public subnet.



    Default Configuration

    Drop Invalid header fields: true
    Removal Policy: Retain in Production


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkPublicApplicationLoadbalancer(this, "LogicalId", {});

    Custom Configuration Example::

       new CkPublicApplicationLoadbalancer(this, "LogicalId", {
          deletionProtection: false
       });


    Compliance

    It addresses the following compliance requirements

    1. Ensure ALB is always using https, by redirecting http to https
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, APRA, NIST4
          - Well Architected Pillar: Security

    2. Security group to only allow https traffic
       .. epigraph::

          - Risk Level: High
          - Compliance: PCI, APRA, MAS, NIST4
          - Well Architected Pillar: Security
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        client_keep_alive: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        desync_mitigation_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.DesyncMitigationMode] = None,
        drop_invalid_header_fields: typing.Optional[builtins.bool] = None,
        http2_enabled: typing.Optional[builtins.bool] = None,
        idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        ip_address_type: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.IpAddressType] = None,
        preserve_host_header: typing.Optional[builtins.bool] = None,
        preserve_xff_client_port: typing.Optional[builtins.bool] = None,
        security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
        waf_fail_open: typing.Optional[builtins.bool] = None,
        x_amzn_tls_version_and_cipher_suite_headers: typing.Optional[builtins.bool] = None,
        xff_header_processing_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.XffHeaderProcessingMode] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        cross_zone_enabled: typing.Optional[builtins.bool] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        deny_all_igw_traffic: typing.Optional[builtins.bool] = None,
        internet_facing: typing.Optional[builtins.bool] = None,
        load_balancer_name: typing.Optional[builtins.str] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param client_keep_alive: The client keep alive duration. The valid range is 60 to 604800 seconds (1 minute to 7 days). Default: - Duration.seconds(3600)
        :param desync_mitigation_mode: Determines how the load balancer handles requests that might pose a security risk to your application. Default: DesyncMitigationMode.DEFENSIVE
        :param drop_invalid_header_fields: Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true) or routed to targets (false). Default: false
        :param http2_enabled: Indicates whether HTTP/2 is enabled. Default: true
        :param idle_timeout: The load balancer idle timeout, in seconds. Default: 60
        :param ip_address_type: The type of IP addresses to use. Default: IpAddressType.IPV4
        :param preserve_host_header: Indicates whether the Application Load Balancer should preserve the host header in the HTTP request and send it to the target without any change. Default: false
        :param preserve_xff_client_port: Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer. Default: false
        :param security_group: Security group to associate with this load balancer. Default: A security group is created
        :param waf_fail_open: Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF. Default: false
        :param x_amzn_tls_version_and_cipher_suite_headers: Indicates whether the two headers (x-amzn-tls-version and x-amzn-tls-cipher-suite), which contain information about the negotiated TLS version and cipher suite, are added to the client request before sending it to the target. The x-amzn-tls-version header has information about the TLS protocol version negotiated with the client, and the x-amzn-tls-cipher-suite header has information about the cipher suite negotiated with the client. Both headers are in OpenSSL format. Default: false
        :param xff_header_processing_mode: Enables you to modify, preserve, or remove the X-Forwarded-For header in the HTTP request before the Application Load Balancer sends the request to the target. Default: XffHeaderProcessingMode.APPEND
        :param vpc: The VPC network to place the load balancer in.
        :param cross_zone_enabled: Indicates whether cross-zone load balancing is enabled. Default: - false for Network Load Balancers and true for Application Load Balancers.
        :param deletion_protection: Indicates whether deletion protection is enabled. Default: false
        :param deny_all_igw_traffic: Indicates whether the load balancer blocks traffic through the Internet Gateway (IGW). Default: - false for internet-facing load balancers and true for internal load balancers
        :param internet_facing: Whether the load balancer has an internet-routable address. Default: false
        :param load_balancer_name: Name of the load balancer. Default: - Automatically generated name.
        :param vpc_subnets: Which subnets place the load balancer in. Default: - the Vpc default strategy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca0d9947670f030b033e47f0f38e0021227de57a7a2b47a2cdc13ac24e32cb5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkPublicApplicationLoadBalancerProps(
            client_keep_alive=client_keep_alive,
            desync_mitigation_mode=desync_mitigation_mode,
            drop_invalid_header_fields=drop_invalid_header_fields,
            http2_enabled=http2_enabled,
            idle_timeout=idle_timeout,
            ip_address_type=ip_address_type,
            preserve_host_header=preserve_host_header,
            preserve_xff_client_port=preserve_xff_client_port,
            security_group=security_group,
            waf_fail_open=waf_fail_open,
            x_amzn_tls_version_and_cipher_suite_headers=x_amzn_tls_version_and_cipher_suite_headers,
            xff_header_processing_mode=xff_header_processing_mode,
            vpc=vpc,
            cross_zone_enabled=cross_zone_enabled,
            deletion_protection=deletion_protection,
            deny_all_igw_traffic=deny_all_igw_traffic,
            internet_facing=internet_facing,
            load_balancer_name=load_balancer_name,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="lbSecurityGroup")
    def lb_security_group(self) -> _aws_cdk_aws_ec2_ceddda9d.SecurityGroup:
        '''Security group created inside load balancer that only allows traffic from https.'''
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.SecurityGroup, jsii.get(self, "lbSecurityGroup"))


@jsii.enum(jsii_type="@cloudkitect/components.CkRegion")
class CkRegion(enum.Enum):
    '''AWS Regions.'''

    US_EAST_1 = "US_EAST_1"
    US_EAST_2 = "US_EAST_2"
    US_WEST_1 = "US_WEST_1"
    US_WEST_2 = "US_WEST_2"
    AF_SOUTH_1 = "AF_SOUTH_1"
    AP_EAST_1 = "AP_EAST_1"
    AP_SOUTH_1 = "AP_SOUTH_1"
    AP_SOUTH_2 = "AP_SOUTH_2"
    AP_SOUTHEAST_1 = "AP_SOUTHEAST_1"
    AP_SOUTHEAST_2 = "AP_SOUTHEAST_2"
    AP_SOUTHEAST_3 = "AP_SOUTHEAST_3"
    AP_SOUTHEAST_4 = "AP_SOUTHEAST_4"
    AP_NORTHEAST_1 = "AP_NORTHEAST_1"
    AP_NORTHEAST_2 = "AP_NORTHEAST_2"
    AP_NORTHEAST_3 = "AP_NORTHEAST_3"
    CA_CENTRAL_1 = "CA_CENTRAL_1"
    EU_SOUTH_1 = "EU_SOUTH_1"
    EU_WEST_1 = "EU_WEST_1"
    EU_WEST_2 = "EU_WEST_2"
    EU_WEST_3 = "EU_WEST_3"
    EU_SOUTH_2 = "EU_SOUTH_2"
    EU_NORTH_1 = "EU_NORTH_1"
    EU_CENTRAL_1 = "EU_CENTRAL_1"
    EU_CENTRAL_2 = "EU_CENTRAL_2"
    ME_SOUTH_1 = "ME_SOUTH_1"
    ME_CENTRAL = "ME_CENTRAL"
    SA_EAST_1 = "SA_EAST_1"


class CkRegionUtil(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkRegionUtil",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="allRegions")
    @builtins.classmethod
    def all_regions(cls) -> typing.List[CkRegion]:
        return typing.cast(typing.List[CkRegion], jsii.sinvoke(cls, "allRegions", []))

    @jsii.member(jsii_name="apRegions")
    @builtins.classmethod
    def ap_regions(cls) -> typing.List[CkRegion]:
        return typing.cast(typing.List[CkRegion], jsii.sinvoke(cls, "apRegions", []))

    @jsii.member(jsii_name="caRegions")
    @builtins.classmethod
    def ca_regions(cls) -> typing.List[CkRegion]:
        return typing.cast(typing.List[CkRegion], jsii.sinvoke(cls, "caRegions", []))

    @jsii.member(jsii_name="euRegions")
    @builtins.classmethod
    def eu_regions(cls) -> typing.List[CkRegion]:
        return typing.cast(typing.List[CkRegion], jsii.sinvoke(cls, "euRegions", []))

    @jsii.member(jsii_name="usRegions")
    @builtins.classmethod
    def us_regions(cls) -> typing.List[CkRegion]:
        return typing.cast(typing.List[CkRegion], jsii.sinvoke(cls, "usRegions", []))


class CkRepository(
    _aws_cdk_aws_ecr_ceddda9d.Repository,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkRepository",
):
    '''CloudKitect ECR Repository component used for creating ECR repositories.



    Default Configuration

    Encryption: KMS (AWS Managed Keys)
    Image Immutable: true


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Backups

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkRepository(this, "LogicalId", {});

    Custom Configuration Example::

       new CkRepository(this, "LogicalId", {
          imageScanOnPush: false
       });


    Compliance

    It addresses the following compliance requirements

    1. Enable scan on image push
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NA
          - Well Architected Pillar: Security

    2. Repository should be encrypted
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NA
          - Well Architected Pillar: Security

    3. Images tags should be immutable
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NA
          - Well Architected Pillar: Security, Operational Excellence

       Compliance Check Report
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
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
    ) -> None:
        '''
        :param scope: -
        :param id: -
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
            type_hints = typing.get_type_hints(_typecheckingstub__2376f4e71a94afd23fd636ce7f1d4eb5d33feec01877418cd71081984d77c78b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkRepositoryProps(
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


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkRepositoryProps",
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
    },
)
class CkRepositoryProps(_aws_cdk_aws_ecr_ceddda9d.RepositoryProps):
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
    ) -> None:
        '''CloudKitect ECR Repository component properties.

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
            type_hints = typing.get_type_hints(_typecheckingstub__64dae39510a9ea521ee30a14e934a7d117886670d130f86965e8561e0839736b)
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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkStack(
    _aws_cdk_ceddda9d.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkStack",
):
    '''CloudKitect stack component that is environment aware and provides several methods to find out the account type it is deployed so that other constructs can make decisions based on environments.



    Examples

    Default Usage Example::

       const stackProps = {
           ckApplication: 'ExampleApp',
           ckCompany: 'CloudKitect',
           ckAccountType: AccountType.UAT,
           env: {account: "ACCOUNT_ID", region: "us-east-1"}
       }
       new CkStack(app, "StackId", {
           ...stackProps
       });


    Compliance

    It addresses the following compliance requirements

    -
      1. Cloudformation stacks in use for defining infrastructure

      .. epigraph::

         - Risk Level: Medium
         - Compliance: APRA, MAS
         - Well Architected Pillar: Reliability, Operational Excellence
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ck_account_type: CkAccountType,
        ck_application: builtins.str,
        ck_company: builtins.str,
        ck_prefix: typing.Optional[builtins.str] = None,
        ck_removal_policy_override: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        cross_region_references: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[_aws_cdk_ceddda9d.Environment, typing.Dict[builtins.str, typing.Any]]] = None,
        permissions_boundary: typing.Optional[_aws_cdk_ceddda9d.PermissionsBoundary] = None,
        stack_name: typing.Optional[builtins.str] = None,
        suppress_template_indentation: typing.Optional[builtins.bool] = None,
        synthesizer: typing.Optional[_aws_cdk_ceddda9d.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ck_account_type: AccountType where the stack will be deployed.
        :param ck_application: Name of the application deployed by the stack.
        :param ck_company: Company the application is associated with.
        :param ck_prefix: Any prefix for the stack name to avoid conflicts. Default: empty
        :param ck_removal_policy_override: Flag to control the removalPolicy override for the components. Default: undefined, meaning it will use environment specific removal policy
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param cross_region_references: Enable this flag to allow native cross region stack references. Enabling this will create a CloudFormation custom resource in both the producing stack and consuming stack in order to perform the export/import This feature is currently experimental Default: false
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param permissions_boundary: Options for applying a permissions boundary to all IAM Roles and Users created within this Stage. Default: - no permissions boundary is applied
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param suppress_template_indentation: Enable this flag to suppress indentation in generated CloudFormation templates. If not specified, the value of the ``@aws-cdk/core:suppressTemplateIndentation`` context key will be used. If that is not specified, then the default value ``false`` will be used. Default: - the value of ``@aws-cdk/core:suppressTemplateIndentation``, or ``false`` if that is not set.
        :param synthesizer: Synthesis method to use while deploying this stack. The Stack Synthesizer controls aspects of synthesis and deployment, like how assets are referenced and what IAM roles to use. For more information, see the README of the main CDK package. If not specified, the ``defaultStackSynthesizer`` from ``App`` will be used. If that is not specified, ``DefaultStackSynthesizer`` is used if ``@aws-cdk/core:newStyleStackSynthesis`` is set to ``true`` or the CDK major version is v2. In CDK v1 ``LegacyStackSynthesizer`` is the default if no other synthesizer is specified. Default: - The synthesizer specified on ``App``, or ``DefaultStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e162fbee6208f9bcf71a043cd6c68f4f0b6e5247772d4d7960e188604fc4b6d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkStackProps(
            ck_account_type=ck_account_type,
            ck_application=ck_application,
            ck_company=ck_company,
            ck_prefix=ck_prefix,
            ck_removal_policy_override=ck_removal_policy_override,
            analytics_reporting=analytics_reporting,
            cross_region_references=cross_region_references,
            description=description,
            env=env,
            permissions_boundary=permissions_boundary,
            stack_name=stack_name,
            suppress_template_indentation=suppress_template_indentation,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createStackId")
    @builtins.classmethod
    def create_stack_id(
        cls,
        id: builtins.str,
        prefix: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''
        :param id: -
        :param prefix: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c76c1cd3932fecd49381b5c6415097ccaa499816f718d3cdca12fc77bd1b9a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "createStackId", [id, prefix]))

    @jsii.member(jsii_name="findStackOf")
    @builtins.classmethod
    def find_stack_of(cls, construct: _constructs_77d1e7e8.Construct) -> "CkStack":
        '''Get stack where the construct is deployed.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62100ca528134b9192d70c847e83d84b2c908790406210aa9230835bae6e824f)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast("CkStack", jsii.sinvoke(cls, "findStackOf", [construct]))

    @jsii.member(jsii_name="accountType")
    def account_type(self) -> CkAccountType:
        '''Account type where the stack is deployed.'''
        return typing.cast(CkAccountType, jsii.invoke(self, "accountType", []))

    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''Application name.'''
        return typing.cast(builtins.str, jsii.invoke(self, "applicationName", []))

    @jsii.member(jsii_name="company")
    def company(self) -> builtins.str:
        '''Company name.'''
        return typing.cast(builtins.str, jsii.invoke(self, "company", []))

    @jsii.member(jsii_name="isDevelopment")
    def is_development(self) -> builtins.bool:
        '''Find out if the stack is running in development account.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isDevelopment", []))

    @jsii.member(jsii_name="isDevelopmentLike")
    def is_development_like(self) -> builtins.bool:
        '''Find out if the stack is running in a development like environment such as dev or test.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isDevelopmentLike", []))

    @jsii.member(jsii_name="isNonProduction")
    def is_non_production(self) -> builtins.bool:
        '''Find out if the stack is running in a non production account such as dev, test, uat.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isNonProduction", []))

    @jsii.member(jsii_name="isProduction")
    def is_production(self) -> builtins.bool:
        '''Find out if the stack is running in production account.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isProduction", []))

    @jsii.member(jsii_name="isProductionLike")
    def is_production_like(self) -> builtins.bool:
        '''Find out if the stack is running in a production like environment such as uat and prod.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isProductionLike", []))

    @jsii.member(jsii_name="isTest")
    def is_test(self) -> builtins.bool:
        '''Find out if the stack is running in test account.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isTest", []))

    @jsii.member(jsii_name="isUAT")
    def is_uat(self) -> builtins.bool:
        '''Find out if the stack is running in uat account.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isUAT", []))

    @jsii.member(jsii_name="removalPolicy")
    def removal_policy(self) -> _aws_cdk_ceddda9d.RemovalPolicy:
        '''Removal policy is based on stack termination protection.'''
        return typing.cast(_aws_cdk_ceddda9d.RemovalPolicy, jsii.invoke(self, "removalPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="removalPolicyOverride")
    def removal_policy_override(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], jsii.get(self, "removalPolicyOverride"))


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkStackProps",
    jsii_struct_bases=[_aws_cdk_ceddda9d.StackProps],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "cross_region_references": "crossRegionReferences",
        "description": "description",
        "env": "env",
        "permissions_boundary": "permissionsBoundary",
        "stack_name": "stackName",
        "suppress_template_indentation": "suppressTemplateIndentation",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "ck_account_type": "ckAccountType",
        "ck_application": "ckApplication",
        "ck_company": "ckCompany",
        "ck_prefix": "ckPrefix",
        "ck_removal_policy_override": "ckRemovalPolicyOverride",
    },
)
class CkStackProps(_aws_cdk_ceddda9d.StackProps):
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        cross_region_references: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[_aws_cdk_ceddda9d.Environment, typing.Dict[builtins.str, typing.Any]]] = None,
        permissions_boundary: typing.Optional[_aws_cdk_ceddda9d.PermissionsBoundary] = None,
        stack_name: typing.Optional[builtins.str] = None,
        suppress_template_indentation: typing.Optional[builtins.bool] = None,
        synthesizer: typing.Optional[_aws_cdk_ceddda9d.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        ck_account_type: CkAccountType,
        ck_application: builtins.str,
        ck_company: builtins.str,
        ck_prefix: typing.Optional[builtins.str] = None,
        ck_removal_policy_override: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    ) -> None:
        '''CloudKitect Stack Component Properties.

        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param cross_region_references: Enable this flag to allow native cross region stack references. Enabling this will create a CloudFormation custom resource in both the producing stack and consuming stack in order to perform the export/import This feature is currently experimental Default: false
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param permissions_boundary: Options for applying a permissions boundary to all IAM Roles and Users created within this Stage. Default: - no permissions boundary is applied
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param suppress_template_indentation: Enable this flag to suppress indentation in generated CloudFormation templates. If not specified, the value of the ``@aws-cdk/core:suppressTemplateIndentation`` context key will be used. If that is not specified, then the default value ``false`` will be used. Default: - the value of ``@aws-cdk/core:suppressTemplateIndentation``, or ``false`` if that is not set.
        :param synthesizer: Synthesis method to use while deploying this stack. The Stack Synthesizer controls aspects of synthesis and deployment, like how assets are referenced and what IAM roles to use. For more information, see the README of the main CDK package. If not specified, the ``defaultStackSynthesizer`` from ``App`` will be used. If that is not specified, ``DefaultStackSynthesizer`` is used if ``@aws-cdk/core:newStyleStackSynthesis`` is set to ``true`` or the CDK major version is v2. In CDK v1 ``LegacyStackSynthesizer`` is the default if no other synthesizer is specified. Default: - The synthesizer specified on ``App``, or ``DefaultStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param ck_account_type: AccountType where the stack will be deployed.
        :param ck_application: Name of the application deployed by the stack.
        :param ck_company: Company the application is associated with.
        :param ck_prefix: Any prefix for the stack name to avoid conflicts. Default: empty
        :param ck_removal_policy_override: Flag to control the removalPolicy override for the components. Default: undefined, meaning it will use environment specific removal policy
        '''
        if isinstance(env, dict):
            env = _aws_cdk_ceddda9d.Environment(**env)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__236c4d0ef02c30c477ac69ed10a2714af3433292e8f43c9dd54f0da9009af4ea)
            check_type(argname="argument analytics_reporting", value=analytics_reporting, expected_type=type_hints["analytics_reporting"])
            check_type(argname="argument cross_region_references", value=cross_region_references, expected_type=type_hints["cross_region_references"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument suppress_template_indentation", value=suppress_template_indentation, expected_type=type_hints["suppress_template_indentation"])
            check_type(argname="argument synthesizer", value=synthesizer, expected_type=type_hints["synthesizer"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument ck_account_type", value=ck_account_type, expected_type=type_hints["ck_account_type"])
            check_type(argname="argument ck_application", value=ck_application, expected_type=type_hints["ck_application"])
            check_type(argname="argument ck_company", value=ck_company, expected_type=type_hints["ck_company"])
            check_type(argname="argument ck_prefix", value=ck_prefix, expected_type=type_hints["ck_prefix"])
            check_type(argname="argument ck_removal_policy_override", value=ck_removal_policy_override, expected_type=type_hints["ck_removal_policy_override"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ck_account_type": ck_account_type,
            "ck_application": ck_application,
            "ck_company": ck_company,
        }
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if cross_region_references is not None:
            self._values["cross_region_references"] = cross_region_references
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if suppress_template_indentation is not None:
            self._values["suppress_template_indentation"] = suppress_template_indentation
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if ck_prefix is not None:
            self._values["ck_prefix"] = ck_prefix
        if ck_removal_policy_override is not None:
            self._values["ck_removal_policy_override"] = ck_removal_policy_override

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in this Stack.

        :default:

        ``analyticsReporting`` setting of containing ``App``, or value of
        'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cross_region_references(self) -> typing.Optional[builtins.bool]:
        '''Enable this flag to allow native cross region stack references.

        Enabling this will create a CloudFormation custom resource
        in both the producing stack and consuming stack in order to perform the export/import

        This feature is currently experimental

        :default: false
        '''
        result = self._values.get("cross_region_references")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[_aws_cdk_ceddda9d.Environment]:
        '''The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        :default:

        - The environment of the containing ``Stage`` if available,
        otherwise create the stack will be environment-agnostic.

        Example::

            // Use a concrete account and region to deploy this stack to:
            // `.account` and `.region` will simply return these values.
            new Stack(app, 'Stack1', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              },
            });
            
            // Use the CLI's current credentials to determine the target environment:
            // `.account` and `.region` will reflect the account+region the CLI
            // is configured to use (based on the user CLI credentials)
            new Stack(app, 'Stack2', {
              env: {
                account: process.env.CDK_DEFAULT_ACCOUNT,
                region: process.env.CDK_DEFAULT_REGION
              },
            });
            
            // Define multiple stacks stage associated with an environment
            const myStage = new Stage(app, 'MyStage', {
              env: {
                account: '123456789012',
                region: 'us-east-1'
              }
            });
            
            // both of these stacks will use the stage's account/region:
            // `.account` and `.region` will resolve to the concrete values as above
            new MyStack(myStage, 'Stack1');
            new YourStack(myStage, 'Stack2');
            
            // Define an environment-agnostic stack:
            // `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            // which will only resolve to actual values by CloudFormation during deployment.
            new MyStack(app, 'Stack1');
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Environment], result)

    @builtins.property
    def permissions_boundary(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.PermissionsBoundary]:
        '''Options for applying a permissions boundary to all IAM Roles and Users created within this Stage.

        :default: - no permissions boundary is applied
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.PermissionsBoundary], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''Name to deploy the stack with.

        :default: - Derived from construct path.
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suppress_template_indentation(self) -> typing.Optional[builtins.bool]:
        '''Enable this flag to suppress indentation in generated CloudFormation templates.

        If not specified, the value of the ``@aws-cdk/core:suppressTemplateIndentation``
        context key will be used. If that is not specified, then the
        default value ``false`` will be used.

        :default: - the value of ``@aws-cdk/core:suppressTemplateIndentation``, or ``false`` if that is not set.
        '''
        result = self._values.get("suppress_template_indentation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def synthesizer(self) -> typing.Optional[_aws_cdk_ceddda9d.IStackSynthesizer]:
        '''Synthesis method to use while deploying this stack.

        The Stack Synthesizer controls aspects of synthesis and deployment,
        like how assets are referenced and what IAM roles to use. For more
        information, see the README of the main CDK package.

        If not specified, the ``defaultStackSynthesizer`` from ``App`` will be used.
        If that is not specified, ``DefaultStackSynthesizer`` is used if
        ``@aws-cdk/core:newStyleStackSynthesis`` is set to ``true`` or the CDK major
        version is v2. In CDK v1 ``LegacyStackSynthesizer`` is the default if no
        other synthesizer is specified.

        :default: - The synthesizer specified on ``App``, or ``DefaultStackSynthesizer`` otherwise.
        '''
        result = self._values.get("synthesizer")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.IStackSynthesizer], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Stack tags that will be applied to all the taggable resources and the stack itself.

        :default: {}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ck_account_type(self) -> CkAccountType:
        '''AccountType where the stack will be deployed.'''
        result = self._values.get("ck_account_type")
        assert result is not None, "Required property 'ck_account_type' is missing"
        return typing.cast(CkAccountType, result)

    @builtins.property
    def ck_application(self) -> builtins.str:
        '''Name of the application deployed by the stack.'''
        result = self._values.get("ck_application")
        assert result is not None, "Required property 'ck_application' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ck_company(self) -> builtins.str:
        '''Company the application is associated with.'''
        result = self._values.get("ck_company")
        assert result is not None, "Required property 'ck_company' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ck_prefix(self) -> typing.Optional[builtins.str]:
        '''Any prefix for the stack name to avoid conflicts.

        :default: empty
        '''
        result = self._values.get("ck_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ck_removal_policy_override(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''Flag to control the removalPolicy override for the components.

        :default: undefined, meaning it will use environment specific removal policy
        '''
        result = self._values.get("ck_removal_policy_override")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkTableV2(
    _aws_cdk_aws_dynamodb_ceddda9d.TableV2,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkTableV2",
):
    '''CloudKitect DynamoDB Table V2 component.



    Default Configuration

    - Encryption: Keys managed by AWS in customer account



    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Backups

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkTableV2(this, "LogicalId", {});

    Custom Configuration Example::

       new CkTableV2(this, "LogicalId", {
          encryption: TableEncryption.AWS_MANAGED
       });


    Compliance

    It addresses the following compliance requirements

    1. DynamoDB point in time recovery
       .. epigraph::

          - Risk Level: High
          - Compliance: NIST4
          - Well Architected Pillar: Reliability

    2. Encryption key in customer account
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NIST4
          - Well Architected Pillar: Security

       Compliance Check Report
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        partition_key: typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]],
        billing: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Billing] = None,
        dynamo_stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
        encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryptionV2] = None,
        global_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.GlobalSecondaryIndexPropsV2, typing.Dict[builtins.str, typing.Any]]]] = None,
        local_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.LocalSecondaryIndexProps, typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        replicas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ReplicaTableProps, typing.Dict[builtins.str, typing.Any]]]] = None,
        sort_key: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        time_to_live_attribute: typing.Optional[builtins.str] = None,
        contributor_insights: typing.Optional[builtins.bool] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param partition_key: Partition key attribute definition.
        :param billing: The billing mode and capacity settings to apply to the table. Default: Billing.onDemand()
        :param dynamo_stream: When an item in the table is modified, StreamViewType determines what information is written to the stream. Default: - streams are disabled if replicas are not configured and this property is not specified. If this property is not specified when replicas are configured, then NEW_AND_OLD_IMAGES will be the StreamViewType for all replicas
        :param encryption: The server-side encryption. Default: TableEncryptionV2.dynamoOwnedKey()
        :param global_secondary_indexes: Global secondary indexes. Note: You can provide a maximum of 20 global secondary indexes. Default: - no global secondary indexes
        :param local_secondary_indexes: Local secondary indexes. Note: You can only provide a maximum of 5 local secondary indexes. Default: - no local secondary indexes
        :param removal_policy: The removal policy applied to the table. Default: RemovalPolicy.RETAIN
        :param replicas: Replica tables to deploy with the primary table. Note: Adding replica tables allows you to use your table as a global table. You cannot specify a replica table in the region that the primary table will be deployed to. Replica tables will only be supported if the stack deployment region is defined. Default: - no replica tables
        :param sort_key: Sort key attribute definition. Default: - no sort key
        :param table_name: The name of the table. Default: - generated by CloudFormation
        :param time_to_live_attribute: The name of the TTL attribute. Default: - TTL is disabled
        :param contributor_insights: Whether CloudWatch contributor insights is enabled. Default: false
        :param deletion_protection: Whether deletion protection is enabled. Default: false
        :param kinesis_stream: Kinesis Data Stream to capture item level changes. Default: - no Kinesis Data Stream
        :param point_in_time_recovery: Whether point-in-time recovery is enabled. Default: false
        :param table_class: The table class. Default: TableClass.STANDARD
        :param tags: Tags to be applied to the table or replica table. Default: - no tags
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c0898474e7611a4b104aef33dd114139f533a833837eae1605a06bbb390834)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkTableV2Props(
            partition_key=partition_key,
            billing=billing,
            dynamo_stream=dynamo_stream,
            encryption=encryption,
            global_secondary_indexes=global_secondary_indexes,
            local_secondary_indexes=local_secondary_indexes,
            removal_policy=removal_policy,
            replicas=replicas,
            sort_key=sort_key,
            table_name=table_name,
            time_to_live_attribute=time_to_live_attribute,
            contributor_insights=contributor_insights,
            deletion_protection=deletion_protection,
            kinesis_stream=kinesis_stream,
            point_in_time_recovery=point_in_time_recovery,
            table_class=table_class,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkTableV2Props",
    jsii_struct_bases=[_aws_cdk_aws_dynamodb_ceddda9d.TablePropsV2],
    name_mapping={
        "contributor_insights": "contributorInsights",
        "deletion_protection": "deletionProtection",
        "kinesis_stream": "kinesisStream",
        "point_in_time_recovery": "pointInTimeRecovery",
        "table_class": "tableClass",
        "tags": "tags",
        "partition_key": "partitionKey",
        "billing": "billing",
        "dynamo_stream": "dynamoStream",
        "encryption": "encryption",
        "global_secondary_indexes": "globalSecondaryIndexes",
        "local_secondary_indexes": "localSecondaryIndexes",
        "removal_policy": "removalPolicy",
        "replicas": "replicas",
        "sort_key": "sortKey",
        "table_name": "tableName",
        "time_to_live_attribute": "timeToLiveAttribute",
    },
)
class CkTableV2Props(_aws_cdk_aws_dynamodb_ceddda9d.TablePropsV2):
    def __init__(
        self,
        *,
        contributor_insights: typing.Optional[builtins.bool] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        partition_key: typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]],
        billing: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Billing] = None,
        dynamo_stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
        encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryptionV2] = None,
        global_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.GlobalSecondaryIndexPropsV2, typing.Dict[builtins.str, typing.Any]]]] = None,
        local_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.LocalSecondaryIndexProps, typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        replicas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ReplicaTableProps, typing.Dict[builtins.str, typing.Any]]]] = None,
        sort_key: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        time_to_live_attribute: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CloudKitect DynamodDB Table Component Properties.

        :param contributor_insights: Whether CloudWatch contributor insights is enabled. Default: false
        :param deletion_protection: Whether deletion protection is enabled. Default: false
        :param kinesis_stream: Kinesis Data Stream to capture item level changes. Default: - no Kinesis Data Stream
        :param point_in_time_recovery: Whether point-in-time recovery is enabled. Default: false
        :param table_class: The table class. Default: TableClass.STANDARD
        :param tags: Tags to be applied to the table or replica table. Default: - no tags
        :param partition_key: Partition key attribute definition.
        :param billing: The billing mode and capacity settings to apply to the table. Default: Billing.onDemand()
        :param dynamo_stream: When an item in the table is modified, StreamViewType determines what information is written to the stream. Default: - streams are disabled if replicas are not configured and this property is not specified. If this property is not specified when replicas are configured, then NEW_AND_OLD_IMAGES will be the StreamViewType for all replicas
        :param encryption: The server-side encryption. Default: TableEncryptionV2.dynamoOwnedKey()
        :param global_secondary_indexes: Global secondary indexes. Note: You can provide a maximum of 20 global secondary indexes. Default: - no global secondary indexes
        :param local_secondary_indexes: Local secondary indexes. Note: You can only provide a maximum of 5 local secondary indexes. Default: - no local secondary indexes
        :param removal_policy: The removal policy applied to the table. Default: RemovalPolicy.RETAIN
        :param replicas: Replica tables to deploy with the primary table. Note: Adding replica tables allows you to use your table as a global table. You cannot specify a replica table in the region that the primary table will be deployed to. Replica tables will only be supported if the stack deployment region is defined. Default: - no replica tables
        :param sort_key: Sort key attribute definition. Default: - no sort key
        :param table_name: The name of the table. Default: - generated by CloudFormation
        :param time_to_live_attribute: The name of the TTL attribute. Default: - TTL is disabled
        '''
        if isinstance(partition_key, dict):
            partition_key = _aws_cdk_aws_dynamodb_ceddda9d.Attribute(**partition_key)
        if isinstance(sort_key, dict):
            sort_key = _aws_cdk_aws_dynamodb_ceddda9d.Attribute(**sort_key)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5043f2ae443400687f2b5a4a02b15888d64136f0a03d98f34138ee3503ddef3e)
            check_type(argname="argument contributor_insights", value=contributor_insights, expected_type=type_hints["contributor_insights"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument table_class", value=table_class, expected_type=type_hints["table_class"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            check_type(argname="argument billing", value=billing, expected_type=type_hints["billing"])
            check_type(argname="argument dynamo_stream", value=dynamo_stream, expected_type=type_hints["dynamo_stream"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument global_secondary_indexes", value=global_secondary_indexes, expected_type=type_hints["global_secondary_indexes"])
            check_type(argname="argument local_secondary_indexes", value=local_secondary_indexes, expected_type=type_hints["local_secondary_indexes"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
            check_type(argname="argument sort_key", value=sort_key, expected_type=type_hints["sort_key"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument time_to_live_attribute", value=time_to_live_attribute, expected_type=type_hints["time_to_live_attribute"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partition_key": partition_key,
        }
        if contributor_insights is not None:
            self._values["contributor_insights"] = contributor_insights
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if table_class is not None:
            self._values["table_class"] = table_class
        if tags is not None:
            self._values["tags"] = tags
        if billing is not None:
            self._values["billing"] = billing
        if dynamo_stream is not None:
            self._values["dynamo_stream"] = dynamo_stream
        if encryption is not None:
            self._values["encryption"] = encryption
        if global_secondary_indexes is not None:
            self._values["global_secondary_indexes"] = global_secondary_indexes
        if local_secondary_indexes is not None:
            self._values["local_secondary_indexes"] = local_secondary_indexes
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if replicas is not None:
            self._values["replicas"] = replicas
        if sort_key is not None:
            self._values["sort_key"] = sort_key
        if table_name is not None:
            self._values["table_name"] = table_name
        if time_to_live_attribute is not None:
            self._values["time_to_live_attribute"] = time_to_live_attribute

    @builtins.property
    def contributor_insights(self) -> typing.Optional[builtins.bool]:
        '''Whether CloudWatch contributor insights is enabled.

        :default: false
        '''
        result = self._values.get("contributor_insights")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether deletion protection is enabled.

        :default: false
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kinesis_stream(self) -> typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream]:
        '''Kinesis Data Stream to capture item level changes.

        :default: - no Kinesis Data Stream
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream], result)

    @builtins.property
    def point_in_time_recovery(self) -> typing.Optional[builtins.bool]:
        '''Whether point-in-time recovery is enabled.

        :default: false
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def table_class(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass]:
        '''The table class.

        :default: TableClass.STANDARD
        '''
        result = self._values.get("table_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_ceddda9d.CfnTag]]:
        '''Tags to be applied to the table or replica table.

        :default: - no tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_ceddda9d.CfnTag]], result)

    @builtins.property
    def partition_key(self) -> _aws_cdk_aws_dynamodb_ceddda9d.Attribute:
        '''Partition key attribute definition.'''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(_aws_cdk_aws_dynamodb_ceddda9d.Attribute, result)

    @builtins.property
    def billing(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Billing]:
        '''The billing mode and capacity settings to apply to the table.

        :default: Billing.onDemand()
        '''
        result = self._values.get("billing")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Billing], result)

    @builtins.property
    def dynamo_stream(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType]:
        '''When an item in the table is modified, StreamViewType determines what information is written to the stream.

        :default:

        - streams are disabled if replicas are not configured and this property is
        not specified. If this property is not specified when replicas are configured, then
        NEW_AND_OLD_IMAGES will be the StreamViewType for all replicas
        '''
        result = self._values.get("dynamo_stream")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryptionV2]:
        '''The server-side encryption.

        :default: TableEncryptionV2.dynamoOwnedKey()
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryptionV2], result)

    @builtins.property
    def global_secondary_indexes(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_dynamodb_ceddda9d.GlobalSecondaryIndexPropsV2]]:
        '''Global secondary indexes.

        Note: You can provide a maximum of 20 global secondary indexes.

        :default: - no global secondary indexes
        '''
        result = self._values.get("global_secondary_indexes")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_dynamodb_ceddda9d.GlobalSecondaryIndexPropsV2]], result)

    @builtins.property
    def local_secondary_indexes(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_dynamodb_ceddda9d.LocalSecondaryIndexProps]]:
        '''Local secondary indexes.

        Note: You can only provide a maximum of 5 local secondary indexes.

        :default: - no local secondary indexes
        '''
        result = self._values.get("local_secondary_indexes")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_dynamodb_ceddda9d.LocalSecondaryIndexProps]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''The removal policy applied to the table.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def replicas(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_dynamodb_ceddda9d.ReplicaTableProps]]:
        '''Replica tables to deploy with the primary table.

        Note: Adding replica tables allows you to use your table as a global table. You
        cannot specify a replica table in the region that the primary table will be deployed
        to. Replica tables will only be supported if the stack deployment region is defined.

        :default: - no replica tables
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_dynamodb_ceddda9d.ReplicaTableProps]], result)

    @builtins.property
    def sort_key(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Attribute]:
        '''Sort key attribute definition.

        :default: - no sort key
        '''
        result = self._values.get("sort_key")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Attribute], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''The name of the table.

        :default: - generated by CloudFormation
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_to_live_attribute(self) -> typing.Optional[builtins.str]:
        '''The name of the TTL attribute.

        :default: - TTL is disabled
        '''
        result = self._values.get("time_to_live_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkTableV2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CkTag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''Interface for tags.

        :param key: 
        :param value: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b09c2bc727ea4dfd3c617d0fa5a0ddcf2505cdffdccf9d266862e5dba45677cc)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CkUtils(metaclass=jsii.JSIIMeta, jsii_type="@cloudkitect/components.CkUtils"):
    '''Utility class, provides several reusable methods.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="domainNameToPascalCase")
    @builtins.classmethod
    def domain_name_to_pascal_case(cls, domain_name: builtins.str) -> builtins.str:
        '''Method to convert domainName to pascal case.

        :param domain_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84093b578799bb48ee71831f1f43a4dab3236aa063cc724f63bb691714b959d0)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "domainNameToPascalCase", [domain_name]))

    @jsii.member(jsii_name="toPascalCase")
    @builtins.classmethod
    def to_pascal_case(cls, str: builtins.str) -> builtins.str:
        '''
        :param str: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57ac3f2465237ce44ce0d456ca6f10fc0a814ed5ddd353673002b2300c900540)
            check_type(argname="argument str", value=str, expected_type=type_hints["str"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "toPascalCase", [str]))


class CkVendorTags(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkVendorTags",
):
    '''Class to add CloudKitect specific tags to all constructs.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="addTagsTo")
    @builtins.classmethod
    def add_tags_to(cls, scope: _constructs_77d1e7e8.Construct) -> None:
        '''
        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28aff407aa4f832c94b37aee02fdd8747d1bbfaaff6b72f8045fd78a621dc83b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(None, jsii.sinvoke(cls, "addTagsTo", [scope]))


class CkVpc(
    _aws_cdk_aws_ec2_ceddda9d.Vpc,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudkitect/components.CkVpc",
):
    '''CloudKitect Virtual Private Cloud - VPC component.



    Default Configuration

    Subnets: Public, Private, Isolated,


    Default Alarms

    Available only in Enhanced components


    Logging and Monitoring

    Available only in Enhanced components


    Examples

    Default Usage Example::

       new CkVpc(this, "LogicalId", {});

    Custom Configuration Example::

       new CkVpc(this, "LogicalId", {
          enableDnsHostnames: false
       });


    Compliance

    It addresses the following compliance requirements

    1. Highly available NAT Gateway in use
       .. epigraph::

          - Risk Level: Medium
          - Compliance: APRA, MAS, NIST4
          - Well Architected Pillar: Performance Efficiency

    2. Restrict default security groups
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NIST4
          - Well Architected Pillar: Security

    3. Create three subnets Public, Private and Isolated
       .. epigraph::

          - Risk Level: Medium
          - Compliance: NIST4
          - Well Architected Pillar: Security
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        cidr: typing.Optional[builtins.str] = None,
        create_internet_gateway: typing.Optional[builtins.bool] = None,
        default_instance_tenancy: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.DefaultInstanceTenancy] = None,
        enable_dns_hostnames: typing.Optional[builtins.bool] = None,
        enable_dns_support: typing.Optional[builtins.bool] = None,
        flow_logs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.FlowLogOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        gateway_endpoints: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpointOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        ip_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpAddresses] = None,
        ip_protocol: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IpProtocol] = None,
        ipv6_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpv6Addresses] = None,
        max_azs: typing.Optional[jsii.Number] = None,
        nat_gateway_provider: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.NatProvider] = None,
        nat_gateways: typing.Optional[jsii.Number] = None,
        nat_gateway_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        reserved_azs: typing.Optional[jsii.Number] = None,
        restrict_default_security_group: typing.Optional[builtins.bool] = None,
        subnet_configuration: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_name: typing.Optional[builtins.str] = None,
        vpn_connections: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpnConnectionOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpn_gateway: typing.Optional[builtins.bool] = None,
        vpn_gateway_asn: typing.Optional[jsii.Number] = None,
        vpn_route_propagation: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param availability_zones: Availability zones this VPC spans. Specify this option only if you do not specify ``maxAzs``. Default: - a subset of AZs of the stack
        :param cidr: (deprecated) The CIDR range to use for the VPC, e.g. '10.0.0.0/16'. Should be a minimum of /28 and maximum size of /16. The range will be split across all subnets per Availability Zone. Default: Vpc.DEFAULT_CIDR_RANGE
        :param create_internet_gateway: If set to false then disable the creation of the default internet gateway. Default: true
        :param default_instance_tenancy: The default tenancy of instances launched into the VPC. By setting this to dedicated tenancy, instances will be launched on hardware dedicated to a single AWS customer, unless specifically specified at instance launch time. Please note, not all instance types are usable with Dedicated tenancy. Default: DefaultInstanceTenancy.Default (shared) tenancy
        :param enable_dns_hostnames: Indicates whether the instances launched in the VPC get public DNS hostnames. If this attribute is true, instances in the VPC get public DNS hostnames, but only if the enableDnsSupport attribute is also set to true. Default: true
        :param enable_dns_support: Indicates whether the DNS resolution is supported for the VPC. If this attribute is false, the Amazon-provided DNS server in the VPC that resolves public DNS hostnames to IP addresses is not enabled. If this attribute is true, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC IPv4 network range plus two will succeed. Default: true
        :param flow_logs: Flow logs to add to this VPC. Default: - No flow logs.
        :param gateway_endpoints: Gateway endpoints to add to this VPC. Default: - None.
        :param ip_addresses: The Provider to use to allocate IPv4 Space to your VPC. Options include static allocation or from a pool. Note this is specific to IPv4 addresses. Default: ec2.IpAddresses.cidr
        :param ip_protocol: The protocol of the vpc. Options are IPv4 only or dual stack. Default: IpProtocol.IPV4_ONLY
        :param ipv6_addresses: The Provider to use to allocate IPv6 Space to your VPC. Options include amazon provided CIDR block. Note this is specific to IPv6 addresses. Default: Ipv6Addresses.amazonProvided
        :param max_azs: Define the maximum number of AZs to use in this region. If the region has more AZs than you want to use (for example, because of EIP limits), pick a lower number here. The AZs will be sorted and picked from the start of the list. If you pick a higher number than the number of AZs in the region, all AZs in the region will be selected. To use "all AZs" available to your account, use a high number (such as 99). Be aware that environment-agnostic stacks will be created with access to only 2 AZs, so to use more than 2 AZs, be sure to specify the account and region on your stack. Specify this option only if you do not specify ``availabilityZones``. Default: 3
        :param nat_gateway_provider: What type of NAT provider to use. Select between NAT gateways or NAT instances. NAT gateways may not be available in all AWS regions. Default: NatProvider.gateway()
        :param nat_gateways: The number of NAT Gateways/Instances to create. The type of NAT gateway or instance will be determined by the ``natGatewayProvider`` parameter. You can set this number lower than the number of Availability Zones in your VPC in order to save on NAT cost. Be aware you may be charged for cross-AZ data traffic instead. Default: - One NAT gateway/instance per Availability Zone
        :param nat_gateway_subnets: Configures the subnets which will have NAT Gateways/Instances. You can pick a specific group of subnets by specifying the group name; the picked subnets must be public subnets. Only necessary if you have more than one public subnet group. Default: - All public subnets.
        :param reserved_azs: Define the number of AZs to reserve. When specified, the IP space is reserved for the azs but no actual resources are provisioned. Default: 0
        :param restrict_default_security_group: If set to true then the default inbound & outbound rules will be removed from the default security group. Default: true if '@aws-cdk/aws-ec2:restrictDefaultSecurityGroup' is enabled, false otherwise
        :param subnet_configuration: Configure the subnets to build for each AZ. Each entry in this list configures a Subnet Group; each group will contain a subnet for each Availability Zone. For example, if you want 1 public subnet, 1 private subnet, and 1 isolated subnet in each AZ provide the following:: new ec2.Vpc(this, 'VPC', { subnetConfiguration: [ { cidrMask: 24, name: 'ingress', subnetType: ec2.SubnetType.PUBLIC, }, { cidrMask: 24, name: 'application', subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS, }, { cidrMask: 28, name: 'rds', subnetType: ec2.SubnetType.PRIVATE_ISOLATED, } ] }); Default: - The VPC CIDR will be evenly divided between 1 public and 1 private subnet per AZ.
        :param vpc_name: The VPC name. Since the VPC resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: this.node.path
        :param vpn_connections: VPN connections to this VPC. Default: - No connections.
        :param vpn_gateway: Indicates whether a VPN gateway should be created and attached to this VPC. Default: - true when vpnGatewayAsn or vpnConnections is specified
        :param vpn_gateway_asn: The private Autonomous System Number (ASN) for the VPN gateway. Default: - Amazon default ASN.
        :param vpn_route_propagation: Where to propagate VPN routes. Default: - On the route tables associated with private subnets. If no private subnets exists, isolated subnets are used. If no isolated subnets exists, public subnets are used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8917f02502111a92ac6c1fea86ccd0172fe2e2e0736bf4ac4196a594066ed9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CkVpcProps(
            availability_zones=availability_zones,
            cidr=cidr,
            create_internet_gateway=create_internet_gateway,
            default_instance_tenancy=default_instance_tenancy,
            enable_dns_hostnames=enable_dns_hostnames,
            enable_dns_support=enable_dns_support,
            flow_logs=flow_logs,
            gateway_endpoints=gateway_endpoints,
            ip_addresses=ip_addresses,
            ip_protocol=ip_protocol,
            ipv6_addresses=ipv6_addresses,
            max_azs=max_azs,
            nat_gateway_provider=nat_gateway_provider,
            nat_gateways=nat_gateways,
            nat_gateway_subnets=nat_gateway_subnets,
            reserved_azs=reserved_azs,
            restrict_default_security_group=restrict_default_security_group,
            subnet_configuration=subnet_configuration,
            vpc_name=vpc_name,
            vpn_connections=vpn_connections,
            vpn_gateway=vpn_gateway,
            vpn_gateway_asn=vpn_gateway_asn,
            vpn_route_propagation=vpn_route_propagation,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cloudkitect/components.CkVpcProps",
    jsii_struct_bases=[_aws_cdk_aws_ec2_ceddda9d.VpcProps],
    name_mapping={
        "availability_zones": "availabilityZones",
        "cidr": "cidr",
        "create_internet_gateway": "createInternetGateway",
        "default_instance_tenancy": "defaultInstanceTenancy",
        "enable_dns_hostnames": "enableDnsHostnames",
        "enable_dns_support": "enableDnsSupport",
        "flow_logs": "flowLogs",
        "gateway_endpoints": "gatewayEndpoints",
        "ip_addresses": "ipAddresses",
        "ip_protocol": "ipProtocol",
        "ipv6_addresses": "ipv6Addresses",
        "max_azs": "maxAzs",
        "nat_gateway_provider": "natGatewayProvider",
        "nat_gateways": "natGateways",
        "nat_gateway_subnets": "natGatewaySubnets",
        "reserved_azs": "reservedAzs",
        "restrict_default_security_group": "restrictDefaultSecurityGroup",
        "subnet_configuration": "subnetConfiguration",
        "vpc_name": "vpcName",
        "vpn_connections": "vpnConnections",
        "vpn_gateway": "vpnGateway",
        "vpn_gateway_asn": "vpnGatewayAsn",
        "vpn_route_propagation": "vpnRoutePropagation",
    },
)
class CkVpcProps(_aws_cdk_aws_ec2_ceddda9d.VpcProps):
    def __init__(
        self,
        *,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        cidr: typing.Optional[builtins.str] = None,
        create_internet_gateway: typing.Optional[builtins.bool] = None,
        default_instance_tenancy: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.DefaultInstanceTenancy] = None,
        enable_dns_hostnames: typing.Optional[builtins.bool] = None,
        enable_dns_support: typing.Optional[builtins.bool] = None,
        flow_logs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.FlowLogOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        gateway_endpoints: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpointOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        ip_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpAddresses] = None,
        ip_protocol: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IpProtocol] = None,
        ipv6_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpv6Addresses] = None,
        max_azs: typing.Optional[jsii.Number] = None,
        nat_gateway_provider: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.NatProvider] = None,
        nat_gateways: typing.Optional[jsii.Number] = None,
        nat_gateway_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        reserved_azs: typing.Optional[jsii.Number] = None,
        restrict_default_security_group: typing.Optional[builtins.bool] = None,
        subnet_configuration: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_name: typing.Optional[builtins.str] = None,
        vpn_connections: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpnConnectionOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpn_gateway: typing.Optional[builtins.bool] = None,
        vpn_gateway_asn: typing.Optional[jsii.Number] = None,
        vpn_route_propagation: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''CloudKitect VPC Component properties.

        :param availability_zones: Availability zones this VPC spans. Specify this option only if you do not specify ``maxAzs``. Default: - a subset of AZs of the stack
        :param cidr: (deprecated) The CIDR range to use for the VPC, e.g. '10.0.0.0/16'. Should be a minimum of /28 and maximum size of /16. The range will be split across all subnets per Availability Zone. Default: Vpc.DEFAULT_CIDR_RANGE
        :param create_internet_gateway: If set to false then disable the creation of the default internet gateway. Default: true
        :param default_instance_tenancy: The default tenancy of instances launched into the VPC. By setting this to dedicated tenancy, instances will be launched on hardware dedicated to a single AWS customer, unless specifically specified at instance launch time. Please note, not all instance types are usable with Dedicated tenancy. Default: DefaultInstanceTenancy.Default (shared) tenancy
        :param enable_dns_hostnames: Indicates whether the instances launched in the VPC get public DNS hostnames. If this attribute is true, instances in the VPC get public DNS hostnames, but only if the enableDnsSupport attribute is also set to true. Default: true
        :param enable_dns_support: Indicates whether the DNS resolution is supported for the VPC. If this attribute is false, the Amazon-provided DNS server in the VPC that resolves public DNS hostnames to IP addresses is not enabled. If this attribute is true, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC IPv4 network range plus two will succeed. Default: true
        :param flow_logs: Flow logs to add to this VPC. Default: - No flow logs.
        :param gateway_endpoints: Gateway endpoints to add to this VPC. Default: - None.
        :param ip_addresses: The Provider to use to allocate IPv4 Space to your VPC. Options include static allocation or from a pool. Note this is specific to IPv4 addresses. Default: ec2.IpAddresses.cidr
        :param ip_protocol: The protocol of the vpc. Options are IPv4 only or dual stack. Default: IpProtocol.IPV4_ONLY
        :param ipv6_addresses: The Provider to use to allocate IPv6 Space to your VPC. Options include amazon provided CIDR block. Note this is specific to IPv6 addresses. Default: Ipv6Addresses.amazonProvided
        :param max_azs: Define the maximum number of AZs to use in this region. If the region has more AZs than you want to use (for example, because of EIP limits), pick a lower number here. The AZs will be sorted and picked from the start of the list. If you pick a higher number than the number of AZs in the region, all AZs in the region will be selected. To use "all AZs" available to your account, use a high number (such as 99). Be aware that environment-agnostic stacks will be created with access to only 2 AZs, so to use more than 2 AZs, be sure to specify the account and region on your stack. Specify this option only if you do not specify ``availabilityZones``. Default: 3
        :param nat_gateway_provider: What type of NAT provider to use. Select between NAT gateways or NAT instances. NAT gateways may not be available in all AWS regions. Default: NatProvider.gateway()
        :param nat_gateways: The number of NAT Gateways/Instances to create. The type of NAT gateway or instance will be determined by the ``natGatewayProvider`` parameter. You can set this number lower than the number of Availability Zones in your VPC in order to save on NAT cost. Be aware you may be charged for cross-AZ data traffic instead. Default: - One NAT gateway/instance per Availability Zone
        :param nat_gateway_subnets: Configures the subnets which will have NAT Gateways/Instances. You can pick a specific group of subnets by specifying the group name; the picked subnets must be public subnets. Only necessary if you have more than one public subnet group. Default: - All public subnets.
        :param reserved_azs: Define the number of AZs to reserve. When specified, the IP space is reserved for the azs but no actual resources are provisioned. Default: 0
        :param restrict_default_security_group: If set to true then the default inbound & outbound rules will be removed from the default security group. Default: true if '@aws-cdk/aws-ec2:restrictDefaultSecurityGroup' is enabled, false otherwise
        :param subnet_configuration: Configure the subnets to build for each AZ. Each entry in this list configures a Subnet Group; each group will contain a subnet for each Availability Zone. For example, if you want 1 public subnet, 1 private subnet, and 1 isolated subnet in each AZ provide the following:: new ec2.Vpc(this, 'VPC', { subnetConfiguration: [ { cidrMask: 24, name: 'ingress', subnetType: ec2.SubnetType.PUBLIC, }, { cidrMask: 24, name: 'application', subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS, }, { cidrMask: 28, name: 'rds', subnetType: ec2.SubnetType.PRIVATE_ISOLATED, } ] }); Default: - The VPC CIDR will be evenly divided between 1 public and 1 private subnet per AZ.
        :param vpc_name: The VPC name. Since the VPC resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: this.node.path
        :param vpn_connections: VPN connections to this VPC. Default: - No connections.
        :param vpn_gateway: Indicates whether a VPN gateway should be created and attached to this VPC. Default: - true when vpnGatewayAsn or vpnConnections is specified
        :param vpn_gateway_asn: The private Autonomous System Number (ASN) for the VPN gateway. Default: - Amazon default ASN.
        :param vpn_route_propagation: Where to propagate VPN routes. Default: - On the route tables associated with private subnets. If no private subnets exists, isolated subnets are used. If no isolated subnets exists, public subnets are used.
        '''
        if isinstance(nat_gateway_subnets, dict):
            nat_gateway_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**nat_gateway_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b239cfe19fc4361b32a03657932c7f146026a16008cce0e8871db5aab5731547)
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument create_internet_gateway", value=create_internet_gateway, expected_type=type_hints["create_internet_gateway"])
            check_type(argname="argument default_instance_tenancy", value=default_instance_tenancy, expected_type=type_hints["default_instance_tenancy"])
            check_type(argname="argument enable_dns_hostnames", value=enable_dns_hostnames, expected_type=type_hints["enable_dns_hostnames"])
            check_type(argname="argument enable_dns_support", value=enable_dns_support, expected_type=type_hints["enable_dns_support"])
            check_type(argname="argument flow_logs", value=flow_logs, expected_type=type_hints["flow_logs"])
            check_type(argname="argument gateway_endpoints", value=gateway_endpoints, expected_type=type_hints["gateway_endpoints"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
            check_type(argname="argument ip_protocol", value=ip_protocol, expected_type=type_hints["ip_protocol"])
            check_type(argname="argument ipv6_addresses", value=ipv6_addresses, expected_type=type_hints["ipv6_addresses"])
            check_type(argname="argument max_azs", value=max_azs, expected_type=type_hints["max_azs"])
            check_type(argname="argument nat_gateway_provider", value=nat_gateway_provider, expected_type=type_hints["nat_gateway_provider"])
            check_type(argname="argument nat_gateways", value=nat_gateways, expected_type=type_hints["nat_gateways"])
            check_type(argname="argument nat_gateway_subnets", value=nat_gateway_subnets, expected_type=type_hints["nat_gateway_subnets"])
            check_type(argname="argument reserved_azs", value=reserved_azs, expected_type=type_hints["reserved_azs"])
            check_type(argname="argument restrict_default_security_group", value=restrict_default_security_group, expected_type=type_hints["restrict_default_security_group"])
            check_type(argname="argument subnet_configuration", value=subnet_configuration, expected_type=type_hints["subnet_configuration"])
            check_type(argname="argument vpc_name", value=vpc_name, expected_type=type_hints["vpc_name"])
            check_type(argname="argument vpn_connections", value=vpn_connections, expected_type=type_hints["vpn_connections"])
            check_type(argname="argument vpn_gateway", value=vpn_gateway, expected_type=type_hints["vpn_gateway"])
            check_type(argname="argument vpn_gateway_asn", value=vpn_gateway_asn, expected_type=type_hints["vpn_gateway_asn"])
            check_type(argname="argument vpn_route_propagation", value=vpn_route_propagation, expected_type=type_hints["vpn_route_propagation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if cidr is not None:
            self._values["cidr"] = cidr
        if create_internet_gateway is not None:
            self._values["create_internet_gateway"] = create_internet_gateway
        if default_instance_tenancy is not None:
            self._values["default_instance_tenancy"] = default_instance_tenancy
        if enable_dns_hostnames is not None:
            self._values["enable_dns_hostnames"] = enable_dns_hostnames
        if enable_dns_support is not None:
            self._values["enable_dns_support"] = enable_dns_support
        if flow_logs is not None:
            self._values["flow_logs"] = flow_logs
        if gateway_endpoints is not None:
            self._values["gateway_endpoints"] = gateway_endpoints
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses
        if ip_protocol is not None:
            self._values["ip_protocol"] = ip_protocol
        if ipv6_addresses is not None:
            self._values["ipv6_addresses"] = ipv6_addresses
        if max_azs is not None:
            self._values["max_azs"] = max_azs
        if nat_gateway_provider is not None:
            self._values["nat_gateway_provider"] = nat_gateway_provider
        if nat_gateways is not None:
            self._values["nat_gateways"] = nat_gateways
        if nat_gateway_subnets is not None:
            self._values["nat_gateway_subnets"] = nat_gateway_subnets
        if reserved_azs is not None:
            self._values["reserved_azs"] = reserved_azs
        if restrict_default_security_group is not None:
            self._values["restrict_default_security_group"] = restrict_default_security_group
        if subnet_configuration is not None:
            self._values["subnet_configuration"] = subnet_configuration
        if vpc_name is not None:
            self._values["vpc_name"] = vpc_name
        if vpn_connections is not None:
            self._values["vpn_connections"] = vpn_connections
        if vpn_gateway is not None:
            self._values["vpn_gateway"] = vpn_gateway
        if vpn_gateway_asn is not None:
            self._values["vpn_gateway_asn"] = vpn_gateway_asn
        if vpn_route_propagation is not None:
            self._values["vpn_route_propagation"] = vpn_route_propagation

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Availability zones this VPC spans.

        Specify this option only if you do not specify ``maxAzs``.

        :default: - a subset of AZs of the stack
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cidr(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The CIDR range to use for the VPC, e.g. '10.0.0.0/16'.

        Should be a minimum of /28 and maximum size of /16. The range will be
        split across all subnets per Availability Zone.

        :default: Vpc.DEFAULT_CIDR_RANGE

        :deprecated: Use ipAddresses instead

        :stability: deprecated
        '''
        result = self._values.get("cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_internet_gateway(self) -> typing.Optional[builtins.bool]:
        '''If set to false then disable the creation of the default internet gateway.

        :default: true
        '''
        result = self._values.get("create_internet_gateway")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_instance_tenancy(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.DefaultInstanceTenancy]:
        '''The default tenancy of instances launched into the VPC.

        By setting this to dedicated tenancy, instances will be launched on
        hardware dedicated to a single AWS customer, unless specifically specified
        at instance launch time. Please note, not all instance types are usable
        with Dedicated tenancy.

        :default: DefaultInstanceTenancy.Default (shared) tenancy
        '''
        result = self._values.get("default_instance_tenancy")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.DefaultInstanceTenancy], result)

    @builtins.property
    def enable_dns_hostnames(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the instances launched in the VPC get public DNS hostnames.

        If this attribute is true, instances in the VPC get public DNS hostnames,
        but only if the enableDnsSupport attribute is also set to true.

        :default: true
        '''
        result = self._values.get("enable_dns_hostnames")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_dns_support(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the DNS resolution is supported for the VPC.

        If this attribute is false, the Amazon-provided DNS server in the VPC that
        resolves public DNS hostnames to IP addresses is not enabled. If this
        attribute is true, queries to the Amazon provided DNS server at the
        169.254.169.253 IP address, or the reserved IP address at the base of the
        VPC IPv4 network range plus two will succeed.

        :default: true
        '''
        result = self._values.get("enable_dns_support")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def flow_logs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_ec2_ceddda9d.FlowLogOptions]]:
        '''Flow logs to add to this VPC.

        :default: - No flow logs.
        '''
        result = self._values.get("flow_logs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_ec2_ceddda9d.FlowLogOptions]], result)

    @builtins.property
    def gateway_endpoints(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpointOptions]]:
        '''Gateway endpoints to add to this VPC.

        :default: - None.
        '''
        result = self._values.get("gateway_endpoints")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpointOptions]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpAddresses]:
        '''The Provider to use to allocate IPv4 Space to your VPC.

        Options include static allocation or from a pool.

        Note this is specific to IPv4 addresses.

        :default: ec2.IpAddresses.cidr
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpAddresses], result)

    @builtins.property
    def ip_protocol(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IpProtocol]:
        '''The protocol of the vpc.

        Options are IPv4 only or dual stack.

        :default: IpProtocol.IPV4_ONLY
        '''
        result = self._values.get("ip_protocol")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IpProtocol], result)

    @builtins.property
    def ipv6_addresses(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpv6Addresses]:
        '''The Provider to use to allocate IPv6 Space to your VPC.

        Options include amazon provided CIDR block.

        Note this is specific to IPv6 addresses.

        :default: Ipv6Addresses.amazonProvided
        '''
        result = self._values.get("ipv6_addresses")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpv6Addresses], result)

    @builtins.property
    def max_azs(self) -> typing.Optional[jsii.Number]:
        '''Define the maximum number of AZs to use in this region.

        If the region has more AZs than you want to use (for example, because of
        EIP limits), pick a lower number here. The AZs will be sorted and picked
        from the start of the list.

        If you pick a higher number than the number of AZs in the region, all AZs
        in the region will be selected. To use "all AZs" available to your
        account, use a high number (such as 99).

        Be aware that environment-agnostic stacks will be created with access to
        only 2 AZs, so to use more than 2 AZs, be sure to specify the account and
        region on your stack.

        Specify this option only if you do not specify ``availabilityZones``.

        :default: 3
        '''
        result = self._values.get("max_azs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nat_gateway_provider(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.NatProvider]:
        '''What type of NAT provider to use.

        Select between NAT gateways or NAT instances. NAT gateways
        may not be available in all AWS regions.

        :default: NatProvider.gateway()
        '''
        result = self._values.get("nat_gateway_provider")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.NatProvider], result)

    @builtins.property
    def nat_gateways(self) -> typing.Optional[jsii.Number]:
        '''The number of NAT Gateways/Instances to create.

        The type of NAT gateway or instance will be determined by the
        ``natGatewayProvider`` parameter.

        You can set this number lower than the number of Availability Zones in your
        VPC in order to save on NAT cost. Be aware you may be charged for
        cross-AZ data traffic instead.

        :default: - One NAT gateway/instance per Availability Zone
        '''
        result = self._values.get("nat_gateways")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nat_gateway_subnets(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''Configures the subnets which will have NAT Gateways/Instances.

        You can pick a specific group of subnets by specifying the group name;
        the picked subnets must be public subnets.

        Only necessary if you have more than one public subnet group.

        :default: - All public subnets.
        '''
        result = self._values.get("nat_gateway_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def reserved_azs(self) -> typing.Optional[jsii.Number]:
        '''Define the number of AZs to reserve.

        When specified, the IP space is reserved for the azs but no actual
        resources are provisioned.

        :default: 0
        '''
        result = self._values.get("reserved_azs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def restrict_default_security_group(self) -> typing.Optional[builtins.bool]:
        '''If set to true then the default inbound & outbound rules will be removed from the default security group.

        :default: true if '@aws-cdk/aws-ec2:restrictDefaultSecurityGroup' is enabled, false otherwise
        '''
        result = self._values.get("restrict_default_security_group")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_configuration(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.SubnetConfiguration]]:
        '''Configure the subnets to build for each AZ.

        Each entry in this list configures a Subnet Group; each group will contain a
        subnet for each Availability Zone.

        For example, if you want 1 public subnet, 1 private subnet, and 1 isolated
        subnet in each AZ provide the following::

           new ec2.Vpc(this, 'VPC', {
             subnetConfiguration: [
                {
                  cidrMask: 24,
                  name: 'ingress',
                  subnetType: ec2.SubnetType.PUBLIC,
                },
                {
                  cidrMask: 24,
                  name: 'application',
                  subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
                },
                {
                  cidrMask: 28,
                  name: 'rds',
                  subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
                }
             ]
           });

        :default:

        - The VPC CIDR will be evenly divided between 1 public and 1
        private subnet per AZ.
        '''
        result = self._values.get("subnet_configuration")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.SubnetConfiguration]], result)

    @builtins.property
    def vpc_name(self) -> typing.Optional[builtins.str]:
        '''The VPC name.

        Since the VPC resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag

        :default: this.node.path
        '''
        result = self._values.get("vpc_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_connections(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_ec2_ceddda9d.VpnConnectionOptions]]:
        '''VPN connections to this VPC.

        :default: - No connections.
        '''
        result = self._values.get("vpn_connections")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _aws_cdk_aws_ec2_ceddda9d.VpnConnectionOptions]], result)

    @builtins.property
    def vpn_gateway(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a VPN gateway should be created and attached to this VPC.

        :default: - true when vpnGatewayAsn or vpnConnections is specified
        '''
        result = self._values.get("vpn_gateway")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpn_gateway_asn(self) -> typing.Optional[jsii.Number]:
        '''The private Autonomous System Number (ASN) for the VPN gateway.

        :default: - Amazon default ASN.
        '''
        result = self._values.get("vpn_gateway_asn")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vpn_route_propagation(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]]:
        '''Where to propagate VPN routes.

        :default:

        - On the route tables associated with private subnets. If no
        private subnets exists, isolated subnets are used. If no isolated subnets
        exists, public subnets are used.
        '''
        result = self._values.get("vpn_route_propagation")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CkVpcProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CkAccountType",
    "CkBucket",
    "CkBucketProps",
    "CkCluster",
    "CkClusterProps",
    "CkDistribution",
    "CkDistributionProps",
    "CkDnsValidatedCertificate",
    "CkDnsValidatedCertificateProps",
    "CkFargateCluster",
    "CkFargateClusterProps",
    "CkFargateService",
    "CkFargateServiceProps",
    "CkFargateTaskDefinition",
    "CkFargateTaskDefinitionProps",
    "CkPublicApplicationLoadBalancerProps",
    "CkPublicApplicationLoadbalancer",
    "CkRegion",
    "CkRegionUtil",
    "CkRepository",
    "CkRepositoryProps",
    "CkStack",
    "CkStackProps",
    "CkTableV2",
    "CkTableV2Props",
    "CkTag",
    "CkUtils",
    "CkVendorTags",
    "CkVpc",
    "CkVpcProps",
]

publication.publish()

def _typecheckingstub__305950b3a114851fa68ea7e16c0814b62283c5e5d995e7d52f848f00a1490c2a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_control: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketAccessControl] = None,
    auto_delete_objects: typing.Optional[builtins.bool] = None,
    block_public_access: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BlockPublicAccess] = None,
    bucket_key_enabled: typing.Optional[builtins.bool] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    cors: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.CorsRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketEncryption] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    enforce_ssl: typing.Optional[builtins.bool] = None,
    event_bridge_enabled: typing.Optional[builtins.bool] = None,
    intelligent_tiering_configurations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.IntelligentTieringConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
    inventories: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.Inventory, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    metrics: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketMetrics, typing.Dict[builtins.str, typing.Any]]]] = None,
    minimum_tls_version: typing.Optional[jsii.Number] = None,
    notifications_handler_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    object_lock_default_retention: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectLockRetention] = None,
    object_lock_enabled: typing.Optional[builtins.bool] = None,
    object_ownership: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectOwnership] = None,
    public_read_access: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    server_access_logs_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    server_access_logs_prefix: typing.Optional[builtins.str] = None,
    target_object_key_format: typing.Optional[_aws_cdk_aws_s3_ceddda9d.TargetObjectKeyFormat] = None,
    transfer_acceleration: typing.Optional[builtins.bool] = None,
    versioned: typing.Optional[builtins.bool] = None,
    website_error_document: typing.Optional[builtins.str] = None,
    website_index_document: typing.Optional[builtins.str] = None,
    website_redirect: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.RedirectTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    website_routing_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.RoutingRule, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac0ad6ea5dc0bc9f7228cd62f328eac77acd69d77ada3adaf155c2be557a785c(
    *,
    access_control: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketAccessControl] = None,
    auto_delete_objects: typing.Optional[builtins.bool] = None,
    block_public_access: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BlockPublicAccess] = None,
    bucket_key_enabled: typing.Optional[builtins.bool] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    cors: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.CorsRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption: typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketEncryption] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    enforce_ssl: typing.Optional[builtins.bool] = None,
    event_bridge_enabled: typing.Optional[builtins.bool] = None,
    intelligent_tiering_configurations: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.IntelligentTieringConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
    inventories: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.Inventory, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    metrics: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketMetrics, typing.Dict[builtins.str, typing.Any]]]] = None,
    minimum_tls_version: typing.Optional[jsii.Number] = None,
    notifications_handler_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    object_lock_default_retention: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectLockRetention] = None,
    object_lock_enabled: typing.Optional[builtins.bool] = None,
    object_ownership: typing.Optional[_aws_cdk_aws_s3_ceddda9d.ObjectOwnership] = None,
    public_read_access: typing.Optional[builtins.bool] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    server_access_logs_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    server_access_logs_prefix: typing.Optional[builtins.str] = None,
    target_object_key_format: typing.Optional[_aws_cdk_aws_s3_ceddda9d.TargetObjectKeyFormat] = None,
    transfer_acceleration: typing.Optional[builtins.bool] = None,
    versioned: typing.Optional[builtins.bool] = None,
    website_error_document: typing.Optional[builtins.str] = None,
    website_index_document: typing.Optional[builtins.str] = None,
    website_redirect: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.RedirectTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    website_routing_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.RoutingRule, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c1b1000bca3bfc90f4a2f2f762c754fc5f4a24071b976a5caa8e08af4d81d8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    container_insights: typing.Optional[builtins.bool] = None,
    default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
    execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0fd78b1b4eb803922b57b83831556117fa86638eb7175748b9da4a2690fc318(
    *,
    capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    container_insights: typing.Optional[builtins.bool] = None,
    default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
    execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ac339f76bd4d2ce81454703e11e442363cdd4fd95a6c2a1b2732f6bf44cf3b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_behavior: typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]],
    additional_behaviors: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    publish_additional_metrics: typing.Optional[builtins.bool] = None,
    ssl_support_method: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SSLMethod] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57704f62d36a0c5e8e2b6683208dba882021cdfddabbe489cab9a442e6076ec(
    *,
    default_behavior: typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]],
    additional_behaviors: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.BehaviorOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    certificate: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate] = None,
    comment: typing.Optional[builtins.str] = None,
    default_root_object: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_logging: typing.Optional[builtins.bool] = None,
    error_responses: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_cloudfront_ceddda9d.ErrorResponse, typing.Dict[builtins.str, typing.Any]]]] = None,
    geo_restriction: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.GeoRestriction] = None,
    http_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.HttpVersion] = None,
    log_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    log_file_prefix: typing.Optional[builtins.str] = None,
    log_includes_cookies: typing.Optional[builtins.bool] = None,
    minimum_protocol_version: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SecurityPolicyProtocol] = None,
    price_class: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.PriceClass] = None,
    publish_additional_metrics: typing.Optional[builtins.bool] = None,
    ssl_support_method: typing.Optional[_aws_cdk_aws_cloudfront_ceddda9d.SSLMethod] = None,
    web_acl_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e74f7843180c4ab8b56ce954ce39086d980f97493103f4d7f89a79fde269b42(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ck_hosted_zone: _aws_cdk_aws_route53_ceddda9d.IHostedZone,
    domain_name: builtins.str,
    certificate_name: typing.Optional[builtins.str] = None,
    key_algorithm: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    transparency_logging_enabled: typing.Optional[builtins.bool] = None,
    validation: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateValidation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dcfc5fe917e31c299483725456c97c8f26932742e88c675e0223b87c5a61a6f(
    *,
    domain_name: builtins.str,
    certificate_name: typing.Optional[builtins.str] = None,
    key_algorithm: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    transparency_logging_enabled: typing.Optional[builtins.bool] = None,
    validation: typing.Optional[_aws_cdk_aws_certificatemanager_ceddda9d.CertificateValidation] = None,
    ck_hosted_zone: _aws_cdk_aws_route53_ceddda9d.IHostedZone,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff4e09e2212846a88aef20544f866acc4f948a06534e4af9f9249ff380eb350(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    container_insights: typing.Optional[builtins.bool] = None,
    default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
    execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb6ff015b18506d60c0f6a9fd254596ec2ea75948af9d88831a604babc5a441(
    *,
    capacity: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.AddCapacityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    container_insights: typing.Optional[builtins.bool] = None,
    default_cloud_map_namespace: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapNamespaceOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_fargate_capacity_providers: typing.Optional[builtins.bool] = None,
    execute_command_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ExecuteCommandConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e12b1694d522e22e1ee4af1e81d5ce1981bdbafbc6b90c2e774f06adf08440(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    task_definition: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
    assign_public_ip: typing.Optional[builtins.bool] = None,
    platform_version: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.FargatePlatformVersion] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]] = None,
    circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_map_options: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_alarms: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_controller: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentController, typing.Dict[builtins.str, typing.Any]]] = None,
    desired_count: typing.Optional[jsii.Number] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    max_healthy_percent: typing.Optional[jsii.Number] = None,
    min_healthy_percent: typing.Optional[jsii.Number] = None,
    propagate_tags: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.PropagatedTagSource] = None,
    service_connect_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps, typing.Dict[builtins.str, typing.Any]]] = None,
    service_name: typing.Optional[builtins.str] = None,
    task_definition_revision: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.TaskDefinitionRevision] = None,
    volume_configurations: typing.Optional[typing.Sequence[_aws_cdk_aws_ecs_ceddda9d.ServiceManagedVolume]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce46173ac88c02abf267864dbd28c447cb4709c7710be240a43dd34036e313b(
    *,
    cluster: _aws_cdk_aws_ecs_ceddda9d.ICluster,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]] = None,
    circuit_breaker: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_map_options: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.CloudMapOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_alarms: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentAlarmConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_controller: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.DeploymentController, typing.Dict[builtins.str, typing.Any]]] = None,
    desired_count: typing.Optional[jsii.Number] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    health_check_grace_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    max_healthy_percent: typing.Optional[jsii.Number] = None,
    min_healthy_percent: typing.Optional[jsii.Number] = None,
    propagate_tags: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.PropagatedTagSource] = None,
    service_connect_configuration: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.ServiceConnectProps, typing.Dict[builtins.str, typing.Any]]] = None,
    service_name: typing.Optional[builtins.str] = None,
    task_definition_revision: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.TaskDefinitionRevision] = None,
    volume_configurations: typing.Optional[typing.Sequence[_aws_cdk_aws_ecs_ceddda9d.ServiceManagedVolume]] = None,
    task_definition: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
    assign_public_ip: typing.Optional[builtins.bool] = None,
    platform_version: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.FargatePlatformVersion] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd42aad99202dee86e6119525894709c82f4f5f00011f17d4c156bee4052b04e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cpu: typing.Optional[jsii.Number] = None,
    ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
    memory_limit_mib: typing.Optional[jsii.Number] = None,
    runtime_platform: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.RuntimePlatform, typing.Dict[builtins.str, typing.Any]]] = None,
    execution_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    family: typing.Optional[builtins.str] = None,
    proxy_configuration: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ProxyConfiguration] = None,
    task_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.Volume, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__361f07a5bc0b8cd028d29946211aa877c11ec722d36e62ea253c80e86dbe3f74(
    *,
    execution_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    family: typing.Optional[builtins.str] = None,
    proxy_configuration: typing.Optional[_aws_cdk_aws_ecs_ceddda9d.ProxyConfiguration] = None,
    task_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ecs_ceddda9d.Volume, typing.Dict[builtins.str, typing.Any]]]] = None,
    cpu: typing.Optional[jsii.Number] = None,
    ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
    memory_limit_mib: typing.Optional[jsii.Number] = None,
    runtime_platform: typing.Optional[typing.Union[_aws_cdk_aws_ecs_ceddda9d.RuntimePlatform, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e087734a19fa17ee4c5f05e24a59d0eed8a597cbbcb90e7afb1a1a3ffd841de(
    *,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    cross_zone_enabled: typing.Optional[builtins.bool] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    deny_all_igw_traffic: typing.Optional[builtins.bool] = None,
    internet_facing: typing.Optional[builtins.bool] = None,
    load_balancer_name: typing.Optional[builtins.str] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    client_keep_alive: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    desync_mitigation_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.DesyncMitigationMode] = None,
    drop_invalid_header_fields: typing.Optional[builtins.bool] = None,
    http2_enabled: typing.Optional[builtins.bool] = None,
    idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ip_address_type: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.IpAddressType] = None,
    preserve_host_header: typing.Optional[builtins.bool] = None,
    preserve_xff_client_port: typing.Optional[builtins.bool] = None,
    security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
    waf_fail_open: typing.Optional[builtins.bool] = None,
    x_amzn_tls_version_and_cipher_suite_headers: typing.Optional[builtins.bool] = None,
    xff_header_processing_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.XffHeaderProcessingMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca0d9947670f030b033e47f0f38e0021227de57a7a2b47a2cdc13ac24e32cb5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    client_keep_alive: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    desync_mitigation_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.DesyncMitigationMode] = None,
    drop_invalid_header_fields: typing.Optional[builtins.bool] = None,
    http2_enabled: typing.Optional[builtins.bool] = None,
    idle_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    ip_address_type: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.IpAddressType] = None,
    preserve_host_header: typing.Optional[builtins.bool] = None,
    preserve_xff_client_port: typing.Optional[builtins.bool] = None,
    security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup] = None,
    waf_fail_open: typing.Optional[builtins.bool] = None,
    x_amzn_tls_version_and_cipher_suite_headers: typing.Optional[builtins.bool] = None,
    xff_header_processing_mode: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_ceddda9d.XffHeaderProcessingMode] = None,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    cross_zone_enabled: typing.Optional[builtins.bool] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    deny_all_igw_traffic: typing.Optional[builtins.bool] = None,
    internet_facing: typing.Optional[builtins.bool] = None,
    load_balancer_name: typing.Optional[builtins.str] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2376f4e71a94afd23fd636ce7f1d4eb5d33feec01877418cd71081984d77c78b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
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
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64dae39510a9ea521ee30a14e934a7d117886670d130f86965e8561e0839736b(
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
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e162fbee6208f9bcf71a043cd6c68f4f0b6e5247772d4d7960e188604fc4b6d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ck_account_type: CkAccountType,
    ck_application: builtins.str,
    ck_company: builtins.str,
    ck_prefix: typing.Optional[builtins.str] = None,
    ck_removal_policy_override: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    analytics_reporting: typing.Optional[builtins.bool] = None,
    cross_region_references: typing.Optional[builtins.bool] = None,
    description: typing.Optional[builtins.str] = None,
    env: typing.Optional[typing.Union[_aws_cdk_ceddda9d.Environment, typing.Dict[builtins.str, typing.Any]]] = None,
    permissions_boundary: typing.Optional[_aws_cdk_ceddda9d.PermissionsBoundary] = None,
    stack_name: typing.Optional[builtins.str] = None,
    suppress_template_indentation: typing.Optional[builtins.bool] = None,
    synthesizer: typing.Optional[_aws_cdk_ceddda9d.IStackSynthesizer] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    termination_protection: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c76c1cd3932fecd49381b5c6415097ccaa499816f718d3cdca12fc77bd1b9a(
    id: builtins.str,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62100ca528134b9192d70c847e83d84b2c908790406210aa9230835bae6e824f(
    construct: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__236c4d0ef02c30c477ac69ed10a2714af3433292e8f43c9dd54f0da9009af4ea(
    *,
    analytics_reporting: typing.Optional[builtins.bool] = None,
    cross_region_references: typing.Optional[builtins.bool] = None,
    description: typing.Optional[builtins.str] = None,
    env: typing.Optional[typing.Union[_aws_cdk_ceddda9d.Environment, typing.Dict[builtins.str, typing.Any]]] = None,
    permissions_boundary: typing.Optional[_aws_cdk_ceddda9d.PermissionsBoundary] = None,
    stack_name: typing.Optional[builtins.str] = None,
    suppress_template_indentation: typing.Optional[builtins.bool] = None,
    synthesizer: typing.Optional[_aws_cdk_ceddda9d.IStackSynthesizer] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    termination_protection: typing.Optional[builtins.bool] = None,
    ck_account_type: CkAccountType,
    ck_application: builtins.str,
    ck_company: builtins.str,
    ck_prefix: typing.Optional[builtins.str] = None,
    ck_removal_policy_override: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c0898474e7611a4b104aef33dd114139f533a833837eae1605a06bbb390834(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    partition_key: typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]],
    billing: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Billing] = None,
    dynamo_stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
    encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryptionV2] = None,
    global_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.GlobalSecondaryIndexPropsV2, typing.Dict[builtins.str, typing.Any]]]] = None,
    local_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.LocalSecondaryIndexProps, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    replicas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ReplicaTableProps, typing.Dict[builtins.str, typing.Any]]]] = None,
    sort_key: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]]] = None,
    table_name: typing.Optional[builtins.str] = None,
    time_to_live_attribute: typing.Optional[builtins.str] = None,
    contributor_insights: typing.Optional[builtins.bool] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
    point_in_time_recovery: typing.Optional[builtins.bool] = None,
    table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5043f2ae443400687f2b5a4a02b15888d64136f0a03d98f34138ee3503ddef3e(
    *,
    contributor_insights: typing.Optional[builtins.bool] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
    point_in_time_recovery: typing.Optional[builtins.bool] = None,
    table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    partition_key: typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]],
    billing: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.Billing] = None,
    dynamo_stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
    encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryptionV2] = None,
    global_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.GlobalSecondaryIndexPropsV2, typing.Dict[builtins.str, typing.Any]]]] = None,
    local_secondary_indexes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.LocalSecondaryIndexProps, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    replicas: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ReplicaTableProps, typing.Dict[builtins.str, typing.Any]]]] = None,
    sort_key: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.Attribute, typing.Dict[builtins.str, typing.Any]]] = None,
    table_name: typing.Optional[builtins.str] = None,
    time_to_live_attribute: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09c2bc727ea4dfd3c617d0fa5a0ddcf2505cdffdccf9d266862e5dba45677cc(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84093b578799bb48ee71831f1f43a4dab3236aa063cc724f63bb691714b959d0(
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ac3f2465237ce44ce0d456ca6f10fc0a814ed5ddd353673002b2300c900540(
    str: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28aff407aa4f832c94b37aee02fdd8747d1bbfaaff6b72f8045fd78a621dc83b(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8917f02502111a92ac6c1fea86ccd0172fe2e2e0736bf4ac4196a594066ed9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    cidr: typing.Optional[builtins.str] = None,
    create_internet_gateway: typing.Optional[builtins.bool] = None,
    default_instance_tenancy: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.DefaultInstanceTenancy] = None,
    enable_dns_hostnames: typing.Optional[builtins.bool] = None,
    enable_dns_support: typing.Optional[builtins.bool] = None,
    flow_logs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.FlowLogOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    gateway_endpoints: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpointOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    ip_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpAddresses] = None,
    ip_protocol: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IpProtocol] = None,
    ipv6_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpv6Addresses] = None,
    max_azs: typing.Optional[jsii.Number] = None,
    nat_gateway_provider: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.NatProvider] = None,
    nat_gateways: typing.Optional[jsii.Number] = None,
    nat_gateway_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    reserved_azs: typing.Optional[jsii.Number] = None,
    restrict_default_security_group: typing.Optional[builtins.bool] = None,
    subnet_configuration: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_name: typing.Optional[builtins.str] = None,
    vpn_connections: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpnConnectionOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpn_gateway: typing.Optional[builtins.bool] = None,
    vpn_gateway_asn: typing.Optional[jsii.Number] = None,
    vpn_route_propagation: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b239cfe19fc4361b32a03657932c7f146026a16008cce0e8871db5aab5731547(
    *,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    cidr: typing.Optional[builtins.str] = None,
    create_internet_gateway: typing.Optional[builtins.bool] = None,
    default_instance_tenancy: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.DefaultInstanceTenancy] = None,
    enable_dns_hostnames: typing.Optional[builtins.bool] = None,
    enable_dns_support: typing.Optional[builtins.bool] = None,
    flow_logs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.FlowLogOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    gateway_endpoints: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.GatewayVpcEndpointOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    ip_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpAddresses] = None,
    ip_protocol: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IpProtocol] = None,
    ipv6_addresses: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IIpv6Addresses] = None,
    max_azs: typing.Optional[jsii.Number] = None,
    nat_gateway_provider: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.NatProvider] = None,
    nat_gateways: typing.Optional[jsii.Number] = None,
    nat_gateway_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    reserved_azs: typing.Optional[jsii.Number] = None,
    restrict_default_security_group: typing.Optional[builtins.bool] = None,
    subnet_configuration: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetConfiguration, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_name: typing.Optional[builtins.str] = None,
    vpn_connections: typing.Optional[typing.Mapping[builtins.str, typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpnConnectionOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpn_gateway: typing.Optional[builtins.bool] = None,
    vpn_gateway_asn: typing.Optional[jsii.Number] = None,
    vpn_route_propagation: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
