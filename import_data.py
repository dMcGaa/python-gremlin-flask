from gremlin_python.driver import client
import json

vertices_rep = ".hasLabel('person')"
gmn_pj = ".project('props', 'id','label')"
gmn_pj_props = ".by(valueMap())"
gmn_pj_id = ".by(id)"
gmn_pj_label = ".by(label)"
vertices_rep = ''.join([vertices_rep,gmn_pj, gmn_pj_props, gmn_pj_id, gmn_pj_label])

def get_db():
    return client.Client('ws://localhost:8182/gremlin', 'g')

def write_person_to_graph(person_label, vertex_id, person_age, person_name):

    gremlin_op = "g.addV().property('name','{}').property('age', '{}').property(label,'{}').property(id, '{}')".format(person_name, person_age, person_label, vertex_id)
    gremlinCmd = ''.join([gremlin_op, vertices_rep])
    result_set = gremlinClient.submit(gremlinCmd)

def process_line(line):
    data = json.loads(line)
    person_label = data["label"]
    person_name = data["props"]["name"][0]
    person_age = data["props"]["age"][0]
    vertex_id = data["id"]

    write_person_to_graph(person_label, vertex_id, person_age, person_name)
    print (person_label+ " " + str(vertex_id) + " " + str(person_age) + " " + person_name)

def remove_all_vertices():
    gremlin_op = "g.V().drop().iterate()"
    gremlinCmd = ''.join([gremlin_op])
    result_set = gremlinClient.submit(gremlinCmd)

def write_file_to_graph():
    file = open("./data/datafile.txt","r")
    for line in file:
        process_line(line)
    file.close() 

gremlinClient = get_db()

remove_all_vertices()
write_file_to_graph()

"""Closes the database connection at end of request"""
gremlinClient.close()

