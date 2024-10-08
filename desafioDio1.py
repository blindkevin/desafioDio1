#Desafio Dio 1: Classificador de Nível de Herói

#primeira variável, usamos o parâmetro da função input para indicar aos leitores de tela e ao usuário em geral o que está sendo pedido
nome = input('Digite o nome do herói')

# segunda variável, mesma coisa do anterior, com o parâmetro sendo a mensagem exibida, mas alinhada dentro da função int para converter o valor para um número inteiro
xp = int(input('Digite o total de xp de ' + nome))

# agora a verificação, usando match...case do python, introduzido no python 3.10, o equivalente do switch...case, de outras linguagens
match xp:
    case _ if xp <1000:
        nivel = "Ferro"
    case _ if xp in range(1001, 2000):
        nivel = "bronze"
    case _ if xp in range(2001, 5000):
        nivel = "Prata"
    case _ if xp in range(5001, 7000):
        nivel = "Ouro"
    case _ if xp in range(7001, 8000):
        nivel = "Platina"
    case _ if xp in range(8001, 9000):
        nivel = "Ascendente"
    case _ if xp in range(9001, 10000):
        nivel = "Imortal"
    case _ if xp >= 10001:
        nivel = "Radiante"
    case _:
        nivel = "what?"

# Após a verificação, fazemos o print, usando f-string para melhor leitura
print(f"O herói de nome {nome} está no nível de {nivel}")
input() # Uma chamada a uma função input vazia apenas para o leitor de tela poder ler todo o texto sem fechar o console na cara do usuário