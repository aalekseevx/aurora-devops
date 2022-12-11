pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -lah'
            }
        }
        
        stage('Poetry Configuration') {
            steps {
                sh "poetry install --no-root"
            }
        }

        stage('Test') {
            steps {
                sh 'poetry run task test'
            }
        }
    }
}
