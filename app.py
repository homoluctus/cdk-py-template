#!/usr/bin/env python3

from aws_cdk import core

from src.stack.sample import Sample


app = core.App()

# Add stacks
Sample(app, 'sample')

app.synth(skip_validation=False)
