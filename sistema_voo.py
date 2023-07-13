voos_disponiveis = [{'Numero': '105', 'Origem': 'São paulo', 'Destino': 'Piauí', 'Data': '23/07/2023','Horário_saída': '12:30','Horário_chegada': '15:20', 'Assentos': []}, {'Numero': '109', 'Origem': 'Rio de janeiro', 'Destino': 'Ceará', 'Data': '30/07/2023','Horário_saída':'16:21','Horário_chegada':'18:10', 'Assentos': []}, {'Numero': '102', 'Origem': 'Amazonas','Destino': 'Pernambuco', 'Data': '02/08/2023', 'Horário_saída': '13:40', 'Horário_chegada': '16:15','Assentos': []}, {'Numero':'110', 'Origem': 'Rio grande do norte', 'Destino': 'Mato grosso do sul', 'Data': '10/08/2023', 'Horário_saída': '19:00', 'Horário_chegada': '21:10', 'Assentos': [] }]

def buscar_voos(origem,destino,data):
	voos = []
	for voo in voos_disponiveis:
		if voo['Origem'] == origem and voo['Destino'] == destino and voo['Data'] == data:
			voos.append(voo)
	return voos
	
def mostrar_voos(voos):
	for voo in voos:
		print("Numero do voo: {}".format(voo['Numero']))
		print('\n')
		print("Origem do voo: {}".format(voo['Origem']))
		print('\n')
		print("Destino: {}".format(voo['Destino']))
		print('\n')
		print("Horário de saída: {}".format(voo['Horário_saída']))
		print('\n')
		print("Horário de chegada: {}".format(voo['Horário_saída']))

def fazer_reserva(numero_voo, nome, numero_passaporte):
	for voo in voos_disponiveis:
		if voo['Numero'] == numero_voo:
			if len(voo['Assentos']) < 10:
				passageiro = { 'Nome': nome, 'Numero_passaporte': numero_passaporte}
				voo['Assentos'].append(passageiro)
				print("Reserva feita")
			else:
				print("Desculpe, esse assento já está ocupado")

def salvar_dados():
	with open("voos.txt", "w") as file:
		for voo in voos_disponiveis:
			file.write("{},{},{},{},{},{}".format(voo['Numero'] , voo['Origem'], voo['Destino'], voo['Data'], voo['Horário_saída'], voo['Horário_chegada']))
		for passageiro in voo['Assentos']:
			file.write("{}, {}".format(passageiro['Nome'], passageiro['Numero_passaporte']))
			
salvar_dados()

def carregar_dados():
	global voos
	with open("voos.txt", "r") as file:
		lines = file.readlines()
		voo_atual = None
		for line in lines:
			dados = line.strip().split(",")
			if len(dados) == 5:
				voo_atual = { 'Numero': dados[0], 'Origem': dados[1], 'Destino': dados[2], 'Horário_chegada': dados[3], 'Horário_saída': dados[4], 'Assentos': []}
			elif len(dados) == 2:
				passageiros = { 'Nome': dados[0], 'Numero_passaporte': dados[1]}
				voo_atual['Assentos'].append(passageiros)
				
carregar_dados()
				
print("Sistema de Vôos")
print("1- Pesquisar voos")
print("2- Fazer reservas")
print("3- Mostrar voos")
print("4- Sair")
opcao = input("Escolha uma opção: ")

if opcao == '1':
	origem_voo = input("Origem: ")
	destino_voo = input("Destino: ")
	data_voo = input("Data: ")
	voos_encontrados = buscar_voos(origem_voo, destino_voo, data_voo)
	print("Voo encontrado {} ".format(voos_encontrados))
elif opcao == '2':
	num_voo = input("Número do voo: ")
	nome_passageiro = input("Nome: ")
	num_passaporte = input("Número do passaporte: ")
	reservas = fazer_reserva(num_voo, nome_passageiro, num_passaporte)
	print(reservas)
	
elif opcao == '3':
	voos = mostrar_voos(voos_disponiveis)
	print(voos)