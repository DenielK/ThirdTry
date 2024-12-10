#1
# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#     if nimi=="JUKU":
#         print("Lähme kinno")
#         try:
#             vanus=int(input(f"Kui vana sa oled {nimi}? "))
#             if vanus<0:
#                 print("Viga!")
#             elif vanus<=6:
#                 print("Tasuta")
#             elif vanus<15:
#                 print("Lastepilet")
#             elif vanus<65:
#                 print("Täispilet")
#             elif vanus<100:
#                 print("Nii palju!!!!!")
#         except:
#             print("Vale andme tüüp - Täisar oli vaja sisestada")
#     else:
#         print("ootan Juku")
# else:
#     print("Segatud sõne")

#2
#variant1
# nimi1=input("Mis on sinu nimi? ")
# nimi2=input("Mis on sinu nimi? ")
# nimed=["Kirill","Gleb","Zhan","Veronika","Wall"]
# if nimi1.isalpha() and nimi2.isalpha():
#     if (nimi1 in nimed) and (nimi2 in nimed):
#         print ("Nad on pinginaabrid")
#     else:
#         print ("Nad ei ole sinu naabrid")
# else:
#     print("Viga!")
# #variant2
# nimi1=input("Mis on sinu nimi? ")
# nimi2=input("Mis on sinu nimi? ")
# if (nimi1=="Kirill" and nimi2=="Gleb" or nimi1=="Gleb" and nimi2=="Kirill"):
#     print ("Nad on pinginaabrid")
# else:
#     print ("Nad ei ole sinu naabrid")

#3
# try:
#     a=float(input("Toa Pikkus:"))
#     b=float(input("Toa laius:"))
#     S=a*b
#     print(f"Põranda pindala on {S} m**2")
#     vastus=input("Kas tahad remondi teha?(Jah-1/Ei-0) ") #Jah/ei
#     if vastus.upper()=="JAH" or vastus=="1":
#         print("Remont")
#         hind=float(input("Ühe meetri hind: "))
#         summa=S*hind
#         print(f"Remondi kulud: {summa} €")
#     elif vastus.upper()=="EI" or vastus=="0":
#         print("-")
#     else:
#         print("Ei saa aru")
# except:
#     print("Numbrid!!!")

#4
try:
    hind=float(input("Hind: "))
    if hind >= 700:
        HS=hind-(hind*0.3)
        print(f"Hind soodustusega: {round(HS,2)}")
    else:
        print(f"Hind on sooduseta: {hind}")
except:
    print("Sul on viga sisestamisel")

#5
try:
    temp=float(input("Sisesta temperatuuri: "))
    if temp >=18:
        print("Sobiv toasoojus")
    else:
        print("Temperatuur on alla 18 kraadi")
except:
    print("Sul on viga sisestamisel")

#6
try:
    pikkus=float(input("Mis on sinu pikkus(sm) ? "))
    if pikkus <=130:
        print("Sina oled madala kasvu")
    elif pikkus <=180:
        print("Sina oled keskmist kasvu")
    elif pikkus <=250:
        print("Sina oled pikka kasvu")
    else:
        print("Kas sa oled kindel?")
except:
    print("Sul on viga sisestamisel")

#7
try:
    sugu=input("Kas sa oled naine (N) või mees (M)?")
    if sugu.upper()=="N":
        pikkus=float(input("Kui pikk sa oled?"))
        if pikkus <=125:
            print("Sina oled madala kasvu")
        elif pikkus <=150:
            print("Sina oled keskmist kasvu")
        elif pikkus <=250:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel?")
    elif sugu.upper()=="M":
        pikkus=float(input("Kui pikk sa oled?"))
        if pikkus <=125:
            print("Sina oled madala kasvu")
        elif pikkus <=150:
            print("Sina oled keskmist kasvu")
        elif pikkus <=250:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel?")
    else:
        print("Sisesta õigesti: Kas N või M")
except:
    print("Midagi läks valesti")

#8

#9
a=float(input("Sisesta külg a: "))
b=float(input("Sisesta külg b: "))
if a==b:
    print("See on ruut")
else:
    print("See on ristkülik")

#10
a=float(input("Sisesta arv a: "))
b=float(input("Sisesta arv b: "))
vastus=input("Kas soovid + või -: ")
try:
    if vastus=="-":
        c=float(a-b)
        print(f"{a}-{b}={c}")
    elif vastus=="+":
        c=float(a+b)
        print(f"{a}+{b}={round(c,2)}")
except:
    print("Vastus peab olema + või -")

#11

#12
hind=float(input("Sisesta toote hinna: "))
if hind<0:
    print("Hind peab olema rohkem kui 0")
elif 0<hind<10:
    print(f"Saate 10% soodustust. Maksmisele: {hind-(hind*0.1)}")
elif hind>10:
    print(f"Saate 20% soodustust. Maksmisele: {hind-(hind*0.2)}")
else:
    print("Midgi läks valesti")

#13
sugu=input("Kas sa oled naine (N) või mees (M)? ")
if sugu.upper()=="N":
    print("Kahjuks naised meeskonnas ei osale")
elif sugu.upper()=="M":
    vanus=int(input("Kui vana sa oled? "))
    if 16<=vanus<=18:
        print("Oled sobiv kandideerija")
    else:
        print("Kahjuks meil on vanuse piirang")
else:
    print("Kirjuta, kas M või N")