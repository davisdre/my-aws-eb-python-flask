#make a virtual envirnment and install all the module 
#import the flask module
from email.mime import application
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests

application = Flask(__name__)
CORS(application)

#make a route and render all the html templates in this route
@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')

        #take a variable to show the json data
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=e76c20c979cce7e839ed673404ba291a&units=imperial')

        #read the json object
        json_object = r.json()

        #take some attributes like temperature,humidity,pressure of this 
        temperature = int(json_object['main']['temp']) #this temparetuure in kelvin
        humidity = int(json_object['main']['humidity'])
        wind = int(json_object['wind']['speed'])

        #atlast just pass the variables
        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']
        
        return render_template('home.html',temperature=temperature,humidity=humidity,city_name=city_name,condition=condition,wind=wind,desc=desc)
    else:
        return render_template('home.html') 


if __name__ == '__main__':
    application.run()
