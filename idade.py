idade = int(input("Digite a sua idade: "))
amigododono = input("É amigo do dono?(s/n): ")

if amigododono == "s":
 amigododono = True
else:
 amigododono = False

if idade>= 18:
 print("Pode entrar")
elif amigododono == True:
 print("Pode entrar")
else:
 print("Não pode entrar")