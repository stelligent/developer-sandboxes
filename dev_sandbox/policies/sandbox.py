project_specific_tags = """{
    "Version": "2012-10-17",
    "Statement": [{
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:*:*:instance/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/project": "vahalla"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "project"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:*/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "RunInstances"
                }
            }
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/project": "vahalla"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "project"
                },
                "StringEqualsIfExists": {
                    "aws:RequestTag/project": "vahalla"
                }
            }
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/project": "vahalla"
                }
            }
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:key-pair/*",
                "arn:aws:ec2:*:*:launch-template/*",
                "arn:aws:ec2:*::snapshot/*",
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:placement-group/*",
                "arn:aws:ec2:*:*:network-interface/*",
                "arn:aws:ec2:*::image/*"
            ]
        },
        {
            "Sid": "PermissionsForRunningTestsOnly",
            "Effect": "Allow",
            "Action": [
                "sts:DecodeAuthorizationMessage",
                "cloudformation:ListExports"
            ],
            "Resource": "*"
        }
    ]
}"""

username_based_policy = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "aws:RequestTag/username": "${aws:username}"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "username"
                }
            }
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:*/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "RunInstances"
                }
            }
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "ec2:ResourceTag/username": "${aws:username}",
                    "aws:RequestTag/username": "${aws:username}"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "username"
                }
            }
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances",
                "ec2:TerminateInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "ec2:ResourceTag/username": "${aws:username}"
                }
            }
        },
        {
            "Sid": "VisualEditor4",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:key-pair/*",
                "arn:aws:ec2:*:*:launch-template/*",
                "arn:aws:ec2:*::snapshot/*",
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:placement-group/*",
                "arn:aws:ec2:*:*:network-interface/*",
                "arn:aws:ec2:*::image/*"
            ]
        },
        {
            "Sid": "PermissionsForRunningTestsOnly",
            "Effect": "Allow",
            "Action": [
                "cloudformation:ListExports",
                "sts:DecodeAuthorizationMessage",
                "iam:GetUser"
            ],
            "Resource": "*"
        }
    ]
}
"""

full_attribute_based_policy = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "aws:RequestTag/access-project": "${aws:PrincipalTag/access-project}",
                    "aws:RequestTag/access-team": "${aws:PrincipalTag/access-team}",
                    "aws:RequestTag/cost-center": "${aws:PrincipalTag/cost-center}"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": ["access-project", "access-team", "cost-center"]
                }
            }
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:*/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "RunInstances"
                }
            }
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "ec2:ResourceTag/access-project": "${aws:PrincipalTag/access-project}",
                    "ec2:ResourceTag/access-team": "${aws:PrincipalTag/access-team}",
                    "ec2:ResourceTag/cost-center": "${aws:PrincipalTag/cost-center}"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": ["access-project", "access-team", "cost-center"]
                },
                "StringEqualsIgnoreCase": {
                    "aws:RequestTag/access-project": "${aws:PrincipalTag/access-project}",
                    "aws:RequestTag/access-team": "${aws:PrincipalTag/access-team}",
                    "aws:RequestTag/cost-center": "${aws:PrincipalTag/cost-center}"
                }
            }
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "ec2:ResourceTag/access-project": "${aws:PrincipalTag/access-project}",
                    "ec2:ResourceTag/access-team": "${aws:PrincipalTag/access-team}",
                    "ec2:ResourceTag/cost-center": "${aws:PrincipalTag/cost-center}"
                }
            }
        },
        {
            "Sid": "VisualEditor4",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:key-pair/*",
                "arn:aws:ec2:*:*:launch-template/*",
                "arn:aws:ec2:*::snapshot/*",
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:placement-group/*",
                "arn:aws:ec2:*:*:network-interface/*",
                "arn:aws:ec2:*::image/*"
            ]
        },
        {
            "Sid": "PermissionsForRunningTestsOnly",
            "Effect": "Allow",
            "Action": [
                "cloudformation:ListExports",
                "sts:DecodeAuthorizationMessage"
            ],
            "Resource": "*"
        }
    ]
}
"""

flexible_policy_permission_boundary = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "cloudformation:ListExports",
                "sts:DecodeAuthorizationMessage"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:key-pair/*",
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ec2:*::snapshot/*",
                "arn:aws:ec2:*:*:launch-template/*",
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:placement-group/*",
                "arn:aws:ec2:*:*:network-interface/*",
                "arn:aws:ec2:*::image/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ec2:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:Describe*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:Describe*",
            "Resource": "*"
        }
    ]
}
"""
