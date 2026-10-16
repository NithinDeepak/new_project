
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Jenkins has checked out the GitHub repository.'
            }
        }

        stage('2. Check Environment') {
            steps {
                bat '''
                    @echo off
                    set "JAVA_HOME=C:\\Program Files\\Microsoft\\jdk-17.0.20.101-hotspot"
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"

                    echo ===== Python Version =====
                    py -3.11 --version
                    if errorlevel 1 exit /b 1

                    echo ===== Java Version =====
                    java -version
                    if errorlevel 1 exit /b 1

                    echo ===== PySpark Version =====
                    py -3.11 -m pip show pyspark
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('3. Install Dependencies') {
            steps {
                bat '''
                    @echo off
                    py -3.11 -m pip install pyspark==3.5.6
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('4. Run PySpark Pipeline') {
            steps {
                bat '''
                    @echo off
                    set "JAVA_HOME=C:\\Program Files\\Microsoft\\jdk-17.0.20.101-hotspot"
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"

                    py -3.11 main.py
                    if errorlevel 1 exit /b 1
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: PySpark ETL pipeline completed.'
        }

        failure {
            echo 'FAILURE: Check the stage and error in Console Output.'
        }

        always {
            echo 'Jenkins pipeline execution finished.'
        }
    }
}
