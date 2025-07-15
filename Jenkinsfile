pipeline {
  agent any

  environment {
    BROKER_USER     = credentials('osb-user')
    BROKER_PASSWORD = credentials('osb-password')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t osb-dummy .'
      }
    }

    stage('Stop & Remove Old Container') {
      steps {
        sh '''
          docker stop osb-dummy || true
          docker rm osb-dummy || true
        '''
      }
    }

    stage('Run New Container') {
      steps {
        sh '''
          docker run -d \
            -e BROKER_USER=$BROKER_USER \
            -e BROKER_PASSWORD=$BROKER_PASSWORD \
            -e PORT=5000 \
            -p 5000:5000 \
            --name osb-dummy osb-dummy
        '''
      }
    }
  }
}
