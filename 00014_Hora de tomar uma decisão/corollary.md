Na programação dizemos que o `if` é _uma estrutura de controle_ porque permite controlar o fluxo de execução: executa uma coisa ou outra dependendo de uma condição.  Em particular, o exemplo anterior podemos ler como:

* _se (`if`) o horário é **menor** que 19, então retornar bom dia concatenado com o nome_;
* _se não (`else`), retornar boa noite concatenado com o nome_;


É por isso que:

* quando cumprimentamos a Juli às 18 h executa-se `return "Bom dia " + quem`;
* mas quando cumprimentamos a Pun Pun às 19 horas (atenção :eye:, 19 **não é menor que** 19)  executa-se `"Boa noite " + quem`.
