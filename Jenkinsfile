pipeline {
    agent any
    
    stages {
	
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/archna-chauhan/new_practice.git', branch: 'main'
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'pytest -s -v tests\\test_login_class.py::Test_Class_Login::test_01'
            }
        }
    }
}
