from loja import Loja

from unit_test import UnitTest

import unittest
from unittest import mock

import io

class LojaTest(UnitTest):
    def test_boas_vindas(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            loja = Loja()
            loja.boas_vindas()
            self._assert(mock_stdout.getvalue() == "Bem-vindo a Loja do Alfredo Neto\n")

    @mock.patch('loja.input', create=True)
    def test_pegar_valor_do_produto(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["a", "5", "-5"]

            loja = Loja()

            result = loja.pegar_valor_do_produto()
            self._assert(mock_stdout.getvalue() == "Insira somente valores numéricos\n")
            self._assert(result == False)

            result = loja.pegar_valor_do_produto()
            self._assert(result == 5.0)

            result = loja.pegar_valor_do_produto()
            # self._assert(mock_stdout.getvalue() == "Insira valores válidos\n")
            self._assert(result == False)

    @mock.patch('loja.input', create=True)
    def test_pegar_quantidade_do_produto(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["a", "200", "-200"]

            loja = Loja()

            result = loja.pegar_quantidade_do_produto()
            self._assert(mock_stdout.getvalue() == "Insira somente valores numéricos\n")
            self._assert(result == False)

            result = loja.pegar_quantidade_do_produto()
            self._assert(result == 200.0)

    @mock.patch('loja.input', create=True)
    def test_valor_sem_desconto(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["100", "5"]
            loja = Loja()

            valor = loja.pegar_valor_do_produto()
            quantidade = loja.pegar_quantidade_do_produto()
            loja.valor_sem_desconto(valor, quantidade)

            self._assert(mock_stdout.getvalue() == "O valor SEM desconto: R$ 500.00\n")

    @mock.patch('loja.input', create=True)
    def test_valor_com_desconto(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["100", "5"]
            loja = Loja()
            valor = loja.pegar_valor_do_produto()
            quantidade = loja.pegar_quantidade_do_produto()
            loja.valor_com_desconto(valor, quantidade, 15)

            self._assert(mock_stdout.getvalue() == "O valor COM desconto: R$ 425.00\n")

LojaTest.call()
