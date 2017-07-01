class NodoMatriz:
	def __init__(self, cX, cY,posX, posY, posmX, posmY):
		self.X = cX
		self.Y = cY
		self.posX = posX
		self.posY = posY
		self.posmX = posmX
		self.posmY = posmY
		self.__isPosCentral = False
		self.__posCentralNave = None
		self.__golpeada = False
		self.__destruida = False
		self.__tipoNave = 0
		self.__modoNave = 0
		self.__valor = None

	def set_valor(self, val):
		self.__valor = val
		
	def get_valor(self):
		if(self.__valor == None):
			return "-"
		return self.__valor

	def set_golpeada(self, val):
		self.__golpeada = val
		
	def get_golpeada(self):
		return self.__golpeada

	def set_destruida(self, val):
		self.__destruida = val
		
	def get_destruida(self):
		return self.__destruida

	def set_tipoNave(self, val):
		self.__tipoNave = val
		
	def get_tipoNave(self):
		return self.__tipoNave

	def set_modoNave(self, val):
		self.__modoNave = val
		
	def get_modoNave(self):
		return self.__modoNave

	def set_posCentral(self, val):
		self.__posCentralNave = val

	def get_posCentral(self):
		return self.__posCentralNave

	def set_isPosCentral(self, val):
		self.__isPosCentral = val
	def get_isPosCentral(self):
		return self.__isPosCentral

