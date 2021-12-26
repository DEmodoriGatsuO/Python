from tkinter import *
from tkinter import messagebox, ttk

class LogonView():
    def __init__(self):
        self.createWidget()

    def createWidget(self):
        self.root = Tk()
        self.root.title("Log On")
        frame1 = ttk.Frame(self.root, padding=(32))
        frame1.grid()

        #### １行目
        label1 = ttk.Label(frame1, text='ユーザー名', padding=(10, 2))
        label1.grid(row=0, column=0, sticky=E)

        # Username Entry
        self.username = StringVar()
        self.username_entry = ttk.Entry(frame1, textvariable=self.username, width=30)
        self.username_entry.grid(row=0, column=1)

        #### 2行目
        label2 = ttk.Label(frame1, text='パスワード', padding=(10, 2))
        label2.grid(row=1, column=0, sticky=E)

        # Password Entry
        self.password = StringVar()
        self.password_entry = ttk.Entry(frame1, textvariable=self.password, width=30, show='*')
        self.password_entry.grid(row=1, column=1)

        #### 3行目
        button1 = ttk.Button(frame1, text='ログイン', command=self.validate_login)
        button1.grid(row=2, column=1, columnspan=2, sticky=E)

        #### 4行目（列を繋げてる）
        label3 = ttk.Label(frame1, text='ユーザー名とパスワードを入力してください。', padding=(5, 2))
        label3.grid(row=3, column=0, columnspan=2, sticky=E)

        self.root.mainloop()


    #ここが実際にやりたい動作になる    
    def validate_login(self):
        import os
        import sys
        cwd = os.getcwd()
        exeDir = sys.exec_prefix
        os.chdir(exeDir)
        import shelve
        shelf_file =shelve.open('mydata')
        shelf_file['USER_ID'] = self.username.get()
        shelf_file['PASSWORD'] = self.password.get()
        mydata = {'USER_ID' : shelf_file['USER_ID'], 'PASSWORD' : shelf_file['PASSWORD']}
        shelf_file.close()
        self.root.destroy()
        return mydata 

def main():
    import os
    import sys
    cwd = os.getcwd()
    exeDir = sys.exec_prefix
    os.chdir(exeDir)

    import shelve
    shelf_file =shelve.open('mydata')
    try:
        Userdata = {'USER_ID' : shelf_file['USER_ID']  , 'PASSWORD' : shelf_file['PASSWORD']}
        shelf_file.close()
    except:
        Userdata = LogonView()
    
    os.chdir(cwd)
    return Userdata

if __name__ == "__main__":
    main()

