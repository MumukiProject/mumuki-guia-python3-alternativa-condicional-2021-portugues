Ah, mas não tão rápido! Algumas vezes em nossa plaquinha :name_badge: só queremos a formação e o sobrenome, sem o nome.

Por isso agora precisamos  melhorar nossa função de forma que receba 4 parâmetros:

* O título
* O nome e o sobrenome, como até agora
* Um booleano que nos indique se queremos uma plaquinha menor só com a formação e o sobrenome, ou uma grande, como até agora.


> Modifique a função `escrever_plaquinha`, de forma que se comporte como está descrito acima.
>
> ```python
> ム escrever_plaquinha("Lic.", "Tomás", "Peralta", True)
> "Lic. Peralta"
> ム escrever_plaquinha("Enga.", "Diana", "Ferreira", False)
> "Enga. Diana Ferreira"
> ```
