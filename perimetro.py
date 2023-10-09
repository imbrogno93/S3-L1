def quadrato(lato):
	return 4 * lato

def cerchio(raggio):
	return 2 * 3.14 * raggio

def rettangolo(base, altezza):
	return 2 * (base + altezza)

print("Seleziona la figura geometrica di cui vuoi calcolare il perimetro:\n1 per Quadrato\n2 per Cerchio\n3 per Rettangolo")
scelta = float(input("Inserisci la tua scelta: ")

if scelta == 1:
	lato = float(input("Inserisci il lato del quadrato: "))
	perimetro = quadrato(lato)
	print("Il perimetro del quadrato e': ", perimetro)
elif scelta == 2:
	raggio = float(input("Inserisci il raggio del cerchio: "))
	perimetro = cerchio(raggio)
	print("La circonferenza del cerchio e': ", perimetro)
elif scelta == 3:
	base = float(input("Inserisci la base del rettangolo: "))
	altezza = float(input("Inserisci l'altezza del rettangolo: "))
	perimetro = rettangolo(base, altezza)
	print("Il perimetro del rettangolo e': ", perimetro)
else:
	print("Scelta non valida")
