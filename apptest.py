from sre_parse import State
import string
import pandas as pd
from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import messagebox
from parsePdf import pdff
from parseXml import xmll
from validator import validates
from tkinter import END, StringVar, filedialog
from attr import validate
import customtkinter
import sys
import os

#customtkinter.ScalingTracker.set_user_scaling(0.5)
customtkinter.set_appearance_mode("standard")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520
    def __init__(self):
        super().__init__()
        self.title("VALIDACION PDF CON XML SUNAT")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.listPdfs=[]
        self.listXml=[]
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(7, weight=1)

        self.button_1 = customtkinter.CTkButton(master=self,
                                                text="Carpeta de archivos pdfs y xml",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:self.button_parse("pdf"))
        self.button_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_2 = customtkinter.CTkButton(master=self,
                                                text="Carpeta de archivos xml",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:self.button_parse("xml"))
        self.button_2.grid(row=4, column=0, pady=10, padx=10)

        self.button_3 = customtkinter.CTkButton(master=self,
                                                text="VALIDAR",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.change_validar) #state=tkinter.DISABLED
        self.button_3.grid(row=7, column=3, pady=10, padx=10)


        
        self.label_1 = customtkinter.CTkLabel(master=self,
                                              text="cantidad de archivos pdfs",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=2, column=0, pady=10, padx=10)

        self.label_2 = customtkinter.CTkLabel(master=self,
                                              text="cantidad de archivos xml",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=6, column=0, pady=10, padx=10)

        self.sv1=StringVar()
        #self.sv1.trace("w", lambda name, index, mode, change_validar)        
        #self.e1=Entry(self, textvariable=self.sv1, validate="focusout", validatecommand=self.change_validar)
        self.e1=customtkinter.CTkEntry(master=self)
        self.e1.grid(row=2,column=1,pady=10, padx=10)
        self.sv1='0'
        self.e1.insert(0,self.sv1)

        self.sv2=StringVar()
        #self.e2=Entry(self, textvariable=self.sv2, validate="focusout", validatecommand=self.change_validar)
        self.e2=customtkinter.CTkEntry(master=self)
        self.e2.grid(row=6,column=1,pady=10, padx=10)
        self.sv2='0'
        self.e2.insert(0,self.sv2)

        self.switch_2 = customtkinter.CTkSwitch(master=self,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=7, column=0, pady=10, padx=20, sticky="w")

    def button_parse(self,ext):
        print(f"parseando los {ext}")
        self.folderPdfs=filedialog.askdirectory()
        #ext="pdf"
        print(self.folderPdfs)
        directory = os.fsencode(self.folderPdfs)
        self.count_files=0
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            #print(filename)
            if filename.endswith(f".{ext}"):
                self.count_files=self.count_files+1
                filePath=f"{self.folderPdfs}/{filename}"
                #print(filePath)
                #print(os.path.join(str(directory), str(filename)))
                #print(filePath)
                #filePath=os.path.join(directory, filename)
                if ext=="pdf":
                    self.listPdfs.append(filePath)
                    self.e1.delete(0,END)
                    self.e1.insert(0,self.count_files)
                if ext=="xml":
                    self.listXml.append(filePath)
                    self.e2.delete(0,END)
                    self.e2.insert(0,self.count_files)
                continue
            else:
                continue
        print(f"cantidad de archivos {ext}: {self.count_files}")
        
        
    def button_parse_xml(self):
        print("parseando los xml")
        self.filename=filedialog.askdirectory()
        ext="xml"
        print(self.filename)
        directory = os.fsencode(self.filename)
        self.count_files_xml=0
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(f".{ext}"):
                self.count_files_xml=self.count_files_xml+1
                filePath=f"{directory}\{filename}"
                print(filePath)
                #print(os.path.join(str(directory), str(filename)))
                #filePath=os.path.join(directory,filename)
                self.listXml.append(filePath)
                continue
            else:
                continue
        print(f"cantidad de archivos {ext}: {self.count_files_xml}")

        
    def button_event(self):
        self.filename=filedialog.askdirectory()
        #self.filename=filedialog.askopenfile(initialdir="/",title="seleciona los archivos",filetype=(("CSV","*CSV"),("All Files","*.*")))
        ext="pdf"
        print(self.filename)
        directory = os.fsencode(self.filename)
        self.count_files=0
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(f".{ext}"):
                self.count_files=self.count_files+1
                print(os.path.join(str(directory), str(filename)))
                continue
            else:
                continue
        print(f"cantidad de archivos {ext}: {self.count_files}")

    def change_validar(self):
        #print("llamando a la validacion de contenido")
        #print(self.listPdfs)
        contentPdfs=[]
        contentXmls=[]
        pdfsPath=self.listPdfs
        for pdf in pdfsPath:
            contentPdfs.append(pdff(pdf))
        for xml in self.listXml:
            contentXmls.append(xmll(xml))
        #pd.DataFrame(contentPdfs).to_csv("conteido pdfs.csv", index=False,sep=";")
        #pd.DataFrame(contentXmls).to_csv("conteido Xmls.csv", index=False,sep=";")

        df1=pd.DataFrame(contentPdfs)
        df2=pd.DataFrame(contentXmls)
        validates(df1,df2)
        messagebox.showinfo("my message","this is an example of showinfo\nmessagebox")
        #print(contentPdfs)
        #print(contentXmls)

    def change_mode(self):
        
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

            
if __name__ == "__main__":
    app = App()
    app.start()
    
