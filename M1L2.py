import random

Password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

LenghtPass= int(input("Especifica la longitud de tu contraseña"))
Pass = ""
PassRepeat= input("¿Piensas repetir valores en tu contraseña?")
if PassRepeat == "No" and LenghtPass >= 30:
    print("Tu contraseña es muy larga")
elif PassRepeat == "Si":
    for i in range(LenghtPass):
        Pass += random.choice(Password)
    


print(Pass)