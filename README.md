![ShareMouse Auto-Reload Banner](assets/banner.png)

# ShareMouse Auto-Reload

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

**ShareMouse Auto-Reload** ist ein Tool, das ShareMouse automatisch neu startet, um den Testzeitraum zurückzusetzen und eine unterbrechungsfreie Nutzung zu ermöglichen.

> [!NOTE]
> Dieses Projekt dient nur zu Bildungszwecken. Bitte unterstützen Sie die Entwickler von ShareMouse, indem Sie eine Lizenz erwerben, wenn Sie die Software produktiv nutzen.

---

## 🚀 Funktionen

- 🔄 **Automatischer Neustart**: Startet ShareMouse alle 5 Minuten neu.
- ⏱️ **Trial Reset**: Umgeht die Zeitbeschränkung der Testversion.
- 🪟 **Windows & macOS Support**: Skripte für beide Betriebssysteme enthalten.
- ⚡ **Autostart**: Einfache Einrichtung für den automatischen Start mit Windows.

## 🛠️ Installation & Nutzung (Windows)

### Option 1: Schneller Start (Empfohlen)

Wir haben eine Batch-Datei für die einfachste Nutzung vorbereitet.

1. Doppelklicken Sie auf **`Start_AutoReload.bat`**.
2. Ein schwarzes Konsolenfenster öffnet sich und startet ShareMouse.
3. Lassen Sie dieses Fenster offen (Sie können es minimieren).

### Option 2: Automatisch mit Windows starten

Damit Sie das Skript nicht jedes Mal manuell starten müssen:

1. Drücken Sie `Windows-Taste + R`.
2. Geben Sie `shell:startup` ein und drücken Sie `Enter`.
3. Erstellen Sie eine **Verknüpfung** zu `Start_AutoReload.bat` in diesem Ordner (Rechtsklick auf `Start_AutoReload.bat` -> Senden an -> Desktop (Verknüpfung erstellen), dann in den Ordner verschieben).

Jetzt startet das Tool automatisch beim Hochfahren Ihres PCs!

### Manuelle Nutzung (Python)

Falls Sie Python installiert haben und das Skript direkt nutzen möchten:

```bash
python sharemouse_windows.py
```

Stellen Sie sicher, dass ShareMouse unter einem der folgenden Pfade installiert ist:
- `C:\Program Files (x86)\ShareMouse\ShareMouse.exe`
- `C:\Program Files\ShareMouse\ShareMouse.exe`

---

## 🍎 Installation & Nutzung (macOS)

Für macOS Nutzer gibt es ein separates Python-Skript (`sharemouse.py`) und einen Daemon.

```bash
# Starten des Daemons (benötigt sudo für Dateizugriffe)
sudo python sharemouse.py start
```

Das Skript kopiert automatisch die notwendige `.plist` Datei und startet den Daemon.

---

## ❓ Häufige Fragen

**Muss ich die originale ShareMouse.exe noch starten?**
Nein. Unser Skript kümmert sich um den Start und Neustart der Anwendung.

**Warum startet sich ShareMouse alle 5 Minuten neu?**
Dies ist notwendig, um den Timer der Testversion zurückzusetzen.

---

Generated with ❤️ by Google Deepmind Agent