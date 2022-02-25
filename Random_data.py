import random
import csv

from numpy import PINF

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']
last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(1,101):
    f_name = random.choice(first_names)
    l_name = random.choice(last_names)
    
    phone = f'{random.randint(100,999)}-555-{random.randint(5000,9999)}'
    streer_num = random.randint(100,999)
    
    street_name = random.choice(street_names)
    city = random.choice(fake_cities)
    
    state = random.choice(states)
    zipcode = random.randint(1000,9999)
    address = f'{streer_num} {street_name} {city} {state} {zipcode}'
    
    email = f_name.lower() + l_name.lower() + "@fakeemail.com"
    
    
    to_csv_file = f_name+","+l_name+","+phone+","+address+","+email
    print(to_csv_file)
    
    # with open("DummyData.csv","w",encoding='UTF-8') as f:
    #     writer = csv.writer(f)        
    #     writer.writerow(to_csv_file)
#print("first_name"+","+"last_name"+","+"phone"+","+"address"+","+"email")
    
    
    
    
    
