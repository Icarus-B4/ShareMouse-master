![ShareMouse Auto-Reload Banner](assets/banner.png)

# ShareMouse Auto-Reload

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

**ShareMouse Auto-Reload** ist ein Tool, das ShareMouse automatisch neu startet, um den Testzeitraum zurückzusetzen und eine unterbrechungsfreie Nutzung zu ermöglichen.
Aktuelle ShareMouseSetup.exe kannst du hier herunterladen: https://sharemouse.io/download

> [!NOTE]
> Dieses Projekt dient nur zu Bildungszwecken. Bitte unterstützen Sie die Entwickler von ShareMouse, indem Sie eine Lizenz erwerben, wenn Sie die Software produktiv nutzen.

---

## 🚀 Funktionen

- 🔄 **Automatischer Neustart**: Startet ShareMouse alle 5 Minuten neu.
- ⏱️ **Trial Reset**: Umgeht die Zeitbeschränkung der Testversion.
- 🪟 **Windows & macOS Support**: Skripte für beide Betriebssysteme enthalten.
- ⚡ **Autostart**: Einfache Einrichtung für den automatischen Start mit Windows.

## 🛠️ Installation & Nutzung (Windows)

### Option 1: Automatisch mit Windows starten (Empfohlen)

Wir haben ein **Setup-Skript** vorbereitet, das alles automatisch einrichtet:

1. **Doppelklicken** Sie auf `Setup_Autostart.vbs`.
2. Es erscheint eine Bestätigung, dass die Verknüpfung erstellt wurde.
3. Fertig! ShareMouse startet ab jetzt automatisch mit Windows – Es **Wird in Autotart von Apps** als **ShareMouse_AutoReload.exe** angezeigt und kann jeder Zeit beendet werden.

> [!TIP]
> Das Setup erstellt eine Verknüpfung im Windows-Autostart, die `ShareMouse_AutoReload.exe` startet. Diese Datei wurde mit dem ShareMouse-Icon kompiliert, sodass sie korrekt im Task-Manager angezeigt wird.

### Option 2: Manueller Start

Falls Sie ShareMouse nur einmalig starten möchten:

- **Mit Fenster (für Fehlersuche):** Doppelklicken Sie auf `Start_AutoReload.bat`
- **Ohne Fenster:** Doppelklicken Sie auf `ShareMouse_AutoReload.exe`

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

Generated with ❤️ by Icarus-B4 Deepmind Agent
