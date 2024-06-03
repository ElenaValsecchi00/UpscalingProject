# Guide

## Configure AWS CLI Account
Create the cluster, the node group an then:
```
#./deploy.sh
./set_envs.sh
./restart.sh
```

Get external ip of load balancer using:
```
kubectl get svc eks-editor-service -o wide
```
