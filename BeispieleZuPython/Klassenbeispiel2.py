class Zahlenklasse():

	def __init__(self):
		self.x = 1
		self.y = 1
		self.z = 1

	def ausgeben(self):
		print( "X: " + str( self.x ) + ", Y: " + str( self.y ) + ", Z: " + str( self.z ) )

	def wertEingeben(self):
		parameter1 = int( input( "Bitte geben Sie den ersten Wert ein: " ) )
		parameter2 = int( input( "Bitte geben Sie den zweiten Wert ein: " ) )
		parameter3 = int( input( "Bitte geben Sie den dritten Wert ein: " ) )
		return parameter1, parameter2, parameter3

	def aufadieren(self):
		a, b, c = self.wertEingeben()
		self.x = self.x + a
		self.y = self.y + b
		self.z = self.z + c

	def werteFestlegen(self):
		self.x, self.y, self.z = self.wertEingeben()

	def andereZahlaufadieren(self, other):
		self.x = self.x + other.x
		self.y = self.y + other.y
		self.z = self.z + other.z

#Ab hier beginnt der eigentliche Programmcode (diese Zeile ist nur ein Kommentar und wird nicht ausgefuehrt)
neueZahl = Zahlenklasse()
neueZahl.aufadieren()
neueZahl.ausgeben()
neueZahl.werteFestlegen()

andereZahl = Zahlenklasse()
andereZahl.werteFestlegen()

neueZahl.andereZahlaufadieren(andereZahl)
neueZahl.ausgeben()

