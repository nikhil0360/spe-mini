pipeline {
    agent any

    environment {
        registry = "nikhil0360/flask-calc"
        credentialID = "dockerhub"
        dockerImage = ""
    }

    stages {
        stage('Installation') {
            steps {
                echo 'Installing dependencies..'
                echo 'Installing requirements..'
                withPythonEnv('python3') {
                    sh 'pip3 install --upgrade pip'
                    sh 'pip3 install -r requirements.txt'
                }
                echo 'Done Installing dependencies..'
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
                script{
                    dockerImage = docker.build(registry + ":latest")
                }
                echo 'Done Building docker image..'
            }
        }

        stage('Push Image to docker hub'){
            steps{
                echo 'Pushing image to docker hub..'
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

                echo 'Done Deploying'
				echo 'your app is running on http://localhost:5000'
            }
        }
    }
}
