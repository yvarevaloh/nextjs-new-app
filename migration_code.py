#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import CfnOutput
from constructs import Construct

class BucketL1Stack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # L1 construct for S3 bucket creation
        bucket = cdk.aws_s3.CfnBucket(
            self, 
            "MyL1Bucket",
            bucket_name="my-l1-example-bucket-123"
        )
        
        # Output the bucket name
        CfnOutput(
            self, 
            "BucketName",
            value=bucket.bucket_name
        )

# Main code to run the CDK app
app = cdk.App()
BucketL1Stack(app, "BucketL1Stack")
