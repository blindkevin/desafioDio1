# desafioDio1
Classificador de nível de herói do bootcamp da #dio

Deixo a baixo o conteúdo do desafio:

# 1️⃣ Desafio Classificador de nível de Herói
**O Que deve ser utilizado**
- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
## Objetivo
Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:
Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante
## Saída
Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"

##Minha explicação

Usei python, por ser uma linguagem na qual me sinto mais confortável, e aproveitei para dar algumas pequenas dicas sobre o comportamento de leitores de tela (sou um desenvolvedor cego), em algumas situações.

O código está todo comentado, mas vou resumir aqui do mesmo jeito, para fins de anotação.

* Fiz duas chamadas a função input do python, com o parâmetro de prompt sendo usado para avisar aos usuários e ao leitor de tela qual informação está sendo requisitada, e armazenei esses valores em duas variáveis: nome e xp, respectivamente
* Na segunda chamada do input para pegar a xp alinho ela dentro de uma chamada a função int, para converter o valor digitado para um número inteiro
* após isso entramos no match...case do python, introduzido na versão 3.10 da linguagem, uma espécie de switch...case, de linguagens como javascript
* dentro dos cases uso ifs e in range, para verificar e respeitar os intervalos pedidos no desafio* Após toda a verificação, onde aliás usei uma terceira variável, nivel, para armazenar os níveis correspondentes, usei o print, com uma f-string para facilitar a leitura, e exibir a mensagem final solicitada no desafio
* Para fechar, uma chamada a uma função input vazia, para o leitor de tela que uso não fechar na minha cara assim que o texto for exibido. Isso faz com que para fechar a janela do console seja preciso precionar qualquer tecla,.

Desafio testado e funcionando.