class Test(unittest.TestCase):

  def test_cumprimentar_a_gus(self):
    self.assertEquals(cumprimentar_a("Gus"), "Bom dia Gus")
    
  def test_cumprimentar_a_may(self):
    self.assertEquals(cumprimentar_a("May"), "Bom dia May")