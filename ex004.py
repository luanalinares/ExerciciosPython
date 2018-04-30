#Verificação de informações de um dado inserido.

info = input('Digite a informação: ')
print('O tipo primitivo desse valor é: ',type(info))
print('Só tem espaços? ', info.isspace())
print('É um número? ', info.isnumeric())
print('É alfabético? ', info.isalpha())
print('É alfanumérico? ', info.isalnum())
print('Está em Maiúscula? ',info.isupper())
print('Está em minúscula? ', info.islower())
print('Está Capitalizada', info.istitle())

