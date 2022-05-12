import pandas as pd
import bs4
import re
def xmll(ruta):
    with open(ruta) as page:
        soup = bs4.BeautifulSoup(page, 'xml')
    suplierOb=soup.find('cac:AccountingSupplierParty')
    dniSupplier=suplierOb.find('cbc:CustomerAssignedAccountID').text
    nameSupplier=suplierOb.find('cbc:Name').text.strip()
    priceAmount=soup.find('cbc:PriceAmount').text
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
#df=pd.DataFrame(list(supplierInfoList))
#print(df)

