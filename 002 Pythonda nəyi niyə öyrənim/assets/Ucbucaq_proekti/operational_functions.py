########################################
## Python lahiyəsi : üçbucağın həlli
## operational_functions modulu
## demo versiyadır müəyyən xətalar düzəldiləcək
## 10 yanvar 01:19
## @author : Ramazan Nuhbalayev
## @e-mail : hiding because of spam
## github : https://github.com/RamonParis
########################################

import math
import turtle
from PIL import Image , ImageTk
import time


def sahe_heron (sol_teref , sag_teref , oturacaq):
    """
    Heron düsturu vasitəsiylə sahəni tapmağa xidmət edir
    
    """
    p=( sol_teref + sag_teref + oturacaq )/2
    sahe=(p* (p - sol_teref) * (p- sag_teref) * (p- oturacaq)) ** 0.5
    return round(sahe , 2)

def sahe_iki_trf_bcq_sinusu_sahe (teref1 , teref2 , bucaq) :
    #üçbucağın iki tərəfi və onlar arasında qalan bucağın sinusu
    """
    Üçbucağın iki tərəfi və onlar arasında
    qalan bucağ verilibsə həmnin üçbucağın
    sahəsi buna uyğun tapılır :
    S = 0.5*a*b*sin(a)    
    """
    bucaq_radianla = math.radians(bucaq)
    bucagin_sinusu = math.sin(bucaq_radianla)
    sahe = 0.5 * teref1 * teref2 * bucagin_sinusu
    return round(sahe , 2)

def sahe_bir_trf_ona_btsk_iki_bcq (teref , bucaq1 , bucaq2):
    """
    Üçbucağın bir tərəfi və ona bitişik iki bucağı
    verilibsə həmnin üçbucağın sahəsi buna uyğun
    tapılır :
    S = (teref ** 2 ) / (2 * (ctg(a) + ctg(b))
    """
    bucaq1_radianla = math.radians(bucaq1)
    bucaq2_radianla = math.radians(bucaq2)
    ctg_bucaq_1 = 1 / math.tan(bucaq1_radianla)
    ctg_bucaq_2 = 1 / math.tan(bucaq2_radianla)
    terefin_kvadrati = teref ** 2
    ctg_cemi = ctg_bucaq_1 + ctg_bucaq_2
    sahe = terefin_kvadrati / (2 * ctg_cemi)
    return round(sahe , 2)
    

def sahe_otrcq_hndrlk(oturacaq , hundurluk):
    """
    Üçbucağın oturacağı və ona endirilmiş hündürlük
    verilibsə həmnin üçbucağın sahəsi buna uyğun
    tapılır :
    S = 0.5*a *h
    """
    sahe = oturacaq * hundurluk * 0.5
    return round(sahe , 2)

def gostericiler_0_bucaq(*gostericiler):
    """
    İki tərəf və onlar arasında qalan bucaq verilibsə
    Üçbucağın həlli bu funksiya əsasında aparılır
    """
    teref1 = gostericiler[0]
    teref2 = gostericiler[1]
    bucaq1 = gostericiler[2] #derece ile
    bucaq1_radianla = math.radians(bucaq1)
    if bucaq1 <= 90 : #bilirik ki, a<90 cos(a) = sin (90 - a)
        cos_hes_bucaq_1 = 90 - bucaq1
        cos_hes_bucaq_1_radianla = math.radians(cos_hes_bucaq_1)
    elif bucaq1 >= 90 :
        cos_hes_bucaq_1 = bucaq1 - 90
        #bilirik ki, a<90 cos(a) = sin (90 - a)
        #və həmçinin bucaq1>90 o zaman bucaq1 - 90 ilƏ UYĞUNLAŞDIRIRIQ
        cos_hes_bucaq_1_radianla = math.radians(cos_hes_bucaq_1)
    cos_hes_sin_bucaq_1 = math.sin(cos_hes_bucaq_1_radianla) # cosnisun cavabını sinus ilə alırıq
    sin_bucaq_1 = math.sin(bucaq1_radianla)
    bucaq1_qar_teref = ((teref1**2) + (teref2**2) - (2 * teref1 * teref2 * cos_hes_sin_bucaq_1)) ** 0.5 #kosinuslar teoremi
    teref3 = round(bucaq1_qar_teref , 2)
    sin_bucaq_2 = (sin_bucaq_1 * teref2)/ teref3 #sin(x)=k
    sin_bucaq_2_radianla = math.asin(sin_bucaq_2) #sin(x)=k tənliyindən radianla cavcab alırıq
    bucaq2 = round(math.degrees(sin_bucaq_2_radianla) , 2)
    bucaq3 = 180 - bucaq1 - bucaq2
    deyer = [[bucaq1 , bucaq2 , bucaq3 ],
             [teref3 , teref2 , teref1]]
    return deyer

