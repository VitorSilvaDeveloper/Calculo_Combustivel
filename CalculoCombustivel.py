#calculo de combustivel v0.1

print('-=-'*15)
print('Calculadora de combustivel para viajem')
print('-=-'*15)

autonomia = float(input('Autonomia do carro? KM\L'))
distancia = float(input('Qual a distancia da viagem? KM'))
preco = float(input('Preço da gasolina? R$'))


resultado1 = distancia / autonomia 
resultado2 = resultado1 * preco

print('Seu carro vai gastar na média {:.2f} Litros de gasolina para fazer essa viajem'.format(resultado1))
print('O valor que vai gastar de gasolina nessa viajem é de aproximadamente R${:.2f} reais'.format(resultado2))

print('-=-'*15)
