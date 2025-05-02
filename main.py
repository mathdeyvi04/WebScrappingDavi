"""
Código capaz de executar os respectivos códigos.
"""

from os import getcwd

base_ = getcwd()

lista_de_arquivos_a_serem_executados = (
    base_ + "\FuncoesBasicas.py",
    base_ + "\Coletor.py",
    base_ + "\Executor.py"
)
for arq in lista_de_arquivos_a_serem_executados:
    with open(
        arq,
        "r"
    ) as namespace:
        exec(namespace.read())

# Executamos os arquivos
getter(
    "https://afiliado.supremaposta.com/login",
    # Por segurança
    # Precisa colocar o usuário, caso não esteja no computador de Deyvisson
    # Precisa colocar a senha, caso não esteja no computador de Deyvisson
)

# Devemos executar o extrador agora.
with open(
    base_ + "\Extrador.py",
    "r"
) as arq:
    exec(arq.read())
