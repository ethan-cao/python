from graphdatascience import GraphDataScience

host = "bolt://localhost:7687"
user = "neo4j"
password= "pwd"

gds = GraphDataScience(host, auth=(user, password))

print(gds.version())