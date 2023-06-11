extends Sprite

onready var show_naming = $Label
onready var http_move = $Moving
var pos_x = 0
var pos_y = 0

func set_naming(naming, show_name, color):
	name = str(naming)
	show_naming.text = str(show_name)
	self_modulate = Color(255.0/color[0], 255.0/color[1], 255.0/color[2])

func get_naming():
	return show_naming.text

func set_pos(x, y):
	global_position.x = x*100
	global_position.y = y*100
	pos_x = x
	pos_y = y

func _process(delta):
	if name == Global.name_user_tech and Global.can_move:
		if Input.is_action_just_pressed("ui_left") and get_parent().can_move_to(pos_x-1, pos_y):
			Global.can_move = false
			send_HTTPRequest(-1, 0)
			global_position.x -= 100
		if Input.is_action_just_pressed("ui_right") and get_parent().can_move_to(pos_x+1, pos_y):
			Global.can_move = false
			send_HTTPRequest(1, 0)
			global_position.x += 100
		if Input.is_action_just_pressed("ui_up") and get_parent().can_move_to(pos_x, pos_y-1):
			Global.can_move = false
			send_HTTPRequest(0, -1)
			global_position.y -= 100
		if Input.is_action_just_pressed("ui_down") and get_parent().can_move_to(pos_x, pos_y+1):
			Global.can_move = false
			send_HTTPRequest(0, 1)
			global_position.y += 100

func send_HTTPRequest(move_x, move_y):
	pos_x += move_x
	pos_y += move_y
	var data = {
		"serv_name" : Global.serv_name,
		"naming" : Global.name_user_tech,
		"move_x" : str(move_x),
		"move_y" : str(move_y)
	}
	var query = JSON.print(data)
	var headers = ["Content-Type: application/json"]
	var url = Global.ip_serv +"/set/moving_client"
	http_move.request(url, headers, false, HTTPClient.METHOD_POST, query)
