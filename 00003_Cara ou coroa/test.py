  
  def test_decisão_com_moeda_cara_pizza_empanado_é_pizza(self):
    self.assertEqual(decisao_com_moeda("cara", "pizza", "empanado"), "pizza")

  def test_decisão_com_moeda_cara_churrasco_empanado_é_churrasco(self):
    self.assertEqual(decisao_com_moeda("cara", "churrasco", "empanado"), "churrasco")

  def test_decisão_com_moeda_coroa_pizza_empanado_é_empanado(self):
    self.assertEqual(decisao_com_moeda("coroa", "pizza", "empanado"), "empanado")

  def test_decisão_com_moeda_coroa_pizza_massas_é_massas(self):
    self.assertEqual(decisao_com_moeda("coroa", "pizza", "massas"), "massas")


