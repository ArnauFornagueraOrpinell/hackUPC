from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
from flask import Flask, render_template, request, jsonify
import socket
import random
app = Flask(__name__)

# Create class MAP
class User:
    def __init__(self, id, id_planes):
        self.ids = id
        self.planes = id_planes
    def get_user_id(self):
        return self.id
class Plane:
    def __init__(self, x, y, direction, id, number):
        self.x = x
        self.y = y
        self.direction = direction
        self.id = id
        self.number = number

class Map:
    def __init__(self, planes, users):
        self.planes = planes
        self.users = users
    def get_users_id(self):
        ids = []
        for user in self.users:
            ids.append(user.get_user_id())
        return ids
    def get_planes_num(self):
        planes_num = []
        for plane in self.planes:
            planes_num.append(plane.number)
        return planes_num
class App:
    def __init__(self, map):
        self.map = map
    def get_map(self):
        return self.map
            
game = App(Map([], []))

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())
@app.route('/handle_client', methods=['POST'])
def handle_client():
    data = request.get_json()
    if not game.map.get_users_id().contains(data["id"]):
        game.map.users.append(User(data["id"], []))
    if not game.map.get_planes_num().contains(data["number"]):
        game.map.planes.append(Plane(data["x"], data["y"], data["direction"], data["id"], data["number"]))
    else:
        for plane in game.map.planes:
            if plane.number == data["number"]:
                plane.x = data["x"]
                plane.y = data["y"]
                plane.direction = data["direction"]

    data = {
        'User_Token': jsonify(user_id),
        'Map': jsonify(self.map)
    }
    return jsonify(data)
@app.route('/')
def index():
    return render_template('index.html')

    
    
if __name__ == '__main__':
    app.run(host=get_local_ip(), port=80)

