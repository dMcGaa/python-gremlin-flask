from flask import Flask
app = Flask('simpleApp')

@app.route('/')
def hello_world():
    return 'hello world!'

