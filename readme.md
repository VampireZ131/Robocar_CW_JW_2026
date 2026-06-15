Hardware des Robocars:
Raspberry Pi 3
PCA9685 PWM-Modul
3x Liniensensoren
4x DC-Motoren


WICHTIG: Damit alles funktioniert muss das Programm in Linux ausgeführt werden.

# Python-Anwendung zur Hardware-Steuerung am Raspberry Pi

Diese Anleitung beschreibt die Vorbereitung der Software-Umgebung, um die GPIO-Pins des Raspberry Pi mittels Python anzusteuern.

## 1. Installation der Hardware-Schnittstelle (lgpio)
Um die Pin-Leiste des Raspberry Pi über Python-Befehle zu steuern, ist die Installation der Software **lgpio** erforderlich.

1.  **System-Voraussetzungen:** Installieren Sie zunächst die benötigten Tools mit:
    `sudo apt install swig python3-dev python3-setuptools`.
2.  **Download & Installation:**
    *   Laden Sie das Paket herunter: `wget http://abyz.me.uk/lg/lg.zip`.
    *   Entpacken und installieren Sie es: `unzip lg.zip`, `cd lg`, `make`, `sudo make install`.
3.  **Dienst starten:** Starten Sie den notwendigen Daemon im Hintergrund mit dem Befehl `rgpiod &`.

## 2. Einrichtung der virtuellen Python-Umgebung
Um Python-Bibliotheken sauber voneinander getrennt zu verwalten, wird eine **virtuelle Umgebung (venv)** verwendet.

*   **Erstellung:** Erzeugen Sie die Umgebung mit `python3 -m venv .robocar`.
*   **Aktivierung:** Nutzen Sie den Befehl `source .robocar/bin/activate`. Eine erfolgreiche Aktivierung erkennen Sie am Kürzel `(.robocar)` am Anfang Ihrer Kommandozeile.
*   **Bibliotheken installieren:** Installieren Sie innerhalb der aktiven Umgebung das Interface für die Hardware-Steuerung:
    `pip3 install gpiozero lgpio`.

## 3. Projektorganisation und Entwicklungsumgebung
Für eine strukturierte Softwareentwicklung wird die Nutzung von **Visual Studio Code (VSC)** auf einem Laptop empfohlen, der per Remote-Verbindung auf den Pi zugreift.

*   **Ordnerstruktur:**
    1. Erstellen Sie ein Projektverzeichnis: `mkdir robocar`.
    2. Legen Sie darin einen Quellcode-Ordner namens `src` an.
*   **Remote-Entwicklung mit VSC:**
    1. Nutzen Sie die Funktion „Connect to Host...“ über das Remote-Window-Symbol in VSC.
    2. Verbinden Sie sich via SSH (`BENUTZERNAME@HOSTNAME.local`).
    3. Öffnen Sie in VSC das Verzeichnis `/home/pi/robocar`.


## 4. Programmausführung
Die Ausführung der Programme erfolgt über das Terminal in VSC. Achten Sie darauf, dass für die Ausführung von Skripten, die auf Hardware-Ressourcen zugreifen, die virtuelle Umgebung aktiviert sein muss.

## 5. Arbeiten mit GitHub
Um Dateien zwischen deinem Laptop und dem Raspberry Pi zu synchronisieren, nutzt du **git**.

### Ersteinrichtung (Clone)
Falls du das Repository noch nicht auf dem Pi hast, kopiere es von GitHub:
*   `git clone <LINK_ZUM_REPO>`.
*   Wechsle in den Ordner: `cd <REPOSITORY_NAME>`.

### Dateien auf den neuesten Stand bringen (Pull)
Bevor du ein Programm startest, stelle sicher, dass du die aktuellste Version von der Cloud hast:
*   `git pull origin`.

### Eigene Änderungen hochladen (Add/Commit/Push)
Wenn du neuen Code (z. B. in `main.py`) erstellt hast:
1.  **Änderungen vormerken:** `git add <NAME_DER_DATEI>`.
2.  **Speichern mit Kommentar:** `git commit -m "DEIN_KOMMENTAR"`.
3.  **In die Cloud hochladen:** `git push origin`.

## 6. Programme starten
Um ein Programm (z. B. im Ordner `src`) auszuführen, folge diesen Schritten im Terminal:

1.  Stelle sicher, dass die virtuelle Umgebung aktiv ist: `source .robocar/bin/activate`.
2.  Navigiere in dein Projektverzeichnis.
3.  Starte das Skript main.py:
    `python3 src/main.py`.

***
*Tipp: Zur besseren Übersicht wird die Verwendung von **Visual Studio Code** mit der Erweiterung „Remote-SSH“ empfohlen, um Dateien direkt auf dem Pi zu bearbeiten. Es wurde jedoch Festgestellt dass VSCode den Arbeitsspeicher des Raspberries voll macht und deshalb wurde auf die Anwendung **Zed** gewechselt, da diese dieses Problem nicht hat*