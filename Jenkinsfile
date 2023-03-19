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
                
                withPythonEnv('env') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest test_calculator.py'
                }

                echo 'Done Testing..'
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
