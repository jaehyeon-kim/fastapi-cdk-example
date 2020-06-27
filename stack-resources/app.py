#!/usr/bin/env python3

import os
from aws_cdk import core
from resources.resource_stack import ResourceStack
from resources.apig_stack import ApigStack

# stacks to create - eg) resource, apig, resource|apig
STACKS_TO_CREATE = os.getenv("STACKS", "resource").split("|")

app = core.App()

ResourceStack(app, app.node.try_get_context("resource-stack-name"), STACKS_TO_CREATE)
ApigStack(app, app.node.try_get_context("apig-stack-name"), STACKS_TO_CREATE)

app.synth()
