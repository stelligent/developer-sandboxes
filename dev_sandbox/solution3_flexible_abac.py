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
    CfnUser,
)
from samtranslator.model import tags

from dev_sandbox.policies.sandbox import (
    full_attribute_based_policy,
    flexible_policy_permission_boundary,
)


class Solution3FlexibleABACStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        attribute_tagged_group = Group(self, "Flexible Tagged")
        access_project = core.CfnTag(key="access-project", value="elysian")
        access_team = core.CfnTag(key="access-team", value="webdev")
        access_cost_center = core.CfnTag(key="cost-center", value="2600")

        flexible_boundary_policy = CfnManagedPolicy(
            self,
            "FlexiblePermissionBoundary",
            policy_document=json.loads(flexible_policy_permission_boundary),
        )

        CfnUser(
            self,
            "Developer",
            tags=[access_project, access_team, access_cost_center],
            groups=[attribute_tagged_group.group_name],
            permissions_boundary=flexible_boundary_policy.ref,
        )

        # Add AWS managed policy for EC2 Read Only access for the console.
        attribute_tagged_group.add_managed_policy(
            ManagedPolicy.from_aws_managed_policy_name(
                managed_policy_name="AmazonEC2ReadOnlyAccess"
            )
        )

        # Import a json policy and create CloudFormation Managed Policy
        CfnManagedPolicy(
            self,
            "FlexibleAttributePolicy",
            policy_document=json.loads(full_attribute_based_policy),
            groups=[attribute_tagged_group.group_name],
        )

        vpc = Vpc.from_lookup(self, "AttributeTaggedVPC", is_default=True)
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

        # Can only add tags to CfnInstance as of cdk v1.31
        valid_instance = CfnInstance(
            self,
            "Valid Instance",
            image_id=image_id,
            instance_type="t2.micro",
            tags=[access_project, access_team, access_cost_center],
        )
        # Empty group as it's not need to complete our tests.
        test_security_group = SecurityGroup(self, "EmptySecurityGroup", vpc=vpc)

        core.CfnOutput(
            self,
            "BlockedInstance",
            value=blocked_instance.instance_id,
            export_name="elysian-blocked-instance",
        )

        core.CfnOutput(
            self,
            "ValidInstance",
            value=valid_instance.ref,
            export_name="elysian-valid-instance",
        )
        core.CfnOutput(
            self,
            "TestSecurityGroup",
            value=test_security_group.security_group_id,
            export_name="test-elysian-sg",
        )
        core.CfnOutput(
            self, "DefaultAMI", value=image_id, export_name="default-elysian-ami"
        )
