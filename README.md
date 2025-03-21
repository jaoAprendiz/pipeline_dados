# Pipeline de Dados: Integração e Transformação de Dados de Empresas Fusionadas

Este projeto demonstra um pipeline de dados completo para integrar e transformar dados de duas empresas que se fundiram. O objetivo principal é consolidar dados de diferentes formatos (JSON e CSV) em um único conjunto de dados CSV, preparado para análise posterior.

## Descrição

Após a fusão de duas empresas, surge a necessidade de integrar e consolidar os dados de ambas para obter uma visão unificada. Este projeto aborda esse desafio, criando um pipeline de dados que lê dados de arquivos JSON e CSV, transforma-os e os combina em um único arquivo CSV. O pipeline é automatizado por meio de scripts ETL (Extração, Transformação e Carga) orientados a objetos.

As duas empresas comercializam diversos produtos, e este pipeline visa unificar os dados de vendas, clientes e produtos de ambas, permitindo uma análise abrangente do novo negócio.

## Tecnologias Utilizadas

* **Python**: Linguagem de programação principal utilizada para a implementação do pipeline.
* **json**: Biblioteca para leitura e processamento de dados em formato JSON.
* **csv**: Biblioteca padrão do Python para leitura e escrita de arquivos CSV.
* **Jupyter Notebook**: Ambiente interativo para exploração e análise de dados.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

* `exploracao.ipynb`: Notebook Jupyter contendo a exploração inicial dos dados e a lógica de transformação.
* `dados_empresaA.json`: Arquivo JSON contendo os dados da primeira empresa.
* `dados_empresaB.csv`: Arquivo CSV contendo os dados da segunda empresa.
* `processamento_dados.py`: Script Python contendo as classes e funções para o pipeline ETL.
* `fusao_mercado_fev.py`: Script Python para executar o pipeline ETL.
* `dados_combinados.csv`: Arquivo CSV gerado pelo pipeline, contendo os dados consolidados.

## Execução

Para executar o projeto, siga os passos abaixo:

1.  Clone este repositório:

    ```bash
    git clone https://github.com/jaoAprendiz/pipeline_dados.git
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd pipeline_dados
    cd scripts
    ```

3.  Execute o script `fusao_mercado_fev.py` para iniciar o pipeline ETL:

    ```bash
    python fusao_mercado_fev.py
    ```

4.  O arquivo `dados_combinados.csv` será gerado no diretório do projeto, contendo os dados consolidados.

## Scripts ETL (POO)

O projeto inclui dois scripts ETL que automatizam o processo de integração e transformação de dados:

* `processamento_dados.py`: Contém as classes e funções para o pipeline ETL, incluindo os seguintes métodos:
    * `__leitura_json`: Lê dados de um arquivo JSON.
    * `__leitura_csv`: Lê dados de um arquivo CSV.
    * `leitura_dados`: Coordena a leitura dos dados de ambas as empresas.
    * `__get_columns`: Obtém os nomes das colunas de um DataFrame.
    * `rename_columns`: Renomeia as colunas para um padrão consistente.
    * `__size_data`: Verifica o tamanho dos dados lidos.
    * `join`: Combina os dados das duas empresas em um único DataFrame.
    * `__transformando_dados_tabela`: Aplica transformações necessárias aos dados.
    * `salvando_dados`: Salva os dados transformados em um arquivo CSV.
* `fusao_mercado_fev.py`: Utiliza as classes e métodos do `processamento_dados.py` para executar o pipeline ETL completo.

## Conclusões

Este projeto demonstra um pipeline de dados eficiente para integrar e transformar dados de diferentes fontes e formatos. A abordagem orientada a objetos facilita a manutenção e extensibilidade do pipeline, permitindo a adição de novas funcionalidades e a adaptação a diferentes cenários de integração de dados.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão de melhoria ou correção, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
