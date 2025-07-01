from src.config.database import Base
from sqlalchemy import String,Integer,Column,DateTime,Boolean,ForeignKey
from sqlalchemy.sql import func

class AssetMaster(Base):
    __tablename__="asset_master"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    created_at = Column(DateTime,server_default=func.now(),nullable=False)
    modified_at = Column(DateTime,server_default=func.now(),onupdate=func.now(),nullable=False)
    is_active=Column(Boolean,default=True)

class AssetAllocation(Base):
    __tablename__="asset_allocation"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,nullable=False)
    asset_id=Column(Integer,ForeignKey('asset_master.id'),nullable=False)
    allocated_status=Column(String,default='active',nullable=True)
    created_at=Column(DateTime,server_default=func.now(),nullable=False)
    created_by=Column(String,nullable=False)
    modified_at=Column(DateTime,server_default=func.now(),onupdate=func.now(),nullable=False)
    modified_by=Column(String,nullable=True) 
    is_active=Column(Boolean,default=True)