def gostericiler_0_teref(*gostericiler):
    """
    Üçbucağın bir tərəfi və ona bitişik
    iki bucağı verilibsə həmnin üçbucağın
    həlli  bu funksiya əsasında aparılır
    """
    #verilənlər
    bucaq1 = gostericiler[0] #derece ile
    bucaq2 = gostericiler[1] #derece ile
    teref1 = gostericiler[2]
    bucaq3 = 180 - bucaq1 - bucaq2 #derece ile
    bucaq1_radianla = math.radians(bucaq1)
    bucaq2_radianla = math.radians(bucaq2)
    bucaq3_radianla = math.radians(bucaq3)
    #sinuslar teoremindən istifadə edirik
    #bucaqlar məlum olduğu üçün yalnız tərəfləri tapmağa ehtiyac var
    sin_bucaq_1 = math.sin(bucaq1_radianla)
    sin_bucaq_2 = math.sin(bucaq2_radianla)
    sin_bucaq_3 = math.sin(bucaq3_radianla)
    bucaq2_qar_teref = (teref1 * sin_bucaq_2) / sin_bucaq_1
    bucaq3_qar_teref = (teref1 * sin_bucaq_3) / sin_bucaq_1
    teref2 = (bucaq2_qar_teref , 2)
    teref3 = (bucaq3_qar_teref , 2)
    #göstəriciləri geri dönüş edirik
    deyer = [[bucaq1 , bucaq2 , bucaq3] ,
             [teref1 , teref2 , teref3]]
    return deyer

