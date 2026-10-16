
pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        JAVA_HOME = 'C:\\Program Files\\Microsoft\\jdk-17.0.20.101-hotspot'
        SPARK_HOME = ''
        PYSPARK_PYTHON = 'python'
        PYSPARK_DRIVER_PYTHON = 'python'
        SPARK_LOCAL_IP = '127.0.0.1'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub.'
            }
        }

        stage('Check Environment') {
            steps {
                bat '''
                    @echo on
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"

                    echo ==== PYTHON ====
                    py -3.11 --version

                    echo ==== PYSPARK ====
                    py -3.11 -c "import pyspark; print('Version:', pyspark.__version__); print('Location:', pyspark.__file__)"

                    echo ==== JAVA ====
                    echo JAVA_HOME=%JAVA_HOME%
                    where java
                    java -version

                    echo ==== SPARK CONFIGURATION ====
                    echo SPARK_HOME=%SPARK_HOME%
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    py -3.11 -m pip install pyspark==3.5.6
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Test Spark') {
            steps {
                bat '''
                    @echo on
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"
                    set "SPARK_HOME="
                    set "PYSPARK_SUBMIT_ARGS=--master local[1] pyspark-shell"

                    py -3.11 -c "from pyspark.sql import SparkSession; s=SparkSession.builder.appName('JenkinsSparkTest').getOrCreate(); print('SUCCESS: Spark version:', s.version); s.stop()"

                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Run ETL Pipeline') {
            steps {
                bat '''
                    @echo on
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"
                    set "SPARK_HOME="
                    set "PYSPARK_SUBMIT_ARGS=--master local[1] pyspark-shell"

                    py -3.11 main.py

                    if errorlevel 1 exit /b 1
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Spark test and ETL pipeline completed.'
        }
        failure {
            echo 'FAILED: Check the first error in Console Output.'
        }
    }
}
