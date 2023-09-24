import unittest
from Classical_Quantum import *
import math

class classicalToQuantum(unittest.TestCase):

    def test_canicas_booleanas(self):
        booleanMatrix = [[False, False, False, False, False, False], [True, False, False, False, False, True],
                         [True, False, False, False, False, False], [False, False, True, False, False, False],
                         [False, False, False, True, False, False], [False, False, False, False, True, False]]

        vectIni = [True, False, False, False, False, False]

        self.assertEqual(canicas_booleanas(1, booleanMatrix[:], vectIni[:]),
                         [False, True, True, False, False, False])

        self.assertEqual(canicas_booleanas(3, booleanMatrix[:], vectIni[:]),
                         [False, False, False, False, True, False])

        self.assertEqual(canicas_booleanas(5, booleanMatrix[:], vectIni[:]),
                         [False, True, False, False, False, False])

    def test_multiple_rendija_clasico(self):
        matrix = [[complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
            [complex(1 / 3, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(1 / 3, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(1 / 3, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(1 / 2, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(1 / 2, 0), complex(1 / 2, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(0, 0), complex(1 / 2, 0), complex(1 / 2, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(0, 0), complex(0, 0), complex(1 / 2, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)]]

        vectIni = [complex(1, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0)]

        self.assertEqual(sistema_probabilistico(matrix[:], vectIni[:], 1), [complex(0, 0),
                                                                                        complex(0.3333333333333333, 0.0),
                                                                                        complex(0.3333333333333333, 0.0),
                                                                                        complex(0.3333333333333333, 0.0),
                                                                                        complex(0.0, 0.0),
                                                                                        complex(0.0, 0.0),
                                                                                        complex(0.0, 0.0),
                                                                                        complex(0.0, 0.0)])
        # Modificando la matriz
        matrix = [
        [complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
        [complex(0.5, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
        [complex(0.5, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
        [complex(0, 0), complex(0.3333333333333333, 0), complex(0, 0), complex(1, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
        [complex(0, 0), complex(0.3333333333333333, 0), complex(0, 0), complex(0, 0), complex(1, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
        [complex(0, 0), complex(0.3333333333333333, 0), complex(0.3333333333333333, 0), complex(0, 0), complex(0, 0),complex(1, 0), complex(0, 0), complex(0, 0)],
        [complex(0, 0), complex(0, 0), complex(0.3333333333333333, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(1, 0), complex(0, 0)],
        [complex(0, 0), complex(0, 0), complex(0.3333333333333333, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(1, 0)]]


        vectIni = [complex(1, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0),complex(0, 0)]

        self.assertEqual(sistema_probabilistico(matrix[:], vectIni[:], 2),[complex(0.0, 0.0),
                                                                          complex(0.0, 0.0),
                                                                          complex(0.0, 0.0),
                                                                          complex(0.16666666666666666, 0.0),
                                                                          complex(0.16666666666666666, 0.0),
                                                                          complex(0.3333333333333333, 0.0),
                                                                          complex(0.16666666666666666, 0.0),
                                                                          complex(0.16666666666666666, 0.0)])

    def testmultiplerendijacuantico(self):
        matrix = [[complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
            [complex(0.7071067811865475, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(0.7071067811865475, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(-0.4082482904638631, 0.4082482904638631), complex(0, 0), complex(1, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(-0.4082482904638631, -0.4082482904638631), complex(0, 0), complex(0, 0),complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(0.4082482904638631, -0.4082482904638631),complex(-0.4082482904638631, 0.4082482904638631), complex(0, 0), complex(0, 0), complex(1, 0),complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(0, 0), complex(-0.4082482904638631, -0.4082482904638631), complex(0, 0),complex(0, 0), complex(0, 0), complex(1, 0), complex(0, 0)],
            [complex(0, 0), complex(0, 0), complex(0.4082482904638631, -0.4082482904638631), complex(0, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(1, 0)]]

        vectIni = [complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)]
        self.assertEqual(multiple_rendija_cuantico(matrix[:], vectIni[:], 1), [[complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
                                                                             [complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
                                                                             [complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
                                                                             [complex(0.1666666666666667, 0), complex(0.3333333333333334, 0), complex(0, 0), complex(1.0, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0)],
                                                                             [complex(0.1666666666666667, 0), complex(0.3333333333333334, 0), complex(0, 0), complex(0, 0),complex(1.0, 0), complex(0, 0), complex(0, 0), complex(0, 0)],
                                                                             [complex(0, 0), complex(0.3333333333333334, 0), complex(0.3333333333333334, 0), complex(0, 0),complex(0, 0), complex(1.0, 0), complex(0, 0), complex(0, 0)],
                                                                             [complex(0.1666666666666667, 0), complex(0, 0), complex(0.3333333333333334, 0), complex(0, 0),complex(0, 0), complex(0, 0), complex(1.0, 0), complex(0, 0)],
                                                                             [complex(0.1666666666666667, 0), complex(0, 0), complex(0.3333333333333334, 0), complex(0, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(1.0, 0)]])

    def testgrafico(self):


        Matriz_Doble_Rendija = [[complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0)],
                                [complex(1/math.sqrt(2), 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
                                [complex(1/math.sqrt(2), 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0)],
                                [complex(0, 0), complex(-1/math.sqrt(6), 1/math.sqrt(6)), complex(0, 0), complex(1, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0)],
                                [complex(0, 0), complex(-1/math.sqrt(6), -1/math.sqrt(6)), complex(0, 0), complex(0, 0),complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)],
                                [complex(0, 0), complex(1/math.sqrt(6), -1/math.sqrt(6)),complex(-1/math.sqrt(6), 1/math.sqrt(6)), complex(0, 0), complex(0, 0), complex(1, 0),complex(0, 0), complex(0, 0)],
                                [complex(0, 0), complex(0, 0), complex(-1/math.sqrt(6), -1/math.sqrt(6)), complex(0, 0),complex(0, 0), complex(0, 0), complex(1, 0), complex(0, 0)],
                                [complex(0, 0), complex(0, 0), complex(1/math.sqrt(6), -1/math.sqrt(6)), complex(0, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(1, 0)]]

        Estado_Inicial = [complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0),complex(0, 0), complex(0, 0), complex(0, 0), complex(0, 0)]

        answ = matrix_action_vector(multiple_rendija_cuantico(Matriz_Doble_Rendija[:],Estado_Inicial[:], 2), Estado_Inicial)
        grafico(answ)


if __name__ == '__main__':
    unittest.main()