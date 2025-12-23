Auto Minecraft Server Joiner

Beschreibung
Auto Minecraft Server Joiner ist ein Python-Skript, das die Spieleranzahl eines Minecraft Java-Servers überwacht und automatisch klickt, sobald ein Slot frei wird. Zusätzlich wird eine Windows-Toast-Benachrichtigung angezeigt. Das Skript ist für Windows und 1080p Auflösung optimiert.

Wichtige Hinweise / Disclaimer
Dieses Skript dient ausschließlich zu Lern- und Testzwecken. Der Autor übernimmt keine Verantwortung für Schäden, Sperrungen, Datenverlust oder rechtliche Konsequenzen, die durch die Nutzung entstehen.  
- Minecraft muss im vollen Fenstermodus laufen.  
- Minecraft muss nach dem Start-Countdown im Vordergrund bleiben.
- Der Server, dem automatisch beigetreten werden soll, muss sich an erster Stelle der Minecraft-Serverliste befinden.
- Das Skript funktioniert aktuell nur zuverlässig auf 1080p-Auflösung.  
- Mauskoordinaten müssen ggf. angepasst werden (pyautogui.moveTo(x, y)).

Funktionen 
- Überwacht die Spieleranzahl eines Servers via mcstatus.  
- Windows-Toast-Benachrichtigungen (win11toast).  
- Automatisches Klicken (pyautogui).  
- Interaktive Auswahl: vorkonfiguriertes Preload oder eigener Server.  

Installation und Nutzung
1. Repository klonen.  
2. Virtuelle Umgebung erstellen (optional).  
3. Pakete installieren: pip install -r requirements.txt.  
4. Skript starten: python Auto Minecraft Server Joiner.py.   
6. Achte darauf, dass Minecraft im Vordergrund läuft.

Fehlerbehebung
- Klick funktioniert nicht → Fenstermodus, Vordergrundstatus, Auflösung, Mauskoordinaten prüfen.  
- Toast-Benachrichtigung fehlt → Windows Notification Center prüfen.  
- Durchgehende mcstatus Timeout → Server-IP prüfen, Firewall prüfen, Intervall erhöhen.  
- Andere Auflösungen → Mauskoordinaten anpassen.

FAQ
- Ist das legal? Nur auf Servern, die automatisierte Verbindungen erlauben. Auf fremden Servern riskant.  
- Funktioniert es auf Linux/Mac? Kernlogik ja, Mausaktionen und Toasts nur unter Windows.  
- Warum nur 1080p? Maus-Koordinaten sind statisch auf 1080p abgestimmt.

Lizenz
MIT License. Nutzung, Kopieren, Modifizieren erlaubt, keine Haftung. Siehe LICENSE-Datei.

Credits
- pyautogui – Maus/Tastaturautomation  
- mcstatus – Serverstatusabfrage  
- win11toast – Windows Toast Notifications

Kontakt
Für Probleme oder Featurewünsche bitte ein Issue im Repository öffnen.
