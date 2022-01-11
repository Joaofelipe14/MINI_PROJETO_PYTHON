import os
import win32com.client as client

excel = client.Dispatch("excel.application")

for file in os.listdir(os.getcwd () + "/pastas/"):
    filename, fileextension = os.path.splitext(file)
    wb = excel.Workbooks.Open(os.getcwd() + "/pastas/" + file)
    output_path = os.getcwd() + "/novo/" + filename
    wb.SaveAs(output_path, 62)
    wb.Close()