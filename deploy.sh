#/bin/bash

# Check out code 
git checkout main
   
# Configure variables
AWS_REGION=us-east-1
ECR_REGISTRY=403843863779.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY=web_django_pages

# Configure AWS credentials
AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

# Get Git Commit ID
IMAGE_TAG=$(git rev-parse HEAD)




# Docker tag latest
#docker tag $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPOSITORY:latest

# Login to ECR (Elastic Container Registry)
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/o1w2h9a8
                                                                                                
# Push to ECR  


# Build
docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
docker push $ECR_REGISTRY/$ECR_REPOSITORY:latest



