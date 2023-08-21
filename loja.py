class Loja:
	def __init__(self):
		self._valor_produto = None
		self._quantidade_produto = None
		self._boas_vindas = None

	def run(self):
		self.boas_vindas()
		while True:
			valor = self.pegar_valor_do_produto()
			quantidade = self.pegar_quantidade_do_produto()

			if not valor or not quantidade:
				continue

			if quantidade < 200:
				self.valor_sem_desconto(valor, quantidade)
			elif quantidade >= 200 and quantidade < 1000:
				self.valor_com_desconto(valor, quantidade, 5)
			elif quantidade >= 1000 and quantidade < 2000:
				self.valor_com_desconto(valor, quantidade, 10)
			else:
				self.valor_com_desconto(valor, quantidade, 15)

	@property
	def valor_produto(self):
		return self._valor_produto

	@property
	def quantidade_produto(self):
		return self._quantidade_produto

	@valor_produto.setter
	def valor_produto(self, novo_valor):
		self._valor_produto = novo_valor

	@quantidade_produto.setter
	def quantidade_produto(self, nova_quantidade):
		self._quantidade_produto = nova_quantidade

	def boas_vindas(self):
		self._boas_vindas = "Bem-vindo a Loja do Alfredo Neto"
		print(self._boas_vindas)

	def pegar_valor_do_produto(self):
		self.valor_produto = input("Entre com o valor do produto: ")
		if self._is_valid_value(self.valor_produto):
			self.valor_produto = float(self.valor_produto)
			return self.valor_produto
		return False

	def pegar_quantidade_do_produto(self):
		self.quantidade_produto = input("Entre com a quantidade do produto: ")
		if self._is_valid_value(self.quantidade_produto):
			self.quantidade_produto = float(self.quantidade_produto)
			return self.quantidade_produto
		return False

	def _is_valid_value(self, value):
		if self._is_convertible_to_numeric(value):
			if float(value) >= 0:
				return True
			print("Insira valores válidos")
			return False
		print("Insira somente valores numéricos")
		return False

	def valor_sem_desconto(self, valor_unitario, quantidade):
		valor = self.calcular_valor(valor_unitario, quantidade)
		formatted_value = "R$ {:.2f}".format(valor)
		print("O valor SEM desconto:", formatted_value)

	def valor_com_desconto(self, valor_unitario, quantidade, desconto):
		valor = self.calcular_valor(valor_unitario, quantidade)
		valor = self.aplicar_desconto(valor, desconto)
		formatted_value = "R$ {:.2f}".format(valor)
		print("O valor COM desconto:", formatted_value)

	def calcular_valor(self, valor, quantidade):
		return valor * quantidade

	def aplicar_desconto(self, valor, desconto):
		return valor * (1 - (desconto/100))

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

loja = Loja()
loja.run()
