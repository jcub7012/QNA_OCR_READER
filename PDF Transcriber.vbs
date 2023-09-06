Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Users\User\transcriber\PDF Transcriber.bat" & Chr(34), 0
Set WshShell = Nothing
