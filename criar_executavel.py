"""
Código capaz de executar os respectivos códigos.
"""

lista_de_arquivos_a_serem_executados = (
    r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\WebScrapping_Davi\FuncoesBasicas.py",
    r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\WebScrapping_Davi\Coletor.py",
    r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\WebScrapping_Davi\Executor.py"
)
for arq in lista_de_arquivos_a_serem_executados:
    with open(
        arq,
        "r"
    ) as namespace:
        exec(namespace.read())

main(
    "https://afiliado.supremaposta.com/login",
    "Junior",
    "Previsao@10M"
)
