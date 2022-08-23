Para finalizar, agora que vimos como escrever a alternativa condicional, é momento de um pequeno lembrete:
Se você usar expressões booleanas corretamente, nem sempre será necessário usar essa estrutura de controle!


Vamos supor que queremos desenvolver uma função `e_maior_de_idade`, que nos informe se alguém tem
18 anos ou mais. Uma tentação é escrever o seguinte:

```python
def e_maior_de_idade(idade):
  if idade >= 18:
	return True
  else:
	return False
```

No entanto, **este `if` é totalmente desnecessário**, pois a expressão `idade >= 18` já é booleana:

```python
def e_maior_de_idade(idade):
  return idade >= 18
```

Muito mais simples, não é verdade? :wink:

> Para Ema um número é da sorte se:
>
> * é positivo, e
> * é menor que 100, e
> * não é o 15.
>
> Defina a função `e_numero_da_sorte` que dado um número diga se obedece a lógica anterior. Não vale usar `if`!

