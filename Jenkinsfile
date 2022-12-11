pipeline {
    agent any
    
    environment {
        TELEGRAM_TOKEN = credentials('telegram-token')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -lah'
            }
        }
        
        stage('Poetry Configuration') {
            steps {
                sh "/var/jenkins_home/.local/bin/poetry install --no-root"
            }
        }

        stage('Test') {
            steps {
                sh '/var/jenkins_home/.local/bin/poetry run task test'
            }
        }
    }
}
