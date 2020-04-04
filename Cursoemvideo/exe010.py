real = float(input('Quanto dinheiro você na carteira? R$'))
dolar = real/4.20
euro = real/4.63
yen = real/0.039

print('Com R$ {:.2f} você pode comprar \nUS$ {:.2f} Dólares\n'
      '€ {:.2f} Euros\n'
      'yen {:.2f} Yens'.format(real, dolar, euro, yen))