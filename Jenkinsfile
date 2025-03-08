pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Deploy') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose build'
                sh 'docker-compose up -d'
                sh 'sleep 5'
                sh 'docker-compose ps'
                sh 'docker-compose logs'
            }
        }
        
        stage('Test Application') {
            steps {
                sh '''
                docker run --rm --network="host" \
                -v ${WORKSPACE}/tests:/tests \
                python:3.9-slim \
                bash -c "pip install pytest requests && python -m pytest /tests/test_app.py -v"
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker-compose down || true'
        }
    }
}
