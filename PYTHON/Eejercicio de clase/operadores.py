#22/04/2024

#condicional ternario 
hace_frio= True

abrigado= True if hace_frio else False

#--------------------------------------------------------------

nivel_ruido = int(input("Cual es el nivel de ruido: "))

if nivel_ruido < 0:
    print("Contrate Psicologo")
elif nivel_ruido == 0:
    print("Silencio")
elif nivel_ruido <= 20:
    print("Ambiente silencioso")
elif nivel_ruido <=60:
    print("Ambiente poco ruidoso")
else:
    print("AMbiente poco ruidoso")

#--------------------------------------------------------------