def cos_bucagi_korbucaq(*gostericiler):
    ##############################
    #kosinus əgər üçbucaq daxilində mənfi qiymət alıbsa
    #bu onun 90 dərəcədən böyük bir korbucaqlı olduğunun göstəricisidir
    #buna görə də əlavə metoda ehtiyac duyulur
    #kod mürəkkəbliyi azaldılaraq rahat
    #oxunaqlığı artırmaq məsədi ilə alqoritm uzadılır
    ##############################
    teref1 = gostericiler[0] 
    teref2 = gostericiler[1] 
    teref3 = gostericiler[2]
    cos_bucaq_1_teref_1_qar = ((teref2 ** 2) + (teref3 ** 2) - (teref1 ** 2)) / (2 * teref2 * teref3)
    cos_bucaq_2_teref_2_qar = ((teref1 ** 2) + (teref3 ** 2) - (teref2 ** 2)) / (2 * teref1 * teref3)
    cos_bucaq_3_teref_3_qar = ((teref1 ** 2) + (teref2 ** 2) - (teref3 ** 2)) / (2 * teref1 * teref2)
    if cos_bucaq_1_teref_1_qar < 0:
        musbet_sinus_bucaq_1 = -math.asin(cos_bucaq_1_teref_1_qar)
        musbet_sinus_bucaq_1_derece = math.degrees(musbet_sinus_bucaq_1)
        bucaq1 = round((90 + musbet_sinus_bucaq_1_derece) , 2)
        
        sinus_bucaq_2 = math.asin(cos_bucaq_2_teref_2_qar)
        sinus_bucaq_2_derece = math.degrees(sinus_bucaq_2)
        bucaq2 = round((90 - sinus_bucaq_2_derece) , 2)
            
        #sinus_bucaq_3 = math.asin(cos_bucaq_3_teref_3_qar)
        #sinus_bucaq_3_derece = math.degrees(sinus_bucaq_3)
        #bucaq3 = round(90 - sinus_bucaq_3_derece)
        bucaq3 = 180 - bucaq1 - bucaq2
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
    elif cos_bucaq_2_teref_2_qar < 0:
        musbet_sinus_bucaq_2 = -math.asin(cos_bucaq_2_teref_2_qar)
        musbet_sinus_bucaq_2_derece = math.degrees(musbet_sinus_bucaq_2)
        bucaq2 = round((90 + musbet_sinus_bucaq_2_derece) , 2)
            
        sinus_bucaq_1 = math.asin(cos_bucaq_1_teref_1_qar)
        sinus_bucaq_1_derece = math.degrees(sinus_bucaq_1)
        bucaq1 = round((90 - sinus_bucaq_1_derece) , 2)
            
        #sinus_bucaq_3 = math.asin(cos_bucaq_3_teref_3_qar)
        #sinus_bucaq_3_derece = math.degrees(sinus_bucaq_3)
        #bucaq3 = round(90 - sinus_bucaq_3_derece)
        bucaq3 = 180 - bucaq1 - bucaq2
        
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
    elif cos_bucaq_3_teref_3_qar < 0:
        musbet_sinus_bucaq_3 = -math.asin(cos_bucaq_3_teref_3_qar)
        musbet_sinus_bucaq_3_derece = math.degrees(musbet_sinus_bucaq_3)
        bucaq3 = round((90 + musbet_sinus_bucaq_3_derece) , 2)
        
        sinus_bucaq_1 = math.asin(cos_bucaq_1_teref_1_qar)
        sinus_bucaq_1_derece = math.degrees(sinus_bucaq_1)
        bucaq1 = round((90 - sinus_bucaq_1_derece) , 2)
        
        #sinus_bucaq_2 = math.asin(cos_bucaq_2_teref_2_qar)
        #sinus_bucaq_2_derece = math.degrees(sinus_bucaq_2)
        #bucaq2 = round(90 - sinus_bucaq_2_derece)
        bucaq2 = 180 - bucaq3 - bucaq1
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
    return deyer

