from typing import List
from aws_cdk import core
from aws_cdk import aws_s3 as _s3


class ResourceStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.resource_bucket_name = self.node.try_get_context("resource-bucket-name")

        self.create_resource_bucket()

    def create_resource_bucket(self):
        _s3.Bucket(
            self,
            "ResourceBucket",
            bucket_name=self.resource_bucket_name,
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            removal_policy=core.RemovalPolicy.RETAIN,
        )
