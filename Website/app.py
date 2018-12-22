from flask import Flask, render_template, jsonify, request
from static import db
from random import sample, randint
app = Flask(__name__)
import datetime

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

@app.route("/atamajhisatakli")
def index():
    try:
        data = {}
        date = datetime.datetime.now()

        data['year'] = date.strftime('%Y')
        data['month'] = date.strftime('%m')
        data['date'] = date.strftime('%d')
        
        date['hour'] = date.strftime('%H')
        data['minute'] = date.strftime('%M')

        data['moisture_0'] = request.args['moisture_0']
        data['moisture_1'] = request.args['moisture_1']
        data['moisture_2'] = request.args['moisture_2']
        #data['moisture_3'] = request.args['moisture_3']
        #data['moisture_4'] = request.args['moisture_4']

        #data['humidity_1'] = request.args['humidity_1']
        #data['temperature_1'] = request.args['temperature_1']

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
def data():
    labels = []
    for i in range(48):
        labels.append(randint(0, 100))
    print(labels)
    d = {
        'results': sample(labels, 48),
        'plot_labels': list(frange(0.5, 24.5, 0.5))
        }

    return jsonify(d)

if __name__ == '__main__':
    app.run()