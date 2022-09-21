  
  def test_pontosDeEnvidoTotais_4_espadas_3_espadas_é_27(self):
    self.assertEqual(pontos_de_envido_totais(4, "espadas", 3, "espadas"), 27)
  
  def test_pontosDeEnvidoTotais_6_copas_11_copas_é_26(self):
    self.assertEqual(pontos_de_envido_totais(6, "copas", 11, "copas"), 26)
  
  def test_pontosDeEnvidoTotais_5_ouros_2_paus_é_5(self):
    self.assertEqual(pontos_de_envido_totais(5, "oro", 2, "bastos"), 5)
  
  def test_pontosDeEnvidoTotais_6_copas_7_espadas_é_7(self):
    self.assertEqual(pontos_de_envido_totais(6, "copas", 7, "espadas"), 7)
    
  def test_pontosDeEnvidoTotais_1_copa_12_espadas_é_1(self):
    self.assertEqual(pontos_de_envido_totais(1, "copas", 12, "espadas"), 1)
  
