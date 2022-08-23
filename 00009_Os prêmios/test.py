
  def test_medalla_segun_puesto_1(self):
    self.assertEqual(medalha_segundo_colocacao(1), "oro")

  def test_medalla_segun_puesto_2(self):
    self.assertEqual(medalha_segundo_colocacao(2), "plata")

  def test_medalla_segun_puesto_3(self):
    self.assertEqual(medalha_segundo_colocacao(3), "bronce")

  def test_medalla_segun_puesto_4(self):
    self.assertEqual(medalha_segundo_colocacao(4), "nada")

  def test_medalla_segun_puesto_5(self):
    self.assertEqual(medalha_segundo_colocacao(5), "nada")

  def test_medalla_segun_puesto_0(self):
    self.assertEqual(medalha_segundo_colocacao(0), "nada")


