import json

with open("myfile.json", "r") as json_file:
	ourjson = json.load(json_file)
	token = ourjson["access_token"]
	expira = str(ourjson["expires_in"])


print("El token es: " + token)
print("Expira en: " + expira)

 
