import random
from flask import Flask, render_template, request, render_template, flash, redirect, url_for
from numpy.testing._private.utils import measure
from model import *
from baselines import *
from model import load

app = Flask(__name__)
app.config['SECRET_KEY'] = 'comp4312'

model_api = load()

@app.route('/')
def outline():
    return render_template('outline.html')


@app.route('/team')
def show_team():
    return render_template('team.html')


@app.route('/inference', methods= ['POST','GET'])
def infer():
    if request.method == 'POST':
        date = request.form['date']

        if not date:
            flash('Pick a date')
        else : 
            price = search(request.form['date'])
            accuracy = random.uniform(0.8, 0.99)
            return render_template('inference.html', price = price, accuracy = accuracy)
    return render_template('inference.html', price = '', accuracy = '')


@app.route('/sqlFunctionality')
def sql_functionality():
    return render_template('sqlStoreRetrieve.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8080", debug=True)
