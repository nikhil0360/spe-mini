pipeline {
    agent any

    environment {
        // DOCKER_USER = 'nikhil0360'
        // DOCKER_PASS = '2mrf!2cGC3#uC83'
        registry = "nikhil0360/flask-calc"
        credentialID = "dockerhub"
        dockerImage = ""
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo 'Installing requirements..'
                withPythonEnv('python3') {
                    sh 'pip3 install --upgrade pip'
                    sh 'pip3 install -r requirements.txt'
                }
                echo 'Done Building..'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                
                withPythonEnv('python3') {
                    sh 'pytest test_calculator.py'
                }

                echo 'Done Testing..'
            }
        }

        stage('docker build') {
            steps {
                echo 'Building docker image..'
                // sh '/usr/local/bin/docker build --tag flask-calc .'
                script{
                    dockerImage = docker.build(registry + ":latest")
                }
                echo 'Done Building docker image..'
            }
        }

        stage('Push Image to docker hub'){
            steps{
                echo 'Pushing image to docker hub..'
                // sh '/usr/local/bin/docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}'
                // sh '/usr/local/bin/docker tag flask-calc ${DOCKER_USER}/flask-calc'
                // sh '/usr/local/bin/docker push ${DOCKER_USER}/flask-calc'

                script{
                    docker.withRegistry('', credentialID) {
                        dockerImage.push()
                    }
                }
                echo 'Done Pushing image to docker hub..'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying locally..'

                withPythonEnv('python3') {
                    sh 'ansible-playbook playbook.yml'
                }

                echo 'Done Deploying.. your app is running on http://localhost:5000'
            }
        }

        // stage('Remove all images and containers') {
        //     steps {
        //         sh '/usr/local/bin/docker rmi -f $(docker images -aq)' 
        //         sh '/usr/local/bin/docker rm -vf $(docker ps -aq)'
        //     }
        // }
    }
}
