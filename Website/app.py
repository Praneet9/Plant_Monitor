from flask import Flask, render_template, jsonify, request
from static import db
from random import sample, randint
app = Flask(__name__)

db.testingdb()

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

@app.route("/test")
def index():
    var = "None now"
    try:
        var = request.args['moisture_0']
        print("SMS0",var)
        var = request.args['moisture_1']
        print("SMS1",var)
        var = request.args['moisture_2']
        print("SMS2",var)
        var = request.args['moisture_3']
        print("SMS3",var)
        var = request.args['moisture_4']
        print("SMS4",var)
        var = request.args['humidity_1']
        print("h1",var)
        var = request.args['temperature_1']
        print("t1",var)
        # var = request.args['h2']
        # print("h2",var)
        # var = request.args['t2']vi
        # print("t2",var)
    except Exception as e:
        print(e)
    return str(var)

@app.route("/test")
def test():
    print("I am here!!!")
    print("SMS2",request.args['x'])
    return "Hello"

@app.route("/data")
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

@app.route("/chart")
def chart():
    d = {'left': [12, 19, 3, 5, 2, 30, 15, 15, 6, 20], 'right': 0.82339555, '_unknown_': 0.0059609693}
    # message = {
    #     'status': 200,
    #     'message': 'OK',
    #     'scores': d
    # }
    # resp = jsonify(message)
    return render_template('index.html') 


    



if __name__ == '__main__':
    app.run(debug=True)