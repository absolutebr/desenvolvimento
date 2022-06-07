import random


print('exercicio advinhacão')


numero_secreto = random.randrange(1,101)
tentativas = 3

print ("Qual nivel de dificuldade?")
print ("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Define o nivel: "))

if(nivel == 1):
    tentivas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada, tentativas)) 
    chute_strg = input("Digite um numero:")
    chute = int(chute_strg)

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue
    
    if(numero_secreto == chute):
        print('voce acertou')
        break   
    else:
        if(chute > numero_secreto):  
            print('voce errou, o chute foi maior que o numero secreto')
        elif(chute < numero_secreto):
            print ('voce errou, o chute foi menor que o numero secreto')
print("FIM DE JOGO")