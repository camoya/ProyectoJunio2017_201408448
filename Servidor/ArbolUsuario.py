import NodoUsuario
NU = NodoUsuario
class ArbolUsuario:
	def __init__(self):
		self.__inicio = None

	def agregar(self, user):
		if self.__inicio == None:
			self.__inicio = user
			return True
		else:
			nodo = self.__inicio
			ultNodo = None
			while nodo != None:
				ultNodo = nodo
				if user.nickname > nodo.nickname:
					nodo = nodo.get_der()	
				else:
					nodo = nodo.get_izq()
			if ultNodo.nickname > user.nickname:
				ultNodo.set_der(user)
			else:
				ultNodo.set_izq(user)	
			return True
		return False

	