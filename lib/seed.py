#!/home/eugene/.local/share/virtualenvs/property-listings-qbpVMiNd/bin python

import random, re

from faker import Faker
from model.models import Agent, ResidentialProperty, CommercialProperty
from database.db import session

fake = Faker()

