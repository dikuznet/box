#!/usr/bin/python
'''
#from flask import Flask
#app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello():
    return "Hello world!"
 
if __name__ == '__main__':
    app.run()
'''

def app(environ, start_response):
	d=dict()
	d=environ
	body = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
	s=""
	for bb in body: s=s+bb
	print(s)
	data=bytes(s)
	start_response("200 OK", [("Content-Type", "text/plain"),("Content-Length", str(len(data)))])
	return iter([data])