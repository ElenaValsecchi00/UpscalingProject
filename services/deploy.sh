# Based on: https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html

# Create Amazon EKS cluster
eksctl create cluster --name editor-cluster --region us-east-1

# # View your cluster nodes
# kubectl get nodes -o wide

# # View the workloads running on your cluster
# kubectl get pods -A -o wide

# Create a namespace for your services
kubectl create namespace eks-editor-app-ns

# Apply the deployment and service configurations
kubectl apply -f eks-sample-deployment.yml

# Apply the service manifest to your cluster
kubectl apply -f eks-sample-deployment.yaml

# View the workloads running on your cluster
kubectl get all -n eks-sample-app-ns