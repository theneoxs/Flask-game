extends Control


func _ready():
	var query = JSON.print({
		"name_serv" : Global.serv_name,
		"naming" : Global.name_user_tech,
		"from_menu" : 0
	})
	var headers = ["Content-Type: application/json"]
	var url = Global.ip_serv +"/set/del_server"
	$ColorRect/DelServer.request(url, headers, false, HTTPClient.METHOD_POST, query)
	Global.serv_name = ""
	$ColorRect/Label2.text = Global.winner


func _on_Leave_pressed():
	get_tree().change_scene("res://main_menu.tscn")
