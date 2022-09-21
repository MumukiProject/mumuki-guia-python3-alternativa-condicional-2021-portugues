
  def test_medalha_segundo_colocação_1(self):
    self.assertEqual(medalha_segundo_colocacao(1), "ouro")

  def test_medalha_segundo_colocação_2(self):
    self.assertEqual(medalha_segundo_colocacao(2), "prata")

  def test_medalha_segundo_colocação_3(self):
    self.assertEqual(medalha_segundo_colocacao(3), "bronze")

  def test_medalha_segundo_colocação_4(self):
    self.assertEqual(medalha_segundo_colocacao(4), "nada")

  def test_medalha_segundo_colocação_5(self):
    self.assertEqual(medalha_segundo_colocacao(5), "nada")

  def test_medalha_segundo_colocação_0(self):
    self.assertEqual(medalha_segundo_colocacao(0), "nada")


