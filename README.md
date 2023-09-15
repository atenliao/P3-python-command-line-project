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


## Using the worker database App
In the github.com, fork the project, and then use git clone to clone the project

```shell
git clone git@github.com:username/P3-python-command-line-project.git
```
## Install packages
please use command "python3.8 -m pipenv install" to install dependant packages such as alembic, sqlalchemy, faker, numpy, prettycli, simple-term-menu, and pyfiglet

```shell
python3.8 -m pipenv install alembic sqlalchemy==1.4.41 faker ipdb numpy prettycli simple-term-menu pyfiglet
```
## generate database
Generate database in pipenv shell envirmont
```shell
python3.8 -m pipenv shell
cd lib
alembic revision --autogenerate -m "generate database"
alembic run head
python3 seed.py
```
## Run project
To run the Worker Database Cli project, you need to run cli.py with python3
```shell
python3 cli.py
```
## Main Menu
There are four options you can choose in the welcome page
- Yes (if you are a new worker)
- No (if you are not a new worker)
- Exit 
- Debug (go to ipdb debug envirmont)
### create new worker in database
You need to choose Yes if you are new worker and then follow the prompt to input your infomation.
The new worker will be ask to input lastname, firstname, gender, and shift. then, the new worker record will be created and automatically generate Employee ID and worker login, be assigned role and department.\
After the new worker being generated, you wil be shown a <b>Woker Options Menu</b>

### Worker record exist in database
If your recored of worker is in database, you can choose 'NO' in main menu. Then, input your login \
the worker login is worker <font color="green">lastname + 4 characters of firstname</font>. If the firstname len is less then 4, you input <font color="green"> lastname + firstname</font> to enter <b>Worker Options Menu</b>, and choose option for showing worker information. <font color='red'><b>The login is case sensitive</b></font>. Thus, please enter your worker login correctly.

### In Worker Options Menu
In the Worker Options Menu, you can choose any option to show worker info, department, roles, edit worker ino, or delete worker.
- Show worker Info
- Show worker Department
- Show worker roles
- Edit worker Info
- Delete worker
- Exit

### Edit Worker Info
Yon can change any info of current worker if choose
- Lastname 
- Firstname 
- Gender 
- Shift 
- Exit

### Exit the Command-line
You can Exit the command line from choosing Exit in menu or press ctrl+c; then you will exit the program.

### video of the Project
[work database](https://www.youtube.com/watch?v=C6c0L_CBqTQ)