pipeline{
    agent any
    stages{
        stage("Checkout"){
			// This step should not normally be used in your script. Consult the inline help for details.
			withDockerRegistry(credentialsId: '491a0346-556e-4c01-9aba-4ca3a502d21f', url: 'https://hub.docker.com/repository/docker/evyatare92/world-of-games') {
				// some block
			}
        }
    }
}