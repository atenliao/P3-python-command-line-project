from sqlalchemy import Column, String, Integer, create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from Department import Department
from Session import session
from base import Base
# engine = create_engine("sqlite:///db/database.db")
# Session = sessionmaker(bind=engine)
# session = Session()



class Workerrole(Base):
    __tablename__ = "workerrole"

    id = Column(Integer, primary_key=True)
    workers_id = Column(Integer, ForeignKey("worker.id"),nullable=True)
    roles_id = Column(Integer, ForeignKey("role.id"),nullable=True)
    
    def __repr__(self):
        return "<workerrole " \
            + f"id={self.id}, " \
            + f"workers_id={self.workers_id}, " \
            + f"roles_id={self.roles_id}, " \
            + ">"


class Worker(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True)
    lastname = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    gender = Column(String(40), nullable=False)
    shift = Column(String(255), nullable= False)
    login = Column(String(100), nullable= False)
    Employee_ID = Column(Integer, nullable= False, unique=True)
    department_id = Column(Integer, ForeignKey("department.id"))
    roles = relationship("Role", secondary= "workerrole", overlaps="roles")
    

    @classmethod
    def create(cls, **kwargs):
        worker = Worker(**kwargs)
        print(worker)
        session.add(worker)
        session.commit()
        return worker

    @classmethod
    def find_or_create_by(cls,login):
        # Query the db for a worker by login
        worker = session.query(Worker).filter(Worker.login.like(login)).first()
        if worker:
            return worker
        else:
            worker = Worker(login = login)
        
        # import ipdb; ipdb.set_trace()

    def __repr__(self):
        return "<Worker " \
            + f"login={self.login}, " \
            + f"lastname={self.lastname}, " \
            + f"firstname={self.firstname}, " \
            + f"gender={self.gender}, " \
            + f"shift={self.shift}, " \
            + f"Employee_ID={self.Employee_ID}, " \
            + f"Department_id={self.department_id} " \
            + ">" \
            + "\n\n"


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False)
    level = Column(Integer, nullable= False)

    workers = relationship("Worker", secondary="workerrole", overlaps="roles")
    def __repr__(self):
        return "<Role " \
            + f"id={self.id}, " \
            + f"name={self.name}, " \
            + f"level={self.level}, " \
            + ">"


