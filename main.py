from datetime import date
print("Olá turma do Python!")
print("Tudo joia!")
nome: str = input("Qual é o seu nome? ")

data_hoje=date.today()
print(f'Olá {nome}! Estamos no ano de', data_hoje.year, 'mês',data_hoje.month, 'dia', data_hoje.day'.')
