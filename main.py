from datetime import date
print("Olá turma do Python!")
print("Tudo joia!")
nome: str = input("Qual é o seu nome? ")

data_hoje=date.today()
print(f'Olá {nome}! Estamos no ano de', data_hoje.year, 'mês',data_hoje.month, 'dia', data_hoje.day'.')

temp=input('Indique a temperatura na sua localidade: ')
if temp<15:
    print('É melhor agasalhar-se.')
elif temp==15:
    print('15ºC ainda é considerado Primavera..Basta uma malhinha.')
else:
    print('Pode cancelar o voo para o Brasil. Vá para a Caparica.')