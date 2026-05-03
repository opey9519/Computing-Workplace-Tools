# CI/CD Notification System

## 📌 Overview

This project demonstrates how modern development tools can be integrated into a cohesive **CI/CD pipeline**. It focuses on automating the process of building, verifying, and deploying a small notification service using industry-standard tools.

Developed as part of the **CIS 4930 Cumulative Project**.

Developed by Gavin Wilson, Stefan Dedic, and Cameron Goz

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

- Flask-based backend service with in-memory notification storage
- Built using:
  - Git and GitHub for version control and source hosting
  - Docker for containerization
  - Jenkins for CI/CD automation
  - pytest for automated testing

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

## 📂 Project Structure
```
ci-cd-notification-system/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── notification_service.py
│   └── routes.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── jenkins_setup.md
├── scripts/
│   └── wait-for-db.sh
├── tests/
│   └── test_app.py
├── Dockerfile.jenkins
├── Jenkinsfile
├── pytest.ini
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Ensure Docker is Installed
   ```
     docker --version
   ```

## Run App (Manual)

   ```
     docker compose -f docker/docker-compose.yml up
   ```

## Visit
  ```
    http://localhost:5000
  ```

---

## Jenkins Setup

Jenkins automates the full pipeline: checkout, build, test, and deploy.

> **Note:** Jenkins must be run using the custom image in `Dockerfile.jenkins` with the
> host Docker socket mounted. The plain `jenkins/jenkins:lts` image does not include the
> Docker CLI and will fail with `docker: not found`. See
> [docs/jenkins_setup.md](docs/jenkins_setup.md) for full setup, rebuild, and
> troubleshooting instructions.

### Prerequisites
- Docker Desktop running
- Custom Jenkins image built from `Dockerfile.jenkins` (see docs/jenkins_setup.md)
- The GitHub repository is accessible from the Jenkins host

### Creating the Pipeline Job

1. Open Jenkins in your browser.
2. Click **New Item**, enter a name (e.g. `ci-cd-notification-system`), select **Pipeline**, and click **OK**.
3. In the job configuration, scroll to the **Pipeline** section.
4. Set **Definition** to `Pipeline script from SCM`.
5. Set **SCM** to `Git`.
6. Paste the GitHub repository URL into the **Repository URL** field.
7. Set **Branch Specifier** to `*/main`.
8. Set **Script Path** to `Jenkinsfile`.
9. Click **Save**.
10. Click **Build Now** to trigger the pipeline.

### Pipeline Stages

| Stage | What it does |
|---|---|
| **Checkout** | Pulls the latest code from the GitHub repository via `checkout scm`. |
| **Build** | Runs `docker build` using `docker/Dockerfile` with the repo root as the build context, producing the image `ci-cd-notification-system`. |
| **Verify** | Creates a Python virtual environment, installs dependencies from `requirements.txt`, and runs the full `pytest` test suite. |
| **Deploy** | Stops any existing containers with `docker compose down`, then starts the app in detached mode with `docker compose up -d --build` using `docker/docker-compose.yml`. |

---