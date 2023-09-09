from sqlalchemy import Column, String, Integer, create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from Session import session
import random
from base import Base
class Department(Base):
    __tablename__ = "department"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(5),nullable=False)
    city = Column(String, nullable=False)
    
    worker = relationship("Worker",backref="department")
    def __repr__(self):
        return "<department " \
            + f"name={self.name}, " \
            + f"city={self.city}, " \
            + ">"



    @classmethod
    def setDepartments(self):
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

        departments=[]
        for i in Departments_dic:
            department = Department(
                name = i.get("name"),
                city = i.get("city"),
            )
            
            session.add(department)
            session.commit()
            departments.append(department)
        # print(departments)
        return departments
    
