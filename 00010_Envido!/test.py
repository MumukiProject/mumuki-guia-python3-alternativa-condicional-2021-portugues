  
  def test_valor_envido_2_é_2(self):
    self.assertEqual(valor_envido(2), 2)
  
  def test_valor_envido_1_é_1(self):
    self.assertEqual(valor_envido(1), 1)
  
  def test_valor_envido_5_é_5(self):
    self.assertEqual(valor_envido(5), 5)
    
  def test_valor_envido_7_é_7(self):
    self.assertEqual(valor_envido(7), 7)  
  
  def test_valor_envido_12_é_0(self):
    self.assertEqual(valor_envido(12), 0)
  
  def test_valor_envido_11_é_0(self):
    self.assertEqual(valor_envido(11), 0)
  
  def test_valor_envido_10_é_0(self):
    self.assertEqual(valor_envido(10), 0)
