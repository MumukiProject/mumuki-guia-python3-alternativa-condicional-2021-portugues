  
  def test_escribe_un_cartelito_largo_cuando_el_nombre_es_carla_toledo(self):
    self.assertEqual(escrever_plaquinha_ideal("Ing.", "Carla", "Toledo"), "Ing. Carla Toledo")
  
  def test_escribe_un_cartelito_largo_cuando_el_nombre_es_branco_luis(self):
    self.assertEqual(escrever_plaquinha_ideal("Ing.", "Branco", "Luis"), "Ing. Branco Luis")
  
  def test_escribe_un_cartelito_corto_cuando_el_nombre_es_estanislao_schwarzschild(self):
    self.assertEqual(escrever_plaquinha_ideal("Dr.", "Estanislao", "Schwarzschild"), "Dr. Schwarzschild")
  
  def test_escribe_un_cartelito_corto_cuando_el_nombre_es_katherine_boumann(self):
    self.assertEqual(escrever_plaquinha_ideal("Ing.", "Katherine", "Boumann"), "Ing. Boumann")