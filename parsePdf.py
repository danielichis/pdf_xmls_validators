import pandas as pd
import datetime
import locale
import pdfplumber
import re

def parse_date(entireText):
  locale.setlocale(locale.LC_TIME, "es_ES")
  day=re.findall(r"Fecha de emisión  (\d+)  de  ([a-zA-z]+)  del  (\d+)",entireText,flags=re.I)[0][0]
  month=re.findall(r"Fecha de emisión  (\d+)  de  ([a-zA-z]+)  del  (\d+)",entireText,flags=re.I)[0][1]
  year=re.findall(r"Fecha de emisión  (\d+)  de  ([a-zA-z]+)  del  (\d+)",entireText,flags=re.I)[0][2]
  fecha=f"{day}-{month}-{year}"
  t = datetime.datetime.strptime(fecha, "%d-%B-%Y").date()
  #print(t)
  return t
def pdff(ruta):
  with pdfplumber.open(ruta) as temp:
    #print(f"validando ruta:...{ruta}")
    first_page = temp.pages[0]
    entireText=first_page.extract_text()
    #print(entireText)
  nameFile=re.findall(r"(\d{9,}.+)\.",ruta)[0]
  nameFile_ext=f"{nameFile}.pdf"
  rucSupplier=re.findall(r"R\.U\.C\.  (\d+)",entireText,flags=re.I)[0]
  nameSupplier=re.findall(r"(\A.*)",entireText,flags=re.I)[0].strip()
  totalPriceAmount=re.findall(r"Total por honorarios:  (\d+.\d+)",entireText,flags=re.I)[0]
  emissionDate=str("'"+str(parse_date(entireText)))
  rucClient=re.findall(r"Identificado con  RUC  número  (\d+)",entireText,flags=re.I)[0]
  nameClient=re.findall(r"Recibí de:  (.+)",entireText,flags=re.I)[0].strip()
  lettersAmount=re.findall(r"La suma de:  (.+) SOLES",entireText,flags=re.I)[0]
  serialNumber=re.findall(r"Nro: (E\d{3})- \d+",entireText,flags=re.I)[0]
  netPriceAmount=re.findall(r"Total Neto Recibido: (\d+\.\d+) SOLES",entireText,flags=re.I)[0]
  vouchNumber=re.findall(r"_(\d+).pdf",ruta)[0]
  typeDocument=re.findall(r"_(\d+)_",ruta)[0]
  supplierInfoList=[]
  supplierInfo={
        'nameFile':nameFile_ext,
        'nameFilee':nameFile,
        'RUC EMISOR':rucSupplier,
        'NOMBRE EMISOR':nameSupplier,
        'PRECIO TOTAL BRUTO':totalPriceAmount,
        'PRECIO TOTAL NETO':netPriceAmount,
        'FECHA DE EMISION':emissionDate,
        'RUC RECEPTOR':rucClient,
        'NOMBRE RECEPTOR':nameClient,
        'PRECIO LETRAS':lettersAmount,
        'NUMERO COMPROBATE':vouchNumber,
        'SERIE':serialNumber,
        'TIPO DOCUMENTO':typeDocument,
  }
  supplierInfoList.append(supplierInfo)
  return supplierInfo
  #df=pd.DataFrame(supplierInfoList)
#print(df)
#print("imprimiendo fuera de la funcion")
#print(pdff(r'C:/Users/LENOVO/Documents/RobotDaniel/XML PDF PARSER/pdfsFolder/10480238011_02_E001_20.pdf'))
#parse_date()