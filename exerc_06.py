distância = float(input(('Qual é a distância da sua viagem? ')))
print('Você está prestes a começar uma viagem de {}Km.')
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
    