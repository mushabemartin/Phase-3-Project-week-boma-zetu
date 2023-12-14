from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    
    commercial_properties = relationship('CommercialProperty', backref='agent')
    residential_properties = relationship('ResidentialProperty', backref='agent')
    
    def __repr__(self):
        return f'Agent - First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}'

class CommercialProperty(Base):
    __tablename__ = 'commercial_properties'
    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    address = Column(String)
    city = Column(String)
    area = Column(String) # estate or neighborhood
    type = Column(String)
    grade = Column(String)
    price_per_sqf = Column(Integer)
    agent_id = Column(String, ForeignKey('agents.id'))
    
    def __repr__(self):
        return f'Commercial Property - Name: {self.name}, Address: ({self.address}), Type: {self.type}, City: {self.city}, Area: {self.area} Agent: {self.agent_id}'

class ResidentialProperty(Base):
    __tablename__ = 'residential_properties'
    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    address = Column(String)
    city = Column(String)
    area = Column(String) # estate or neighborhood
    type = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    floor_space_sqf = Column(Integer)
    agent_id = Column(String, ForeignKey('agents.id'))
    
    def __repr__(self):
        return f'Residential Property - Name: {self.name}, Address: ({self.address}), Type: {self.type}, City: {self.city}, Area: {self.area} Agent: {self.agent_id}'