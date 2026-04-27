# CI-CD-Notification-System

CI/CD Notification System. A project demonstrating a real-world development workflow using **Jenkins**, **Docker**, and a **Flask application**, with optional **MongoDB** integration for persistent storage.

# CI/CD Notification System

## 📌 Overview

This project demonstrates how modern development tools can be integrated into a cohesive **CI/CD pipeline**. It focuses on automating the process of building, verifying, and deploying a small notification service using industry-standard tools.

Developed as part of the **CIS 4930 Cumulative Project**.

---

## Problem Statement

How can we design a realistic software development workflow that integrates multiple tools to automate code integration, testing, and deployment while supporting a functional notification system?

---

### System Representation

- **Users:** Clients interacting with the API  
- **Notifications:** Messages created and retrieved by users  
- **System Type:**
  - RESTful API
  - Containerized application
  - CI/CD automated pipeline  

---

## 🏗️ System Construction

- Flask-based backend service  
- Built using:
  - Docker for containerization  
  - Jenkins for CI/CD automation  
  - MongoDB (optional) for data persistence  

---

## 📊 Workflow & Pipeline Analysis

For the CI/CD pipeline, we provide in our report:

- Pipeline stages:
  - **Checkout**
  - **Build**
  - **Verify**
  - **Deploy**
- Automation details using Jenkins  
- Integration between GitHub, Docker, and Jenkins  

---

## 🧪 Experimental Analysis

We evaluate the system in our report based on:

- Pipeline execution time  
- Build and deployment success rate  
- System behavior during updates  
- Observations on:
  - Automation efficiency  
  - Container performance  
  - Reliability of deployment workflow  

---

## 💡 Discussion & Insights

- Benefits of CI/CD automation in modern development  
- Trade-offs of containerization  
- Challenges in pipeline configuration and debugging  
- Key observations from integrating multiple tools  

---

## 📂 Projected Project Structure (Up for Change)
```
ci-cd-notification-system/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── services/
│ ├── notification_service.py
│ └── utils/
│
├── tests/
│ └── test_app.py
│
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
│
├── jenkins/
│ └── Jenkinsfile
│
├── scripts/
│ └── wait-for-db.sh
│
├── docs/
│ ├── architecture.png
│ └── pipeline_screenshot.png
│
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Ensure Docker is Installed
   ```
     docker --version
   ```
   
## Run App

   ```
     docker compose up 
   ```

## Visit
  ```
    http://localhost:5000
  ```