def gostericiler_0_b_bucaqlar(*gostericiler):
    """
    üç tərəf məlumdur kosinuslar
    teoremindən istifadə edərək
    bütün bucaqlar hesablanır
    """
    teref1 = gostericiler[0] 
    teref2 = gostericiler[1] 
    teref3 = gostericiler[2]
    cos_bucaq_1_teref_1_qar = ((teref2 ** 2) + (teref3 ** 2) - (teref1 ** 2)) / (2 * teref2 * teref3)
    cos_bucaq_2_teref_2_qar = ((teref1 ** 2) + (teref3 ** 2) - (teref2 ** 2)) / (2 * teref1 * teref3)
    cos_bucaq_3_teref_3_qar = ((teref1 ** 2) + (teref2 ** 2) - (teref3 ** 2)) / (2 * teref1 * teref2)
    
    if cos_bucaq_1_teref_1_qar < 0 or cos_bucaq_2_teref_2_qar < 0 or cos_bucaq_3_teref_3_qar < 0 : #korbucaq
        ##############################
        #kosinus əgər üçbucaq daxilində mənfi qiymət alıbsa
        #bu onun 90 dərəcədən böyük bir korbucaqlı olduğunun gğstəricisidir
        #buna görə də əlavə metoda ehtiyac duyulur
        #kod mürəkkəbliyi azaldılaraq rahat
        #oxunaqlığı artırmaq məsədi ilə alqoritm uzadılır
        ##############################
        deyer = cos_bucagi_korbucaq(teref1 , teref2 , teref3)
    elif cos_bucaq_1_teref_1_qar == 0:
        # cos(90°) = 0 üçbucaq düzbucaqlıdır buna uyğun bir bucaq artıq tapılmış olur
        bucaq1 = 90
        #ikinci bucaq heablanır
        sinus_bucaq_2 = math.asin(cos_bucaq_2_teref_2_qar) #sin(x)=k tənliyindən radianla cavcab alırıq
        sinus_bucaq_2_derece = math.degrees(sinus_bucaq_2) 
        bucaq2 = round((90 - sinus_bucaq_2_derece) , 2)
        bucaq3 = 180 - bucaq1 - bucaq2 
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
        
    elif cos_bucaq_2_teref_2_qar == 0:

        sinus_bucaq_1 = math.asin(cos_bucaq_1_teref_1_qar) #sin(x)=k tənliyindən radianla cavcab alırıq
        sinus_bucaq_1_derece = math.degrees(sinus_bucaq_1)
        bucaq1 = round((90 - sinus_bucaq_1_derece) , 2)
        bucaq2 = 90
        # cos(90°) = 0 üçbucaq düzbucaqlıdır buna uyğun bir bucaq artıq tapılmış olur
        bucaq3 = 180 - bucaq1 - bucaq2 #üçbucağın bucaqlar cəmi 180 dərəcədir
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
        
    elif cos_bucaq_3_teref_3_qar == 0: #düzbucaq
        bucaq3 = 90
        # cos(90°) = 0 üçbucaq düzbucaqlıdır buna uyğun bir bucaq artıq tapılmış olur
        sinus_bucaq_2 = math.asin(cos_bucaq_2_teref_2_qar) #sin(x)=k tənliyindən radianla cavcab alırıq
        sinus_bucaq_2_derece = math.degrees(sinus_bucaq_2)
        bucaq2 = round((90 - sinus_bucaq_2_derece) , 2)
        bucaq1 = 180 - bucaq2 - bucaq3 #üçbucağın bucaqlar cəmi 180 dərəcədir
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
        
    elif cos_bucaq_1_teref_1_qar > 0 and cos_bucaq_2_teref_2_qar > 0 and cos_bucaq_3_teref_3_qar > 0 : #itibucaq
        # 0 < cos(x) < 1 , x < 90° üçbucaq itibucaqlıdır buna uyğun bucaqlar hesablanır
        #cosinusla aparılan hesablamalar zamanı errorlarla üzləşildiyindən sinus ilə hesablama aparılır
        sinus_bucaq_1 = math.asin(cos_bucaq_1_teref_1_qar) #sin(x)=k tənliyindən radianla cavcab alırıq
        sinus_bucaq_1_derece = math.degrees(sinus_bucaq_1)
        #bucaq1 = 90 - sinus_bucaq_1_derece #milyonda bir dəqiqliklə cavab əldə edə bilərsən
        bucaq1 = round((90 - sinus_bucaq_1_derece) , 2)
        sinus_bucaq_2 = math.asin(cos_bucaq_2_teref_2_qar) #sin(x)=k tənliyindən radianla cavcab alırıq
        sinus_bucaq_2_derece = math.degrees(sinus_bucaq_2)
        #bucaq2 = 90 - sinus_bucaq_2_derece #milyonda bir dəqiqliklə cavab əldə edə bilərsən
        bucaq2 = round((90 - sinus_bucaq_2_derece) , 2)
        bucaq3 = 180 - bucaq1 - bucaq2 #üçbucağın bucaqlar cəmi 180 dərəcədir
        deyer = [[bucaq1 , bucaq2 , bucaq3] ,
                 [teref1 , teref2 , teref3]]
    return deyer

def sin_teo_hesab(*gostericiler):
    """
    Sinuslarla və cosinuslar teoremi
    vasitəsiylə hesablamaların aparılmasına
    xidmət edən metodların idarəedici funksiyası.
    
    gostericiler[0] == "bucaq" olarsa
    bucaq2 tapılaraq bucaq3 hesablanır ,
    sinuslar teoremindən tərəf3 hesablanır
    
    gostericiler[0] == "teref" olarsa
    bucaq3 tapılır ardınca sinuslar teoremindən
    istifadə olunaraq tərəf2  tapılır
    bucaq3 vasitəsiylə sinuslar teoremindən
    istifadə olunaraq tərəf3 hesablanır
    
    gostericiler[0] == "butun bucaqlar" olarsa
    kosinuslar teoremindən istifadə olunaraq
    radianlarla bucaqlar hesablanır və ona
    uyğun bucağlar hesablanaraq cavablar əldə edilir
    """
    #ya iki bucaq bir tərəf
    #ya da ki bir bucaq iki tərəf
    if gostericiler[0] == "bucaq" :  #bucagi tapırıqsa
        teref1 = gostericiler[1]
        teref2 = gostericiler[2]
        bucaq1 = gostericiler[3] #derece ile
        deyer = gostericiler_0_bucaq(teref1 , teref2 , bucaq1)
    elif gostericiler[0] == "teref" :  #tərəfi tapırıqsa
        bucaq1 = gostericiler[1] #derece ile
        bucaq2 = gostericiler[2] #derece ile
        teref1 = gostericiler[3]
        deyer = gostericiler_0_teref(bucaq1 , bucaq2 , teref1)
    elif gostericiler[0] == "butun bucaqlar" :  #butun bucaqları tapırıqsa
        teref1 = gostericiler[1] 
        teref2 = gostericiler[2] 
        teref3 = gostericiler[3]
        deyer = gostericiler_0_b_bucaqlar(teref1 , teref2 , teref3)
        
    return deyer
    
    

