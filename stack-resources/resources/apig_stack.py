from typing import List
from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as _apig
from aws_cdk import aws_logs as _logs


class ApigStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.resource_bucket_name = self.node.try_get_context("resource-bucket-name")
        self.lambda_package_key = self.node.try_get_context("lambda-package-key")
        self.lambda_function_name = self.node.try_get_context("lambda-function-name")

        self.add_lambda_function()
        self.add_apig()

    def add_lambda_function(self):
        self.lambda_function = _lambda.Function(
            self,
            "LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="lambda_handler.lambda_function",
            code=_lambda.S3Code(bucket=self.resource_bucket_name, key=self.lambda_package_key),
        )

        _logs.LogGroup(
            self,
            "LambdaFunctionLog",
            log_group_name=f"/aws/lambda/{self.lambda_function.function_name}",
            removal_policy=core.RemovalPolicy.DESTROY,
            retention=_logs.RetentionDays.ONE_WEEK,
        )

    def add_apig(self):
        self.api = _apig.LambdaRestApi(self, "FastApiCdkDemo", handler=self.lambda_function)

        core.CfnOutput(
            self, "FastApiCdkDemoUrl", value=f"{self.api.url}", description="api gateway url"
        )
