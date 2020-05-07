import json

from aws_cdk import core
from aws_cdk.aws_ec2 import (
    CfnInstance,
    Instance,
    InstanceType,
    MachineImage,
    Vpc,
    SecurityGroup,
)
from aws_cdk.aws_iam import (
    CfnManagedPolicy,
    Group,
    ManagedPolicy,
    Policy,
    PolicyDocument,
    PolicyStatement,
    User,
)

from dev_sandbox.policies.sandbox import username_based_policy


class Solution2UsernameTaggedStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        username_tagged = Group(self, "Username Tagged")

        developer = User(self, "Developer")
        developer.add_to_group(username_tagged)

        # Add AWS managed policy for EC2 Read Only access for the console.
        username_tagged.add_managed_policy(
            ManagedPolicy.from_aws_managed_policy_name(
                managed_policy_name="AmazonEC2ReadOnlyAccess"
            )
        )

        # Import a json policy and create CloudFormation Managed Policy
        CfnManagedPolicy(
            self,
            "UserTaggedPolicy",
            policy_document=json.loads(username_based_policy),
            groups=[username_tagged.group_name],
        )

        vpc = Vpc.from_lookup(self, "UsernameTaggedVPC", is_default=True)
        instance_type = InstanceType("t2.micro")
        ami = MachineImage.latest_amazon_linux()

        blocked_instance = Instance(
            self,
            "Blocked Instance",
            machine_image=ami,
            instance_type=instance_type,
            vpc=vpc,
        )
        # Re-use the AMI from t
        image_id = blocked_instance.instance.image_id

        # Can only add tags to CfnInstance as of 1.31
        dev_username_tag = core.CfnTag(
            key="username", value=developer.user_name)
        valid_instance = CfnInstance(
            self,
            "Valid Instance",
            image_id=image_id,
            instance_type="t2.micro",
            tags=[dev_username_tag],
        )
        # Empty group as it's not need to complete our tests.
        test_security_group = SecurityGroup(
            self, "EmptySecurityGroup", vpc=vpc)

        core.CfnOutput(
            self,
            "BlockedInstance",
            value=blocked_instance.instance_id,
            export_name="username-blocked-instance",
        )

        core.CfnOutput(
            self,
            "ValidInstance",
            value=valid_instance.ref,
            export_name="username-valid-instance",
        )
        core.CfnOutput(
            self,
            "TestSecurityGroup",
            value=test_security_group.security_group_id,
            export_name="test-username-sg",
        )
        core.CfnOutput(
            self, "DefaultAMI", value=image_id, export_name="default-username-ami"
        )
