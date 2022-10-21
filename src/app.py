from flask import Flask, render_template,request, session ,url_for,redirect 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'read my mind'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lawncare')
def lawncare():
    return render_template('lawncare.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/positivenegative')
def positivenegative():
    return render_template('positivenegative.html')

@app.route('/inputoutput')
def inputoutput():
    return render_template('inputoutput.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=200)
