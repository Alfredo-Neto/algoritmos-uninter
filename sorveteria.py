class Sorveteria:
		
		def __init__(self):
			self._boas_vindas = None
			self._flavour = None
			self._num_of_icecream_scoops = None
			self._table_data = [
				["1", "R$ 6,00", "R$ 7,00", "R$ 8,00"],
				["2", "R$ 10,00", "R$ 12,00", "R$ 14,00"],
				["3", "R$ 14,00","R$ 17,00", "R$ 20,00"]
			]

			self._table_headers = [
				"Nº DE BOLAS", 
				"Sabor Tradicional (tr)", 
				"Sabor Premium (pr)", 
				"Sabor Especial (es)"
			]

		# encapsulando valores privados com getters e setters
		@property
		def flavour(self):
			return self._flavour
		
		# encapsulando valores privados com getters e setters
		@property
		def num_of_icecream_scoops(self):
			return self._num_of_icecream_scoops

		# encapsulando valores privados com getters e setters
		@flavour.setter
		def flavour(self, novo_valor):
			self._flavour = novo_valor
		
		# encapsulando valores privados com getters e setters
		@num_of_icecream_scoops.setter
		def num_of_icecream_scoops(self, novo_valor):
			self._num_of_icecream_scoops = novo_valor

    # método que atribui um valor para um atributo do objeto e printa uma mensagem na tela
		def boas_vindas(self):
			self._boas_vindas = "Bem-vindo a Sorveteria do Alfredo de Aguiar Braule Pinto Neto"
			print(self._boas_vindas)
			self._tabulate(self._data, self._headers)

		def pegar_pedidos(self, user_flavour, user_scoop):
			scoops = [
				["1", "R$ 6,00", "R$ 7,00", "R$ 8,00"],
				["2", "R$ 10,00", "R$ 12,00", "R$ 14,00"],
				["3", "R$ 14,00","R$ 17,00", "R$ 20,00"]
			]

			flavours = {
				"tr": "TRADICIONAL", 
				"pr": "PREMIUM", 
				"es": "ESPECIAL"
			}

			preco, sabor, bola = '', '', ''
			for index, (flavour, value) in enumerate(flavours.items()):
				if flavour == user_flavour:
					sabor = value
					for scoop in scoops:
						if scoop[0] == str(user_scoop):
							bola = scoop[0]
							preco = scoop[index + 1]
			
			plural = 'bola'
			if int(bola) > 1:
				plural += "s"
			formatted_string = "Você pediu {} {} de sorvete no sabor {}: {}".format(bola, plural, sabor, preco)	
			print(formatted_string)
			return True


		def pegar_sabor_do_sorvete(self):
			self.flavour = input("Entre com o Sabor desejado (tr/es/pr): ")
			if self._is_valid_flavour(self.flavour):
				return self.flavour
			return False
		
		def pegar_num_de_scoops(self):
			self.num_of_icecream_scoops = input("Entre com o número de bolas de sorvete desejado (1/2/3): ")
			print(self.num_of_icecream_scoops)
			if self._is_valid_number_of_icecream_scoops(self.num_of_icecream_scoops):
				return self.num_of_icecream_scoops
			return False
		
		def _is_valid_flavour(self, value):
			if value not in ["tr", "es", "pr"]:
				print("Sabor inválido. Tente novamente")
				return False
			
			return True
		
		def _is_valid_number_of_icecream_scoops(self, value):
			if value not in ["1", "2", "3"]:
				print("Número de bolas de sorvete inválido. Tente novamente.")
				return False
			
			return True

		def _tabulate(self, data, headers):
			# Encontrar a largura ideal para cada coluna
			column_widths = [
					max(len(str(item)) 
							for item in col) 
								for col in zip(headers, *data)
			]

			# Imprimir a linha superior
			line = "+"
			cardapio = "+"
			sum_widths = 0
			for width in column_widths:
					sum_widths += width
					line += "-" * (width + 2) + "+"
			cardapio += ("-" * (int(sum_widths / 2) + 2)) + "Cardápio" + ("-" * (int(sum_widths / 2) + 1)) + "+"
			print(cardapio)

			# Imprimir cabeçalhos
			header_line = "| "
			for word, width in zip(headers, column_widths):
					header_line += word.ljust(width) + " | "
			print(header_line)
			print(line)

			# Imprimir os dados da tabela
			for row in data:
					data_line = "| "
					for word, width in zip(row, column_widths):
							data_line += word.ljust(width) + " | "
					print(data_line)
					print(line)

sorveteria = Sorveteria()
user_flavour = "es"
user_scoop = "3"
result = sorveteria.pegar_pedidos(user_flavour, user_scoop)
print(result)