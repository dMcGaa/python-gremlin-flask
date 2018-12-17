# Data from Gremlin [Tinkerpop](https://github.com/apache/tinkerpop) using Flask and [gremlinpython](https://pypi.org/project/gremlinpython/)

## Running a Gremlin Server
1. Intro info on [gremlin server](http://tinkerpop.apache.org/docs/3.3.4/reference/#gremlin-server).
2. Download the gremlin server [files from here](http://tinkerpop.apache.org/downloads.html) - NOTE that both the `Console` and the `Server` are available.
3. Start the gremlin server with default config.
```bash
bin/gremlin-server.sh conf/gremlin-server-modern.yaml
```

## Running the Flask app
1. From the directory of your flask app.py file:
```bash
export FLASK_APP=app.py
```

2. From anywhere after the `FLASK_APP` is set.
```bash
flask run
```

## Flask and gremlin-python setup
1. Install gremlin-python
```bash
pip install gremlinpython
```
2. Fix any errors (mine was "no module pip._internal"
```bash
python get-pip.py --force-reinstall
```
```bash
pip install futures
```

## Issue commands with `curl`
1. Basic flask get
```bash
curl localhost:5000
```

2. GET the 'person' endpoint
```bash
curl localhost:5000/person
```

3. POST to the 'person' endpoint
```bash
curl -d '{"name": "your name", "age": 95, "label": "person"}' localhost:5000/person --header "content-type:application/json"
```

## Extra Info
- [azure-cosmos-db-graph-python-getting-started](https://azure.microsoft.com/en-us/resources/samples/azure-cosmos-db-graph-python-getting-started/
- [reading-and-writing-files-in-python](https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
