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
                sh 'sleep 2'
                sh 'docker logs simple-python-app'
                sh 'docker ps -a | grep simple-python-app'
            }
        }
        
        stage('Test Application') {
            steps {
                sh 'sleep 5' 
                sh '''
                docker run --rm --network="host" \
                -v ${WORKSPACE}/tests:/app/tests \
                simple-python-app:${BUILD_NUMBER} \
                python -m pytest /app/tests/test_app.py -v
                '''
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