import tkinter as tk
from tkinter import messagebox
import sys

def main(argv1,argv2,argv3):
	with open("test.txt",mode = 'w') as f:
		f.write(argv1)
		f.write(argv2)
		f.write(argv3)
	root = tk.Tk()
	root.withdraw()
 
	title = "実行確認"
	msg = argv1 + " " + argv2 + " " + argv3 + " チェック"

	messagebox.showinfo(title, msg)
 
if __name__ == "__main__":
	argv = sys.argv
	argv1 = str(argv[1])
	argv2 = str(argv[2]) 
	argv3 = str(argv[3])
	main(argv1,argv2,argv3)