pipeline {
    agent {label 'python && kubectl'}

    parameters {
        string(name: 'app', defaultValue: '', description: 'Used inside pipeline')
        string(name: 'docker_username', defaultValue: 'alexandrafedotova', description: 'Username for DockerHub')
        string(name: 'docker_reponame', defaultValue: 'private', description: 'DockerHub user repository name')
        string(name: 'app_name', defaultValue: 'rps_game', description: 'Image name')
        string(name: 'branch', defaultValue: 'master', description: 'Branch name for work')
        string(name: 'repo_url', defaultValue: 'https://github.com/AlexandraFedotova/RPS_game.git',
        description: 'Git repository url')
    }

    stages {
        stage('Get code'){
            steps {
                echo "Get code "
                checkout scmGit(branches: [[name: "${branch}"]], userRemoteConfigs: [[url: "${repo_url}"]])
            }
        }
        stage('Build image') {
            steps {
                script {
                    echo "Build stage"
                    def app = docker.build("${docker_username}/${docker_reponame}/${app_name}:${env.BUILD_TAG}")
                }
            }
        }
        stage('Run tests') {
            steps {
                withPythonEnv('python3'){
                    echo "Test stage"
                    sh 'pip install -r requirements-tests.txt'
                    echo "Run tests with coverage report"
                    sh 'pytest --cov-fail-under=70 --cov=game tests'
                    echo "Run pylint"
                    sh 'pylint --fail-under 7 --fail-on E --output-format json2 main.py game'
                }
            }
        }
        stage('Push image') {
            steps {
                script {
                    echo "Push stage"
                    withDockerRegistry(credentialsId: 'DockerCreds') {
                        app.push()
                        app.push('latest')
                    }
                }
            }
        }
        stage('Deploy new app version') {
            steps {
                echo "Deploy stage - passed "
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}


