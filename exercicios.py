import re
import string 

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

logs = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
       {'timestamp': '2021-07-28 10:00:00', 'level': 'SUCESS', 'message': 'Usuário autenticado'},
       {'timestamp': '2021-07-28 10:00:00', 'level': 'ERROR', 'message': 'Senha inválida'}]

for log in logs:
    if log['level'] == 'ERROR':
        print(log)

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 28
email = "igor@gmail.com.br"

padrao_email = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

idade_valida = idade_valida = 18 <= idade <= 65

if idade_valida <= 65 and padrao_email.match(email):
    print("Entrada válida.")
else:
    print("Entrada inválida.")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

contagem_de_palavras = {}

texto = "hoje, nossa segunda aula do bootcamp, bootcamp de python! Python é uma das melhores linguagens de programação e a aula está ótima"

padrao_pontuacao = re.compile(f"[{re.escape(string.punctuation)}]")

texto_sem_pontuacao = padrao_pontuacao.sub('', texto)

lista_palavras = texto_sem_pontuacao.lower().split()

for palavra in lista_palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

print('\n', texto)
print(contagem_de_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_com_dados_faltantes = [usuario for usuario in usuarios if usuario["email"] == '']

print('\n', usuarios_com_dados_faltantes)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
total_vendas_por_categoria = {}

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_vendas_por_categoria:
        total_vendas_por_categoria[categoria] += valor
    else:
        total_vendas_por_categoria[categoria] = valor

print("\n", total_vendas_por_categoria)
### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while valor != 'sair':
    valor = input("Digite um valor (ou 'sair' para terminar): ")
    if valor != 'sair':
        valor = int(valor)
        print(f"\nO número que você digitou {valor} multiplicado por 2 é {valor*2}")


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

valor = int(input("Digite um valor entre 1000 e 2000: "))
while valor < 1000 or valor > 2000:
    print("\nNúmero fora do intervalo!")
    valor = int(input("Por favor, digite um valor entre 1000 e 2000: "))
print(f"\nVocê digitou um valor conforme solicitado.")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

numero_paginas = 5
pagina_atual = 1

while pagina_atual <= numero_paginas:
    print(f"\nLendo arquivos da página {pagina_atual}...")
    pagina_atual += 1

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.