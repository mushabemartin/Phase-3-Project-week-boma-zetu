Real Estate CLI - Property Listing App(boma zetu)

The Real Estate CLI is a command-line interface (CLI) application designed to simplify the process of listing and searching for properties across the country. Whether you're a property owner looking to list your real estate or a user in search of the perfect home, this app provides a streamlined solution for managing property listings and accessing property details.
Features

    Property Listing: Users can easily list their properties, providing essential details such as property type, location, and contact information.

    Advanced Filtering: Seamlessly filter through property listings based on categories, location, and other criteria, making it effortless to find the right real estate.

    Detailed Property Information: Users can retrieve comprehensive details for a specific property, including contact information for the property owner or listing agent.

    Owner/Agent Contact Details: Enable users to inquire about a property directly by accessing the contact details of the property owner or listing agent.

Add an Agent:

python app.py add-agent

This command will prompt you to enter details for a new agent.

Add a Residential Property:

python app.py add-residence

This command allows you to add a new residential property. It will prompt you for property details.

Add a Commercial Property:

python app.py add-commercial-property

Similar to the previous command, this allows you to add a new commercial property.

Show All Properties:

python app.py show-all

This command displays all the property listings.

Search by Name:

python app.py search-by-name

This command prompts you to enter a property name and then searches for listings matching that name.

Search by ID:

python app.py search-by-id

This command prompts you to enter a property ID and then searches for a listing with that ID.

Show All Agents:

python app.py show-agents

This command displays a list of all agents.

Show All Cities:

python app.py show-cities

This command displays all cities that have a property listing.

Show All Areas:

python app.py show-areas

This command displays all areas that have a property listing.

Delete a Listing:

python app.py delete-listing

This command prompts you to enter a property type, ID, and agent ID to delete a listing.

Remember to replace python with python3 if that's the command you use in your environment. Additionally, follow the prompts for each command to input the required information.nds to use the app



Setup Requirements

    Visual Studio Code: Installation Guide

    Supported OS / Environments: Compatible with various operating systems, including Windows Subsystem for Linux (WSL).

    Git and GitHub: Installation Guide

    Python (Recommended version 3.10+): Download the Latest Version

    Pipenv: Python virtualenv management tool, Installation Guide

    SQLite: Lightweight relational database management system.

Installation

    Clone or download the code from the repository. Navigate to the directory in the terminal.

    Run pipenv install to install the required packages.

    Run pipenv shell to activate the project environment.

    To run the program and access features, navigate to the lib directory (cd lib), and run python app.py to start the app.

    To populate the database with sample data, run python seed.py in the lib directory.

Language(s)

    Python

Packages

    SQLAlchemy
    Click
    Alembic
    Faker

Authors

    Abright Muchori
    Ian Maboi
    Eric Wachiuri
    Felix Kahuta
    Martin Mushabe
