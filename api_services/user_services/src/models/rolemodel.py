from ..config.database import Base
from sqlalchemy import String,Integer,Boolean,Column,ForeignKey
from sqlalchemy.orm import relationship

class Rolemaster(Base):
    __tablename__='role_master'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    rolemapping=relationship("Rolemapping",back_populates="role")

class Rolemapping(Base):
    __tablename__='role_mapping'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('custom_user.id'),unique=True,nullable=False)
    role_id=Column(Integer,ForeignKey('role_master.id'),unique=True,nullable=False)

    user=relationship("CustomUser",back_populates="role_mapping")
    role=relationship("Rolemaster",back_populates="rolemapping")
