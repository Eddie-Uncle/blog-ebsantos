pipeline {
  agent { label 'docker' }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  triggers {
    cron('@daily')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -f "Dockerfile" -t eddie75/blog:latest .'
      }
    }
    stage('Publish') {
      when {
        branch 'master'
      }
      steps {
        withDockerRegistry([ credentialsId: "6544de7e-17a4-4576-9b9b-e86bc1e4f903", url: "" ]) {
          sh 'docker push eddie75/blog:latest'
        }
      }
    }
  }
}