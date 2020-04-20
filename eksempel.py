from pylab import * #importerer mattefunksjoner
from turtle import * #importerer tegnefunksjoner

'''1. Print'''
print("Hei")        #tekst
print(1)            #heltalltall
print("Hei", 1)     #tekst og tall
print(1.45)         #desimaltall
print(True)         #boolsk variabel


print("-" * 20)

'''2. Summering av tall'''
print("1 + 1 =", 1 + 1)

print("-" * 20)

'''3. Variabler'''
#I programmering kan en variabel være et tall, men også en tekststreng
tall = 2
tekst = "tekst"
print(tall, tekst) #skriver ut variabler

#Legge sammen variabler
x = 2
y = "en"
print("tall + x =", tall + x)
print("tekst + y =", tekst + y)

#Ny variabel
nyVariabel = tall + x
print("Ny variabel =", nyVariabel)

print("-" * 20)

'''4. Regnerekkefølge'''
#Potenser -> Divisjon -> Multiplikasjon -> Addisjon og subtraksjon
print("2^2 =", 2**2)      #potenser
print("2 + 2 =", 2 + 2)   #addisjon
print("2 - 2 =", 2 - 2)   #subtraksjon
print("2 * 2 =", 2 * 2)   #multiplikasjon
print("4 / 2 =", 4 / 2)   #divisjon
print("5 // 2 =", 5 // 2) #heltallsdivision
print("5 mod 2 =", 5 % 2) #rest
print("2 * (2 + 1) =", 2 * (2 + 1)) #parentester
print("2 * 2 + 1 =", 2 * 2 + 1)

#Mattefunksjoner
print("√4 =", sqrt(4))
print("Tilfeldig tall mellom 1 og 10:", randint(10))

print("-" * 20)

'''5. Skriv inn tekst'''
'''inp = input("Skriv et heltall: ")
x = int(inp) #gjør om til heltall

inp = input("Skriv et desimaltall: ")
y = float(inp) #gjør om til desimaltall
print("x + y =", x + y)

print("-" * 20)'''

'''6. If-setninger'''
#gjøre sammenlikninger
tall = 30

if tall == 0:
  print("tall = 0")
elif tall < 30:
  print("tall er mindre enn 30")
elif tall > 30:
  print("tall er større enn 30")
else:
  print("tall = 30")

print("-" * 20)

'''7. While-løkke'''
#kjører så lenge argumentet er sant
x = 0
while x < 5:
  x += 1
  print("x =", x)

print("-" * 20)

'''8. For-løkke'''
#går igjennom iterasjoner
for i in range(5):
  print("i =", i)

print("-" * 20)

'''9. Lister'''
liste = [0, 1, 2]
print(liste)
print(liste[1]) #Henter element på indeks 1

liste.append(8) #Legge til nytt element
print(liste)

liste.pop() #fjerner siste element
print(liste)

print("-" * 20)

'''10. Funksjoner'''
def funksjon(tall):
  tall = tall * 2
  print("tall =", tall)

funksjon(3) #kaller på funksjonen

print("-" * 20)

'''11. Grafer'''
x = linspace(-5, 5, 3)
y = 2**2*x + 2*x + 1
plot(x, y)
savefig('plot.png')



print("-" * 20)

'''12. Figurer'''

print("-" * 20)