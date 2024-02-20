# CI/CD Pipeline for Deploying Applications on Google Kubernetes Engine (GKE)


## Introduction

In the modern software development landscape, Continuous Integration/Continuous Deployment (CI/CD) pipelines play a pivotal role in automating the process of building, testing, and deploying applications. In this blog post, we’ll deep dive into the implementation of a robust CI/CD pipeline to deploy applications on Google Kubernetes Engine (GKE) using Google Cloud Build and Cloud Deploy services.

Video Tutorial :   [![YouTube](https://img.shields.io/badge/YouTube-Video-green)](https://youtu.be/L_1qbt-Iii0?feature=shared)

## Requirements

To achieve our goal, we have the following requirements:
- Deployment of two simple Flask applications (app1 & app2) on the GKE clusters.
- Automation of the entire deployment process, triggered by a developer’s code push.
- Dev-cluster deployment precedes production deployment, allowing for review before promoting to the prod-cluster.

## Architecture

![image](https://github.com/vishal-bulbule/gke-test/assets/143475073/66c914bb-4466-4a23-b977-f0880e1e1f12)

## Technical Stack Summary

This CI/CD pipeline leverages several key components:
- Google Kubernetes Engine (GKE): Google’s managed Kubernetes service, providing a scalable and reliable platform for deploying containerized applications.
- Cloud Build: A fully managed continuous integration and continuous delivery platform that allows developers to build, test, and deploy applications on Google Cloud Platform.
- Cloud Deploy: A service for continuous delivery that automates the deployment of containerized applications to Google Kubernetes Engine and other platforms.
- GitHub: A popular version control platform where developers collaborate, manage, and version control their codebase.

## Solution

We are going to implement the solution using the following steps to implement the CI/CD pipeline for deploying applications on GKE:

1. Create two simple Flask applications (app1 & app2).
2. Set up a GitHub repository and push the application code.
3. Create two GKE clusters: dev-cluster and prod-cluster, using Google Kubernetes Engine.
4. Create Kubernetes manifest files in the Kubernetes folder to deploy the application and expose it as a service.
5. Create skaffold.yaml file now.
6. Now Create cloudbuild.yaml file to build and push docker images to Artifact registry for both application and Configure a Cloud Build trigger to initiate the pipeline upon code push events in the GitHub repository.
7. Implement the necessary code to define the Cloud Deploy pipeline and targets for both dev-cluster and prod-cluster.
8. Push the updated code to the GitHub repository, triggering the Cloud Build and Cloud Deploy processes.

   If you encounter any confusion, please refer to the [Video](https://youtu.be/L_1qbt-Iii0?feature=shared)
 linked at the beginning of the blog.