def eskiz(*gostericiler):
    """
    turtle vasitəsiylə fiqurun eskizi cızılır
    """
    miqyas_deyer = gostericiler[1]
    gostericiler = gostericiler[0]
    bucaqlar = gostericiler[0] 
    terefler = gostericiler[1]
    bucaqlar.sort()
    #print ("bucaqlar",bucaqlar)
    terefler.sort()
    #print("terefler",terefler)
    bucaq1_o = bucaqlar[0]
    bucaq2_o = bucaqlar[1]
    bucaq3_o = bucaqlar[2]
    teref1_o = terefler[0]
    teref2_o = terefler[1]
    teref3_o = terefler[2]
    
    
    teref1 = miqyas_deyer * teref1_o
    teref2 = miqyas_deyer * teref2_o
    teref3 = miqyas_deyer * teref3_o
    
    bucaq1_ciz = bucaq1_o
    bucaq2_ciz = 90 - bucaq2_o
    bucaq3_ciz = bucaq3_o
    
    pencere = turtle.Screen()
    """icon = Image.open('regular_triangle.png')
    pencere._root.iconphoto(False,icon)"""
    pencere._root.winfo_toplevel().title("Üçbucağın eskizi")
    pencere.clear()
    qelem_t = turtle.Turtle()
    qelem_t_2 = turtle.Turtle()
    
    qelem_t.ht() #birincil işçi qələmi gizlədir
    qelem_t_2.ht() #ikincil işçi qələmi gizlədir
    
    qelem_t_2.speed(0)
    qelem_t_2.pendown()
    
    
    qelem_t_2.forward(-(teref3/2)) #soldan başlasın deyə
    
    style = ('Times New Roman', 11, 'italic' , 'bold') #font stilini müəyyən edir
    qelem_t_2.write(f"   α", font=style, align='left')
    #qələm_t_2 ən başda gözləmə vəziyyətindədir
    qelem_t.pendown()
    
    qelem_t.speed(0)
    #qelem_t.write(f"α = {bucaq1}°", font=style, align='left')
    
    qelem_t.write(f"t₃", font = style , align='center')
    qelem_t.forward(teref3/2)
    #qelem_t.write(f"teref₃ = {teref3_o}", font=style, align='center')
    #qelem_t.write(f"β = {bucaq2}°", font=style, align='right')
    qelem_t.write(f"β   ", font=style, align='right')
    
    #bucağı düzəld
    qelem_t.setheading(90)
    qelem_t.left(bucaq2_ciz)
    qelem_t.forward(teref1/2)
    qelem_t.write(f"t₁", font=style, align='left')
    #qelem_t.write(f"t₁ = {teref1_o}", font=style, align='left')
    qelem_t.forward(teref1/2)
    #qelem_t.write(f"γ = {bucaq3}°", font=style, align='center')
    qelem_t.write(f"\n\n\nγ", font=style, align='center')
    qelem_t.setheading(qelem_t.towards(qelem_t_2))
    qelem_t.forward(teref2/2)
    qelem_t.write(f"t₂", font=style, align='right')
    #qelem_t.write(f"teref₂ = {teref2_o}", font=style, align='right')
    qelem_t.goto(qelem_t_2.pos())
    qelem_t.penup()
    #qelem_t.left(bucaq3 / 2)
    qelem_t_2.forward(teref3/2)
    qelem_t_2.setheading(-90)
    qelem_t_2.penup()
    qelem_t_2.forward(170)
    qelem_t_2.pendown()
    qelem_t_2.write(f"""1 ci tərəf və onun qarşısındakı bucaq
t₁  = {teref1_o}\tα = {bucaq1_o}°
2 ci tərəf və onun qarşısındakı bucaq
t₂  = {teref2_o}\tβ = {bucaq2_o}°
3 cü tərəf və onun qarşısındakı bucaq
t₃  = {teref3_o}\tγ = {bucaq3_o}°""", font=style, align='left')
    pencere.mainloop()
    #pencere.exitonclick()
    
    return quit()

