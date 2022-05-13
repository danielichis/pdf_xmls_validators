import pandas as pd
import bs4
import re
def xmll(ruta):
    with open(ruta) as page:
        soup = bs4.BeautifulSoup(page, 'xml')
    nameFile=re.findall(r"(\d{9,}.+)\.",ruta)[0]
    nameFile_ext=f"{nameFile}.xml"
    suplierOb=soup.find('cac:AccountingSupplierParty')
    rucSupplier=suplierOb.find('cbc:CustomerAssignedAccountID').text
    nameSupplier=suplierOb.find('cbc:Name').text.strip()
    totalPriceAmount=soup.find('cbc:PayableAmount').text
    netPriceAmount=soup.find('cbc:PriceAmount').text
    emissionDate=soup.find('cbc:IssueDate').text
    vouchNumber=re.findall(r"_(\d+).xml",ruta)[0]
    lettersAmount=soup.find('cbc:Note').text
    lettersAmount=re.findall(r"(.+)SOLES",lettersAmount)[0].strip()
    serialNumber=soup.find('cac:OrderReference').find('cbc:ID').text
    serialNumber=re.findall(r"(E\d+)-\d+",serialNumber)[0].strip()
    rucClient=soup.find('cac:AccountingCustomerParty').find('cbc:CustomerAssignedAccountID').text
    nameClient=soup.find('cac:AccountingCustomerParty').find('cac:Party').find('cac:PartyName').find('cbc:Name').text.strip()
    typeDocument=re.findall(r"_(\d+)_",ruta)[0]
   
    supplierInfoList=[]
    supplierInfo={
        'nameFile':nameFile_ext,
        'nameFilee':nameFile,
        'RUC EMISOR':rucSupplier,
        'NOMBRE EMISOR':nameSupplier,
        'PRECIO TOTAL BRUTO':totalPriceAmount,
        'PRECIO TOTAL NETO':netPriceAmount,
        'FECHA DE EMISION':"'"+str(emissionDate),
        'RUC RECEPTOR':rucClient,
        'NOMBRE RECEPTOR':nameClient,
        'PRECIO LETRAS':lettersAmount,
        'NUMERO COMPROBATE':vouchNumber,
        'SERIE':serialNumber,
        'TIPO DOCUMENTO':typeDocument,
    }
    supplierInfoList.append(supplierInfo)
    return supplierInfo
#df=pd.DataFrame(list(supplierInfoList))
#print(df)
#print(xmll(r"xmlFolder\10480238011_02_E001_20.xml"))
