#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, request
from bottle_httpauth import HTTPBasicAuth
import pdb
#pdb.set_trace()
app = Bottle()
basicAuth = HTTPBasicAuth()
users = [{'username' : 'brian', 'password' : '123456'},
         {'username' : 'test', 'password' : 'test'},
        ]

@app.route('/hello')
@basicAuth.login_required
def hello():
    #pdb.set_trace()
    return "Hello World!"
    
@basicAuth.error_handler
def unauthorized():
    print('=========================')
    return ['Unauthorized access']

@basicAuth.get_password
def get_password(username):
    #user = User.query.filter_by(username=username).first()
    
    #if user:
    #    if user.username == username:
    #        return user.password
    #return None
    user = None
    for i in users:
        if i['username'] == username:
            user = i
    if user:
        if user['username'] == username:
            return user['password']

@basicAuth.verify_password
def verify_password(username, client_password):
    user = None
    for i in users:
        if i['username'] == username:
            user = i
    if user:
        if user['username'] == username:
            if user['password'] == client_password:
                return True
    return False
    
if __name__ == '__main__':
    import bottle
    bottle.DEBUG = True
    run(app, host='localhost', port=8080)