def ucbucagin_novu(*gostericiler):
    """
    Üçbucağın tipini ifadə edən
    dəyəri əldə edərik
    """
    gostericiler = gostericiler[0]
    bucaqlar = gostericiler[0] 
    terefler = gostericiler[1]
    bucaqlar.sort()
    #print ("bucaqlar",bucaqlar)
    terefler.sort()
    #print("terefler",terefler)
    bucaq1 = bucaqlar[0]
    bucaq2 = bucaqlar[1]
    bucaq3 = bucaqlar[2]
    teref1 = terefler[0]
    teref2 = terefler[1]
    teref3 = terefler[2]
    
    if ((bucaq1 == bucaq2 or bucaq2 == bucaq3) or (teref1 == teref2 or teref2 == teref3)) and bucaq3 != 90 :
        ucbucagin_novu = "Bərabəryanlı üçbucaq"
    elif 90 in bucaqlar:
        ucbucagin_novu = "Düzbucaqlı üçbucaq"
    elif (90 in bucaqlar) and ((bucaq1 == bucaq2 or bucaq2 == bucaq3) or (teref1 == teref2 or teref2 == teref3)):
        ucbucagin_novu = "Bərabəryanlı düzbucaqlı üçbucaq"
    elif bucaq3 > 90:
        ucbucagin_novu = "Korbucaqlı üçbucaq"
    elif bucaq3 < 90: #itibucaqlı üçbucaq
        ucbucagin_novu = "İtibucaqlı üçbucaq"
    elif ((bucaq1 == bucaq2 and bucaq2 == bucaq3) or (teref1 == teref2 and teref2 == teref3)) :
        ucbucagin_novu = "Bərabərtərəfli üçbucaq"
    
    return ucbucagin_novu
    
def ucb_helleri_qeydler(*gostericiler):
    ucbucag_sahe = gostericiler[1]
    uvbucag_novu = gostericiler[2]
    gostericiler = gostericiler[0]
    bucaqlar = gostericiler[0] 
    terefler = gostericiler[1]
    bucaqlar.sort()
    #print ("bucaqlar",bucaqlar)
    terefler.sort()
    #print("terefler",terefler)
    bucaq1_o = bucaqlar[0]
    bucaq2_o = bucaqlar[1]
    bucaq3_o = bucaqlar[2]
    teref1_o = terefler[0]
    teref2_o = terefler[1]
    teref3_o = terefler[2]
    tarix = time.asctime()
    ucb_sened = open(r"Ucbucagin_helli_hesablari_siyahisi.txt" , mode = "a")
    ucb_sened.write(f"\n{tarix}\n\n")
    ucb_sened.write(f"Üçbucağın sahəsi : {ucbucag_sahe}\n")
    ucb_sened.write(f"Üçbucağın növü : {uvbucag_novu}\n")
    ucb_sened.write(f"""1 ci tərəf və onun qarşısındakı bucaq
t₁  = {teref1_o}\tα = {bucaq1_o}°
2 ci tərəf və onun qarşısındakı bucaq
t₂  = {teref2_o}\tβ = {bucaq2_o}°
3 cü tərəf və onun qarşısındakı bucaq
t₃  = {teref3_o} \tγ = {bucaq3_o}°\n\n""")
    ucb_sened.close()
    
