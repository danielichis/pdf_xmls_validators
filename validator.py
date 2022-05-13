import pandas as pd
import datetime
def validates(df1,df2):
    df=pd.merge(df1,df2,how="outer",on=["nameFilee"])
    df.to_csv("data merged.csv")
    dfm=df.to_dict()
    results=[]
    for idx,emi in enumerate(dfm['nameFilee']):
        inconsistencia=[]
        estado="OK"
        if isinstance(dfm["nameFile_x"][idx],float):
            estado="falta pdf"
        if isinstance(dfm["nameFile_y"][idx],float):
            estado="falta xml"
        if dfm["RUC EMISOR_x"][idx]!=dfm["RUC EMISOR_y"][idx]:
            inconsistencia.append("RUC EMISOR")
        if dfm["NOMBRE EMISOR_x"][idx]!=dfm["NOMBRE EMISOR_y"][idx]:
            inconsistencia.append("NOMBRE EMISOR")
        if dfm["PRECIO TOTAL BRUTO_x"][idx]!=dfm["PRECIO TOTAL BRUTO_y"][idx]:
            inconsistencia.append("PRECIO TOTAL BRUTO")
        if dfm["PRECIO TOTAL NETO_x"][idx]!=dfm["PRECIO TOTAL NETO_y"][idx]:
            inconsistencia.append("PRECIO TOTAL NETO")
        if dfm["FECHA DE EMISION_x"][idx]!=dfm["FECHA DE EMISION_y"][idx]:
            inconsistencia.append("FECHA DE EMISION")
        if dfm["RUC RECEPTOR_x"][idx]!=dfm["RUC RECEPTOR_y"][idx]:
            inconsistencia.append("RUC RECEPTOR")
        if dfm["NOMBRE RECEPTOR_x"][idx]!=dfm["NOMBRE RECEPTOR_y"][idx]:
            inconsistencia.append("NOMBRE RECEPTOR")
        if dfm["PRECIO LETRAS_x"][idx]!=dfm["PRECIO LETRAS_y"][idx]:
            inconsistencia.append("PRECIO LETRAS")
        if dfm["NUMERO COMPROBATE_x"][idx]!=dfm["NUMERO COMPROBATE_y"][idx]:
            inconsistencia.append("NUMERO COMPROBATE")
        if dfm["SERIE_x"][idx]!=dfm["SERIE_y"][idx]:
            inconsistencia.append("SERIE")
        if dfm["TIPO DOCUMENTO_x"][idx]!=dfm["TIPO DOCUMENTO_y"][idx]:
            inconsistencia.append("TIPO DOCUMENTO")
        if inconsistencia==[]:
            diferences="OK"
        else:
            for i,elem in enumerate(inconsistencia):
                if i==0:
                    diferences=elem
                else:
                    diferences=f"{diferences}-{elem}"

        nombrePdf=dfm["nameFile_x"][idx]
        nombreXml=dfm["nameFile_y"][idx]
        ruc_emisor=dfm["RUC EMISOR_x"][idx]
        tipoDocumento=dfm["TIPO DOCUMENTO_x"][idx]
        serie=dfm["SERIE_x"][idx]
        numeroDocumento=dfm["NUMERO COMPROBATE_x"][idx]

        if estado.find("falta")!=-1:
            ruc_emisor=""
            tipoDocumento=""
            serie=""
            numeroDocumento=""
            diferences=""
        result={
            'NOMBRE PDF':nombrePdf,
            'NOMBRE XML':nombreXml,
            'ESTADO':estado,
            'RUC EMISOR':ruc_emisor,
            'TIPO DOCUMENTO':tipoDocumento,
            'SERIE':serie,
            'NUMERO DE DOCUMENTO':numeroDocumento,
            'DIFERENCIAS ENCONTRADAS':diferences,
        }
        results.append(result)
    #dfm.to_csv("data_merge.csv",sep=";")
    #print(merge_dict)
    df_final=pd.DataFrame(results)
    df_final.to_csv(f"Reporte{datetime.datetime.today().strftime('%m%d%Y%H%M%S')}.csv",sep=";",index=False)   

