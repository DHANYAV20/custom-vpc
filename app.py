#!/usr/bin/env python3

from aws_cdk import core

from custom_vpc.custom_vpc_stack import CustomVpcStack


app = core.App()
CustomVpcStack(app, "custom-vpc", env={'region': 'us-west-2'})

app.synth()