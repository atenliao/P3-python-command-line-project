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
    - Table: Department (Association table)
        - id
        - workers_id
        - roles_id
        - name
        - City
    - Talbe: (Many-to-Many) roles
        - id
        - roles_type
        - roles_name
        - level
- Object Relationship
    - worker can be differenct roles
    - department has many roles
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
    - Single Source of True
    - LIST: workers could have a list of roles
    - Dictionary: Department has set of roles and workers

#### What area I think wil be most challenging
- Deciding how data join table and connect each table


