class Test(unittest.TestCase):

  def test_saludar_a_gus(self):
    self.assertEquals(cumprimentar_a("Gus"), "Buenos días Gus")
    
  def test_saludar_a_may(self):
    self.assertEquals(cumprimentar_a("May"), "Buenos días May")