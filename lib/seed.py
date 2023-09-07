from faker import Faker
import random
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from Session import session
from models import Worker, Role, Department,Workerrole

if __name__ == '__main__':
        engine = create_engine('sqlite:///db/database.db',pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.query(Worker).delete()
        session.query(Role).delete()
        session.query(Department).delete()
        session.query(Workerrole).delete()

        fake = Faker()
        Gender = ['Female', 'Male']
        Shift = ['7:30am-6:00pm', '7:30am-12:30pm', '1:00pm-6:00pm', '6:30pm-5:00am', '6:30pm-11:30pm','0:00am-5:00am']
        Departments_dic= [
            {
                "name": "OAK7",
                "city": "Neward"
            },
            {
                "name": "OAK4",
                "city": "Fremont"
            },
            {
                "name": "SJC8",
                "city": "Tracy"
            },
            {
                "name":"SCK9",
                "city":"Oakland"
            },
            {
                "name": "EAC2",
                "city": "San Francisco"
            }
            ]
        
        departments = []
        for i in Departments_dic:
            department = Department(
                name = i.get("name"),
                city = i.get("city"),
            )
            session.add(department)
            session.commit()
            departments.append(department)
        workers = []
        rolename = ['Pack Flow', 'Picking','Pack Single', 'Customer Return', 'Waterspider','Sort Flow','Rebin','Ship Dock', 'Problem solve']
        for i in range(50):
            gender= np.random.choice(Gender, p=[0.5, 0.5]),
            lastname = fake.last_name_male() if gender == 'Male' else fake.last_name_female()
            firstname = fake.first_name_male() if gender== 'Male' else fake.first_name_female()
            department = random.choice(departments)
            worker = Worker(
                lastname = lastname,
                firstname= firstname,
                gender= gender[0],
                shift = random.choice(Shift),
                login = lastname + firstname[0:4] ,
                Employee_ID= random.randint(10000,50000),
                department_id = department.id
            )
            # import ipdb; ipdb.set_trace()
            session.add(worker)
            session.commit()

            workers.append(worker)

        roles=[]
        # departments=[]
        for i in range(len(rolename)):
            role = Role(
                name = rolename[i],
                level = random.randint(0,10)
            )
            session.add(role)
            session.commit()
            roles.append(role)
        
            # import ipdb; ipdb.s
        for worker in workers:
            for i in range(random.randint(1,4)):
                role = random.choice(roles)
                # get_department = random.choice(departments)
                if role not in worker.roles:
                    worker.roles.append(role)
                    # worker.departments.append(department)
                    session.add(worker)
                    session.commit()
            
        # for worker in workers:
        #     roles = []
        #     for i in range(random.randint(1,4)):
                
        #         role = Role(
        #             name = random.choice(rolename),
        #             level = random.randint(0,10),
        #         )
        #         if role.name not in worker.roles:
        #         # import ipdb; ipdb.set_trace()
        #             role.workers.append(worker)
        #     session.add(role)
        #     session.commit()
            # session.close()
          

# import ipdb; ipdb.set_trace()
    