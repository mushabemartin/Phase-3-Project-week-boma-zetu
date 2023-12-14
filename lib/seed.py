#!/home/eugene/.local/share/virtualenvs/property-listings-qbpVMiNd/bin python

import random, re

from faker import Faker
from model.models import Agent, ResidentialProperty, CommercialProperty
from database.db import session

fake = Faker()

session.query(Agent).delete()
session.query(ResidentialProperty).delete()
session.query(CommercialProperty).delete()

agents = []
for i in range(25):
    f_name = fake.first_name()
    l_name = fake.last_name()
    agent_email = f'{f_name.lower()}.{l_name.lower()}{random.randint(25,2500)}@example.com'
    
    agent = Agent(
        first_name = f_name,
        last_name = l_name,
        email = agent_email
    )
    
    session.add(agent)
    session.commit()
    agents.append(agent)
    

cities = [fake.city() for i in range(6)]
ar = [fake.city() for i in range(20)]

for i in range(100):
    residence_suffixes = ['Apartments', 'Court', 'Heights', 'Point', 'Suites', 'Place']
    sample_address = fake.address()
    sample_address_name = re.findall(r'\s([A-Z a-z]+),?', sample_address)
    sample_bedrooms = random.randint(1,5)
    sample_city = random.choice(cities)
    
    residence = ResidentialProperty(
        name = sample_address_name[0].strip(),
        address = sample_address,
        city = sample_city,
        area = ar[(((cities.index(sample_city)+1)*3)-random.randint(0,2))],
        type = random.choice(['Apartment', 'Townhouse', 'Bungalow', 'Duplex', 'Condominium']),
        bedrooms = sample_bedrooms,
        bathrooms = sample_bedrooms if sample_bedrooms > 2 else 1,
        floor_space_sqf = random.randint(2000, 8000),
        agent = random.choice(agents)
    )
    
  