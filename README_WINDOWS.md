# ShareMouse Auto-Reload for Windows

Dieses Skript ist eine Windows-Adaption des ursprünglichen ShareMouse-Auto-Reload-Tools. ShareMouse startet automatisch alle 5 Minuten neu, um den Testtimer zurückzusetzen.

## Voraussetzungen
- Python installiert (wahrscheinlich bereits vorhanden, wenn Sie dies ausführen).
- ShareMouse installiert unter `"C:\Program Files (x86)\ShareMouse\ShareMouse.exe"`.

## Verwendung

## Einfacher Start (Easy Start)

Anstatt den Befehl jedes Mal einzutippen, habe ich eine Datei **`Start_AutoReload.bat`** erstellt.
1. Einfach doppelt auf `Start_AutoReload.bat` klicken.
2. ShareMouse wird gestartet und alle 5 Minuten neu geladen.
3. Das schwarze Fenster muss offen bleiben (Sie können es minimieren).

## Automatisch mit Windows starten (Autostart)

Wenn Sie möchten, dass das Skript immer automatisch läuft, wenn Sie den PC einschalten:

1. Drücken Sie `Windows-Taste + R`.
2. Geben Sie `shell:startup` ein und drücken Sie Enter. Ein Ordner öffnet sich.
3. Klicken Sie mit der **rechten Maustaste** auf meine Datei `Start_AutoReload.bat`.
4. Wählen Sie "Senden an" -> "Desktop (Verknüpfung erstellen)".
5. Verschieben Sie diese neue Verknüpfung vom Desktop in den gerade geöffneten `Startup` (Autostart) Ordner.

Ab jetzt startet das Skript automatisch mit Windows! Sie müssen ShareMouse dann **nicht** mehr manuell starten. Unser Skript erledigt das für Sie.

## Häufige Fragen
**F: Muss ich die originale `ShareMouse.exe` noch starten?**
A: Nein. Starten Sie einfach nur noch dieses Skript (oder lassen Sie es per Autostart laufen). Es kümmert sich um den Start von ShareMouse.
