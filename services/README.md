# Guide

## Configure AWS CLI Account
Insert in the ~/.aws/credentials file the credentials of the account as seen in the "Learner Lab".

Replace credentials inside services/eks-secrets.yml and .env files.
Secrets in eks-secrets.yml have to be in base64.

Then create the kubefile for the cluster:
```
aws eks update-kubeconfig --region us-east-1 --name image-editor-cluster
```