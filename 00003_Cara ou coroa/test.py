  
  def test_decision_con_moneda_cara_pizzas_empanadas_es_pizzas(self):
    self.assertEqual(decisao_com_moeda("cara", "pizzas", "empanadas"), "pizzas")

  def test_decision_con_moneda_cara_asado_empanadas_es_asado(self):
    self.assertEqual(decisao_com_moeda("cara", "asado", "empanadas"), "asado")

  def test_decision_con_moneda_ceca_pizzas_empanadas_es_empanadas(self):
    self.assertEqual(decisao_com_moeda("ceca", "pizzas", "empanadas"), "empanadas")

  def test_decision_con_moneda_ceca_pizzas_pastas_es_pastas(self):
    self.assertEqual(decisao_com_moeda("ceca", "pizzas", "pastas"), "pastas")


