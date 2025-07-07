from ..config.database import Base
from sqlalchemy import String,Integer,Boolean,Column,DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
class CustomUser(Base):
    __tablename__='custom_user'
    id = Column(Integer, primary_key=True)
    name=Column(String)
    email=Column(String,unique=True,nullable=False)
    mobile_number=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=True) 
    created_at = Column(DateTime,server_default=func.now(),nullable=False)
    modified_at = Column(DateTime,server_default=func.now(),onupdate=func.now(),nullable=False)
    is_active=Column(Boolean,default=True)
    role_mapping=relationship("Rolemapping",back_populates="user")
    