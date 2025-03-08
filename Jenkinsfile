pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t simple-python-app:${BUILD_NUMBER} .'
            }
        }
        
        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker stop simple-python-app || true'
                sh 'docker rm simple-python-app || true'
                sh 'docker run -d -p 5000:5000 --name simple-python-app simple-python-app:${BUILD_NUMBER}'
            }
        }
        
        stage('Test Application') {
            steps {
                sh 'sleep 5' // Wait for the app to start
                sh 'python -m pytest tests/test_app.py -v'
            }
        }
    }
    
    post {
        failure {
            sh 'docker stop simple-python-app || true'
            sh 'docker rm simple-python-app || true'
        }
    }
}
