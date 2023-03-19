pipeline {
    agent any

    environment {
        DOCKER_USER = 'nikhil0360'
        DOCKER_PASS = '2mrf!2cGC3#uC83'
    }

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

        stage('Push Image to docker hub'){
            steps{
                sh '/usr/local/bin/docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}'
                sh '/usr/local/bin/docker tag flask-calc ${DOCKER_USER}/flask-calc'
                sh '/usr/local/bin/docker push ${DOCKER_USER}/flask-calc'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying locally..'

                sh 'docker stop $(docker ps -a -q)'

                withPythonEnv('python3') {
                    // sh 'pip3 install -r requirements.txt'
                    sh 'ansible-playbook playbook.yml'
                }

                echo 'Done Deploying.. your app is running on http://localhost:5000'
            }
        }
    }
}
