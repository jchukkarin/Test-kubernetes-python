#!/bin/bash

echo "🧹 Cleaning up Kubernetes resources..."

helm uninstall myapp

kubectl delete all --all

echo "✅ Cleanup complete!"