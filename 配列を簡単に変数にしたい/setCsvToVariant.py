def setCsvToVariant(input,output):
    import csv
    with open(input) as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    arr = l[0] #ヘッダー部分1行目
    for i in range(len(arr)):
        arr[i] = '"' + arr[i] + '"' #ダブルクオーテーションで囲む

    str_arr = "[" + ",".join(arr) + "]"
    
    output += r"\output.txt"
    with open(output, 'w', encoding='UTF-8') as f:
        f.write(str_arr)

import sys
import os
import time
input = sys.argv[1]
output = os.path.dirname(sys.argv[0])

print(input)
time.sleep(5)
setCsvToVariant(input,output)    

