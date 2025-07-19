ACL = int(input("Ingrese su el numero de ACL IPv4: "))
if ACL <= 99:
	print("----- La ACL es Estandar -----")
elif ACL <= 199:
	print("----- La ACL es Extendida -----")

else :
	print("No corresponde a una lista de acceso")
