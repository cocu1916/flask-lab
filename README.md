# flask-lab
 This repo's purpose is to hold all the files necessary to complete the flask lab.  The repo contains a gitignore file, an app.py file, a docker-compose.yml file, a Dockerfile, a make-request.py file and a requirements.txt file.  After completion, this lab sets up a flask app, sends 3 requests, and allows the Flask container to be run via a docker-compose command. 

### With `docker-compose` run Flask container
Build and run:
```bash
docker-compose up
```
### With `docker-compose` execute make-request.py within running container
Build and run:
```bash
docker-compose exec web python make-request.py
```
