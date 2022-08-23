Agora que já vimos vários `if`s, vamos voltar para a função com a qual iniciamos a lição:

```python
ム cumprimentar_a("Ivi", 17)
"Bom dia Ivi"
```

Não é um pouco tarde para dizer  _bom dia_? :dizzy_face: Não seria melhor que `cumprimentar_a` fizesse o seguinte?

 1. Se são menos de 12h, que diga _Bom dia_;
 2. **em caso contrário** e se são menos de 19 h, que diga _Boa tarde_;
 3. **em caso contrário**, finalmente, que diga _Boa noite_.
 
Sim, isso é exatamente o que queremos! Vamos dar as boas vindas a um amigo inseparável do `if` e do `else`: o `elif`.

```python
def cumprimentar_a(quem, horario):
  if horario < 12:
	return "Bom dia " + quem
  elif horario < 19:
	return "Boa tarde " + quem
  else:
	return "Boa noite " + quem
```

Como podemos ver, o `elif` permite tomar uma decisão quando a condição anterior não se cumpriu, e da mesma forma que seu nome sugere, funciona como a combinação de um `if` logo depois de um `else`.

> :warning: Isso significa que as condições são avaliadas **em ordem**? Esta definição alternativa...
>
> ```python
> def cumprimentar_a_recarregado(quem, horario):
>  if horario < 19:
>	return "Boa tarde " + quem
>  elif horario < 12:
>	return "Bom dia " + quem
>  else:
>	return "Boa noite " + quem
> ```
>
> ... vai fazer o mesmo que a anterior? Deixamos no console a `cumprimentar_a` e `cumprimentar_a_recarregado` para que você teste e compare.
>
> Quando terminar, escreva `pronto()`

