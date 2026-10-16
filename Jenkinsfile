
pipeline {
    agent any

    environment {
        JAVA_HOME = 'C:\\Program Files\\Microsoft\\jdk-17.0.20.101-hotspot'
        SPARK_HOME = ''
        PYSPARK_PYTHON = 'python'
        PYSPARK_DRIVER_PYTHON = 'python'
        SPARK_LOCAL_IP = '127.0.0.1'
    }

    stages {
        stage('Check Spark Configuration') {
            steps {
                bat '''
                    @echo on
                    echo ==== JAVA ====
                    echo JAVA_HOME=%JAVA_HOME%
                    where java
                    java -version

                    echo ==== SPARK HOME ====
                    echo SPARK_HOME=%SPARK_HOME%

                    echo ==== PYSPARK ====
                    py -3.11 -c "import pyspark; print(pyspark.__version__); print(pyspark.__file__)"
                '''
            }
        }

        stage('Test SparkSession') {
            steps {
                bat '''
                    @echo on
                    set "PATH=%JAVA_HOME%\\bin;%PATH%"
                    set "SPARK_HOME="
                    set "PYSPARK_SUBMIT_ARGS=--master local[1] pyspark-shell"
                    py -3.11 -c "from pyspark.sql import SparkSession; s=SparkSession.builder.appName('JenkinsSparkTest').getOrCreate(); print('SUCCESS: Spark version:',s.version); s.stop()"
                    if errorlevel 1 exit /b 1
                '''
            }
        }
    }
}
