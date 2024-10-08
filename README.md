# Project Overview

This project implements a REST API with CRUD (Create, Read, Update, Delete) endpoints for managing **teams** and **people** within those teams. The main components of the API include:

- **Team Object**: Represents a team with a name.
- **Person Object**: Represents an individual with a first name, last name, and email.

The API enables functionalities to assign people to teams and create both teams and individuals. It leverages the **Django REST Framework**, which provides an intuitive front-end interface for interacting with the API.

Additionally, the project includes comprehensive tests for serializers, models, and views related to the user and team applications, ensuring the reliability and correctness of the implemented features.
### List of endpoints
1. ```http://localhost:8001/api/users/``` - for representing list of users and creating a new ones.
2. ```http://localhost:8001/api/users/<int:pk>/``` - for updating and deleting exact user.
3. ```http://localhost:8001/api/teams/``` - for representing list of teams and creating a new ones.
4. ```http://localhost:8001/api/teams/<int:pk>/``` - for updating and deleting exact team.
5. ```http://localhost:8001/admin/``` - where you can login as superuser for administration actions. 
### Installing using GitHub
Copy the repo
   ```bash
   git clone https://github.com/BileichukIvan/drf_test.git
   cd drf_test
   ```
Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
Set all necessary environment variables
   ```bash
   set DB_HOST=<your db hostname>
   set DB_NAME=<your db name>
   set DB_USER=<your db username>
   set DB_PASSWORD=<your db password>
   set POSTGRES_PORT=<your db port>
   set DJANGO_SECRET_KEY=<your django secret key>
   ```
Apply migrations
  ```bash
   python manage.py migrate
   python manage.py runserver
  ```
If you need an admin user you can create it with  
    ```bash
    python manage.py createsuperuser
    ```


### Run with docker

Docker should be installed
Create .env file inside project directory and copy text from .env.template and fill the variables with your own values.

  ```bash
   docker-compose up
  ```
If you need an admin user you can create it by doing this steps:
1. Type ```docker ps``` in your console.
2. Type ```docker exec -it <container_name_or_id> python manage.py createsuperuser``` to run ```createsuperuser``` command inside necessary container 