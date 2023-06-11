from random import randint
from flask import Flask, request, json, jsonify
import time

app = Flask(__name__)

server_list = {
    "test_server" : {
        "user1" : {
            "name" : "name_1",
            "color" : [187, 255, 212],
            "x" : 1,
            "y" : 2,
            "num" : 1,
            "is_moving" : True
        }
    }
}

pole = [
			[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			[ 1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,2,1],
			[ 1,0,1,1,0,0,2,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1],
			[ 1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1],
			[ 1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1],
			[ 1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
			[ 1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1],
			[ 1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1],
			[ 1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1],
			[ 1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
			[ 1,0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
			[ 1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1],
			[ 1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1],
			[ 1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,2,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,1],
			[ 1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1],
			[ 1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1],
			[ 1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
			[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		]

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<naming>')
def print_naming(naming):
    return f'Hello, {naming}!'

@app.route('/get/servers', methods=["GET", "POST"])
def get_servers():
    if request.method == "POST":
        return {
            "title" : "Server's list",
            "data" : get_servers_with_users(),
            "status" : 0
        }
    else:
        return f"Server's list:</br>{server_list.keys()}"

@app.route('/set/create_server', methods=["GET", "POST"])
def create_server():
    if request.method == "GET":
        serv_name = request.args.get('server_name')
        server_list[serv_name] = {}
        return f"Server {serv_name} has been created!"
    else:
        data = json.loads(request.data)
        try:
            if data["name"] in server_list.keys():
                raise Exception("Exist")
            server_list[data["name"]] = {}
            return {
                "title" : "Create server",
                "data" : get_servers_with_users(),
                "status" : 0
            }
        except:
            return {
                "title" : "Create server",
                "status" : 1,
                "description" : "Name is not a valid"
            }

@app.route('/get/server_users', methods=["GET", "POST"])
def get_users():
    if request.method == "POST":
        data = json.loads(request.data)
        if data["name"] in server_list.keys():
            if data["naming"] in server_list[data["name"]].keys():
                server_list[data["name"]][data["naming"]]["last_time"] = int(time.time())
            return server_list[data["name"]]
        else:
            return {"answer": "none"}
    else:
        return "None"

@app.route('/set/moving_client', methods=["GET", "POST"])
def moving_client():
    if request.method == "POST":
        data = json.loads(request.data)
        server_list[data["serv_name"]][data["naming"]]["is_moving"] = False
        server_list[data["serv_name"]][data["naming"]]["x"] += int(data["move_x"])
        server_list[data["serv_name"]][data["naming"]]["y"] += int(data["move_y"])
        server_list[data["serv_name"]][data["naming"]]["last_time"] = int(time.time())
        numing = server_list[data["serv_name"]][data["naming"]]["num"]
        next_num = 1 if numing == len(server_list[data["serv_name"]].keys()) else numing+1
        for i in server_list[data["serv_name"]]:
            if server_list[data["serv_name"]][i]["num"] == next_num:
                server_list[data["serv_name"]][i]["is_moving"] = True
            if server_list[data["serv_name"]][i]["last_time"] + 15 < int(time.time()):
                server_list[data["serv_name"]].pop(i)
        return {"data" : "Correct"}
    else:
        return "None"

@app.route('/get/pole', methods=["GET", "POST"])
def get_pole():
    return {"pole" : pole}

@app.route('/set/add_user', methods=["GET", "POST"])
def enter_in_servering():
    if request.method == "POST":
        print(request.data)
        data = json.loads(request.data)
        x = randint(2, 14)
        y = randint(2, 14)
        color = [randint(120, 255), randint(120, 255), randint(120, 255)]
        server_list[data["serv_name"]][data["name_tech"]] = {
            "name" : data["name"],
            "color" : color,
            "x" : x,
            "y" : y,
            "num" : len(server_list[data["serv_name"]])+1,
            "is_moving" : False,
            "last_time" : int(time.time())
        }
        if len(server_list[data["serv_name"]]) == 1:
            server_list[data["serv_name"]][data["name_tech"]]["is_moving"] = True
        return {"data" : "Correct",
                "pole" : pole}
    else:
        return "None"

@app.route('/set/del_user', methods=["GET", "POST"])
def del_user():
    if request.method == "POST":
        data = json.loads(request.data)
        if data["serv_name"] in server_list.keys():
            server_list[data["serv_name"]].pop(data["name_tech"])
        return {"data" : "Correct"}
    else:
        return "None"

@app.route('/set/del_server', methods=["GET", "POST"])
def del_server():
    if request.method == "POST":
        data = json.loads(request.data)
        if data["from_menu"] == 1 and data["name_serv"] in server_list.keys():
            server_list.pop(data["name_serv"])
        elif data["from_menu"] == 0:
            server_list[data["name_serv"]][data["naming"]]["color"] = [0, 0, 0]
            count = 0
            counter = 0
            for i in server_list[data["name_serv"]]:
                if server_list[data["name_serv"]][i]["name"] == "bot":
                    print("Delete a bot")
                    continue
                count += 1
                if server_list[data["name_serv"]][i]["color"] == [0, 0, 0]:
                    counter += 1
            if count == counter:
                server_list.pop(data["name_serv"])
        return {"data" : "Correct"}
    else:
        return "None"

def get_servers_with_users():
    servs = {}
    for i in server_list:
        servs[i] = list(server_list[i].keys())
    return servs
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)