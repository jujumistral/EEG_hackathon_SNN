## neue Variablen - dafür zuerst math packages in script einbauen
import math 
a = round(1.7,1)
b = round(1.76,1)
c = round(1.34,2)
d = round(1.347,2)
e = math.floor(3.7)
f = math.floor(3.4)
g = math.ceil(3.7)
h = math.ceil(3.4)

## mathemathische Operationen mit definierten Variablen
L = b / e
LL = b // e

## Listen erstelllen
my_list_a = [9, 10, "aloha", "friend", 76, 28]
my_list_b = [12, 222, ["fire", "water", "air", "earth"], "rose", "peach", 11, 54]
my_list_0 = [777]
my_list_array = [4, 8, 9, 11]

## Operationen mit Listen
my_list_a.append(12)
my_list_a.insert(0, "hell")
my_list_b.insert(2, 21)
my_list_b.remove(222)
my_list_a.pop(2)
my_list_0.clear()
länge_liste = len (my_list_array) 
# Operationen mit den Indexen von Listen
first_item = my_list_a[0]
last_item = my_list_a[-1]
sequence = my_list_a [3:5]
two_step = my_list_a [3:7:2]
backwards = my_list_a[::-1]
middle_item = my_list_array [len(my_list_array) // 2] # nur bei geraden Längen der jeweiligen Liste!
dimensional = my_list_b[3][2]

# Tupels erstellen
my_tupel_a = (4, 8, 12, 16)
my_tupel_b = (9, 9, 9)

## Operationen mit Tupels
länge_tupel = len (my_tupel_a)

## Dictionaries erstellen
# Kategorien (wie title) sind key und Informationen dazu (wie Der Marisaner) values (auch Listen können Values sein) - es sind Wertepaare
my_dict_a = {
    "title": "Der Marsianer",
"year": 2015,
    "random": ["Why", "should", "we", "do" "this", "?"]
}

## Operationen mit Dictionaries
länge_dictionarie = len (my_dict_a) # ergibt die Anzahl der keys!

## NumPy - enthält Arrays und Matrizen
# Jede Matrix ist ein Array, aber nicht jedes Array eine Matrix!
import numpy as np
array_a = np.zeros(10)
array_b = np.ones(10)
array_list = np.array(my_list_array)
array_list1 = ([[1, 4, 8], [5, 8, 7]])

## Operationen mit Arrays
# 2D Array t aus einer Liste von Listen
array2D_listen = np.array([[1, 2, 3], [4, 5, 6]])
# ein 2D Array gefüllt mit Nullen
array2D_nullen = np.zeros((3, 4))
# Ein 2D Array gefüllt mit Einsen
array2D_einsen = np.ones((2, 2))
# Ein 2D Array mit zufälligen Kommazahlen zwischen 0 und 1
array2D_random = np.random.rand(2, 3)
# Ein 3D Array gefüllt mit Nullen
array3D_nullen = np.zeros((3, 2, 4))
# Ein 3D Array gefüllt mit Einsen
array3D_einsen = np.ones((3, 2, 4))
# Ein 3D Array gefüllt mit Zufallszahlen
array3D_random = np.random.rand(2, 3, 2)
# Ein 3D Array gefüllt mit bestimmten Werten
array3D_werte = np.full((2, 2, 2), 5)
# Zurgiffe auf Elemente aus Arrays
zu1 = array_list1[1][2] # Zugriff auf Zeile 2, Spalte 3
zu2 = array_list1 [0:2][1:2] # mehrdiomesionales Sequenzieren
zu3 = np.array(array_list1)[np.array(array_list1) > 4] # Boolean-Indexierung
zu4 = array_list1 [1] = 9 # Werte zuweisen

##Logische Variablen
tt = True
ff = False
# "==" heißt quasi "ist identisch mit"
test1 = tt == True
test2 = tt == ff

## Relationale Operatoren
var1 = 4;

## ergebnisse werden gerechnet
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)
print (h)
print ()
print (L)
print (LL)
print ()
print (my_list_a)
print (my_list_b)
print (my_list_0)
print ()
print (my_tupel_a)
print (my_tupel_b)
print ()
print (my_dict_a)
print ()
print (array_a)
print (array_b)
print (array_list)
print (array_list1)
print ()
print (first_item)
print (last_item)
print (sequence)
print (two_step)
print (backwards)
print (middle_item)
print (dimensional)
len (my_tupel_a)
len (my_list_array) 
print ()
print (länge_liste)
print (länge_tupel)
print (länge_dictionarie)
print ()
print (array2D_listen)
print (array2D_nullen)
print (array2D_einsen)
print (array2D_random)
print (array3D_nullen)
print (array3D_einsen)
print (array3D_random)
print (array3D_werte)
print ()
print (zu1)
print (zu2)
print (zu3)
print (zu4)
print ()
print (test1)
print (test2)
print()

## Rechnen mit relationalen Operatoren
print (4 < 6)
print (4 > 6)
print (4 == 6)
print (4 != 6)
print (4 >= 6)
print (4 <= 6)
print ()
print (var1)
print ((var1 > 3) and (var1 < 6))
print ((var1 > 5) and (var1 < 6))
print ((var1 > 5) or (var1 < 6))
print ((var1 > 5) or (var1 < 3))
print ((var1 > 3) ^ (var1 < 6))
print ((var1 > 5) ^ (var1 < 6))

## If- und Match-Statements sowie hilfreiche Commands
# If-Statement

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

while True:
        try:
            größe = input ("Bitte geben Sie Ihre Körpergröße in cm ein (ganze Zahlen):")
            Größe = int(größe)
            if 0 <= Größe <= 300:
                break
            else:
                print(RED + "Ungültige Eingabe. Bitte geben Sie eine ganze Zahl zwischen 0 und 300 ein." + RESET)
        except ValueError:
            print(RED + "Ungültige Eingabe. Bitte machen Sie eine gültige Eingabe." + RESET)

if 0 <= Größe < 100:
     print("Hmmmmmm ...")
elif 100 <= Größe < 150:
     print("Darfst du schon an den Computer?")
elif 150 <= Größe < 160:
    print("Klein aber Oho!")
elif 160 <= Größe < 170:
    print("Willkommen in der deutschen Norm.")
elif 170 <= Größe < 180:
    print("Willkommen in der deutschen Norm.")
elif 180 <= Größe < 190:
    print("Fast schon groß!")
elif 190 <= Größe < 200:
    print("Größe ist nicht alles!")
elif 200 <= Größe < 300:
    print("Entweder lügt hier jemand oder wir haben einen Riesen gefunden!")
else:
    print("Warum bist du noch wach?")

# Match -Statement
options = ["Methylphenidate", "Placebo", "None", "?"]
print("Available options:", options) 

eingabe = "" 

while True:
        eingabe = input("Please enter your given Method: ") 

        if eingabe in options:
            break 
        else:
            print(RED + "Invalid Information. Please choose one of the following: " + str(options) + RESET)

match eingabe:
    case "None":
        print("No treatment.")
    case "Placebo":
        print("You hope so :)")
    case "Methylphenidate":
        print("Most likely treated with Ritalin.")
    case "?":
        print("Please do not sleep while participating in our experiments!")

# hilfreiche Commands
my_string = "5"
my_int = int(my_string)
print(my_int)
print(type(my_int))
print(my_string)
print(type(my_string))
print()
my_float = float(my_int)
print (my_float)
print(type(my_float))
print()
my_str = str(my_float)
print(my_str)
print(type(my_str))
print()
my_in = int(my_float)
print(my_in)
print(type(my_in))
print()

print(isinstance(my_float, float))
print(isinstance(my_float, int))










