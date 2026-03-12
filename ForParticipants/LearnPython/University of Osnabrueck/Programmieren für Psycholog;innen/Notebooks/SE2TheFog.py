import re
import getpass

RED = '\033[91m'
GREEN = '\033[92m'
DARK_RED = '\033[31m'
BLACK_BACKGROUND = '\033[40m'
RESET = '\033[0m'

accounts = {}

def create_account():
    while True:
        username = input("Bitte geben Sie einen Usernamen ein (nur Buchstaben): ")
        if not re.match("^[a-zA-Z]+$", username):
            print(RED + "Der Username darf nur Buchstaben enthalten." + RESET)
            continue
# aus irgendeinem Grund kann ich bei getpass.getpass kein Passwort mehr eingeben - daher ist die Passworteingabe hier nicht im eigentlichen Sinne geschützt, vielleicht findet ja jemand meinen Fehler 
        while True:
            password = input ("Bitte geben Sie ein Passwort ein: ")
            if len(password) < 8:
                print(RED + "Das Passwort muss mindestens 8 Zeichen lang sein." + RESET)
                continue
            if not re.search("[a-z]", password):
                print(RED + "Das Passwort muss mindestens einen Kleinbuchstaben enthalten." + RESET)
                continue
            if not re.search("[A-Z]", password):
                print(RED + "Das Passwort muss mindestens einen Großbuchstaben enthalten." + RESET)
                continue
            if not re.search("[0-9]", password):
                print(RED + "Das Passwort muss mindestens eine Zahl enthalten." + RESET)
                continue
            if not re.search("[^a-zA-Z0-9]", password):
                print(RED + "Das Passwort muss mindestens ein Sonderzeichen enthalten." + RESET)
                continue
            break

        accounts[username] = password
        print(GREEN + "Account erfolgreich erstellt." + RESET)
        break

def login():
    username = input("Bitte geben Sie Ihren Usernamen ein: ")
    password = input ("Bitte geben Sie Ihr Passwort ein: ")

    if username == "TheBrokenScript" and password == "Run666The/Fog999Comes":
        print(BLACK_BACKGROUND + DARK_RED + "Null is coming..." + RESET)
        import time
        time.sleep(10)
        return False  # Programm soll sich beenden

    if username in accounts and accounts[username] == password:
        print(GREEN + "Zugang gewährt." + RESET)
        return True
    else:
        print(RED + "Fehlerhafte Eingabe." + RESET)
        return False

def get_greeting():
    while True:
        try:
            hour_str = input("Bitte geben Sie die aktuelle Tageszeit ein (ganze Zahl, 0-23): ")
            current_hour = int(hour_str)
            if 0 <= current_hour <= 23:
                break
            else:
                print(RED + "Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 0 und 23 ein." + RESET)
        except ValueError:
            print(RED + "Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein." + RESET)

    if 5 <= current_hour < 10:
        print("Guten Morgen!")
    elif 10 <= current_hour < 12:
        print("Mahlzeit!")
    elif 12 <= current_hour < 17:
        print("Einen schönen guten Mittag")
    elif 17 <= current_hour < 23:
        print("Gute Nacht!")
    else:
        print("Warum bist du noch wach?")

def check_temperature():
    while True:
        try:
            temp_str = input("Bitte geben Sie die aktuelle Temperatur in Celsius ein: ")
            temperature = float(temp_str)
            break
        except ValueError:
            print(RED + "Ungültige Eingabe. Bitte geben Sie eine Zahl ein." + RESET)

    if temperature < 0:
        print("Es ist eisig.")
    elif 0 <= temperature <= 13:
        print("Es ist kalt.")
    elif 14 <= temperature <= 25:
        print("Es ist angenehm.")
    else:
        print("Es ist heiß.")

if __name__ == "__main__":
    print("Willkommen bei TheFog!")
    create_account()

    print("\n--- Einloggen ---")
    while True: 
        login_successful = login() 

        if login_successful: 
            print("\n--- Informationen ---")
            get_greeting()
            check_temperature()
            print("\nSchön, dass Sie sich für TheFog entschieden haben! Wir freuen uns auf das nächste Mal.")
            break