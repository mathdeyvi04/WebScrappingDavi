from FuncoesBasicas import *


def destroy():
    """
    Devemos apagar os arquivos que fizemos conversões.
    """

    for arq in listdir(getcwd()):
        if arq.endswith(".csv"):
            remove(arq)


class Extrador:
    """
    Classe responsável por executar a análise geral dos dados obtidos.
    """

    def __init__(self):
        """
        Vamos inicializar todos os elementos possíveis de .csv na pasta Downloads.
        """

        self.arquivos_disponiveis = []
        self.casa_de_download = Path.home() / "Downloads"

        for arquivo in listdir(self.casa_de_download):
            # Vamos buscar os últimos arquivos .csv
            if arquivo.endswith(".csv") and arquivo.startswith("data"):
                self.arquivos_disponiveis.append(
                    arquivo
                )

        if len(self.arquivos_disponiveis) > 4:
            # Então há um intruso, devemos fazer algo.
            pass

        if len(self.arquivos_disponiveis) < 4:
            # Há um faltante.
            pass

    def verificacoes(self):
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
            "data.csv": "relatorio_de_midia.json",
            "data (1).csv": "relatorio_de_registros.json",
            "data (2).csv": "relatorio_de_ganhos.json",
            "data (3).csv": "relatorio_de_atividades.json"
        }

        for i in range(0, 4):
            rename(
                self.casa_de_download / self.arquivos_disponiveis[i],
                correspondentes[self.arquivos_disponiveis[i]]
            )
            self.arquivos_disponiveis[i] = Extrador.conversor(
                correspondentes[self.arquivos_disponiveis[i]]
            )

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


if __name__ == '__main__':
    analiser = Extrador()

    analiser.verificacoes()

    destroy()
