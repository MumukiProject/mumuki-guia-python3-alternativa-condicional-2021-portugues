  
  # positivos menores a 100 diferentes de 15
  
  def test_é_numero_da_sorte_2_é_verdadeiro(self):
    self.assertTrue(e_numero_da_sorte(2))

  def test_é_numero_da_sorte_5_é_verdadeiro(self):
    self.assertTrue(e_numero_da_sorte(5))

  def test_é_numero_da_sorte_9_é_verdadeiro(self):
    self.assertTrue(e_numero_da_sorte(9))

  def test_é_numero_da_sorte_45_é_verdadeiro(self):
    self.assertTrue(e_numero_da_sorte(45))
    
  def test_é_numero_da_sorte_97_é_verdadeiro(self):
    self.assertTrue(e_numero_da_sorte(97))  
    
  # mayores a 100
  
  def test_é_numero_da_sorte_101_é_falso(self):
    self.assertFalse(e_numero_da_sorte(101))

  def test_é_numero_da_sorte_12456_é_falso(self):
    self.assertFalse(e_numero_da_sorte(12456))

  def test_é_numero_da_sorte_3003_é_falso(self):
    self.assertFalse(e_numero_da_sorte(3003))

  # negativos

  def test_é_numero_da_sorte_é_falso_se_é_negativo(self):
    self.assertFalse(e_numero_da_sorte(-3))

  # el 15

  def test_é_numero_da_sorte_15_é_falso(self):
    self.assertFalse(e_numero_da_sorte(15))
