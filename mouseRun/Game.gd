extends Node2D

onready var http_pull = $GetUsers
onready var main_camera = $MainCamera
var server_url_get_users = Global.ip_serv +"/get/server_users"
var den = preload("res://Den.tscn")
var main_hero = null
onready var status = $MainCamera/CanvasLayer/Status

var flag_fin = preload("res://Flag.tscn")

var pole = Global.pole

func can_move_to(x, y):
	if x < 0 or x > len(pole[0]) or y < 0 or y > len(pole):
		return 0
	else:
		if pole[y][x] == 1:
			return 0
		return 1

func _ready():
	if pole != [[]]:
		create_pole()
	else:
		var query = JSON.print({})
		var headers = ["Content-Type: application/json"]
		var url = Global.ip_serv +"/get/pole"
		$GetPole.request(url, headers, false, HTTPClient.METHOD_POST, query)
	send_HTTPRequest(server_url_get_users, {
		"name" : Global.serv_name, 
		"naming" : Global.name_user_tech
		})

func _process(delta):
	if main_hero != null:
		main_camera.position = main_hero.position
	if Global.can_move:
		status.text = "Твой ход"
	else:
		status.text = "Ожидание"


func _on_GetUsers_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	for i in json.result:
		if !has_node(str(i)):
			var new_den = den.instance()
			add_child(new_den)
			print(json.result[i])
			new_den.set_naming(str(i), json.result[i]["name"], json.result[i]["color"])
			new_den.set_pos(json.result[i]["x"], json.result[i]["y"])
			if i == Global.name_user_tech:
				main_hero = new_den
				Global.can_move = json.result[i]["is_moving"]
		else:
			get_node(i).set_pos(json.result[i]["x"], json.result[i]["y"])
			if i == Global.name_user_tech:
				Global.can_move = json.result[i]["is_moving"]
#	send_HTTPRequest(server_url_get_users, {
#		"name" : Global.serv_name, 
#		"naming" : Global.name_user_tech
#		})

func send_HTTPRequest(url, data, use_ssl = false):
	var query = JSON.print(data)
	var headers = ["Content-Type: application/json"]
	http_pull.request(url, headers, use_ssl, HTTPClient.METHOD_POST, query)


func _on_RequestTimer_timeout():
	send_HTTPRequest(server_url_get_users, {
		"name" : Global.serv_name, 
		"naming" : Global.name_user_tech
		})


func _on_Flag_area_entered(area):
	if area.name == "DenArea":
		Global.winner = area.get_parent().get_naming()
		get_tree().change_scene("res://WinScreen.tscn")

func create_pole():
	for i in range(len(pole[0])):
		for j in range(len(pole)):
			if pole[j][i] == 1:
				$TileMap.set_cell(i-1, j-1, 0)
			elif pole[j][i] == 2:
				var finflag = flag_fin.instance()
				$TileMap.add_child(finflag)
				finflag.global_position = Vector2((i-1)*100+50, (j-1)*100+50)
				finflag.connect("area_entered", self, "_on_Flag_area_entered") # Replace with function body.

func _on_GetPole_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	Global.pole = json.result["pole"]
	pole = Global.pole
	create_pole()
	
