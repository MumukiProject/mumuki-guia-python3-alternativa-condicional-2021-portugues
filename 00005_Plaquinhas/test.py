  
  def test_escrever_plaquinha_Dra_Ana_Perez_é_Dra_Ana_Perez(self):
    self.assertEqual(escrever_plaquinha("Dra.", "Ana", "Perez"), "Dra. Ana Perez")
  
  def test_escrever_plaquinha_Dr_Julio_Gelman_é_Dr_Julio_Gelman(self):
    self.assertEqual(escrever_plaquinha("Dr.", "Julio", "Gelman"), "Dr. Julio Gelman")

