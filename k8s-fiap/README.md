# Projeto FIAP/SOAT - FastAPI

O objetivo é fazer um cluster da aplicação criada pelo FastAPI
## Processo de instalaçao do kubectl + minikube em um ambiente Linux 22.04 LTS (AMD64)

```bash
sudo snap install kubectl --classic
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
kubectl cluster-info
minikube start
```
1 - Se registrar no [Docker Hub](https://hub.docker.com).

2 - Criar uma chave de acesso (Account Settings > Security > Access Tokens).

3 - Efetuar o login no docker (terminal):
```bash
sudo docker login
usuário: [usuário da conta do Docker Hub]
senha: [chave criada no passo 2]
```
4 - Copilar as images (Dockerfile) e armazenar no Docker Hub:
```bash
cd k8s-fiap
cd api && sudo docker build -t fastapi .
sudo docker tag fastapi:latest [usuario-dockerhub]/fastapi:latest
sudo docker push [usuario-dockerhub]/fastapi:latest
```
5 - Iniciar o K8s com o projeto:
```bash
kubectl apply -f k8s-fiap
```
6 - Consultando o K8s criado
```bash
kubectl get all
```
