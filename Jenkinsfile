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
        withDockerRegistry([ credentialsId: "eddie75/!#75CRghb18up@", url: "https://hub.docker.com/" ]) {
          sh 'docker push eddie75/blog:latest'
        }
      }
    }
  }
}