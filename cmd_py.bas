Attribute VB_Name = "Module1"
Option Explicit
'1. VBE(Visual Basic Editor)の[ツール]タブから[参照設定]
'2.「Windows Script Host Object Model」にチェックして[OK]
Sub runPyfile()

Dim wsh As WshShell
Set wsh = CreateObject("WScript.Shell")
Dim pyCmd As String
Dim argv As Variant

argv = Array("引数1", "引数2", "引数3")

pyCmd = "python " + "--File FullPath-- " & " " & argv(0) & " " & argv(1) & " " & argv(2)
Call wsh.Exec(pyCmd)

End Sub
