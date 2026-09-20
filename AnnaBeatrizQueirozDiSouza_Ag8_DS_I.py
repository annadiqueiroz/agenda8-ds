count_excelente = 0 #começa com 0 avaliações para cada classificaçao
count_ruim = 0

for i in range(10): #range 50 por serem 50 respostas/entrevistados
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: ")) #int para interpretar ser número inteiro
    opiniao = int(input("Qual sua nota para o atendimento? Digite 1 para 'Excelente', 2 para 'Bom' e 3 para 'Ruim': "))
    if opiniao == 1: #cada vez que alguem digitar 1 (excelente), soma +1 na quantidade de excelentes
        count_excelente +=1
    elif opiniao == 3: #cada vez que alguem digitar 3 (ruim), soma +1 resposta na quantidade de ruins
        count_ruim +=1

print(f"A quantidade de respostas de nota Excelente (1) foi: {count_excelente} respostas")
print(f"A quantidade de respostas de nota Ruim (3) foi: {count_ruim} respostas")