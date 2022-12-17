########################################
## Python lahiyəsi : üçbucağın həlli
## classes modulu
## demo versiyadır müəyyən xətalar düzəldiləcək
## 10 yanvar 01:18
## @author : Ramazan Nuhbalayev
## @e-mail : hiding because of spam
## github : https://github.com/RamonParis
########################################

import tkinter as tk
import turtle
import operational_functions as opf


class Ucbucaq():
    """
    Üçbucağın adı və ya tipi ilə bağlı
    bir neçə obyekt yaratmağa imkan verə bilər
    self.ucbucagin_sahesi - Üçbucağın sahəsini alan dəyişən
    self.ucbucag_hes_parametrler - Üçbucağın həll nəticələrini alan dəyişən
    self.ucbucagin_novu - Üçbucağın tipini ifadə edən dəyişəndir
    
    """
    def __init__ (self,*deyerler):
        self.deyerler=deyerler #sinifə göndərilən dəyərləri obyektin istifadəsinə veririk
        self.ucbucagin_sahesi=0
        self.ucbucag_hes_parametrler = list()
        self.ucbucagin_novu = ""
        
        if self.deyerler[0] == "Üçbucağın üç tərəfi verilib" :
            self.ucbucagin_sahesi = opf.sahe_heron(deyerler[1] , deyerler[2] , deyerler[3])
            self.ucbucag_hes_parametrler = opf.sin_teo_hesab("butun bucaqlar", deyerler[1] , deyerler[2] , deyerler[3])
             
            
        elif self.deyerler[0] == "Üçbucağın iki tərəfi və onlar arasında qalan bucaq" :
            #iki tərəf və onların arasında qalan bucaq verilərsə
            self.ucbucagin_sahesi = opf.sahe_iki_trf_bcq_sinusu_sahe(deyerler[1] , deyerler[2] , deyerler[3])
            self.ucbucag_hes_parametrler = opf.sin_teo_hesab("bucaq" ,deyerler[1] , deyerler[2] , deyerler[3])
             
        
        elif self.deyerler[0] == "Üçbucağın bir tərəfi və ona bitişik iki bucaq verilib" :
            self.ucbucagin_sahesi = opf.sahe_bir_trf_ona_btsk_iki_bcq(deyerler[1] , deyerler[2] , deyerler[3])
            self.ucbucag_hes_parametrler = opf.sin_teo_hesab("teref" , 180 - deyerler[2] - deyerler[3] , deyerler[3] , deyerler[1])
            
        
        elif self.deyerler[0] == "Üçbucağın bir tərəfi və ona endirilmiş hündürlük verilib" :
            self.ucbucagin_sahesi = opf. sahe_otrcq_hndrlk(deyerler[1] , deyerler[2])
        
        self.ucbucagin_novu = opf.ucbucagin_novu(self.ucbucag_hes_parametrler)
        #self.ucbucaq_eskiz = opf.eskiz(self.ucbucag_hes_parametrler)
