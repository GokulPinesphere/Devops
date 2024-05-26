pipeline{
    agent any
    environment {
        KUBECONFIG = '/home/ubuntu/.kube/config'
    }
    stages{
        stage("checkout from git"){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/GokulPinesphere/Devops.git']])
            }
        }
        stage("Creating image"){
            steps{
                sh 'docker build -t gokulsrepo/myfirstdocker .'
            }
        }
        stage("Pushing to dockerhub"){
            steps{
                script{
                    withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerpwd')]) {
                    sh 'docker login -u gokulsrepo -p ${dockerpwd}'
                    }
                    sh 'docker push gokulsrepo/myfirstdocker'
                }
            }
        }
        stage("Pushing to K8's"){
            steps{
                script{
                    kubernetesDeploy (configs: 'deploymentservice.yaml', kubeconfigId: 'Kubeconfig')
                }
            }
        }
    }
}
