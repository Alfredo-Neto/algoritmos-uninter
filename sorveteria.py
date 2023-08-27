class Sorveteria:
		
		def __init__(self):
			self._boas_vindas = None
			self._data = [
				["1", "R$ 6,00", "R$ 7,00", "R$ 8,00"],
				["2", "R$ 10,00", "R$ 12,00", "R$ 14,00"],
				["3", "R$ 14,00","R$ 17,00", "R$ 20,00"]
			]

			self._headers = [
				"Nº DE BOLAS", 
				"Sabor Tradicional (tr)", 
				"Sabor Premium (pr)", 
				"Sabor Especial (es)"
			]

    # método que atribui um valor para um atributo do objeto e printa uma mensagem na tela
		def boas_vindas(self):
			self._boas_vindas = "Bem-vindo a Sorveteria do Alfredo de Aguiar Braule Pinto Neto"
			print(self._boas_vindas)
			self._tabulate(self._data, self._headers)

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
sorveteria.boas_vindas()