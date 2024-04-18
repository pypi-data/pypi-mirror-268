import unittest
import numpy as np
from Paquetes.Hola.test3 import generar_arrray

class PruebasHola(unittest.TestCase):

    def test_generar_array(self):
        np.testing.assert_array_equal(
            np.array([0,1,2,3,4,5]),
            generar_arrray(6)
        )

