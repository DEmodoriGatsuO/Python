# テキストファイルからraw文字列を取得してみる
def textToVar(path):
    import os
    dir = os.path.dirname(__file__)
    output = dir + r"\output.txt"
    
    with open(path,'rt',encoding="utf-8") as f:
        b = True
        while True:
            line = f.readline()
            line = line.replace('\n', '\\n"\n')
            if line:
                if b:
                    str_data = 'let txt = "' + line
                    b = False
                else:
                    str_data += r'txt += "' + line
            else:
                break
        str_data += '"'
    with open(output,'w') as f:
        f.write(str_data)
        
import sys
path = sys.argv[1]
textToVar(path)
