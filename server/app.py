#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return "<h1>Welcome to my page!</h1>"

@app.route('/str/<username>')
def user(username):
    return f"<h1>Profile for {username}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
