pipeline {

    agent any

    stages {

        stage("build") {
            
            steps {

                echo "Building the application..."
                sh '''echo "creating image.."
                    sudo docker build -t myimage .
                    echo "image build"'''

            }

        }

        stage("test") {
            
            steps {

                echo "Testing the application..."


            }
            
        }

        stage("deploy") {
            
            steps {

                echo "Deploying the app"
                sh '''echo "removing container if present"
                    sudo docker rm -f testcontainer
                    echo "container deleted"
                    echo "creating new container"
                    sudo docker run -d --name testcontainer -p 81:80 myimage
                    echo "container created"
                    echo "check your project ar http://http://ec2-13-233-117-88.ap-south-1.compute.amazonaws.com/"
                '''

            }
            
        }
    }

    post {
        always {
            echo "sending an email.."
        }
        success {
            echo "success..."
        }
        failure {
            echo "failure..."
        }
    }
}