# Delete all the services and restart them
echo "Deleting all services"
kubectl delete -f eks-service.yml
kubectl delete -f eks-deployment.yml
kubectl delete -f eks-secrets.yml

echo "Restarting all services"
kubectl apply -f eks-service.yml
kubectl apply -f eks-deployment.yml
kubectl apply -f eks-secrets.yml

# Get the external IP address of the service
kubectl get svc eks-editor-service -o wide