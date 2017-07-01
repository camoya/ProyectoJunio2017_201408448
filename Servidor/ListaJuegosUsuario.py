import NodoJuegosUsuario
NJU = NodoJuegosUsuario
class ListaJuegosUsuario:
	def __init__(self):
		self.__inicio = None
		self.__fin = None

	def agregar(self, opo, tirosR, tirosAcer, tirosFall, ganador, dan):
		juegoAdd = NJU.NodoJuegosUsuario(opo, tirosR, tirosAcer, tirosFall, ganador, dan, int(int(tirosAcer)/int(tirosR)))
		if self.__inicio == None:
			self.__inicio = self.__fin = juegoAdd
			return True
		else:
			juegoAdd.set_ant(self.__fin)
			self.__fin.set_sig(juegoAdd)
			self.__fin = juegoAdd
			return True
		return False