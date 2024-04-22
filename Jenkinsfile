pipeline {
    agent {label 'python && kubectl'}

    stages {
        stage('Get code'){
            steps {
                checkout scmGit(
                    branches: [[name: 'master']],
                    userRemoteConfigs: [[url: 'https://github.com/AlexandraFedotova/RPS_game.git']])
            }
        }
        stage('Test') {
            try {
                echo "Test stage"
                sh 'pytest tests/'
            }
            finally {
                echo "Tests done"
            }
        }
        stage('Build image') {
            steps {
                echo "Build stage"
                sh 'docker build --tag alexandrafedotova/rps_game_test:latest .'
            }
        }
        stage('Push image') {
            environment {
                DockerUser = credentials('DockerCreds')
            }
            steps {
                echo "Push stage"
                sh 'docker login -u $DockerUser_USR -p $DockerUser_PSW'
                sh 'docker push alexandrafedotova/rps_game_test:latest'
                sh 'docker logout'
            }
        }
        stage('Deploy new app version') {
            steps {
                echo "Deploy stage"
                withKubeConfig([credentialsId: 'KubeConfig', serverUrl: 'https://158.160.71.172']) {
                    sh 'kubectl set image deployment/rps-game-deployment rps-game=alexandrafedotova/rps_game_test:latest --record'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}


