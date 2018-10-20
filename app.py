from flask import Flask
from flask import g #needed to use the application context 'g' namespace variable
from flask import jsonify
from gremlin_python.driver import client
app = Flask('simpleApp')

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/names')
def gremlin_names():
    client = get_db()
    names = g.client.submitAsync("g.V().values('name')")
    result_set = names.result()
    result = result_set.one()
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
