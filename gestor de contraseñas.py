import random 

elementos = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lon = int(input("escribe la longitud"))

password = ""

for i in range(lon):    
    password += random.choice(elementos)

print (password)
