pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                // Dockerfile is in docker/, build context is the repo root
                sh 'docker build -t ci-cd-notification-system -f docker/Dockerfile .'
            }
        }

        stage('Verify') {
            steps {
                echo 'Running automated tests...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application with Docker Compose...'
                // docker-compose.yml is in docker/
                sh 'docker compose -f docker/docker-compose.yml down || true'
                sh 'docker compose -f docker/docker-compose.yml up -d --build'
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
