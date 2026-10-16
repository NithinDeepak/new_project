
pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        JAVA_HOME = 'C:\\Program Files\\Microsoft\\jdk-17.0.20.101-hotspot'
        PYSPARK_PYTHON = 'python'
        PYSPARK_DRIVER_PYTHON = 'python'
        SPARK_LOCAL_IP = '127.0.0.1'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Repository checked out from GitHub.'
            }
        }

        stage('Check Environment') {
            steps {
                bat '''
                    @echo off
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"

                    echo ==== Python ====
                    py -3.11 --version

                    echo ==== Java ====
                    where java
                    java -version

                    echo ==== PySpark ====
                    py -3.11 -m pip show pyspark
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -3.11 -m pip install pyspark==3.5.6'
            }
        }
        stage('Diagnose Spark Environment') {
            steps {
                bat '''
                    @echo off
                    echo ==== Python version ====
                    py -3.11 --version

                    echo ==== PySpark version and location ====
                    py -3.11 -c "import pyspark; print(pyspark.__version__); print(pyspark.__file__)"

                    echo ==== Java location ====
                    where java
                    java -version

                    echo ==== Spark environment variables ====
                    echo SPARK_HOME=%SPARK_HOME%
                    echo PYTHONPATH=%PYTHONPATH%
                    echo JAVA_HOME=%JAVA_HOME%
                '''
            }
        }



        stage('Run PySpark Pipeline') {
            steps {
                bat '''
                    @echo off
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"
                    set "PYSPARK_PYTHON=python"
                    set "PYSPARK_DRIVER_PYTHON=python"
                    set "PYSPARK_SUBMIT_ARGS=--conf spark.driver.extraJavaOptions=--add-exports=java.base/sun.nio.ch=ALL-UNNAMED pyspark-shell"

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
            echo 'FAILURE: Check the console output for the Spark error.'
        }
    }
}
 