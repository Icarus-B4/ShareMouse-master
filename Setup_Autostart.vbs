Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is running
ScriptPath = FSO.GetParentFolderName(WScript.ScriptFullName)

' Path to the Startup folder
StartupPath = WshShell.SpecialFolders("Startup")

' Cleanup old shortcuts or files to ensure clean state
FilesToDelete = Array("Start ShareMouse Silent.lnk", "Start_AutoReload.bat", "Start_Silent.vbs", "Start_Silent.lnk", "ShareMouse AutoReload.lnk", "ShareMouse_AutoReload.lnk")
For Each File In FilesToDelete
    FilePath = StartupPath & "\" & File
    If FSO.FileExists(FilePath) Then
        FSO.DeleteFile(FilePath)
    End If
Next

' Create the shortcut pointing to the compiled EXE (which has the icon embedded)
Set Shortcut = WshShell.CreateShortcut(StartupPath & "\ShareMouse AutoReload.lnk")

' Set shortcut properties - now pointing to the EXE
Shortcut.TargetPath = ScriptPath & "\ShareMouse_AutoReload.exe"
Shortcut.WorkingDirectory = ScriptPath
Shortcut.Description = "Starts ShareMouse AutoReload Silently"
' The EXE has the icon embedded, but we also set it on the shortcut for good measure
Shortcut.IconLocation = ScriptPath & "\ShareMouse_AutoReload.exe"

' Save the shortcut
Shortcut.Save

MsgBox "Setup Complete!" & vbCrLf & vbCrLf & "Shortcut created: ShareMouse AutoReload.lnk" & vbCrLf & "Target: ShareMouse_AutoReload.exe (with embedded icon)", 64, "ShareMouse AutoReload"

Set Shortcut = Nothing
Set FSO = Nothing
Set WshShell = Nothing
