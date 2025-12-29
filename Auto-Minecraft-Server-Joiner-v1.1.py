import time
import pyautogui
from win11toast import toast
from mcstatus import JavaServer

def joinProcess():
    for i in range(10, -1, -1):
        print(f"\rSkript startet in: {i:2d} seconds", end="")
        time.sleep(1)
    print("")
    
    server = JavaServer.lookup(serverIp)
    
    while True:
        try:
            serverStatus = server.status()
            onlinePlayers = serverStatus.players.online
            print(f"Aktuell online: {onlinePlayers}/{maxSlots}")

            if onlinePlayers < maxSlots:
                print("\nSlot frei! Betrete Server...")
                pyautogui.moveTo(702, 127)
                pyautogui.click()
                toast("Auto Minecraft Server Joiner v1.1", "Slot frei! Betrete Server...")
                break
        except Exception as e:
            print("Error:", e)

        time.sleep(checkInterval)

print("-- Auto Minecraft Server Joiner v1.1 --")

print("Wähle die Auflösung deines Monitors aus")
print("Gib die Nummer 1 für 1080p ein")
chosenResolution = input("Wähle eine Nummer: ")

if int(chosenResolution) == 1:
    print("Preloads / Custom")
    print("Gib die Nummer 1 für das HugoSMP Preload ein")
    print("Gib die Nummer 2 für eine Custom Config ein")
    chosenPreloadOrCustom = input("Wähle eine Nummer: ")

    if int(chosenPreloadOrCustom) == 1:
        serverIp = "play.hugosmp.net"
        maxSlots = int(input("Gib die Maximalen Slots vom Server ein: "))
        checkInterval = int(input("Gib in Sekunden ein wie oft das Script die Daten vom Minecraft Server abrufen soll (Default: 4 Sekunden): "))
        joinProcess()
    elif int(chosenPreloadOrCustom) == 2:
        serverIp = input("Gib die IP Adresse/URL des Servers ein: ")
        maxSlots = int(input("Gib die Maximalen Slots vom Server ein: "))
        checkInterval = int(input("Gib in Sekunden ein wie oft das Script die Daten vom Minecraft Server abrufen soll (Default: 4 Sekunden): "))
        joinProcess()
    else:
        print("Error: Bitte starte diese App neu!")
        input("Drück Enter um diese App zu beenden: ")
else:
    print("Error: Bitte starte diese App neu!")
    input("Drück Enter um diese App zu beenden: ")
