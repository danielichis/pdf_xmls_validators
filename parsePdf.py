import pandas as pd
import pdfplumber
import re
def pdff(ruta):
  with pdfplumber.open(ruta) as temp:
    print(f"validando ruta:...{ruta}")
    first_page = temp.pages[0]
    entireText=first_page.extract_text()
    print(entireText)
    nameSupplier=re.findall(r"(\A.*)",entireText,flags=re.I)[0]
    dniSupplier=re.findall(r"R\.U\.C\.  (\d+)",entireText,flags=re.I)[0]
    priceAmount=re.findall(r"Total Neto Recibido: (\d+\.\d+) SOLES",entireText,flags=re.I)[0]
    nameFile=re.findall(r"(\d{9,}.+)\.",ruta)[0]
  supplierInfoList=[]
  supplierInfo={
      'nameFile':nameFile,
      'DNI':dniSupplier,
      'NOMBRES':nameSupplier,
      'PRECIO_SERVICIO':priceAmount,
  }
  supplierInfoList.append(supplierInfo)
  return supplierInfo
  #df=pd.DataFrame(supplierInfoList)
#print(df)
print("imprimiendo fuera de la funcion")
print(pdff(r'C:/Users/LENOVO/Documents/RobotDaniel/XML PDF PARSER/pdfsFolder/10480238011_02_E001_20.pdf'))
