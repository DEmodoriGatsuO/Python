Attribute VB_Name = "Module1"
Option Explicit
'1. VBE(Visual Basic Editor)��[�c�[��]�^�u����[�Q�Ɛݒ�]
'2.�uWindows Script Host Object Model�v�Ƀ`�F�b�N����[OK]
Sub runPyfile()

Dim wsh As WshShell
Set wsh = CreateObject("WScript.Shell")
Dim pyCmd As String
Dim argv As Variant

argv = Array("����1", "����2", "����3")

pyCmd = "python " + "--File FullPath-- " & " " & argv(0) & " " & argv(1) & " " & argv(2)
Call wsh.Exec(pyCmd)

End Sub
