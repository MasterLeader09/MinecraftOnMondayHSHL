import sys, os
class Ex(Exception):
	pass

class Bruch(Ex):
	def __init__(self, zaehler, nenner=1):
		self.Zaehler = int(zaehler)
		self.Nenner = int(nenner)
		if self.Nenner == 0:
			raise ZeroDivisionError

	def multiplizieren(self, other):
		self.Zaehler *= other.Zaehler
		self.Nenner *= other.Nenner
		self.ausgeben()

	def dividieren(self, other):
		self.Zaehler *= other.Nenner
		self.Nenner *= other.Zaehler
		self.ausgeben()

	def addieren(self, other):
		self.Zaehler = self.Zaehler * other.Nenner + self.Nenner * other.Zaehler
		self.Nenner = self.Nenner * other.Nenner
		self.ausgeben()

	def subtrahieren(self, other):
		self.Zaehler = self.Zaehler * other.Nenner - self.Nenner * other.Zaehler
		self.Nenner = self.Nenner * other.Nenner
		self.ausgeben()

	def ausgeben(self):
		print(str(self.Zaehler) + " / " + str(self.Nenner))


	def ganzzahl(self):
		print(str(self.Zaehler / self.Nenner))


b_zaehler = int(input("Bitte einen Zaehler eingeben: "))
b_nenner = int(input("Bitte einen Nenner eingeben: "))
b = Bruch(b_zaehler,b_nenner)
b.ganzzahl()
