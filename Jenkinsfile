pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'cd source; ls | xargs "python"';
                bat 'echo lol'
            }
        }
        stage('Test') {
            steps {
                bat 'cd CITools; autopep.bat';
                bat 'grok_for_sensitive_stuff.bat';

            }
        }
        stage('Deploy') {
            steps {
                echo "deploying"
            }
        }
    }
}