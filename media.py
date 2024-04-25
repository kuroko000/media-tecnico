#vamos desenvolver um programa que calcula a media entre duas notas

#nesse "input" abaixo vamos explica o que nosso programa vai fazer
input("Vamos calcular a media entre duas notas, aperte enter para continuar:...\n")

Nota1 = float(input("Fale a primeira nota: ")) #adicionar um dos valores para pode fazer a media
Nota2 = float(input("Fale a segundanota: ")) #adicionar um outro valor para pode calcular a media

notafinal = (Nota1 + Nota2) /2 #calculo para chegar a media

print ("\nSua nota foi ", notafinal)#exibir a media que foi calculada

if notafinal >= 7.0 : #caso a pessoa tenha sido aprovada
    print("\nMeus parabens, você foi aprovado !")

else:
    falta = notafinal - 7.0#caso a pessoa tenha sido reprovada
    falta1 = falta * (-1)
    print ("\nVocê foi reprovado, é lhe faltaram ", falta1," pontos para poder passar.")

    