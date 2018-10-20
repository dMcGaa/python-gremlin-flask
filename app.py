from flask import Flask
from flask import g #needed to use the application context 'g' namespace variable
from flask import jsonify
from flask import request
from gremlin_python.driver import client
app = Flask('simpleApp')

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/person', methods = ['POST', 'GET'])
def gremlin_names():
    client = get_db()

    vertices_rep = ".values('name')"

    if request.method == 'POST':
        print "Received 'person' POST"
        data = jsonify(request.data) # has data
        json_data = request.get_json() # has json
        person_name = json_data["name"]
        print "person name:", person_name
        print "data:", data
        print "json data:", json_data
        gremlin_op = "g.addV().property('name','{}')".format(person_name)
        gremlinCmd = ''.join([gremlin_op, vertices_rep])
        result_set = g.client.submit(gremlinCmd)
        future_person = result_set.all()
        person = future_person.result()
        print "person created: ", person
        result = person[0]
        #result = newPerson.result() # one vertice is resultset

    else:
        gremlin_op = "g.V()"
        gremlinCmd = ''.join([gremlin_op, vertices_rep])
        result_set = g.client.submitAsync(gremlinCmd)
        future_persons = result_set.result()
        result = future_persons.one()

    return jsonify(result)

def get_db():
    if not hasattr(g, 'client'):
        g.client = client.Client('ws://localhost:8182/gremlin', 'g')
    return g.client

@app.teardown_appcontext
def close_db(error):
    """Closes the database connection at end of request"""
    if hasattr(g, 'client'):
        g.client.close()

"""
result_set = client.submit("[1,2,3,4]")
future_results = result_set.all()
results = future_results.result()
assert results == [1,2,3,4]

future_result_set = client.submitAsync("[1,2,3,4]")
result_set = future_result_set.result()
result = result_set.one()
print result
assert results == [1,2,3,4]
assert result_set.done.done()

names = client.submitAsync("g.V().values('name')")
result_set = names.result()
result = result_set.one()
print result

client.close()
"""
