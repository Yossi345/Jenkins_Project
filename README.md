This is a CI/CD automation process which is monitoring the EC2 on AWS by displaying an output that is regularly updated about our active EC2.

•	This repository contains a jenkinsfile wich is configured by github webhook to get triggered anytime there is a change in the content of this repository.
•	Whenever someone commit a change in one of the repository’s file, github triggers Jenkins and Jenkins start building the triggered pipeline.
•	The trigger pipeline is configured clone the git repository and to build a docker image using the dockerfile include in the repository and push it to DockerHub with a tag added by the env.BUILD_NUMBER variable
•	The run.py file is the python script that is running when you run the image.
•	The script monitor your EC2 on AWS account using boto3 in order to be notified of active EC2 on the account
•	The Jenkinsfile-Cron file is the second pipeline which is trigger to run every 5 minutes in order to check according to the first pipline and according to the image tag  whether the app has changed and there is a need to pull the image from DockerHub and rebuild it or there was no change and no need to rebuild the image.

Requirements:  
•	The docker commands require installation of “Docker plugin” and “Docker Pipeline”
•	When running the Jenkinsfile-Cron there is a need for signature approvals of the above:
o	method groovy.lang.GroovyObject invokeMethod java.lang.String java.lang.Object
o	method hudson.model.ItemGroup getItem java.lang.String
o	method hudson.model.Job getLastSuccessfulBuild
o	method hudson.model.Run getNumber
o	staticMethod jenkins.model.Jenkins getInstance
