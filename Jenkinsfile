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
                
                withPythonEnv('python3') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest test_calculator.py'
                }

                echo 'Done Testing..'
            }
        }

        stage('docker build') {
            steps {
                sh '/usr/local/bin/docker build --tag flask-calc .'
            }
        }

        stage('docker run') {
            steps {
                sh '/usr/local/bin/docker run -d -p 5000:5000 --name flask-calc-app flask-calc'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
