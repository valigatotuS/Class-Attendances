# Database Management: Project
Author: Valentin Quevy
Created: 09/12/2021

## Summary:
The purpose of this project is to learn developping simple 
database driven web-sites using python [flask], html & css.

## Description
[project description and requiremnts...]

## API
For the website we will extensively use python and python's modules for the API.

## Database
We are using the python module "sqlalchemy" for the database managament part of this project.
This module will be used for creating the tables and querying it.
The database will be stored in an sqlite-file.

### Database-design
![ER_pic](app/database/ER_diagram.png)

## Folder Structure
    .
    ├── app
    │   ├── classes
    │   ├── courses
    │   ├── database
    │   ├── home
    │   ├── __init__.py
    │   ├── login
    │   ├── static
    │   └── templates
    ├── config.py
    ├── Makefile
    ├── notebook.ipynb
    ├── README.md
    └── run.py

## Deploy

1. open terminal and enter following commands (bash)
2. . .venv/bin/activate
3. export FLASK_APP=run.py
4. flask run
