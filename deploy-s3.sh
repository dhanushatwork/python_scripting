#!/bin/bash

# Variables
STACK_NAME="MyS3Stack"
TEMPLATE_FILE="S3_template.json"
PARAM_FILE="S3_params.json"
REGION="ap-south-1"   # Change this to your AWS region

echo "Deploying CloudFormation stack: $STACK_NAME"

aws cloudformation create-stack \
  --stack-name $STACK_NAME \
  --template-body file://$TEMPLATE_FILE \
  --parameters file://$PARAM_FILE \
  --region $REGION \
  --capabilities CAPABILITY_NAMED_IAM