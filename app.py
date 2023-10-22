from flask import Flask,request,render_template,jsonify
import requests
import os 
import json

save_dir = "data/"

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/weatherapp',methods = ['POST'])
def weather():
    city = request.form['city']
    units = request.form['units']
    key = request.form['appids']
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q':city,
         'appid': key,
         'units': units}

    print(params)

    data = requests.get(url,params=params)
    data_json = data.json()
    file_path = f"{city}.json"

    try:
        with open(file_path, "w") as json_file:
            json.dump(data_json, json_file, indent=4)
        print("JSON data saved to", file_path)
    except Exception as e:
        print("Error:", str(e))

    return data_json



if __name__ == '__main__':
    app.run('0.0.0.0',port=8000)
