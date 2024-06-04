# Delete all the services and restart them
echo "Deleting all services"
kubectl delete -f eks-secrets.yml
kubectl delete -f eks-service.yml
kubectl delete -f eks-deployment.yml
kubectl delete -f eks-hoz-scaling.yml


echo "Restarting all services"
kubectl apply -f eks-secrets.yml
kubectl apply -f eks-service.yml
kubectl apply -f eks-deployment.yml
kubectl apply -f eks-hoz-scaling.yml


# Wait for 15 seconds
sleep 15

# Get the external IP address of the service
kubectl get svc eks-editor-service -o wide