from sorveteria import Sorveteria

from unit_test import UnitTest

import unittest
from unittest import mock

import io

class SorveteriaTest(UnitTest):
    @mock.patch('sorveteria.input', create=True)
    def test_pegar_valor_do_produto(self, mocked_input):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            mocked_input.side_effect = ["a", "5", "-5"]

            sorveteria = Sorveteria()

            result = sorveteria.pegar_valor_do_produto()
            self._assert(mock_stdout.getvalue() == "Insira somente valores numéricos\n")
            self._assert(result == False)

            result = sorveteria.pegar_valor_do_produto()
            self._assert(result == 5.0)

            result = sorveteria.pegar_valor_do_produto()
            # self._assert(mock_stdout.getvalue() == "Insira valores válidos\n")
            self._assert(result == False)

SorveteriaTest.call()
