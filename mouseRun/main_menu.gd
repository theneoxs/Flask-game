extends Control

var server_row = preload("res://ServerRow.tscn")

onready var http_pull = $GetServers
onready var http_enter = $EnterInServer
var server_url_get_servers = Global.ip_serv +"/get/servers"
var server_url_create_servers = Global.ip_serv +"/set/create_server"
onready var text_data = $ColorRect/Label
onready var server_name = $ColorRect/ServerName
onready var server_list = $ColorRect/ScrollContainer/VBoxContainer

func _ready():
	_on_Button_pressed()

func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	if json.result["status"] == 0:
		if json.result["data"] != {}:
			for i in server_list.get_children():
				i.queue_free()
			for i in json.result["data"]:
				var server_row_added = server_row.instance()
				server_list.add_child(server_row_added)
				server_row_added.set_data(i, "Nobody" if len(json.result["data"][i]) == 0 else json.result["data"][i] )
				server_row_added.connect("enter_server", self, "enter_in_server")
			text_data.text = str(json.result["data"])
			if text_data.text == "{}":
				text_data.text = "No servers"
		else:
			text_data.text = "No servers"
	else:
		text_data.text = json.result["description"]


func _on_Button_pressed():
	send_HTTPRequest(server_url_get_servers, {"dummy" : true})
	
	
func send_HTTPRequest(url, data, use_ssl = false):
	var query = JSON.print(data)
	var headers = ["Content-Type: application/json"]
	http_pull.request(url, headers, use_ssl, HTTPClient.METHOD_POST, query)


func _on_Create_pressed():
	send_HTTPRequest(server_url_create_servers, {"name" : server_name.text})

func enter_in_server():
	var enter_data = {
		"serv_name" : Global.serv_name,
		"name" : Global.name_user,
		"name_tech" : Global.name_user_tech
	}
	var query = JSON.print(enter_data)
	var headers = ["Content-Type: application/json"]
	var url = Global.ip_serv + "/set/add_user"
	http_enter.request(url, headers, false, HTTPClient.METHOD_POST, query)

func _on_EnterInServer_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	Global.pole = json.result["pole"]
	get_tree().change_scene("res://Game.tscn")
