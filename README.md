
# Building Developer Sandboxes with Tags

Demonstrates three solutions for building Developer Sandboxes using tags on AWS using Attribute based Access Control(ABAC).

## Proof of Concept for each Solution

 1. Project Based EC2 Access
 1. Individual Access Control
 1. Highly Flexible and Granular Access Control

### Installing tools to Deploy proof of concept stacks

Requirements

 1. Install aws-cdk: `npm install -g aws-cdk` or `brew install aws-cdk`
 1. Install aws-vault and add your administrator. `brew install aws-vault` or other install methods
 1. [Setup your CDK project requirements](#setup-aws-cdk)
 1. Finally, before deploying you need to configure your **account** and **region** values in the `app.py` file. The default region is set to `us-east-2`, and your AWS account environment can be set with an variable: `export CDK_DEFAULT_ACCOUNT=01234567890`
 1. Now you are ready to proceed to **Deploy a Solution**

### Deploy a Solution

Pre-flight check.
`aws-vault exec <Your Admin User> -- cdk synth "solution-1*"`

Because our CDK app has multiple stacks, we either need to specify the stack name(s) or use a wildcard.

`aws-vault exec <Your Admin User> -- cdk deploy "solution-1*"`

Deploy All 3 Solutions:

`aws-vault exec <Your Admin User> -- cdk deploy "*"`

Note: When you deploy your region must have a default VPC. If needed, create a Default VPC.

## Running Tests using aws-vault

Each solution has it's own set of tests, you don't use your administrator account to run these tests. Instead you'll need to find the User created by the CloudFormation Stack. The Solution 1 username would be something like `solution-1-vahalla-projec-VahallaDeveloper4EA7C9DC-1QTP7AV1JSXPS`, which you can find under the Resources section in the CloudFormation Stack.

 1. Find the Test User on the CloudFormation Stack
 1. Create API keys for the <Solution User Account> that was created.
 1. Add the User to `aws-vault`

Test Solution 1
`aws-vault exec <vault profile name> -- pytest tests/test_solution1_project_policy.py`

Test Solution 2
`aws-vault exec <vault profile name> -- pytest tests/test_solution2_username.py`

Test Solution 3
`aws-vault exec <vault profile name> -- pytest tests/test_solution3_flexible.py`

Note: If you are using Mult-Factor Authentication (MFA) for your administrator accounts. You will need to edit your `.aws/config` profile you added to include your account MFA arn. AWS CDK does not support MFA

```config
[profile johnadmin]
region=us-east-2
mfa_serial=arn:aws:iam::012345678901:mfa/john.doe.administrator
```

### Setup AWS CDK

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```bash
python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```bash
source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```Windows
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```bash
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```bash
cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

### Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk docs`        open CDK documentation

### Implementation Details

Each policy in dev-sandbox/policies/sandbox.py has a permission section labeled `sid = "PermissionsForRunningTestsOnly"`

Limitations of the Proof of Concept policies:

* Users are not able to create security groups; only existing Security groups can be used.
* No restrictions on AMI usage
* No restrictions on EBS volumes creation
* User's don't have the ability to create Key Pairs for ssh access.
