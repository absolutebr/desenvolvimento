print ('********************')
print ('***Salario do Mes***')
print ('********************')


ganhoHora= []
horasTrabalho = [] 
Inss = []
Sindicato = []

ganhoHora =int(input('Quantos voce ganha por hora? '))
horasTrabalho = int(input('Quantas horas voce trabalhas no mes? '))
Inss = int(input ("Qual porcetagem de desconto do INSS?"))
Sindicato = int(input ("Qual porcetagem de desconto do Sindicato?"))


salarioBruto = ganhoHora * horasTrabalho
print("Salario Bruto:R$", salarioBruto)

DescontoInss = (salarioBruto * Inss)/100
print("Desconto de Inss:R$",DescontoInss)
DescontoSind = (salarioBruto * Sindicato)/100
print("Sindicato:R$", DescontoSind)

Desconto = DescontoInss + DescontoSind

print('O total do salario liquido do mes')

SalarioLiquido = salarioBruto - Desconto

print("Salario Liquido:R$", SalarioLiquido)