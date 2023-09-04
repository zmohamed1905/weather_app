import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from weather import main as get_weather


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city, state, country)
    return render_template('weather.html', title='Weather App', data=data)
