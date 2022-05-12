import enum
from docxtpl import DocxTemplate
from docx2pdf import convert
import pandas as pd
df_test=pd.read_csv("data test.csv",sep=";")
doc=DocxTemplate("PlantillaRHE.docx")
print(df_test)
data_test=df_test.to_dict()
for idx,emi in enumerate(data_test['RUC EMISOR']):
    context={
    "rucProvider":data_test['RUC EMISOR'][idx],
    "rucClient":data_test['RUC RECEPTOR'][idx],
    "nameProvider":data_test['NOMBRE EMISOR'][idx],
    "nameClient":data_test['NOMBRE RECEPTOR'][idx],
    "amountBrut":'{:.2f}'.format(data_test['PRECIO'][idx]),
    "amountNet":'{:.2f}'.format(data_test['PRECIO'][idx]),
    "serialNumber":data_test['SERIE'][idx],
    "id":'{:02.0f}'.format(data_test['NUMERO DOCUMENTO'][idx])
        }
    file_name=f"{data_test['RUC EMISOR'][idx]}_{'{:02.0f}'.format(data_test['TIPO DOCUMENTO'][idx])}_{data_test['SERIE'][idx]}_{data_test['NUMERO DOCUMENTO'][idx]}"
    print(file_name)
    doc.render(context)
    doc.save(f"{file_name}.docx")
    pdfpath = file_name+'.pdf'
    xmlpath = file_name+'.xml'
    convert(f"{file_name}.docx", pdfpath)
    #convert(f"{file_name}.docx", xmlpath)
print("listos")
