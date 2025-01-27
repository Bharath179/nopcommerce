pipeline {
    agent any  // Use any available Jenkins executor

    stages {
        // 1. Checkout code from GitHub repository
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']],
                                 extensions: [],
                                 userRemoteConfigs: [[url: 'https://github.com/Bharath179/nopcommerce.git']])
            }
        }

        // 2. Build (optional, if you want to add build commands here)
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add your build steps here if needed
                // For example: sh 'mvn clean install' or other build commands
            }
        }

        // 3. Run Tests
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run tests using pytest
                sh 'pytest tests/'  // This assumes your tests are in the 'tests/' directory
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Optional: clean up resources, such as temporary files
        }

        success {
            echo 'Build and tests passed!'
        }

        failure {
            echo 'Build or tests failed, check the logs for errors.'
        }
    }
}
