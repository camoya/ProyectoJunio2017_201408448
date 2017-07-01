class NodoJuegosUsuario:
	def __init__(self, opo, tirosR, tirosAcer, tirosFall, ganador, dan, porAciertos):
		self.oponente = opo
		self.tirosRealizados = tirosR
		self.tirosAcertados = tirosAcer
		self.tirosFallados = tirosFall
		self.isWin = int(ganador)
		self.danger = dan
		self.porAciertos = porAciertos
		self.__sig = None
		self.__ant = None

	def set_sig(self, siguiente):
		self.__sig = siguiente
	def get_sig(self):
		return self.__sig
	def set_ant(self, anterior):
		self.__ant = anterior
	def get_ant(self):
		return self.__ant