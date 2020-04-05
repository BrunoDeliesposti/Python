salario = float(input('Digite o seu salario: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))
reajuste = salario + (salario*porcentagem/100)

print('Um funcionário que ganhava R$ {:.2f}, com {:.0f}% de aumento '.format(salario, porcentagem))
print('Seu novo salário será R$ {:.2f} '.format(reajuste))