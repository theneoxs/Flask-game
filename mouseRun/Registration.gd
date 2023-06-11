extends Control

func _ready():
	$ColorRect/Server.text = Global.ip_serv

func _on_Enter_pressed():
	Global.ip_serv = $ColorRect/Server.text
	Global.name_user = $ColorRect/NameUser.text
	Global.name_user_tech = Global.name_user + str("_") + str(hash(Global.name_user + str(OS.get_unix_time())))
	get_tree().change_scene("res://main_menu.tscn")
