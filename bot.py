import requests
import time

ip_conf = "http://192.168.1.160:80"
serv_name = "Main"
name = "bot"
name_tech = "bot001"
can_move = False

vect_x = 1
vect_y = 0

pole = [[]]

def can_move_to(x, y):
	if x < 0 or x > len(pole[0]) or y < 0 or y > len(pole):
		return 0
	else:
		if pole[y][x] == 1:
			return 0
		return 1
def rotate_v(x, y):
    vect = [-1, 0, 1, 0]
    if x == 1:
        return (0, 1)
    elif x == -1:
        return (0, -1)
    else:
        if y == 1:
            return (-1, 0)
        else:
            return (1, 0)
def rotate_l(x, y):
    vect = [-1, 0, 1, 0]
    if x == 1:
        return (0, -1)
    elif x == -1:
        return (0, 1)
    else:
        if y == 1:
            return (1, 0)
        else:
            return (-1, 0)
def right_check(x, y, move_x, move_y):
    vec_x, vec_y = rotate_v(move_x, move_y)
    if can_move_to(x+vec_x, y+vec_y) == 0:
        return 1
    else:
        return 0

def send_move_req(move_x, move_y):
    requests.post(ip_conf+"/set/moving_client",
                              json = {
		"serv_name" : serv_name,
		"naming" : name_tech,
		"move_x" : str(move_x),
		"move_y" : str(move_y)
	})

name_tech = input("Tech name = ")

req = requests.post(ip_conf+"/set/add_user", 
                    json = {"serv_name" : str(serv_name), 
                            "name_tech" : str(name_tech),
                            "name" : str(name)}
                            )
pole = req.json()["pole"]

while True:
    time.sleep(1)
    get_users = requests.post(ip_conf+"/get/server_users",
                              json = {"name" : serv_name,
                                  "naming" : name_tech
                              }).json()
    if "answer" not in get_users.keys():
        bot_data = get_users[name_tech]
        if bot_data["is_moving"]:
            pos_x = bot_data["x"]
            pos_y = bot_data["y"]
            if can_move_to(pos_x+vect_x, pos_y+vect_y) and right_check(pos_x, pos_y, vect_x, vect_y):
                send_move_req(vect_x, vect_y)
            else:
                if not right_check(pos_x, pos_y, vect_x, vect_y):
                    vect_x, vect_y = rotate_v(vect_x, vect_y)
                    send_move_req(vect_x, vect_y)
                else:
                    vect_x, vect_y = rotate_l(vect_x, vect_y)
                    if can_move_to(pos_x+vect_x, pos_y+vect_y):
                        send_move_req(vect_x, vect_y)
                    else:
                        vect_x, vect_y = rotate_l(vect_x, vect_y)
                        send_move_req(vect_x, vect_y)
    else:
        break
        
    
    print(get_users)
