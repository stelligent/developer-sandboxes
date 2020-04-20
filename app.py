#!/usr/bin/env python3
import os

from aws_cdk import core

from dev_sandbox.solution1_by_project import Solution1ProjectStack
from dev_sandbox.solution2_by_username import Solution2UsernameTaggedStack
from dev_sandbox.solution3_flexible_abac import Solution3FlexibleABACStack

env = {
    "region": "us-east-2",
    "account": os.environ.get("CDK_DEFAULT_ACCOUNT"),
}

app = core.App()
Solution1ProjectStack(app, "solution-1-vahalla-project-tagged", env=env)

Solution2UsernameTaggedStack(app, "solution-2-username-tagged", env=env)

Solution3FlexibleABACStack(app, "solution-3-flexible-attribute", env=env)

app.synth()
