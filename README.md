# Database Management: Project
Author: valigatotuS
Created: 09/12/2021

## Context
The purpose of this project is to learn developping simple 
database driven web-sites using python [flask], html & css.

## Description
The website must serve to log the attendances at school. 
The users involved are: students, teachers & administrators.

## Application 

### Requirements
- Users  are e.g. students who log in and join classes
- Teachers can organize classes for a course 
- Administartors can create new courses and assign teachers and users to
these courses

### Database
We are using the python module "sqlalchemy" for the database managament part of this project.
This module will be used for creating the tables and querying it.
The database will be stored in an sqlite-file.

#### Database-design
![ER_pic](app/database/ER_diagram.png)

### API
[...]

### Folder Structure
    .
    ├── app
    │   ├── classes             => blueprint: classes       (sub-app)
    │   ├── courses             => blueprint: courses       (sub-app)
    │   ├── database            => database & management    (db, queries, models:tables)
    │   ├── home                => blueprint: home          (sub-app)
    │   ├── __init__.py         => app initialiser
    │   ├── login               => blueprint: login         (sub-app)
    │   ├── static              => css & js assets
    │   └── templates           => html templates
    ├── config.py               => app configuration settings
    ├── Makefile                => executing terminal commands
    ├── notebook.ipynb          => python playground
    ├── README.md
    └── run.py                  => pyfile running the application

### Deploy
1. open terminal
2. install the needed requirements
3. $ make run

## Credits
This project is part of the course "Database Management" at the VUB for 3BA Industrial Sciences ELO-ICT students given by the instructors Ann Braeken & Tom Godden.
### Sources
![Miguel Grinberg's Flask tuto](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
![Hackersandlackers Flask tuto](https://hackersandslackers.com/series/build-flask-apps/)
