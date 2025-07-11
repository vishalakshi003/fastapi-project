from ..config.database import Base
from sqlalchemy import String,Integer,Boolean,Column,DateTime,UniqueConstraint,ForeignKey,JSON,ARRAY
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
    __table_args__=(UniqueConstraint("email","mobile_number",name="unique_users")),
    profile=relationship("UserPersonalProfile",back_populates="users", uselist=False)
    role_mapping=relationship("Rolemapping",back_populates="user")
    

class UserPersonalProfile(Base):
    __tablename__ = "user_personal_profile"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("custom_user.id"), unique=True, nullable=False)
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    profilephoto = Column(JSON, default=dict,nullable=True)
    hobbies = Column(ARRAY(String), default=[])
    address_info = Column(JSON, default=dict) 
    created_at=Column(DateTime,server_default=func.now(),nullable=False)
    created_by=Column(String)
    modified_at=Column(DateTime,server_default=func.now(),onupdate=func.now(),nullable=False)
    modified_by=Column(String) 
    is_active=Column(Boolean,default=True)   

    users=relationship("CustomUser",back_populates="profile")
