from faker import Faker
import random
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Session import session
from models import Worker, Role, Workerrole
from Department import Department

myDepartment = Department()

if __name__ == '__main__':

        session.query(Worker).delete()
        session.query(Role).delete()
        session.query(Department).delete()
        session.query(Workerrole).delete()

        fake = Faker()
        Gender = ['Female', 'Male']
        Shift = ['7:30am-6:00pm', '7:30am-12:30pm', '1:00pm-6:00pm', '6:30pm-5:00am', '6:30pm-11:30pm','0:00am-5:00am']
        
        departments =myDepartment.setDepartments()
        
        workers = []
        rolename = ['Pack Flow', 'Picking','Pack Single', 'Customer Return', 'Waterspider','Sort Flow','Rebin','Ship Dock', 'Problem solve']
        for i in range(50):
            gender= np.random.choice(Gender, p=[0.5, 0.5]),
            lastname = fake.last_name_male() if gender == 'Male' else fake.last_name_female()
            firstname = fake.first_name_male() if gender == 'Male' else fake.first_name_female()
            department =  random.choice(departments)
            worker = Worker(
                lastname = lastname,
                firstname= firstname,
                gender= gender[0],
                shift = random.choice(Shift),
                login = lastname + firstname[0:4] ,
                Employee_ID= random.randint(10000,50000),
                department_id = department.id
            )
            
            session.add(worker)
            session.commit()
            workers.append(worker)

        roles=[]
        
        for i in range(len(rolename)):
            role = Role(
                name = rolename[i],
                level = random.randint(0,10)
            )
            session.add(role)
            session.commit()
            roles.append(role)
        
        for worker in workers:
            for i in range(random.randint(1,4)):
                role = random.choice(roles)
                if role not in worker.roles:
                    worker.roles.append(role)
                    session.add(worker)
                    session.commit()
            
       
    