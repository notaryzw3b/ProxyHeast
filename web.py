import sys
from flask import Flask, json, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class WebServer:
    def __init__(self):
        socketio.run(app)

    def send(data):
        socketio.send(data, True)  #send only json!

    @socketio.on('connect')
    def connect():
        socketio.send(json.dumps({'event': 'login', 'data': 'success'}), True)

    @app.get("/")
    def index():
        return render_template("index.html")
