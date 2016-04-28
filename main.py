import random
'''from py2neo import Node,Relationship,Graph

graph = Graph("http://localhost:7474/db/data/")
graph.delete_all()

person = open("Data\person.txt")
for line in person:
    line_data = line.split(',')
    graph.create(Node("Person", name=line_data[0], gender=line_data[1], country=line_data[2]))'''

#Fetching, Cleaning, and Storing User Names in a List
fh1 = open("Data/Names.txt", "r")
nameslist = []
for line in fh1:
    cleanline = line.strip()
    nameslist.append(cleanline)

#Getting the AgeList for each User
agelist = []
for i in range(0,250):
    agelist.append(random.randint(15,20))
for i in range(0,500):
    agelist.append(random.randint(21,30))
for i in range(0,200):
    agelist.append(random.randint(31,40))
for i in range(0,50):
    agelist.append(random.randint(41,50))
random.shuffle(agelist)

#Fetching the Gender of every User
genderlist = []
for i in range(0, 1000):
    if random.randint(1,2) == 1:
        genderlist.append('M')
    else:
        genderlist.append('F')

#Getting the Nationality of every User
country = ["US", "JAPAN", "FRANCE", "PORTUGAL", "CHILE", "TAIWAN", "SOUTH KOREA", "ITALY", "UAE",
               "COSTA RICA", "SLOVENIA", "BELGIUM", "SPAIN", "SINGAPORE", "UK", "GERMANY", "AUSTRIA", "CANADA",
               "IRELAND", "FINLAND", "NETHERLANDS", "NEW ZEALAND", "QATAR", "SWITZERLAND", "LUXEMBOURG",
               "ICELAND", "AUSTRALIA", "NORWAY", "SWEDEN", "DENMARK"]
countrylist = []
for i in range(0, 1000):
    countrylist.append(country[random.randint(0,29)])
