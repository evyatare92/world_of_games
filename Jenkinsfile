pipeline{
    agent any
    stages{
        stage("Checkout, Build and Run"){
			withDockerRegistry(credentialsId: '491a0346-556e-4c01-9aba-4ca3a502d21f', url: 'https://hub.docker.com/repository/docker/evyatare92/world-of-games') {
				step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: false])
			}
        }
        stage("Test"){
            script{
                def result = sh script: 'python /tests/e2e.py'
                if(result == -1){
                    error "invalid score"
                }
            }
        }
        stage("Finalize"){
            step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StopAllServices'], useCustomDockerComposeFile: false])
            sh script: 'docker-compose push'
        }
    }
}