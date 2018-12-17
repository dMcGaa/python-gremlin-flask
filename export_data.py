from gremlin_python.driver import client

def get_db():
    return client.Client('ws://localhost:8182/gremlin', 'g')

def get_person():
    gremlin_op = "g.V()"
    vertices_rep = ".hasLabel('person')"
    gremlinCmd = ''.join([gremlin_op, vertices_rep])
    result_set = gremlinClient.submitAsync(gremlinCmd)
    future_persons = result_set.result() # a ResultSet
    result = future_persons.one() # an array

    return result

def write_array(arr):
    file = open("datafile.txt","w")
    for i in arr:
        file.write(str(i))
        file.write("\n")
    file.close() 

gremlinClient = get_db()

write_array(get_person())

"""Closes the database connection at end of request"""
gremlinClient.close()

