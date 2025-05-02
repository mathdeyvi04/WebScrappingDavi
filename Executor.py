from Coletor import Coletor


def getter(
        url_desejada: str,
        usuario: str = None,
        senha: str = None
):
    bot = Coletor(usuario, senha)
    resp_de_carregamento = bot.init(
        url_desejada,
    True
    )

    if not resp_de_carregamento:
        exit()
    print("Carregamento Concluído")

    resp_de_login = bot.tentativa_de_login()

    if not resp_de_login:
        bot.destroy()
        exit()

    print("Login Concluído")

    bot.carregar_informacoes()

    print("Download Concluído")
    bot.destroy()
