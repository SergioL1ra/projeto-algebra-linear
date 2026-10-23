import unittest

import numpy as np

from src.principal import principal


class PrincipalContractTests(unittest.TestCase):
    def test_preserves_known_values_and_shape(self):
        observada = np.array([[2.0, 0.0], [0.0, 6.0]])
        mascara = np.array([[True, False], [False, True]])

        resultado = principal(observada, mascara)

        self.assertEqual(resultado.shape, observada.shape)
        np.testing.assert_array_equal(resultado[mascara], observada[mascara])
        self.assertTrue(np.all(np.isfinite(resultado)))

    def test_returns_finite_values_when_all_positions_are_hidden(self):
        observada = np.zeros((3, 2))
        mascara = np.zeros((3, 2), dtype=bool)

        resultado = principal(observada, mascara)

        self.assertEqual(resultado.shape, observada.shape)
        self.assertTrue(np.all(np.isfinite(resultado)))


if __name__ == "__main__":
    unittest.main()
