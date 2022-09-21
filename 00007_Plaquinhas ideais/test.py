  
  def test_escreva_uma_plaquinha_longa_quando_o_nome_é_carla_toledo(self):
    self.assertEqual(escrever_plaquinha_ideal("Ing.", "Carla", "Toledo"), "Ing. Carla Toledo")
  
  def test_escreva_uma_plaquinha_longa_quando_o_nome_é_branco_luis(self):
    self.assertEqual(escrever_plaquinha_ideal("Ing.", "Branco", "Luis"), "Ing. Branco Luis")
  
  def test_escreva_uma_plaquinha_curta_quando_o_nome_é_estanislao_schwarzschild(self):
    self.assertEqual(escrever_plaquinha_ideal("Dr.", "Estanislao", "Schwarzschild"), "Dr. Schwarzschild")
  
  def test_escreva_uma_plaquinha_curta_quando_o_nome_é_katherine_boumann(self):
    self.assertEqual(escrever_plaquinha_ideal("Ing.", "Katherine", "Boumann"), "Ing. Boumann")