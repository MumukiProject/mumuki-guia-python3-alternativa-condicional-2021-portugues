  
  def test_escribir_cartelito_Dra_Ana_Perez_es_Dra_Ana_Perez(self):
    self.assertEqual(escrever_plaquinha("Dra.", "Ana", "Perez"), "Dra. Ana Perez")
  
  def test_escribir_cartelito_Dr_Julio_Gelman_es_Dr_Julio_Gelman(self):
    self.assertEqual(escrever_plaquinha("Dr.", "Julio", "Gelman"), "Dr. Julio Gelman")

