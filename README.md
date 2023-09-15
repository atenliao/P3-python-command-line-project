# P3-python-command-line-project
A Python Command Line Project

#### How I will use the concepts I recently learned to meet the project requirements

- Object Oriented Python
    - Class for worker with attributes
    - Class for shit with attributes
    - Class for roles with attributes
- Database Table
    - use SQLaichemy to create and interact with two or more related databased
    - Table: worker
        - ID
        - lastname
        - firstname
        - gender
        - Shift
        - login
        - Employee_ID
        - Department_id
    - Table: Department (Association table)
        - id
        - name
        - City
    - Talbe: (Many-to-Many) roles
        - id
        - roles_name
        - level
- Object Relationship
    - worker can get differenct roles
    - each worker is assigned in a department
    - roles be workers == many to many
- Aggregate and Association Methods
    - CRUD
    - Create 
        - create a list like roles and workers
    - Read
        - Read All
            - Display all workers
            - Display all department
            - Display all roles
        - Read one
            - Display 1 department by worker
    - Update
            - change role to a workers
    - Delete
- Use of Data Structures
    - LIST: workers have a list of roles
    - Dictionary: Department has its name and location city

#### What area I think wil be most challenging
- Deciding how data join table and connect each table


### Using the worker database App
In the github.com, fork the project, and then use git clone to clone the project

```shell
git clone git@github.com:username/P3-python-command-line-project.git
```
### Install packages
please use command "python3.8 -m pipenv install" to install dependant packages such as alembic, sqlalchemy, faker, numpy, prettycli, simple-term-menu, and pyfiglet

```shell
python3.8 -m pipenv install alembic sqlalchemy==1.4.41 faker ipdb numpy prettycli simple-term-menu pyfiglet
```
### generate database
Generate database in pipenv shell envirmont
```shell
python3.8 -m pipenv shell
cd lib
alembic revision --autogenerate -m "generate database"
alembic run head
```