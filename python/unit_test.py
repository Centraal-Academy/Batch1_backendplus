import unittest
import functions
import my_exceptions as exc

class TestFunctions(unittest.TestCase):

    def test_product(self):
        self.assertEqual(functions.add_by(5,5), 25)
        self.assertEqual(functions.add_by(5,5), 25)
        self.assertEqual(functions.sum_by(5,10), 15)
        self.assertEqual(functions.sum_by(5,15), 20)

    def test_boolean(self):
        self.assertTrue(functions.compareValue(6))
        self.assertTrue(functions.compareValue(10))

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            functions.compareValue(1)
        with self.assertRaises(TypeError):
            functions.add_by('x','hola')
            functions.add_by(5,'hola')
            functions.add_by(5,False)
            functions.add_by(5,[1,2,3,4])
        with self.assertRaises(exc.AnotherError):
            functions.sum_by(1,1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)