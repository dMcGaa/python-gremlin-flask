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

    if request.method == 'POST':
        print "Hello World!"
        json_post = jsonify(request.form)
        form_values = jsonify(request.values)
        data = jsonify(request.data) # has data
        json_data = request.get_json() # has json
        request_files = jsonify(request.files)
        form_name = request.form.get('name')
        arg_name = request.args.get('name')
        print "json_post",json_post
        print "form_values", form_values
        print "files", request_files
        print "data", data
        print "json data", json_data
        print "form name: ",form_name
        print "arg name: ",arg_name
        print request.values.get('name')
        result = request.values

    else:
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
