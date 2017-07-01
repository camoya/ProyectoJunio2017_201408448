import NodoMatriz
Nm = NodoMatriz
class MatrizDispersa:

	def __init__(self):
		self.__nodoInicial = Nm.NodoMatriz(0,0,None, None, None, None, None)

	def insertarNodo(self, corX, corY, valor, central, posC, tipoNave, modoNave):
		existY = False
		existX = False
		casPosX = None
		casPosY = None
		cas = self.__nodoInicial
		while cas != None:
			if cas.Y == int(corY):
				existY = True
				casPosY = cas
				break
			elif cas.Y > int(corY):
				casAn = cas.posY
				cabAddY = Nm.NodoMatriz(0, int(corY), None, casAn, None, cas, None)
				casAn.posmY = cabAddY
				cas.posY = cabAddY
				casPosY = cabAddY
				existY = True
				break
			cas = cas.posmY
		if existY == False:
			cabAddY = Nm.NodoMatriz(0, int(corY), None, cas, None, None, None)
			cas.posmY = cabAddY
			casPosY = cabAddY

		cas = self.__nodoInicial
		while cas != None:
			if cas.X == int(corX):
				existX = True
				casPosX = cas
				break
			elif cas.X > int(corX):
				casAn = cas.posmX
				cabAddX = Nm.NodoMatriz(int(corX), 0, cas, None, casAn, None, None)
				casAn.posX = cabAddX
				cas.posmX = cabAddX
				existX = True
				casPosX = cabAddX
				break
			cas = cas.posX
		if existX == False:
			cabAddX = Nm.NodoMatriz(int(corX), 0, None, None, cas, None, None)
			cas.posX = cabAddX
			casPosX = cabAddX

		if casPosY.X == int(corX) and casPosY.Y == int(corY):
			casPosY.set_valor(valor)
			casPosY.set_tipoNave(tipoNave)
			casPosY.set_modoNave(modoNave)
			casPosY.set_isPosCentral(central)
			casPosY.set_posCentral(posC)
		elif casPosX.X == int(corX) and casPosX.Y == int(corY):
			casPosX.set_valor(valor)
			casPosX.set_tipoNave(tipoNave)
			casPosX.set_modoNave(modoNave)
			casPosX.set_isPosCentral(central)
			casPosX.set_posCentral(posC)
		else:
			#Buscador de las casillas asociadas en Columnas
			apunY = casPosY
			casAsocXAnt = None
			casAsocXPos = None
			while apunY != None:
				if apunY.X > int(corX):
					casAsocXPos = apunY
					casAsocXAnt = apunY.posmX
			casAsocXAnt = apunY
			apunY = apunY.posX
			#Buscador de las casillas asociada en Filas
			apunX = casPosX
			casAsocYAnt = None
			casAsocYPos = None
			while apunX != None:
				if apunX.Y > int(corY):
					casAsocYPos = apunX
					casAsocYAnt = apunX.posY
			casAsocYAnt = apunX
			apunX = apunX.posmY
			#Creacion de casilla asociada
			casAddAsocidada = Nm.NodoMatriz(int(corX), 0, None, None, cas, None, None)

				






