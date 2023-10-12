# Calix_code
Calix Interview Assignment


To build a Python-based Kubernetes operator to deploy a microservice application (custom CRUD app) where data is stored in MongoDB, etc., and to add a feature to expand the persistent volume associated with the MongoDB pod, we can follow these steps:

1. Create a Python project and install the necessary dependencies.**

Create a new Python project and install the following dependencies:


pip install operator-sdk kubebuilder pyyaml


2. Create a new Kubernetes operator.

Use the "operator-sdk" tool to create a new Kubernetes operator:


operator-sdk new my-operator --api-version apps/v1 --kind Deployment


This will create a new directory called `my-operator/` containing the basic structure for a Kubernetes operator.

3. Add the necessary code to the operator.

k8s_operator.py codes shows how to add the necessary code to the operator to deploy a microservice application with MongoDB:

4. Build and deploy the operator.

To build and deploy the operator, run the following commands:


make build
kubectl apply -f deploy/operator.yaml


5. Create a persistent volume claim for MongoDB.

To create a persistent volume claim for MongoDB, run the following command:


kubectl apply -f deploy/mongodb-pvc.yaml


6. Deploy your microservice application.

To deploy your microservice application, run the following command:


kubectl apply -f deploy/my-app.yaml


This will deploy your microservice application with MongoDB.

7. Expand the persistent volume associated with the MongoDB pod.

To expand the persistent volume associated with the MongoDB pod, run the following commands:


# Get the name of the MongoDB pod.
mongodb_pod_name=$(kubectl get pods -l app=my-app -o jsonpath='{.items[0].metadata.name}')

# Get the name of the persistent volume claim associated with the MongoDB pod.
mongodb_pvc_name=$(kubectl get pod "$mongodb_pod_name" -o jsonpath='{.spec.volumes[0].persistentVolumeClaim.claimName}')

# Expand the persistent volume claim.
kubectl patch persistentvolumeclaims "$mongodb_pvc_name" --type json -p '[{"op": "replace", "path": "/spec/resources/requests/storage", "value": "10Gi"}]'


This will expand the persistent volume associated with the MongoDB pod to 10Gi.

You can now use your microservice.

#2 Question 

To create a simple CRUD application only APIs using Python, we can follow these steps:

1. Create a new Python project and install the necessary dependencies.

pip install flask

2. Create a Flask app.

Create a new file called `app.py` and add the following code:


