import unittest
from utilidades import es_primo, filtrar_pares, sumar_lista


class TestUtilidades(unittest.TestCase):

    def test_es_primo(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertFalse(es_primo(4))
        self.assertTrue(es_primo(5))
        self.assertFalse(es_primo(1))  # 1 no es primo
        self.assertFalse(es_primo(-3))  # Números negativos no son primos

    def test_filtrar_pares(self):
        self.assertEqual(filtrar_pares([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filtrar_pares([10, 15, 20, 25]), [10, 20])
        self.assertEqual(filtrar_pares([]), [])
        self.assertEqual(filtrar_pares([1, 3, 5]), [])

    def test_sumar_lista(self):
        self.assertEqual(sumar_lista([1, 2, 3]), 6)
        self.assertEqual(sumar_lista([10, 20, 30]), 60)
        self.assertEqual(sumar_lista([]), 0)
        self.assertEqual(sumar_lista([1, "a", 3]), 4)
        self.assertEqual(sumar_lista([1, None, 3]), 4)


if __name__ == "__main__":
    unittest.main()
