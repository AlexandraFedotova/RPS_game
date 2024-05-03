def app
pipeline {
    agent {label 'python'}

    parameters {
        string(name: 'docker_username', defaultValue: 'alexandrafedotova', description: 'Username for DockerHub')
        string(name: 'app_name', defaultValue: 'rps_game', description: 'Docker image name')
        string(name: 'branch', defaultValue: 'master', description: 'Project branch name')
        string(name: 'repo_url', defaultValue: 'https://github.com/AlexandraFedotova/RPS_game.git', description: 'Git repository url')
        string(name: 'k8s_namespace', defaultValue: 'rps-game-develop', description: 'k8s namespaces for resource creation')
    }

    stages {
        stage('Get source code'){
            steps {
                checkout scmGit(branches: [[name: "${branch}"]], userRemoteConfigs: [[url: "${repo_url}"]])
            }
        }
        stage('Build image') {
            steps {
                echo "Build app image: ${docker_username}/${app_name}:${env.BUILD_TAG}"
                script {
                    app = docker.build("${docker_username}/${app_name}:${env.BUILD_TAG}")
                }
            }
        }
        stage('Run tests and SAST') {
            steps {
                withPythonEnv('python3'){
                    // Install tests requirements
                    sh 'pip install -r requirements-tests.txt'
                    // Run pytest
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh 'pytest --cov-fail-under=70 --cov=game --cov-report term-missing tests'
                    }
                    // Run pylint
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh 'pylint --fail-under 7 --fail-on E --output-format json2 game'
                    }
                }
            }
        }
        stage('Push image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'DockerCreds') {
                        app.push()
                        app.push('latest')
                    }
                }
            }
        }
        stage('Deploy app') {
            steps {
                withKubeConfig([credentialsId: 'KubeConfig', namespace: "${k8s_namespace}"]) {
                    sh 'kubectl cluster-info'
                    sh 'kubectl get services -A'
                    sh 'kubectl apply -f k8s/game-service.yaml -f k8s/game-deployment.yaml --record'
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


