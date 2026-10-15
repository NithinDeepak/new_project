
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
            }
        }

        stage('Run ETL Pipeline') {
            steps {
                bat 'python main.py'
            }
        }

        stage('Test Pipeline') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'ETL pipeline completed successfully!'
        }

        failure {
            echo 'ETL pipeline failed. Check the console output.'
        }
    }
}
