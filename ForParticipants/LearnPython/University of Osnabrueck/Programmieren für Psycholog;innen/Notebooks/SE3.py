##For-Loops:
## Syntax von for-Schleifen allgemein
# for <variable> in <sequence>:
# <statements>
# else:
# <statements>

# Summe der Zahlen: Schreibe einen Loop, der die Summe der Zahlen von 1 bis n (InputVariable) berechnet und ausgibt.
Eingabe = input("Bitte geben Sie eine Zahl ein: ")
n = int(Eingabe)
Summe = 0
for n in range(n):
    Summe += n+1
print(Summe)
print()

RED = '\033[91m'
RESET = '\033[0m'
GREEN = '\033[92m'

n = 0

while True:
    try:
        eingabe = input("Bitte geben Sie eine Zahl ein: ")
        n = int(eingabe)
        break
    except ValueError:
        print(RED + "Ungültige Eingabe. Bitte geben Sie eine (ganze) Zahl ein: " + RESET)
        
Summe = 0
for i in range(1, n + 1): 
    Summe += i
print(f"Die Summe der Zahlen von 1 bis {n} ist: {Summe}")
print()

# Vokalzählung: Zähle die Anzahl der Vokale (a, e, i, o, u) in einem Input-String.
vokale = ["a", "e", "i", "o", "u"]
anzahl = 0
words = input("Bitte geben Sie die Vokale aus dem deutschen Alphabet in korrekter Reihenfolge ein: ")
for v in words:
    if v in vokale:
      anzahl += 1
print(anzahl)
print()

Vokale = ["a", "e", "i", "o", "u"]
Words = ""

while True:
        Words = input("Bitte geben Sie Vokale aus dem deutschen Alphabet ein: ")
    
        if not Words.isalpha():
          print(RED + "Ungültige Eingabe. Bitte geben Sie Vokale aus dem deutschen Alphabet ein: " + RESET)
          continue
            
        break 
        
Anzahl = 0
for w in Words:
    if w in Vokale:
     Anzahl += 1
print(f"Die Anzahl der Vokale in deiner Eingabe {Words} ist: {Anzahl}")
print()

## While-Loops:
# Stop-Eingabe: Schreibe einen Loop, der Benutzereingaben in einer Schleife sammelt, bis der Benutzer "stop" eingibt. Das Programm gibt dann alle gesammelten Eingaben aus.
speicher = []
while True:
    inp = input("Bitte geben Sie beliebigen Input ein - mit der Eingabe 'Stop' beenden Sie den Prozess: ")
    
    if inp == "Stop":
      break
    
    speicher.append(inp)

print("Ihre Eingaben waren: ", speicher)
print()

# Zufallszahlen raten: Schreibe einen Loop, der eine Zufallszahl zwischen 1 und 100 wählt und den Benutzer dazu auffordert, sie zu erraten. Das Programm gibt Hinweise, ob die Schätzung zu hoch oder zu niedrig ist, und fährt fort, bis die Zahl richtig erraten wurde.(Tipp: Vielleicht ist hier das Package „random“ hilfreich.)
import random
        
print("Willkommen bei GuessTheNumber! Wir wünschen Ihnen viel Erfolg.")
zz = random.randint(1, 100)

versuche = 0 

while True:
    try:
        raten = input(f"Versuch {versuche + 1}: Bitte geben Sie eine ganze Zahl zwischen 1 und 100 ein: ")
        zahl = int(raten) 

        versuche += 1

        if not (1 <= zahl <= 100):
            print(RED + "Ungültige Eingabe. Bitte geben Sie eine Zahl ZWISCHEN 1 und 100 ein:" + RESET)
            continue 

    except ValueError:
        print(RED + "Ungültige Eingabe. Das ist keine ganze Zahl. Bitte versuchen Sie es erneut." + RESET)
        continue 

    if zahl == zz:
        print(GREEN + f"Ach du heiliger Neptun! Sie haben die Zahl {zz} in {versuche} Versuchen erraten! \n Herzlichen Glückwunsch! \n Ihre Belohnung wartet hier 'https://www.your-reward.com/?v=xvFZjo5PgG'" + RESET)
        break

    elif zahl > zz:
        diff = zahl - zz
        if diff >= 30:
            print("Hoppala! Ihre Zahl ist deutlich größer als die gesuchte Zahl. Versuchen Sie es gerne nochmal!")
        elif diff >= 20:
            print("Schade! Ihre Zahl ist größer als die gesuchte Zahl. Versuchen Sie es gerne nochmal!")
        elif diff >= 10:
            print("Schade! Ihre Zahl ist etwas größer als die gesuchte Zahl. Versuchen Sie es gerne nochmal!")
        else: 
            print("Autsch! Hier wird es heiß! Deine Zahl ist nur etwas zu hoch.")

    elif zahl < zz:
        diff = zz - zahl
        if diff >= 30:
            print("Hoppala! Ihre Zahl ist deutlich kleiner als die gesuchte Zahl. Versuchen Sie es gerne nochmal!")
        elif diff >= 20:
            print("Schade! Ihre Zahl ist kleiner als die gesuchte Zahl. Versuchen Sie es gerne nochmal!")
        elif diff >= 10:
            print("Schade! Ihre Zahl ist etwas kleiner als die gesuchte Zahl. Versuchen Sie es gerne nochmal!")
        else:
            print("Autsch! Hier wird es heiß! Deine Zahl ist nur etwas zu niedrig.")
print()

##Textfiles: Bei StudIP ist ein Textfile hochgeladen (04_read_in_example.txt), dass ihr einlesen könnt und ein eigenes Textfile als Antwort schreiben und hochladen könnt.
with open('example.txt','r') as file:
    content = file.read()

print(content)
print()
with open ('answer.txt', 'w') as file:
    file.write("Answering your request: \n")
    file.write(":) \n")

with open ('answer.txt', 'a') as file:
    file.write("Ad on.")







    