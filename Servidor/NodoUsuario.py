import ListaJuegosUsuario
LJU = ListaJuegosUsuario
class NodoUsuario:
	def __init__(self, nick, password, conec):
		self.nickname = nick
		self.contra = password
		self.online = conec
		self.__ListJuegos = LJU.ListaJuegosUsuario()
		self.__izq = None
		self.__der = None

	def set_izq(self, izquierdo):
		self.__izq = izquierdo
	def get_izq(self):
		return self.__izq
	def set_der(self, derecho):
		self.__der = derecho
	def get_der(self):
		return self.__der