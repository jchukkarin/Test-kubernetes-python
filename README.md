# 🚀 FastAPI Login + Kubernetes + CI/CD

## 📌 Features
- FastAPI Login (JWT)
- Kubernetes (Helm)
- CI/CD with GitHub Actions
- Docker

## 📁 Project Structure
- `k8s/` : raw Kubernetes manifests for debugging or learning
- `helm/python-app/` : production-ready Helm chart
- `app/` : Python application source and Dockerfile
- `scripts/` : deployment and cleanup helper scripts

---

## 🐳 Run Local

```bash
docker build -t login-app .
docker run -p 8000:8000 login-app