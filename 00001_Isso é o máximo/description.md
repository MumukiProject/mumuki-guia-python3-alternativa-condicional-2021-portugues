_Bom, talvez não seja para taaaanto, mas sim, o `if` é muito útil_  :stuck_out_tongue_closed_eyes:

Vamos ver outro exemplo...

```python
# Equivalente a abs
def valor_absoluto(numero):
  if numero >= 0:
	return numero
  else:
	return -numero
```

...e vamos colocar nome para cada parte da alternativa condicional:  

 1. em primeiro lugar, temos a _condição_, que é o que decide qual a ação que vamos executar. Poderia ser qualquer _expressão booleana_, ou dito de forma simples qualquer coisa que represente uma "pergunta" que possa ser respondida com sim (`True`) ou não (`False`);
 2. logo está _a ação_ do `if`, que retornará o que queremos no caso de que a condição anterior seja **verdadeira**;
 3. por último contamos con  _a ação_ do `else`, que retornará o que queremos no caso de que a condição anterior seja **falsa**.

Além disso,  cada uma dessas ações são conhecidas como _ramos_ :deciduous_tree:, porque ramificam o fluxo de execução, introduzindo em nosso programa caminhos alternativos. Ah, e algo não menos importante: as tabulações `↹` em cada ramo são necessárias para que tudo funcione. :sweat_smile:

> Vamos escrever nossso primeiro `if`! Defina uma função `maximo`, que funcione como `max` (não vale usá-la!) e retorne o máximo entre dois números:
>
> ```python
> ム maximo(4, 5)
> 5
> ム maximo(10, 4)
> 10
> ```
