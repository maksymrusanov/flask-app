from flask import Flask
# from 
import requests
app=Flask(__name__)

@app.route('/')
def main_page():
    return '<h1>main page<h1>'

if __name__=='__main__':
    app.run(debug=True)
