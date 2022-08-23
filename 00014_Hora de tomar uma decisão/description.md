Na verdade nem sempre cumprimentamos com _bom dia_: por exemplo, depois de certo horário dizemos _boa noite_. :night_with_stars:

Por isso, agora gostaríamos de modificar nossa função `cumprimentar_a` para que utilize um parâmetro adicional, `horario`, e retorne um cumprimento diferente como este:

```python
ム cumprimentar_a("Dani", 10)
"Bom dia Dani"
ム cumprimentar_a("Feli", 22)
"Boa noite Feli"
```

Mas como poderíamos conseguir isso? Nenhuma introdução à linguagem Python estaria completa sem mostrar _a estrutura de controle _ mais famosa da programação: a alternativa condicional!

```python
def cumprimentar_a(quem, horario):
  if horario < 19:
	return "Bom dia " + quem
  else:
	return "Boa noite " + quem
```

> :hourglass_flowing_sand: Reserve alguns minutos para ler este `if` e tentar entender o que está acontecendo aqui. E depois tente o seguinte no console:
>
>  1. cumprimente a `"Juli"` às `18`
>  2. cumprimente a `"Pun Pun"` às `19`
>
> Acontece o que você esperava? :thinking:

