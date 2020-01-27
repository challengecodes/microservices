# Microservice example
2 microservices deploy independently a without downtime on a k8s.

## Prerequisite
1. minikube - https://kubernetes.io/docs/tasks/tools/install-minikube/
1. helm - https://helm.sh/docs/intro/install/

## Running
1. `$ minikube start`
1. `$ ./microservice-a/deploy.sh` - Build a docker image and deploy to k8s
1. `$ ./microservice-b/deploy.sh` - Build a docker image and deploy to k8s

## Updating
1. Increase `appVersion` at `/chart/Chart.yalm`
1. Change docker tag accordingly at `/deploy.sh`
1. `$ ./deploy.sh`

## Testing
1. `$ kubectl port-forward <microservice-a-pod-id> 8080:5000` - get `pod-id` via `kubectl get pods`

```
$ curl -X POST -H "Content-Type: application/json" --url "http://127.0.0.1:8080/api" --data '{"message":"abcdef"}'

{"message":"fedcba","rand":0.7504616839345337}
```

## Deploying to GCP
1. Create a kubernetes project
1. Automate uploading process of docker images to [GCR](https://cloud.google.com/container-registry)
1. Create a machine user that has a permission to complete CI/CD tasks.
1. Downtime is handled via kubernetes as it is using [rolling update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/).

## CI/CD
1. CI will run on every pull request: linting, formatting and testing + security checks
1. ```
                             CD
   -----master-------------merge------
         \                  /
          \               CI
           \____feature___/
   ```
   CD will run on every merges to master branch doing the similar task at `deploy.sh`
1. Machine user will handle all these tasks therefore will reduce human error - Will keep human direct access to kubernetes at minimum
1. Both CI and CD can be done via [concourse](https://concourse-ci.org/), [jenkins](https://jenkins.io/) or [argocd](https://argoproj.github.io/argo-cd/). It will depend on the situation.
