
Author: Shashwati Diware (sdiware@iu.edu)

1. Folder Structure:

Assignment3/
	- server/
   		- Dockerfile.server
   		- server.py
	- client/
   		- Dockerfile.client
   		- client.py
	-docker-compose.yml

2. Build and Start Containers:
	Navigate to the Assigment3/ directory in the Ubuntu terminal.
    Build and start the Docker containers using below commands.

	docker-compose build
	docker-compose up -d

3. Execute Scripts in Containers:
   Execute scripts within the server and client containers.

   docker-compose exec server sh
   docker-compose exec client sh

4. To check if everything is working and verify logs:

   docker-compose ps
   docker-compose logs client

All the packages to be downloaded are mentioned in docker file.



