salário = float(input('Digite o salário do funcionario: '))
if salário <= 1560:
    novo = salário + (salário * 20 / 100)
else:
    novo = salário + (salário * 15 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))        