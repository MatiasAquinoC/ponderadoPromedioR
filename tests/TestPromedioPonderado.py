import unittest
from src.logica.PromedioPonderado import ConjuntoPonderado

class TestConjuntoPonderado(unittest.TestCase):
    def test_promedio_ponderado_caso1(self):
        datos = [10, 12, 14]
        pesos = [3, 4, 2]
        conjunto_ponderado = ConjuntoPonderado(datos, pesos)
        self.assertAlmostEqual(11.78, conjunto_ponderado.promedio_ponderado(), delta=0.01)

    def test_promedio_ponderado_caso2(self):
        datos = [15, 15, 17]
        pesos = [3, 4, 2]
        conjunto_ponderado = ConjuntoPonderado(datos, pesos)
        self.assertAlmostEqual(15.44, conjunto_ponderado.promedio_ponderado(), delta=0.01)

if __name__ == '__main__':
    print("Ejecutando pruebas...")
    unittest.main()
