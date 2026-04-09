#!/bin/bash

echo "🚀 Deploying app..."

# build image
docker build -t arm0614903790/login-app:latest ./app

# push image
docker push arm0614903790/login-app:latest

# deploy ด้วย helm
helm upgrade --install myapp ./helm/project-app

echo "✅ Deploy complete!"