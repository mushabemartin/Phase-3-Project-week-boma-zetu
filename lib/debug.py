# testing
from database.db import session
from model.models import Agent, ResidentialProperty, CommercialProperty

print('AGENTS\n')
print(*session.query(Agent).all(), sep='\n')

print('RESIDENCES\n')
print(*session.query(ResidentialProperty).all(), sep='\n')

print('COMMERCIAL\n')
print(*session.query(CommercialProperty).all(), sep='\n')

agent = session.query(Agent).filter(Agent.id==2).first()
property = session.query(ResidentialProperty).filter(ResidentialProperty.id==2).first()

print('', *agent.residential_properties, '', sep='\n\n')
print([city[0] for city in session.query(ResidentialProperty.area).distinct()])
print(agent.residential_properties)