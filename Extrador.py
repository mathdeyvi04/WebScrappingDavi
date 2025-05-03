from FuncoesBasicas import *


def destroy():
    """
    Devemos apagar os arquivos que fizemos conversões.
    """

    for arq in listdir():
        if arq.endswith(".json"):
            remove(arq)


class Extrador:
    """
    Classe responsável por executar a análise geral dos dados obtidos.
    """

    def __init__(self):
        """
        Vamos inicializar todos os elementos possíveis de .csv na pasta Downloads.
        """

        self.config = {
            'user': 'writer',
            'password': '7TjmP0E3q4fm',
            'host': '34.9.125.77',
            'port': '5432',
            'dbname': 'postgres'
        }

        self.arquivos_disponiveis = []
        self.casa_de_download = Path.home() / "Downloads"

        for arquivo in listdir(self.casa_de_download):
            # Vamos buscar os últimos arquivos .csv
            if arquivo.endswith(".csv") and arquivo.startswith("data"):
                self.arquivos_disponiveis.append(
                    arquivo
                )

        if not any(arq.endswith(".json") for arq in listdir()):
            if len(self.arquivos_disponiveis) > 4:
                # Então há um intruso, devemos fazer algo.
                exit(-1)

            if len(self.arquivos_disponiveis) < 4:
                # Há um faltante.
                exit(-2)

    def verificar_converter(self):
        """
        Descrição:
            Faremos verificações intrínsecas à qual relatório pertence a qual.
            Dado que o site apenas exporta relatórios com nome 'data.csv', o
            sistema operacional força a renomeação para 'data (x).csv'.

            Tento em vista isso, devemos realizar verificações e deduzir
            qual arquivo .csv corresponde a que.
        """

        # É natural que 'data (a).csv' seja um arquivo mais antigo que 'data (b).csv'
        # caso a < b. Com isso poderemos fazer nossas deduções.

        # Do jeito que construimos Coletor, só nos resta:
        correspondentes = {
            "data.csv": "platformmidia.json",
            "data (1).csv": "platform_registros.json",
            "data (2).csv": "platform_ganhos.json",
            "data (3).csv": "platform_atividades.json"
        }

        for i in range(0, 4):
            rename(
                self.casa_de_download / self.arquivos_disponiveis[i],
                correspondentes[self.arquivos_disponiveis[i]]
            )
            self.arquivos_disponiveis[i] = Extrador.conversor(
                correspondentes[self.arquivos_disponiveis[i]]
            )

    def enviar(self):
        """
        Vamos enviar à tabela.
        """

        if len(self.arquivos_disponiveis) == 0:
            self.arquivos_disponiveis = [
                arq for arq in listdir() if arq.endswith(".json")
            ]

        conn = psycopg2.connect(
            **self.config
        )
        cursor = conn.cursor()

        for arquivo in self.arquivos_disponiveis:
            with open(
                    arquivo,
                    "r"
            ) as arq:
                conteudo_json = json.load(arq)

            # Vamos inserir
            query = """
                INSERT INTO aposta_suprema_events (file_name, source_name, payload)
                VALUES (%s, %s, %s);
            """

            cursor.execute(
                query,
                (
                    arquivo.replace(".json", ""),
                    "scrapping_server",
                    json.dumps(conteudo_json)
                )
            )

            print(f"{arquivo} foi enviado com sucesso")

        cursor.close()
        conn.close()

    @staticmethod
    def conversor(arquivo: str) -> str:
        """
        Devemos fazer a conversão de .csv para .json.
        """

        df = pd.read_csv(arquivo)

        arquivo = arquivo.replace(".csv", ".json")
        df.to_json(
            arquivo,
            orient='records',
            indent=4
        )

        return arquivo


    def ver_tabela(self) -> None:
        conn = psycopg2.connect(
            **self.config
        )
        cursor = conn.cursor()

        query = "SELECT file_name, source_name, payload FROM aposta_suprema_events LIMIT 10;"
        cursor.execute(query)

        # 📋 Captura os resultados
        registros = cursor.fetchall()

        # 📤 Mostra os dados
        for file_name, source_name, payload in registros:
            print(f"\n📂 file_name: {file_name}")
            print(f"🛰️ source_name: {source_name}")
            print(f"📦 payload:\n{json.dumps(payload, indent=4)}")

        cursor.close()
        conn.close()


if __name__ == '__main__':
    analiser = Extrador()

    # analiser.verificar_converter()

    # analiser.enviar()

    analiser.ver_tabela()

    destroy()
