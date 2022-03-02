#%% フォルダ内のPowerPointをPDFに変換
#Editor De'modori Gatsuo
# ---------------------
import sys
import os
import comtypes.client
import datetime

dt_now = datetime.datetime.now()
str_dt_now = dt_now.strftime('%Y%m%d%H%M%S')

# #%% arguments
file_folder_path = sys.argv[0]
input_folder_path = sys.argv[1]
output_folder_path = os.path.dirname(file_folder_path) + "\\" + str_dt_now

#%% Windows用
input_folder_path = os.path.abspath(input_folder_path)
output_folder_path = os.path.abspath(output_folder_path)
# folderを作る_日付を文字列yyyyMMddhhmmss
os.mkdir(output_folder_path)

#%% ドラッグアンドドロップするフォルダのファイルをリストで取得する
input_file_paths = os.listdir(input_folder_path)

#%% Convert each file
office_flg = {"ppt":False, "doc":False,"xlsx":False}
for input_file_name in input_file_paths:
    # 開くファイルのパスを作成
    input_file_path = os.path.join(input_folder_path, input_file_name)
    file_name = os.path.splitext(input_file_name)[0]
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
    if input_file_name.lower().endswith((".ppt", ".pptx")):
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1
        slides = powerpoint.Presentations.Open(input_file_path)
        slides.SaveAs(output_file_path, 32)
        slides.Close()
        office_flg["ppt"] = True
    elif input_file_name.lower().endswith((".doc", ".docx")):
        word = comtypes.client.CreateObject("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(input_file_path)
        doc.SaveAs(output_file_path, 17)
        doc.Close()
        office_flg["doc"] = True
    elif input_file_name.lower().endswith((".xls", ".xlsx")):
        excel = comtypes.client.CreateObject("Excel.Application")
        excel.Visible = False
        xl = excel.Workbooks.Open(input_file_path)
        xl.ExportAsFixedFormat(0,output_file_path,1,0)
        xl.Close()
        office_flg["xlsx"] = True

if office_flg["ppt"]:
    powerpoint.Quit()
elif office_flg["doc"]:
    word.Quit()
elif office_flg["xlsx"]:
    excel.Quit() 

print("Complete")