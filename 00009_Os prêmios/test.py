
  def test_medalla_segun_puesto_1(self):
    self.assertEqual(medalha_segundo_colocacao(1), "ouro")

  def test_medalla_segun_puesto_2(self):
    self.assertEqual(medalha_segundo_colocacao(2), "prata")

  def test_medalla_segun_puesto_3(self):
    self.assertEqual(medalha_segundo_colocacao(3), "bronze")

  def test_medalla_segun_puesto_4(self):
    self.assertEqual(medalha_segundo_colocacao(4), "nada")

  def test_medalla_segun_puesto_5(self):
    self.assertEqual(medalha_segundo_colocacao(5), "nada")

  def test_medalla_segun_puesto_0(self):
    self.assertEqual(medalha_segundo_colocacao(0), "nada")


