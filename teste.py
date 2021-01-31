import unittest
from random import randint
from models.calcular import Calcular


class CalcularTestes(unittest.TestCase):

    def setUp(self: object) -> None:
        self.calcular: Calcular = Calcular(randint(1, 4))
        self.resposta: int = self._gerar_resposta()

    def test_dificuldade(self: object) -> None:
        self.assertIn(self.calcular.dificuldade, (1, 2, 3, 4))

    def test_valor1(self: object) -> None:
        self.assertIn(self.calcular.valor1, range(0, 100000))

    def test_valor2(self: object) -> None:
        self.assertIn(self.calcular.valor2, range(0, 100000))

    def test_operacao(self: object) -> None:
        self.assertIn(self.calcular.operacao, range(1, 4))

    def test_resultado(self: object) -> None:
        self.assertEqual(self.calcular.resultado, self.resposta)

    def test_simbolo(self: object) -> None:
        if self.calcular.operacao == 1:
            simbolo: str = '+'
        elif self.calcular.operacao == 2:
            simbolo: str = '-'
        else:
            simbolo: str = '*'
        self.assertEqual(self.calcular._op_simbolo, simbolo)

    def test_checar_resultado_correto(self: object) -> None:
        self.assertTrue(self.calcular.checar_resutado(self.resposta))

    def test_checar_resultado_errado(self: object) -> None:
        self.assertFalse(self.calcular.checar_resutado(self.resposta + 1))

    def _gerar_resposta(self: object) -> int:
        if self.calcular.operacao == 1:  # Somar
            return self.calcular.valor1 + self.calcular.valor2
        elif self.calcular.operacao == 2:  # Diminuir
            return self.calcular.valor1 - self.calcular.valor2
        else:  # Multiplicar
            return self.calcular.valor1 * self.calcular.valor2


if __name__ == '__main__':
    unittest.main()
