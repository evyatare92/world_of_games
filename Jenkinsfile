pipeline{
    agent any
    stages{
        stage("Checkout"){
			steps{
				withCredentials([usernamePassword(credentialsId: 'docker-hub',usernameVariable: 'DOCKERHUB_USER',passwordVariable: 'DOCKERHUB_PASSWORD')]){
					sh script: "docker login -u  ${DOCKERHUB_USER} -p ${DOCKERHUB_PASSWORD}"
				}
			}
        }
		stage("Build and Run"){
			steps{
				sh script: "docker-compose up -d"
			}
		}
        stage("Test"){
			steps{
				script{
					def result = sh script: 'python /tests/e2e.py'
					if(result == -1){
						error "invalid score"
					}
				}
			}
        }
        stage("Finalize"){
			steps{
				sh script: 'docker-compose push'
			}
        }
    }
}