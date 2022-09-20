  
  def test_decisão_com_moeda_cara_pizzas_empanadas_é_pizzas(self):
    self.assertEqual(decisao_com_moeda("cara", "pizzas", "empanadas"), "pizzas")

  def test_decisão_com_moeda_cara_churrasco_empanadas_é_churrasco(self):
    self.assertEqual(decisao_com_moeda("cara", "asado", "empanadas"), "asado")

  def test_decisão_com_moeda_coroa_pizzas_empanadas_é_empanadas(self):
    self.assertEqual(decisao_com_moeda("ceca", "pizzas", "empanadas"), "empanadas")

  def test_decisão_com_moeda_coroa_pizzas_massas_é_massas(self):
    self.assertEqual(decisao_com_moeda("ceca", "pizzas", "pastas"), "pastas")


