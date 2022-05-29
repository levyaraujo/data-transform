# Transform Data

Script em Python que recebe um PDF como entrada, filtra o arquivo PDF em busca de tabelas e transforma essas tabelas em um arquivo **.csv**. Este programa utiliza as bibliotecas **pandas** e **tabula-py** para a filtragem e transformação desses dados.

## Requisitos

- Python 3.7+
- tabula-py
- pandas
- Java 8+ (A biblioteca tabula-py tem o Java como requisito para executar as tarefas corretamente.)



## Como baixar e executar

1. Abra seu terminal e digite o seguinte comando:

   `git clone https://github.com/levyaraujo/webScraper.git`

   ou baixe o [arquivo zip](https://github.com/levyaraujo/webScraper/archive/refs/heads/main.zip).

2. No terminal, entre na pasta principal do projeto e execute o comando `pip install -r requirements.txt` e em seguida. Este comando irá instalar todas as dependências do projeto.

3. Execute o comando `python filterTables.py`. O programa irá executar as tarefas necessárias e o resultado será um arquivo zip contendo a tabela final. 
