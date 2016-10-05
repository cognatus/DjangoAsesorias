from django.contrib.auth.models import User
from .models import Usuario, Mamadas

def guardarUser(datos):
	username = datos.get('nombre')
	password = datos.get('contra')
	telefono = datos.get('telefono')
	email = datos.get('email')
	direccion = datos.get('direccion')
	try:
		user = User.objects.create_user(username=username, password=password, email=email)
		user.save()
	except Exception as e:
		print(e)
		print(type(e))

	try:
		datos = Mamadas()
		datos.user = user
		datos.telefono = telefono
		datos.direccion = direccion
		datos.save()
	except Exception as e:
		print(e)
		print(type(e))