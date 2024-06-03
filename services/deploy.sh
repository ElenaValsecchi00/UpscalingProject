# Based on: https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html

# Create Amazon EKS cluster
eksctl create cluster --name editor-cluster --region us-east-1

# Create nodegroup for Amazon EKS cluster
# eksctl create nodegroup --cluster editor-cluster --region us-east-1 --name editor-ng --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 3 --node-volume-size 20 --ssh-access --ssh-public-key UpscalingProject --managed