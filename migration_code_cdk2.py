#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import (
    CfnOutput,
    aws_s3 as s3
)
from constructs import Construct

class BucketL2Stack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # L2 construct for S3 bucket creation
        bucket = s3.Bucket(
            self, 
            "MyL2Bucket",
            bucket_name="my-l2-example-bucket-123",
            # Additional L2 properties that improve the default configuration:
            removal_policy=cdk.RemovalPolicy.DESTROY,  # For easy cleanup during development
            auto_delete_objects=True,                  # Auto-delete objects when bucket is removed
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # Security best practice
            encryption=s3.BucketEncryption.S3_MANAGED,  # Enable encryption by default
            versioned=True                             # Enable versioning for data protection
        )
        
        # Output the bucket name
        CfnOutput(
            self, 
            "BucketName",
            value=bucket.bucket_name
        )

# Main code to run the CDK app
app = cdk.App()
BucketL2Stack(app, "BucketL2Stack")
app.synth()
