# check webhook3
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
            stage('Build and Push Docker Image') {
            steps {
                script {
                    def imageTag = "yossig3/list_active_ec2:${env.BUILD_NUMBER}"
                    def dockerImage = docker.build(imageTag, '-f Dockerfile .')
                    docker.withRegistry('https://registry.hub.docker.com', 'efc3c6f8-5e82-49e1-95e3-8a4754f11935') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Build successful - image pushed to Docker Hub'
        }
        failure {
            echo 'Build failed'
        }
    }
}
