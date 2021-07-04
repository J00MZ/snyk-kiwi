# snyk-kiwi
Kiwi for summer 🥝🥝
Sweet little exercise in bundling up Docker based apps to run on K8s.

## Building the App image
```
cd <repo_directory>
docker build -t cherry-syte .
```

## Running the App locally
```
docker run -p 5000:5000 cherry-syte
```

## Deploy Kubernetes cluster in AWS
**`NOTE: This will create a VPC that includes subnets and EKS cluster`**

### Install pre-requisites to run following commands - Mac
```
brew install terraform awscli wget kubernetes-cli aws-iam-authenticator
```
### Run Terraform
**`NOTE: AWS credentials must exist locally with permissions to create VPC, EC2 and EKS AWS resources`**
```
cd terraform
terraform init -upgrade
terraform plan
terraform apply  (enter yes)
```

## Basic Kubernetes configuration
```
aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name)
wget -O v0.3.6.tar.gz https://codeload.github.com/kubernetes-sigs/metrics-server/tar.gz/v0.3.6 && tar -xzf v0.3.6.tar.gz
kubectl apply -f metrics-server-0.3.6/deploy/1.8+/
kubectl get deployment metrics-server -n kube-system
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml
kubectl proxy
```

## Accessing k8s Dashboard
In seperate terminal run
```
kubectl apply -f https://raw.githubusercontent.com/hashicorp/learn-terraform-provision-eks-cluster/master/kubernetes-dashboard-admin.rbac.yaml
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep service-controller-token | awk '{print $1}')
```
Now copy and past token from last step into the Dashboard UI  
UI can then be accessed at [this link](http://127.0.0.1:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/)

## Deploy App to Kubernetes
```
cd <REPOSITORY_ROOT>
kubectl apply -f k8s
kubectl port-forward service/app 5000
```
Then you can access the application on `localhost:5000`

## App Functionality
1. To get the current bitcoin price (From [Coindesk](https://www.coindesk.com/coindesk-api))
Access the link **`http://localhost:5000/price`** in a browser, or use CURL command
```
    curl http://localhost:5000/price
```
