from flask import Flask
# from 
import requests
app=Flask(__name__)

@app.route('/')
def main_page():
    return '<h1>main page<h1>'
@app.route('/about')
def about():
    return '<h1>about us<h1>'

if __name__=='__main__':
    app.run(debug=True)
