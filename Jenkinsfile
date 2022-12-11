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
                sh 'sudo apt-get update && sudo apt-get install -y curl python'
                sh "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"
                sh "$HOME/.poetry/bin/poetry install --no-root"
                sh "$HOME/.poetry/bin/poetry shell --no-interaction"
            }
        }

        stage('Test') {
            steps {
                sh 'poetry run task test'
            }
        }
    }
}
