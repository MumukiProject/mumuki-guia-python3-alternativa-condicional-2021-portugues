  
  def test_escrever_plaquinha_Dra_Ana_Perez_false_é_Dra_Ana_Perez(self):
    self.assertEqual(escrever_plaquinha("Dra.", "Ana", "Perez", False), "Dra. Ana Perez")
  
  def test_escrever_plaquinha_Dr_Julio_Gelman_false_é_Dr_Julio_Gelman(self):
    self.assertEqual(escrever_plaquinha("Dr.", "Julio", "Gelman", False), "Dr. Julio Gelman")
  
  def test_escrever_plaquinha_Dra_Ana_Perez_true_é_Dra_Perez_(self):
    self.assertEqual(escrever_plaquinha("Dra.", "Ana", "Perez", True), "Dra. Perez")
  
  def test_escrever_plaquinha_Dr_Julio_Gelman_true_é_Dr_Gelman_(self):
    self.assertEqual(escrever_plaquinha("Dr.", "Julio", "Gelman", True), "Dr. Gelman")
  
