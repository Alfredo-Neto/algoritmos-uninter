from sorveteria import Sorveteria

from unit_test import UnitTest

import unittest
from unittest import mock

import io

class SorveteriaTest(UnitTest):
    @mock.patch('sorveteria.input', create=True)
    def test_pegar_valor_do_produto(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["aa"]

            sorveteria = Sorveteria()

            result = sorveteria.pegar_sabor_do_sorvete()
            self._assert(mock_stdout.getvalue() == "Sabor inválido. Tente novamente\n")
            self._assert(result == False)

    @mock.patch('sorveteria.input', create=True)
    def test_pegar_num_de_scoops(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["a"]

            sorveteria = Sorveteria()
            
            result = sorveteria.pegar_num_de_scoops()
            # self._assert(mock_stdout.getvalue() == "Número de bolas de sorvete inválido. Tente novamente.\n")
            self._assert(result == False)
    
    @mock.patch('sorveteria.input', create=True)
    def test_pegar_pedidos(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sorveteria = Sorveteria()
            user_flavour = "tr"
            user_scoop = "1"
            
            result = sorveteria.pegar_pedidos(user_flavour, user_scoop)
            self._assert(mock_stdout.getvalue() == "Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$ 6,00.\n")
            self._assert(result == True)

SorveteriaTest.call()
