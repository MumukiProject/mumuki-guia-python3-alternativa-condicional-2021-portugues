  
  def test_valor_canto_truco_retruco_é_3(self):
    self.assertEqual(valor_canto_truco("retruco"), 3)
  
  def test_valor_canto_truco_truco_é_2(self):
    self.assertEqual(valor_canto_truco("truco"), 2)
  
  def test_valor_canto_truco_vale_cuatro_é_4(self):
    self.assertEqual(valor_canto_truco("vale quatro"), 4)
  
