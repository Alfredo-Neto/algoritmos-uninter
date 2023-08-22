class Loja:

	def __init__(self):
		# declaração e inicialização de valores
		self._valor_produto = None
		self._quantidade_produto = None
		self._boas_vindas = None

	# método que inicia o programa no terminal
	def run(self):
		self.boas_vindas() # print de boas-vindas na tela
		while True:
			valor = self.pegar_valor_do_produto() # capturar entrada do usuário
			quantidade = self.pegar_quantidade_do_produto() # capturar entrada do usuário

			# se ambos os valores forem inválidos, pular iteração, reiniciando o programa
			if not valor or not quantidade:
				continue

			# implementação da regra de negócio, calculando o valor, aplicando os descontos
			# e printando com e sem desconto para cada caso
			if quantidade < 200:
				self.valor_sem_desconto(valor, quantidade)
				self.valor_com_desconto(valor, quantidade, 0)
			elif quantidade >= 200 and quantidade < 1000:
				self.valor_sem_desconto(valor, quantidade)
				self.valor_com_desconto(valor, quantidade, 5)
			elif quantidade >= 1000 and quantidade < 2000:
				self.valor_sem_desconto(valor, quantidade)
				self.valor_com_desconto(valor, quantidade, 10)
			else:
				self.valor_sem_desconto(valor, quantidade)
				self.valor_com_desconto(valor, quantidade, 15)

	# encapsulando valores privados com getters e setters
	@property
	def valor_produto(self):
		return self._valor_produto

	# encapsulando valores privados com getters e setters
	@property
	def quantidade_produto(self):
		return self._quantidade_produto

	# encapsulando valores privados com getters e setters
	@valor_produto.setter
	def valor_produto(self, novo_valor):
		self._valor_produto = novo_valor

	# encapsulando valores privados com getters e setters
	@quantidade_produto.setter
	def quantidade_produto(self, nova_quantidade):
		self._quantidade_produto = nova_quantidade

	# método que atribui um valor para um atributo do objeto e printa uma mensagem na tela
	def boas_vindas(self):
		self._boas_vindas = "Bem-vindo a Loja do Alfredo de Aguiar Braule Pinto Neto"
		print(self._boas_vindas)

	# captura o input do usuário, verifica se é válido, e, se for
	# salva o valor no atributo. Se for inválido retorna False
	def pegar_valor_do_produto(self):
		self.valor_produto = input("Entre com o valor do produto: ")
		if self._is_valid_value(self.valor_produto):
			self.valor_produto = float(self.valor_produto)
			return self.valor_produto
		return False

	# captura o input do usuário, verifica se é válido, e, se for
	# salva o valor no atributo. Se for inválido retorna False
	def pegar_quantidade_do_produto(self):
		self.quantidade_produto = input("Entre com a quantidade do produto: ")
		if self._is_valid_value(self.quantidade_produto):
			self.quantidade_produto = float(self.quantidade_produto)
			return self.quantidade_produto
		return False

	# verifica se o valor pode ser convertido em um número e se é positivo.
	# Se as duas coisas forem verdadeiras, retorna True. Se for negativo, retorna uma mensagem de erro de acordo
	# Se não for conversível para numérico, retorna mensagem de erro de acordo
	# Para ambos os casos de erro, retorna False
	def _is_valid_value(self, value):
		if self._is_convertible_to_numeric(value):
			if float(value) >= 0:
				return True
			print("Insira valores válidos")
			return False
		print("Insira somente valores numéricos")
		return False

	# calcula, formata e printa o valor sem desconto
	def valor_sem_desconto(self, valor_unitario, quantidade):
		valor = self.calcular_valor(valor_unitario, quantidade)
		formatted_value = "R$ {:.2f}".format(valor)
		print("O valor SEM desconto:", formatted_value)

	# calcula, formata, aplica desconto e printa o valor com desconto
	def valor_com_desconto(self, valor_unitario, quantidade, desconto):
		valor = self.calcular_valor(valor_unitario, quantidade)
		valor = self.aplicar_desconto(valor, desconto)
		formatted_value = "R$ {:.2f}".format(valor)
		print("O valor COM desconto:", formatted_value)

	# multiplica valor pela quantidade
	def calcular_valor(self, valor, quantidade):
		return valor * quantidade

	# aplica o desconto
	def aplicar_desconto(self, valor, desconto):
		return valor * (1 - (desconto/100))

	# verifica se o valor(string) pode ser convertido para número usando o método isdigit()
	def _is_convertible_to_numeric(self, valor):
		if isinstance(valor, str):
			if valor.startswith('-'):
				valor_sem_sinal = valor[1:]
				return valor_sem_sinal.isdigit() or (
					valor_sem_sinal.replace('.', '', 1).isdigit() and valor_sem_sinal.count('.') <= 1
				)
			else:
				return valor.isdigit() or (
					valor.replace('.', '', 1).isdigit() and valor.count('.') <= 1
				)
		return False

loja = Loja() #instancia o objeto
loja.run() #chama o método de inicialização da aplicação
