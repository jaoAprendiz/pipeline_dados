import json
import csv


class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    def __leitura_json(self, path):
        with open(path, 'r') as file:
            return json.load(file)

    def __leitura_csv(self, path):
        dados_csv = []
        with open(path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        obj_temp = cls([])  # Criamos um objeto temporário para acessar os métodos de instância

        if tipo_dados == 'csv':
            dados = obj_temp.__leitura_csv(path)
        elif tipo_dados == 'json':
            dados = obj_temp.__leitura_json(path)
        else:
            raise ValueError("Tipo de dados inválido. Use 'csv' ou 'json'.")

        return cls(dados)

    def __get_columns(self):
        return list(self.dados[-1].keys()) if self.dados else []

    def rename_columns(self, key_mapping):
        new_dados_csv = []

        for old_dict in self.dados:
            dict_temp = {key_mapping.get(old_key, old_key): value for old_key, value in old_dict.items()}
            new_dados_csv.append(dict_temp)

        self.dados = new_dados_csv
        self.nome_colunas = self.__get_columns()

    def __size_data(self):
        return len(self.dados)

    def join(self, dadosB):
        self.dados += dadosB.dados
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = [row.get(coluna, 'Indisponível') for coluna in self.nome_colunas]
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela

    def salvando_dados(self, path):
        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
