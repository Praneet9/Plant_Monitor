from flask import Flask, render_template, jsonify, request
from static import db
app = Flask(__name__)

db.testingdb()

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
        # var = request.args['t2']
        # print("t2",var)
    except Exception as e:
        print(e)
    return str(var)

@app.route("/test")
def test():
    print("I am here!!!")
    print("SMS2",request.args['x'])
    return "Hello"

@app.route("/chart")
def chart():
    d = {'left': [12, 19, 3, 5, 2, 30, 15, 15, 6, 20], 'right': 0.82339555, '_unknown_': 0.0059609693}
    # message = {
    #     'status': 200,
    #     'message': 'OK',
    #     'scores': d
    # }
    # resp = jsonify(message)
    return render_template('index.html', name = d )



if __name__ == '__main__':
    app.run(debug=True)