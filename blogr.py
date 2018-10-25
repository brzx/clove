#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, request
from bottle_httpauth import HTTPBasicAuth
import pdb
app = Bottle()
basicAuth = HTTPBasicAuth()

@app.route('/hello')
@basicAuth.login_required
def hello():
    pdb.set_trace()
    return "Hello World!"

if __name__ == '__main__':
    import bottle
    bottle.DEBUG = True
    run(app, host='localhost', port=8080)