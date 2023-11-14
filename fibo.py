# Importación de librerias
import unittest

#Funcion que genera lista de fibonnacy
def fibonnacy(num_esperado):
    list_fibonnacy = [0,1]
    while list_fibonnacy[-1] < num_esperado:
        list_fibonnacy.append(list_fibonnacy[-1]+list_fibonnacy[-2])
    return list_fibonnacy

# Clase que hara la comprobación
class test(unittest.TestCase):
    # Función requerida para el unitest
    def test_fibonnacy(self):
        # Preguntas al usuario
        num_esperado = int(input("numero esperado: "))
        posicion_esperada = int(input("posicion esperada: "))
        
        # Ejecución comprobación
        self.assertEqual(fibonnacy(num_esperado)[posicion_esperada-1],num_esperado)

# Ejecucion codigo base
if __name__ == "__main__":
    unittest.main()