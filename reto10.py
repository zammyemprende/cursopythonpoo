peso = float(input("dame tu peso en KG:"))
estatura = float(input("dame tu estatura en KG:"))
#imc =(peso/(estatura+estatura))
imc =(peso/(estatura)**2)

imc=round(imc,2)
# para otros casos con sumas imc+=round(imc,2)
print("Tu indice de masa corporal es:"+str(imc))
