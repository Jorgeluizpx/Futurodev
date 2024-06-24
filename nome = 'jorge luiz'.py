nome = 'jorge luiz'
altura = 1.67
peso = 52
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:,.2f} de altura' # IGUAL
linha_2 = f'pesa {peso} quilos e imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(nome , 'tem' , altura, 'de altura' ,) # IGUAL
print("pesa", peso, 'quilos e imc é',)
print(imc)


