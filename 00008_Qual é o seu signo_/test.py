
  def test_signo_10_é_1(self):
    self.assertEqual(signo(10), 1)

  def test_signo_1_é_1(self):
    self.assertEqual(signo(1), 1)

  def test_signo_0_é_0(self):
    self.assertEqual(signo(0), 0)

  def test_signo_menos_65_é_menos_1(self):
    self.assertEqual(signo(-65), -1)

  def test_signo_menos_87_é_menos_1(self):
    self.assertEqual(signo(-87), -1)


