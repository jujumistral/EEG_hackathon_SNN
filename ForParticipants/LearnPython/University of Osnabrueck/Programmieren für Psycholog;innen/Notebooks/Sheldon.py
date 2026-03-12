import random

RED = '\033[91m'
RESET = '\033[0m'
GREEN = '\033[92m'

print("Willkommen bei Schere, Stein, Papier, Echse, Spock!")
print("Ihr heutiger Gegner ist niemand Geringeres als Dr. Sheldon Cooper!")
print("-" * 40)

print()
spieler_name = ""
while True:
    spieler_name = input("Bitte geben Sie Ihren Namen ein: ").strip() # .strip() entfernt Leerzeichen am Anfang/Ende (Anmerkung von Gemini)
    if spieler_name: 
        break
    else:
        print(RED + "Sie haben keinen Namen? Das muss wohl ein Versehen gewesen sein! Bitte geben Sie einen gültigen Namen ein." + RESET)

print(f"\nHallo, {spieler_name}! Machen Sie sich bereit für eine intellektuelle Auseinandersetzung mit Sheldon.")
print("Sheldon: Ich bin nur wegen des Geldes hier! Ich möchte niemandes keimstrotzende Hände schütteln!")
print()
print("Scheldon: Die Regeln sind ganz einfach:")
print("  Scheldon: 1. Schere schneidet Papier, Schere köpft Echse.")
print("  Scheldon: 2. Papier bedeckt Stein, Papier widerlegt Spock.")
print("  Scheldon: 3. Stein zerquetscht Echse, Stein zertrümmert Schere.")
print("  Scheldon: 4.Echse vergiftet Spock, Echse frisst Papier.")
print("  Scheldon: 5. Spock verdampft Stein, Spock zerschmettert Schere.")
print ("Gespielt wird, bis jemand 3 Punkte gesammelt hat! Und Los!")
print("-" * 40)

options = ["Schere", "Stein", "Papier", "Echse", "Spock"]

## Definition der Regeln 
# Der Schlüssel ist das gewinnende Element und der Wert eine Liste der Elemente, die gegen ihn verlieren.
rules = {
    "Schere": ["Papier", "Echse"],
    "Papier": ["Stein", "Spock"],
    "Stein": ["Echse", "Schere"],
    "Echse": ["Spock", "Papier"],
    "Spock": ["Schere", "Stein"]
}

# Punkteverteilung
spieler_punkte = 0
sheldon_punkte = 0 
runden_count = 0

# Zielpunkte
ZIELPUNKTE = 3


while spieler_punkte < ZIELPUNKTE and sheldon_punkte < ZIELPUNKTE:
    print(f"\n{spieler_name}, Ihre Optionen: " + ", ".join(options))
    spieler_wahl = input(f"{spieler_name}, Ihre Wahl: ").capitalize()

    # 1. Validierung der Spielereingabe
    if spieler_wahl not in options:
        print(RED + "Ungültige Eingabe. Bitte wählen Sie eine der verfügbaren Optionen!" + RESET)
        continue

    # 2. Zufällige Wahl von Sheldon
    sheldon_wahl = random.choice(options)
    print(f"Sheldon wählt: {sheldon_wahl}")

    runden_count += 1

    # 3. Spiel-Logik (Wer gewinnt?)
    if spieler_wahl == sheldon_wahl:
        print("Unentschieden!" "\nSheldon: Wie amüsant, wir sind einer Meinung.")
    elif sheldon_wahl in rules[spieler_wahl]:
        print(GREEN + f"{spieler_name} hat gewonnen! ({spieler_wahl} besiegt {sheldon_wahl})" + RESET)
        spieler_punkte += 1
    else:
        print(RED + f"Sheldon hat gewonnen! ({sheldon_wahl} besiegt {spieler_wahl})" "\nSheldon: BAZINGA!" + RESET)
        sheldon_punkte += 1

    print(f"Aktueller Punktestand: {spieler_name} {spieler_punkte} - Sheldon {sheldon_punkte}")

print("\n--- Spiel beendet ---")
print(f"Endstand nach {runden_count} Runden: {spieler_name} {spieler_punkte} - Sheldon {sheldon_punkte}")

if spieler_punkte >= ZIELPUNKTE:
    print(GREEN + f"Herzlichen Glückwunsch, {spieler_name}! Sie haben Sheldon mit {spieler_punkte} zu {sheldon_punkte} besiegt!" "\nSheldon: Ich bin nicht verrückt. Meine Mutter hat mich testen lassen!" + RESET)
elif sheldon_punkte >= ZIELPUNKTE:
    print(RED + f"Schade {spieler_name}, leider hat Dr. Cooper mit {sheldon_punkte} zu {spieler_punkte} Punkten gewonne. Vielleicht beim nächsten Mal." "\nSheldon: Ich habe zwar Applaus erwartet. Aber ich nehme an, ehrfürchtiges Schweigen ist auch angemessen." + RESET)
else:
    print("Das Spiel endete unentschieden! Irgendwer hat hier geschummelt!")

print("Vielen Dank fürs Spielen!")