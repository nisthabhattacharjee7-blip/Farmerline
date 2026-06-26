from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class FarmerVisit(Base):
    __tablename__ = "farmer_visits"

    id = Column(Integer, primary_key=True)
    worker_name = Column(String)        # field worker who logged it
    farmer_name = Column(String)        # farmer visited
    village = Column(String)            # village name
    crop = Column(String)               # crop being grown
    issue = Column(Text)                # problem observed
    action_taken = Column(Text)         # what the worker did
    logged_at = Column(DateTime, default=datetime.utcnow)

class FieldWorker(Base):
    __tablename__ = "field_workers"

    id = Column(Integer, primary_key=True)
    slack_user_id = Column(String, unique=True)   # Slack user ID
    name = Column(String)
    region = Column(String)                        # assigned area
    joined_at = Column(DateTime, default=datetime.utcnow)

# Database setup
engine = create_engine("sqlite:///farmerline.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
