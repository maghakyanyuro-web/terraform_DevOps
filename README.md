# 🚀 DevOps Foundations: Single Container Deployment on AWS EC2

This repository represents the **first milestone** of my DevOps learning journey. It focuses on the core principles of containerization, cloud infrastructure setup, and automated CI/CD pipelines.

## 📌 Project Goals
The main objective of this project was to move from a local development environment to a live cloud infrastructure, ensuring a seamless and automated deployment process.

### 🛠 Technology Stack
*   **Infrastructure:** AWS EC2 (Ubuntu 22.04 LTS)
*   **Containerization:** Docker
*   **Backend:** Python (Flask)
*   **Automation (CI/CD):** GitHub Actions
*   **Communication:** SSH Protocol for Remote Management

## 🏗 Key Features & Implementation
1.  **Dockerization:** Created a custom `Dockerfile` to package the Flask application, ensuring environment consistency across local and cloud environments.
2.  **AWS Infrastructure:** Configured an **EC2 instance**, managed Security Groups (Inbound/Outbound rules), and handled SSH authentication.
3.  **Automated CI/CD:** Set up a GitHub Actions workflow that:
    *   Triggers on every `push` to the main branch.
    *   Securely connects to the AWS instance using SSH Secrets.
    *   Pulls the latest code and restarts the Docker container automatically.

> **Note:** The cloud instance is currently decommissioned to manage costs, but the architecture remains fully documented and reproducible.

## 🚀 How to Run Locally
To replicate the environment on your machine, ensure you have Docker installed and run:

# Clone the repository
git clone https://github.com
cd devops-master-project

# Build and run the Docker container
docker build -t flask-app .
docker run -p 5000:5000 flask-app
Используйте код с осторожностью.

🗺 Road to Mastery
This project is Part 1 of a 3-part DevOps series:
Part 1: Single Container Deployment (This Repo) ✅
Part 2: Multi-Container Orchestration (Docker Compose) 🔜
Part 3: Scalable Infrastructure with Kubernetes (K8s) 🔜
Stay tuned for the next stages of the journey!
