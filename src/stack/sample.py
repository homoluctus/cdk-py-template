from typing import Any

from aws_cdk import core


class Sample(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs: Any) -> None:
        super().__init__(scope, id, **kwargs)
