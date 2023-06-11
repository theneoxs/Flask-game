extends HTTPRequest


func _():
	var enter_data = {
		"serv_name" : Global.serv_name,
		"name_tech" : Global.name_user_tech
	}
	var query = JSON.print(enter_data)
	var headers = ["Content-Type: application/json"]
	var url = Global.ip_serv +"/set/del_user"
	request(url, headers, false, HTTPClient.METHOD_POST, query)
