pipeline{
    agent any
    stages{
        stage("Checkout, Build and Run"){
			steps{
				withDockerRegistry(credentialsId: '385920f9-ab69-4f00-a422-d9065c136a43', url: 'https://hub.docker.com/repository/docker/evyatare92/world-of-games') {
					step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: false])
				}
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
				step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StopAllServices'], useCustomDockerComposeFile: false])
				sh script: 'docker-compose push'
			}
        }
    }
}