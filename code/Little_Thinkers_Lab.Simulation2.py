# ==========================================================
# Digitales System – Kinderarztpraxis "Little Thinkers Lab"
# Simulation eines sicheren Informatiksystems
# Funktionen:
# - Benutzerlogin
# - Rollenbasierte Zugriffskontrolle
# - Patientenaktenverwaltung
# - Datensicherungssimulation
# ==========================================================

# Benutzerdatenbank (Simulation)
benutzer_db = {
    "arzt": {"passwort": "1234", "rolle": "Arzt"},
    "mfa": {"passwort": "abcd", "rolle": "MFA"},
    "admin": {"passwort": "admin", "rolle": "Administrator"}
}

# Patientenakte (Simulation)
patientenakte = {
    "Name": "Emma Schneider",
    "Alter": "5",
    "Diagnose": "Grippe"
}


# =============================
# Funktionen
# =============================

def login():
    print("=== Login System ===")

    benutzername = input("Benutzername: ")
    passwort = input("Passwort: ")

    if benutzername in benutzer_db:
        if benutzer_db[benutzername]["passwort"] == passwort:
            rolle = benutzer_db[benutzername]["rolle"]
            print(f"\nLogin erfolgreich. Rolle: {rolle}\n")
            return rolle
        else:
            print("Falsches Passwort.")
            return None
    else:
        print("Benutzer nicht gefunden.")
        return None


def patientenakte_anzeigen():
    print("\n=== Patientenakte ===")
    for key, value in patientenakte.items():
        print(f"{key}: {value}")
    print("=====================\n")


def patientenakte_bearbeiten():
    print("\n=== Patientenakte bearbeiten ===")

    neue_diagnose = input("Neue Diagnose eingeben: ")
    patientenakte["Diagnose"] = neue_diagnose

    print("Patientenakte wurde erfolgreich aktualisiert.\n")


def backup_erstellen():
    print("\n=== Datensicherung ===")
    print("Backup wird vorbereitet...")
    print("Patientendaten werden gesichert...")
    print("Backup erfolgreich abgeschlossen.\n")


def arzt_menu():
    while True:
        print("=== Arzt Menü ===")
        print("1 - Patientenakte anzeigen")
        print("2 - Patientenakte bearbeiten")
        print("3 - Logout")

        auswahl = input("Auswahl: ")

        if auswahl == "1":
            patientenakte_anzeigen()

        elif auswahl == "2":
            patientenakte_bearbeiten()

        elif auswahl == "3":
            print("Logout erfolgreich.\n")
            break

        else:
            print("Ungültige Eingabe.\n")


def mfa_menu():
    while True:
        print("=== MFA Menü ===")
        print("1 - Patientenakte anzeigen")
        print("2 - Logout")

        auswahl = input("Auswahl: ")

        if auswahl == "1":
            patientenakte_anzeigen()

        elif auswahl == "2":
            print("Logout erfolgreich.\n")
            break

        else:
            print("Zugriff verweigert oder ungültige Eingabe.\n")


def admin_menu():
    while True:
        print("=== Administrator Menü ===")
        print("1 - Backup erstellen")
        print("2 - Logout")

        auswahl = input("Auswahl: ")

        if auswahl == "1":
            backup_erstellen()

        elif auswahl == "2":
            print("Logout erfolgreich.\n")
            break

        else:
            print("Ungültige Eingabe.\n")


# =============================
# Hauptprogramm
# =============================

def main():

    print("===================================")
    print("Little Thinkers Lab – System Start")
    print("===================================\n")

    while True:   # ← Das sorgt dafür, dass das System weiterläuft

        rolle = login()

        if rolle == "Arzt":
            arzt_menu()

        elif rolle == "MFA":
            mfa_menu()

        elif rolle == "Administrator":
            admin_menu()

        else:
            print("Login fehlgeschlagen.\n")

        # Nach Logout zurück zum Login oder beenden?
        print("Möchten Sie sich erneut einloggen?")
        print("1 - Ja")
        print("2 - Programm beenden")

        auswahl = input("Auswahl: ")

        if auswahl == "2":
            print("System wird beendet...")
            break   # ← beendet die while-Schleife


# Programm starten
main()
