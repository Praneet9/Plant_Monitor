from flask import Flask, render_template, jsonify, request
from static import db
from random import sample, randint
from bson import json_util
import datetime
import pytz
import math

app = Flask(__name__)


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

@app.route("/atamajhisatakli")
def index():
    try:
        data = {}
        tz = pytz.timezone('Asia/Kolkata')
        date = datetime.datetime.now(tz)

        data['year'] = date.strftime('%Y')
        data['month'] = date.strftime('%m')
        data['date'] = date.strftime('%d')
        
        data['hour'] = date.strftime('%H')
        data['minute'] = date.strftime('%M')

        data['moisture_1'] = request.args['moisture_1']
        # data['moisture_1'] = request.args['moisture_1']
        # data['moisture_2'] = request.args['moisture_2']
        #data['moisture_3'] = request.args['moisture_3']
        #data['moisture_4'] = request.args['moisture_4']

        data['humidity_1'] = request.args['humidity_1']
        data['temperature_1'] = request.args['temperature_1']

        #data['humidity_2'] = request.args['humidity_2']
        #data['temperature_2'] = request.args['temperature_2']

        db.insert_data('data', data)
        return "Inserted"
    except Exception as e:
        print(e)
        return "Not_Inserted"

@app.route("/test")
def test():
    print("I am here!!!")
    print("SMS2",request.args['x'])
    return "Hello"

@app.route("/chart")
def chart():
    labels = []
    for i in range(48):
        labels.append(randint(0, 100))
    print(labels)
    d = {
        'results': sample(labels, 48),
        'plot_labels': list(frange(0.5, 24.5, 0.5))
        }
    d['results'][10] = 40.50
    d['results'][15] = 45.50
    d['results'][20] = 50.50
    return jsonify(d)

@app.route("/data")
def data():
    cols = db.read_data("data")
    data = {'plot_labels': [], 'moisture_1': [], 'temperature_1': [], 'humidity_1': []}

    for col in cols:
        data['plot_labels'].append(col['date'] + '/' + col['month'] + ' - ' + col['hour'] + ":" + col['minute'])
        data['moisture_1'].append(int(col['moisture_1']))
        
        if math.isnan(float(col['temperature_1'])):
            data['temperature_1'].append(0)
        else:
            data['temperature_1'].append(float(col['temperature_1']))
            
        if math.isnan(float(col['humidity_1'])):
            data['humidity_1'].append(0)
        else:
            data['humidity_1'].append(float(col['humidity_1']))
    # print(data)
    return jsonify(data)

@app.route("/")
def index_main():
    return render_template('index.html')

@app.route('/api/get/apigetfn', methods=['GET'])
def flutter_api():
    record=[]
    cols = db.read_data("data")
    for col in cols:
        record.append(col)
    return json_util.dumps(record)

if __name__ == '__main__':
    app.run(debug=False)