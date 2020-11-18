from random import randint

class Game():
	def __init__(self):
		self.number = randint(0,100)
		self.numero_utente = 0
		self.go = True
		self.attempt = 0
	def print_game(self):
		print("Benvenuto al gioco: Indovina il Numero")
		print("Le regole sono le seguenti: il computer estrarrà in modo casuale un numero da 0 a 100 e tu dovrai cercare di indovinarlo.")
		print("Se il numero che hai scritto è più grande di quello estratto dal computer, allora ti uscirà la scritta MINORE, se è più piccolo MAGGIORE.")
		print("Se invece azzecchi il numero avrai vinto. Hai a disposizione 5 tentativi")
	def ask_number(self):
		print("Che numero scegli?")
		self.numero_utente = int(input())
	def number_check(self):
		if(self.numero_utente < 0 or self.numero_utente > 100):
			print("Non fare il furbo!")
		elif(self.numero_utente > self.number):
			print(">>>MINORE")
			self.attempt += 1
		elif(self.numero_utente < self.number):
			print(">>>MAGGIORE")
			self.attempt += 1
		else:
			print("Hai indovinato in ", self.attempt, "tentativo/i")
			self.go = False
	def game_logic(self):
		while self.go:
			self.ask_number()
			self.number_check()
			if(self.attempt >= 5):
				print("Il numero era", self.number)
				self.go = False
g = Game()
g.print_game()
g.game_logic()

while True:
	print("se vuoi continuare a giocare premi 1 altrimenti 0")
	continuo = int(input())
	if(continuo==1):

		g = Game()
		g.game_logic()
	else:
		print("END")
		break


