from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///db/database.db",pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()