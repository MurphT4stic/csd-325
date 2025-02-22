import unittest 
from city_functions import city_country 

class TestCityCountry (unittest.TestCase):
    def test_city_country(self): 
        result = city_country("Santiago", "Chile")
        expected_output = "Santiago, Chile"
        self.assertEqual(result, "Santiago, Chile") 

if __name__ == "__main__": 
    unittest.main() 


