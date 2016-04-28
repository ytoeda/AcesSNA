from py2neo import Node,Relationship,Graph

graph = Graph("http://localhost:7474/db/data/")
graph.delete_all()

person = open("Data\person.txt")
for line in person:
    line_data = line.split(',')
    graph.create(Node("Person", name=line_data[0], gender=line_data[1], country=line_data[2]))
