preco = float(input('Qual é o preço do produto? R$ '))
porcento = float(input('Qual a porcentagem de desconto? '))
desconto = preco - (preco*porcento/100)

print('O produto que custava R${:.2f}, na promoção com desconto '
      'de {:.0f}% vai custar R${:.2f} '.format(preco, porcento, desconto))