pipeline {
    agent any
    
    environment {
        TELEGRAM_TOKEN = credentials('telegram-token')
        CODECOV_TOKEN = credentials('codecov-token')
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
                sh "poetry install --no-root"
            }
        }
        
        stage('Build') {
            steps {
                sh "make texts-compile"
            }
        }

        stage('Test') {
            steps {
                sh 'make test'
                sh 'codecov -t ${CODECOV_TOKEN}'
            }
        }
        
        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }
    }
}
