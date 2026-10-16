
pipeline {
    agent any

    stages {
        stage('Verify Jenkins Environment') {
            steps {
                bat '''
                    @echo on
                    echo ==== CONFIRM JENKINSFILE ====
                    echo DIAGNOSTIC VERSION 1

                    echo ==== PYTHON ====
                    py -3.11 --version
                    py -3.11 -c "import pyspark; print('PySpark:', pyspark.__version__); print('Location:', pyspark.__file__)"

                    echo ==== JAVA ====
                    echo JAVA_HOME=%JAVA_HOME%
                    where java
                    java -version

                    echo ==== SPARK VARIABLES ====
                    echo SPARK_HOME=%SPARK_HOME%
                    echo PYTHONPATH=%PYTHONPATH%
                    echo PYSPARK_SUBMIT_ARGS=%PYSPARK_SUBMIT_ARGS%

                    echo ==== SPARK JARS DIRECTORY ====
                    py -3.11 -c "import os,pyspark; p=os.path.join(os.path.dirname(pyspark.__file__),'jars'); print(p); print('Exists:',os.path.isdir(p))"
                '''
            }
        }
    }
}
