pipeline {
    agent any
    stages {
        stage('Initialize') {
            steps {
                cleanWs()
            }
        }
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Yossi345/Jenkins_Project.git'
            }
        }
        stage('build App') {
            steps {
                script {
                    bat "docker --version"
                    // sh "docker build -t list-ec2:lastst"
                    // docker.build('list-ec2:latest')
                }
            }
        }

            }
        }
