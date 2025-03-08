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
                // Запускаємо тести всередині контейнера з певними параметрами мережі
                sh 'docker exec -i simple-python-app bash -c "cd /app && python -m pytest -v"'
            }
        }
    }
    
    post {
        always {
            sh 'docker stop simple-python-app || true'
            sh 'docker rm simple-python-app || true'
        }
    }
}
