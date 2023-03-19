pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip3 install -r requirements.txt'
                sh 'pytest test_calculator.py'
            }
        }

        stage('docker build') {
            steps {
                sh 'docker build .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
