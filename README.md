# Agenda 8 — Desenvolvimento de Sistemas I

Este projeto foi desenvolvido como parte da **Agenda 8 da disciplina de Desenvolvimento de Sistemas I**, do **Curso Técnico em Desenvolvimento de Sistemas da ETEC**.

## Objetivo

O objetivo deste programa é praticar o uso de **estruturas de repetição e estruturas condicionais em Python**, utilizando o comando `for` para repetir a coleta de dados dos entrevistados e os comandos `if` e `elif` para verificar as respostas informadas.

O programa simula uma pesquisa de satisfação realizada pela empresa de marketing para avaliar a opinião dos clientes sobre o atendimento.

## Funcionamento

O programa solicita as seguintes informações:

* Nome;
* Idade;
* Opinião sobre o atendimento.

A avaliação do atendimento deve ser informada utilizando uma das seguintes opções:

* **1 — EXCELENTE**
* **2 — BOM**
* **3 — RUIM**

Para cada entrevistado, o programa verifica a resposta informada utilizando estruturas condicionais.

Quando a opção **1 (EXCELENTE)** é selecionada, o programa adiciona uma resposta ao contador de avaliações excelentes.

Quando a opção **3 (RUIM)** é selecionada, o programa adiciona uma resposta ao contador de avaliações ruins.

Ao final da pesquisa, o programa exibe:

* A quantidade total de respostas **EXCELENTE**;
* A quantidade total de respostas **RUIM**.

## Estrutura de repetição

A estrutura `for` é utilizada para repetir a pesquisa para cada entrevistado.

O exercício determina que a pesquisa completa seja realizada com **50 entrevistados**. Entretanto, para realizar os testes solicitados na atividade, o programa foi configurado inicialmente com **10 entrevistados**:

```python
for i in range(10):
```

Após a validação do funcionamento do programa, a quantidade foi alterada para 50:

```python
for i in range(50):
```

## Contadores

Antes do início da pesquisa, são criadas duas variáveis para armazenar a quantidade de avaliações:

```python
count_excelente = 0
count_ruim = 0
```

Cada vez que um entrevistado informa a opção **1**, o contador de respostas excelentes é incrementado:

```python
if opiniao == 1:
    count_excelente += 1
```

Caso o entrevistado informe a opção **3**, o contador de respostas ruins é incrementado:

```python
elif opiniao == 3:
    count_ruim += 1
```

Ao final das entrevistas, os resultados são apresentados na tela, mostrando a quantidade de avaliações classificadas como **Excelente** e **Ruim**.
