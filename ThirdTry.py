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

x=17
y=23
y=x+y+1
x=x+y
print(f"answer {x}")