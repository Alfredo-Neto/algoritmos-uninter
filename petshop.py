class Petshop:
		
		# construtor para inicialização de alguns valores
		def __init__(self):
			self._extra = 0
			self._pelo = None
			self._peso = None
			self._multiplicador = None
			self._valor_base = None
			self._total = None

		# roda o programa
		def run(self):
			self.boas_vindas()
			while True:
				try:
					valor_base = self.cachorro_peso()
					if valor_base:
						break
					else:
						print("\nPor favor entre com o peso do cachorro novamente.\n")
				except ValueError as e:
					print("Algo deu errado", e)
					return
					
			while True:
				try:
					multiplicador = self.cachorro_pelo()
					if multiplicador:
						break
					else:
						print("\nPor favor entre com um valor válido.")
				except ValueError as e:
					print("Algo deu errado", e)
					return
			
			while True:
				try:
					valor_extra = self.cachorro_extra()
					if valor_extra:
						continue
					else:
						break
				except ValueError as e:
					print("Algo deu errado", e)
					return
			
			self.calcular_total(self.valor_base, self.multiplicador, self.extra)
			if self.total is not None:
				formatted_string = "Total a pagar(R$): R$ {},00 (peso: {} * pelo: {} + adicional(is): {})".format(self.total, self.valor_base, self.multiplicador, self.extra)	
				print(formatted_string)
			
		# encapsulando valores privados com getters e setters
		@property
		def extra(self):
			return self._extra
		
		# encapsulando valores privados com getters e setters
		@property
		def pelo(self):
			return self._pelo
		
		# encapsulando valores privados com getters e setters
		@property
		def peso(self):
			return self._peso
		
		# encapsulando valores privados com getters e setters
		@property
		def multiplicador(self):
			return self._multiplicador

		# encapsulando valores privados com getters e setters
		@property
		def valor_base(self):
			return self._valor_base
	
		# encapsulando valores privados com getters e setters
		@property
		def total(self):
			return self._total

		@extra.setter
		def extra(self, novo_valor):
			self._extra = novo_valor
		
		# encapsulando valores privados com getters e setters
		@pelo.setter
		def pelo(self, novo_valor):
			self._pelo = novo_valor
	
		# encapsulando valores privados com getters e setters
		@peso.setter
		def peso(self, novo_valor):
			self._peso = novo_valor
		
		@multiplicador.setter
		def multiplicador(self, novo_valor):
			self._multiplicador = novo_valor
		
		# encapsulando valores privados com getters e setters
		@valor_base.setter
		def valor_base(self, novo_valor):
			self._valor_base = novo_valor
		
		# encapsulando valores privados com getters e setters
		@total.setter
		def total(self, novo_valor):
			self._total = novo_valor
		
		def boas_vindas(self):
			print("Bem-vindo ao Petshop do Alfredo de Aguiar Braule Pinto Neto")

		def cachorro_peso(self):
			self.peso = input("Entre com o peso do cachorro: ")
			if self._is_convertible_to_numeric(self.peso):
				if self._is_valid_weight(int(self.peso)):
					return self.valor_base
				print("\nNão aceitamos cachorros tão grandes")
				return False
			else:
				print("\nVocê digitou um valor não numérico")
				return False

		def _is_valid_weight(self, value):
			if value < 3:
				self.valor_base = 40
				return True
			if value >= 3 and value < 10:
				self.valor_base = 50
				return True
			if value >= 10 and value < 30:
				self.valor_base = 60
				return True
			if value >= 30 and value < 50:
				self.valor_base = 70
				return True
			
			return False
		
		def cachorro_pelo(self):
			self.pelo = input(
									"Entre com o pelo do cachorro:\n"
									"c - Pelo Curto\n"
									"m - Pelo Médio\n"
									"l - Pelo Longo\n"
									)
			
			if self._is_valid_furr(self.pelo):
				return self.multiplicador
			return False

		def _is_valid_furr(self, value):
			if value not in ["c", "m", "l"]:
				return False
			
			if value == "c":
				self.multiplicador = 1
				return True
			if value == "m":
				self.multiplicador = 1.5
				return True
			if value == "l":
				self.multiplicador = 2
				return True
		
		def cachorro_extra(self):
			adicional = int(input("Deseja adicionar mais algum serviço?\n"
                  "1 - Corte de Unhas - R$ 10,00\n"
                  "2 - Escovar Dentes - R$ 12,00\n"
                  "3 - Limpeza de Orelhas - R$ 15,00\n"
                  "0 - Não desejo mais nada\n"))

			if self._is_valid_extra(adicional):
				return self.extra
			return False
		
		def _is_valid_extra(self, value):
			if value not in [1, 2, 3, 0]:
				return False
			
			if value == 1:
				self.extra += 10
				return True
			if value == 2:
				self.extra += 12
				return True
			if value == 3:
				self.extra += 15
				return True
			if value == 0:
				self.extra += 0
				return False
		
		def calcular_total(self, base, multiplicador, extra):
			self.total = (base * multiplicador) + extra
			
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
		
# executa o programa
petshop = Petshop()
petshop.run()