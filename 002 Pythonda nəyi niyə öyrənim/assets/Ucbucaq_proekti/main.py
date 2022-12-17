########################################
## Python lahiyəsi : ucbucagin helli
## demo versiyadır müəyyən xətalar düzəldiləcək
## 10 yanvar 01:18
## @author : Ramazan Nuhbalayev
## @e-mail : hiding because of spam
## github : https://github.com/RamonParis
########################################

import re
from tkinter import *
import tkinter as tk
from tkinter import ttk
#from os import system
#system('cmd /k "pip install pillow"')
from PIL import Image , ImageTk
import classes
import operational_functions as opf



class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self) #pəncərəni örnəkləyirik
        icon = ImageTk.PhotoImage(file = 'regular_triangle.png')
        #canvas_element_1 = Canvas(self, bg="blue", height=900, width=600)
        #arxa_fon_sekil_fayl = Image.open("arxa_plan_2.jpg")
        #arxa_fon_sekil = ImageTk.PhotoImage(arxa_fon_sekil_fayl)
        #self.arxa_fon_sekil_label = Label(self, image = arxa_fon_sekil)
        #self.arxa_fon_sekil_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.winfo_toplevel().title("Üçbucağın həlli")
        self.ucbucaq_parametr_eskiz = list()
        self.configure(background = '#16b39e')
        self.geometry("600x900+70+70")
        self.resizable(False, False)
        self.iconphoto(False,icon)
        #canvas_element_1.pack()
        
        self.izah_metin = Label(self, text = """Üçbucağın həlli dedikdə verilmiş 3 element vasitə-
silə onun bütün tərəflərinin və bucaqlarının tapılma-
sı nəzərdə tutulur. Üçbucaqların həlli məsələlərinin
hamısında tərəfləri t1, t2, t3, qarşı bucaqları isə uy-
ğun olaraq α, β, γ ilə işarə edəcəyik.""",
                                 background = '#16b39e' ,
                                 fg = 'white',
                                 relief = tk.FLAT,
                                 borderwidth = 5)
        self.izah_metin.config(font = ('Times New Roman',15,'bold'))
        self.izah_metin.place(x = 100 , y = 5)

        # Input noqteleri
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.deyisen_1 = Entry(self,bd = 5,
                               relief = tk.RIDGE,
                               validate='key',
                               validatecommand=valid ,
                               width=8)
        self.deyisen_2 = Entry(self,bd = 5,
                               relief = tk.RIDGE,
                               validate='key',
                               validatecommand=valid ,
                               width=8)
        self.deyisen_3 = Entry(self,bd = 5,
                               relief = tk.RIDGE,
                               validate='key',
                               validatecommand=valid ,
                               width=8)
        self.miqyas = Entry(self,bd = 5,
                            relief = tk.RIDGE,
                            width=8)
        #Output mətnləri
        self.deyisen_1_ad = Label(self, text = '',
                                  fg = 'black',
                                  bg = '#16b39e' ,
                                  relief = tk.FLAT,
                                  justify = "left",
                                  anchor="w" , 
                                  width = 28, borderwidth = 5 ,
                                  font = ('Times New Roman',10,'bold'))
        self.deyisen_2_ad = Label(self, text = '',
                                  fg = 'black',
                                  bg = '#16b39e' ,
                                  relief = tk.FLAT,
                                  justify = "left",
                                  anchor="w" , 
                                  width = 28, borderwidth = 5 ,
                                  font = ('Times New Roman',10,'bold'))
        self.deyisen_3_ad = Label(self, text = '',
                                  fg = 'black',
                                  bg = '#16b39e' ,
                                  relief = tk.FLAT,
                                  justify = tk.LEFT,
                                  anchor="w" , 
                                  width = 28, borderwidth = 5 ,
                                  font = ('Times New Roman',10,'bold'))
        self.miqyas_info = Label(self, text = 'Eskizin miqyasını\nKiçiltmə üçün mənfi\nBöyütmə üçün müsbət\nədəd yazın :',
                                  fg = 'black',
                                  bg = '#16b39e' ,
                                  relief = tk.FLAT,
                                  justify = tk.LEFT,
                                  anchor="w" , 
                                  width = 20, 
                                  font = ('Times New Roman',10,'bold'))
        
        
        self.ucbucagin_sahesi = Label(self, text = '',
                                      fg = 'black',
                                      bg = '#16b39e' ,
                                      relief = tk.FLAT,
                                      justify = "left",
                                      anchor="w" ,
                                      width = 28, borderwidth = 5 ,
                                      font = ('Times New Roman',10,'bold'))
        self.teref_1_bucaq_1 = Label(self, text = '',
                                     fg = 'black',
                                     bg = '#16b39e' ,
                                     relief = tk.FLAT,
                                     justify = "left",
                                     anchor="w" ,
                                     width = 28, borderwidth = 5 ,
                                     font = ('Times New Roman',10,'bold'))
        self.teref_2_bucaq_2 = Label(self, text = '',
                                     fg = 'black',
                                     bg = '#16b39e' ,
                                     relief = tk.FLAT,
                                     justify = "left",
                                     anchor="w" ,
                                     width = 28, borderwidth = 5 ,
                                     font = ('Times New Roman',10,'bold'))
        self.teref_3_bucaq_3 = Label(self, text = '',
                                     fg = 'black',
                                     bg = '#16b39e' ,
                                     relief = tk.FLAT,
                                     justify = "left",
                                     anchor="w" ,
                                     width = 28, borderwidth = 5 ,
                                     font = ('Times New Roman',10,'bold'))
        self.ucbucagin_novu = Label(self, text = '',
                                    fg = 'black',
                                    bg = '#16b39e' ,
                                    relief = tk.FLAT,
                                    justify = "left",
                                    anchor="w" ,
                                    width = 36, borderwidth = 5 ,
                                    font = ('Times New Roman',10,'bold'))

        # aşağı açılan siyahı
        self.secilmis_hell_m = StringVar(self)
        self.secilmis_hell_m.set("Üçbucağın üç tərəfi verilib") # default value
        font = ("Times New Roman", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.hell_secimi = ["Üçbucağın üç tərəfi verilib" ,
                            "Üçbucağın iki tərəfi və onlar arasında qalan bucaq" ,
                            "Üçbucağın bir tərəfi və ona bitişik iki bucaq verilib" ,
                            "Üçbucağın bir tərəfi və ona endirilmiş hündürlük verilib"]
        self.asagi_acil_siyahi = ttk.Combobox(self, textvariable=self.secilmis_hell_m,
                                                   values=self.hell_secimi,
                                                   font = font,
                                                   width = 48,
                                                   justify = tk.LEFT)

        #Verilənləri adlandıracaq düymə
        self.duy_sec_tesd = Button(self, text = "Həlli seç",
                                     fg = "black",
                                     command = self.hell_secimi_icrasi,
                                     height=1 ,
                                     width=10 ) 
        self.duy_sec_tesd.config(font=('Times New Roman', 11, 'bold'))
        
        
        #Hesablamaları icra edəcək düymə
        self.hesabla = Button(self, text = "Hesabla",
                                     fg = "black",
                                     command = self.hesabla_ucbucaq,
                                     height=1 ,
                                     width=10 ,
                              state = "disabled") 
        self.hesabla.config(font=('Times New Roman', 11, 'bold'))
        
        #Eskizi cızacaq düymə
        self.eskizi_hazırla = Button(self, text = "Eskizi cız",
                                     fg = "black",
                                     command = self.eskizi_cek,
                                     height=1 ,
                                     width=10 ,
                                     state = "disabled") 
        self.eskizi_hazırla.config(font=('Times New Roman', 11, 'bold'))
        #qeydi aparacaq düymə
        
        self.hesab_qeydi_apar = Button(self, text = "Hesabları \nMətnə qeyd et",
                                     fg = "black",
                                     command = self.qeydi_apar,
                                     height=1 ,
                                     width=10 ,
                                     state = "disabled") 
        self.hesab_qeydi_apar.config(font=('Times New Roman', 11, 'bold'))
        
        #yerləşmə
        self.asagi_acil_siyahi.place(x = 72, y= 150)
        self.deyisen_1.place(x = 300, y = 240)
        self.deyisen_2.place(x = 300, y = 300)
        self.deyisen_3.place(x = 300, y = 360)
        self.deyisen_1_ad.place(x = 72, y = 240)
        self.deyisen_2_ad.place(x = 72, y = 300)
        self.deyisen_3_ad.place(x = 72, y = 360)
        self.duy_sec_tesd.place(x = 490, y = 150)
        self.miqyas_info.place(x = 420, y = 240)
        self.miqyas.place(x = 420, y = 360)
        self.eskizi_hazırla.place(x = 420, y = 420)
        self.hesab_qeydi_apar.place(x = 420, y = 490)
        self.hesabla.place(x = 300, y = 420)
        self.ucbucagin_sahesi.place(x = 72, y = 480)
        self.teref_1_bucaq_1.place(x = 72, y = 540)
        self.teref_2_bucaq_2.place(x = 72, y = 600)
        self.teref_3_bucaq_3.place(x = 72, y = 660)
        self.ucbucagin_novu.place(x = 72, y = 720)
        
        
        
        
    def hell_secimi_icrasi(self):
        """
        Həlli seçərək əməliyyatın gedişini
        və dəyişənlərin adlarını təyin etməklə
        istifadəçi seçimini düzgün yönləndirən funksiya
        """
        deyer_1 = self.secilmis_hell_m.get()
        self.hesabla.config(state = "normal")
        if deyer_1 == "Üçbucağın üç tərəfi verilib" :
            self.deyisen_1_ad.config(text = "1-ci tərəf - t1 = ",
                                      justify="left")
            self.deyisen_2_ad.config(text = "2-ci tərəf - t2 = ")
            self.deyisen_3_ad.config(text = "3-cü tərəf - t3 = ")
            
        elif deyer_1 == "Üçbucağın iki tərəfi və onlar arasında qalan bucaq" :
            self.deyisen_1_ad.config(text = "1-ci tərəf - t1 = ")
            self.deyisen_2_ad.config(text = "2-ci tərəf - t2 = ")
            self.deyisen_3_ad.config(text = "Tərəflər arasındakı bucaq  = ")
            
        elif deyer_1 == "Üçbucağın bir tərəfi və ona bitişik iki bucaq verilib" :
            self.deyisen_1_ad.config(text = "1 tərəf - t1 = ")
            self.deyisen_2_ad.config(text = "Tərəfə bitişik bucaq = ")
            self.deyisen_3_ad.config(text = "Tərəfə bitişik bucaq  = ")
            
        elif deyer_1 == "Üçbucağın bir tərəfi və ona endirilmiş hündürlük verilib":
            self.deyisen_1_ad.config(text = "1 tərəf - t1 = " ,
                                     justify="left" ,
                                     anchor="w")
            self.deyisen_2_ad.config(text = "Tərəfə endirilmiş h hündürlüyü = " ,
                                     justify="left" ,
                                     anchor="w")
            self.update()

    def hesabla_ucbucaq(self):
        """
        Üçbucağın verilən parametrlərini
        operational_functions modulu vasitəsiylə
        hesablayıb dəyişən labellərinə yazdıran funksiya
        """
        deyer_1 = self.secilmis_hell_m.get()
        deyer_2 = float(self.deyisen_1.get())
        deyer_3 = float(self.deyisen_2.get())
        deyer_4 = float(self.deyisen_3.get())
        hell_secimi = self.hell_secimi
        self.eskizi_hazırla.config(state = "normal")
        self.hesab_qeydi_apar.config(state = "normal")
        if deyer_1 == hell_secimi[0] or deyer_1 == hell_secimi[1] or deyer_1 == hell_secimi[2] :
            ucbucaq_1 = classes.Ucbucaq(deyer_1 , deyer_2 , deyer_3 , deyer_4)
            ucb_sahe = ucbucaq_1.ucbucagin_sahesi
            ucb_par = ucbucaq_1.ucbucag_hes_parametrler
            ucbucagin_novu = ucbucaq_1.ucbucagin_novu
            self.ucbucaq_parametr_eskiz = ucb_par
            self.ucbucaq_sahe_hesabat = ucb_sahe
            self.ucbucagin_novu_hesabat = ucbucagin_novu
            
            bucaqlar = ucb_par[0]
            terefler = ucb_par[1]
            bucaqlar.sort()
            terefler.sort()
            bucaq1 = bucaqlar[0]
            bucaq2 = bucaqlar[1]
            bucaq3 = bucaqlar[2]
            teref1 = terefler[0]
            teref2 = terefler[1]
            teref3 = terefler[2]
            
            #self.update()
            ucbucagin_sahesi_str = str(f"Üçbucağın sahəsi : {ucb_sahe}")
            teref_1_bucaq_1_str = str(f"t1 = {teref1} \tα = {bucaq1}")
            teref_2_bucaq_2_str = str(f"t2 = {teref2} \tβ = {bucaq2}")
            teref_3_bucaq_3_str = str(f"t3 = {teref3} \tγ = {bucaq3}")
            ucbucagin_novu_str = str(f"Üçbucağın növü : {ucbucagin_novu}")
            self.ucbucagin_sahesi.config(text = ucbucagin_sahesi_str)
            self.teref_1_bucaq_1.config(text = teref_1_bucaq_1_str)
            self.teref_2_bucaq_2.config(text = teref_2_bucaq_2_str)
            self.teref_3_bucaq_3.config(text = teref_3_bucaq_3_str)
            self.ucbucagin_novu.config(text = ucbucagin_novu_str)
            
        else:
            ucbucaq_1 = classes.Ucbucaq(deyer_1 , deyer_2 , deyer_3)
            ucb_sahe = ucbucaq_1.ucbucagin_sahesi
            ucbucagin_sahesi_str = str(f"Üçbucağın sahəsi : {ucb_sahe}")
            ucbucagin_novu_str = str(f"Üçbucağın növü : {ucbucagin_novu}")
            #self.update()
            self.ucbucagin_sahesi.config(text = ucbucagin_sahesi_str)
            self.teref_1_bucaq_1.config(text = ucbucagin_novu_str)
            self.teref_2_bucaq_2.config(text = "")
            self.teref_3_bucaq_3.config(text = "")
            self.ucbucagin_novu.config(text = "")
            #self.update()
    
    def eskizi_cek(self):
        """
        Eskizi uyğun parametrlərlə miqyas
        hasilini funksiya olaraq alıb işləyərək
        operational_functions modulundan eskiz
        funksiyasınasa göndərir
        """
        ucbucaq_parametr_eskiz = self.ucbucaq_parametr_eskiz
        miqyas_deyer = int(self.miqyas.get())
        if miqyas_deyer < 0 :
            miqyas_deyer_gonder = ((-1) * miqyas_deyer) ** (-1)
        elif miqyas_deyer == None or miqyas_deyer == 0 :
            miqyas_deyer_gonder = 1
        elif miqyas_deyer > 0:
            miqyas_deyer_gonder = miqyas_deyer
        opf.eskiz(ucbucaq_parametr_eskiz,miqyas_deyer_gonder)
    
    def qeydi_apar(self):
        ucbucaq_parametr_eskiz = self.ucbucaq_parametr_eskiz
        ucb_sahe = self.ucbucaq_sahe_hesabat
        ucbucagin_novu = self.ucbucagin_novu_hesabat
        
        opf.ucb_helleri_qeydler(ucbucaq_parametr_eskiz , ucb_sahe ,  ucbucagin_novu)
    
    def restrictNumberOnly(self, action, string):
        """
        Yalnış verilən tipi daxil
        etmənin qarşısını alır
        """
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    App()
    mainloop()


