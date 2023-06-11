extends Control

signal enter_server

var name_server = ""
onready var name_server_label = $NameServer
onready var users_label = $Users
onready var http_del = $Deletion

func set_data(name_server_data, users):
	name = name_server_data
	name_server = name_server_data
	name_server_label.text = name_server_data
	users_label.text = str(users)


func _on_Enter_pressed():
	Global.serv_name = name_server
	emit_signal("enter_server")



func _on_Delete_pressed():
	Global.serv_name = name_server
	var query = JSON.print({"name_serv" : Global.serv_name, "naming" : Global.name_user_tech, "from_menu" : 1})
	var headers = ["Content-Type: application/json"]
	var url = Global.ip_serv +"/set/del_server"
	http_del.request(url, headers, false, HTTPClient.METHOD_POST, query)


func _on_Delete_request_completed(result, response_code, headers, body):
	get_parent().get_parent().get_parent().get_parent()._on_Button_pressed()
