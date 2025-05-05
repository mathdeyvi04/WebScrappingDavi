#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Versão OOP do script principal para o sistema de WebScrapping da plataforma.
Este arquivo substitui o uso de exec() por importações explícitas e abordagem orientada a objetos.
"""

from Coletor import Coletor
from Extrador import Extrador
import os
from config import LOGIN_URL, USERNAME, PASSWORD
from datetime import datetime, timedelta
from time import sleep


class WebScrapperApp:
    """
    Classe principal que orquestra o processo de web scraping,
    substituindo os exec() calls por importações explícitas e métodos.
    """

    def __init__(self, url, usuario=None, senha=None):
        """
        Inicializa a aplicação com os dados de conexão necessários.
        
        Args:
            url (str): URL da página de login
            usuario (str, optional): Nome de usuário. Default é None.
            senha (str, optional): Senha. Default é None.
        """
        self.url = url
        self.usuario = usuario
        self.senha = senha

    def executar_coleta(self) -> bool:
        """
        Executa o processo de coleta de dados utilizando o Coletor.
        Substitui o processo que antes era feito com exec() do arquivo Executor.py
        """
        bot = Coletor(self.usuario, self.senha)

        # Inicializa o navegador
        resp_de_carregamento = bot.init(self.url, True)
        if not resp_de_carregamento:
            print("Falha no carregamento do navegador.")
            return False
        print("Carregamento Concluído")

        # Tenta fazer login
        resp_de_login = bot.tentativa_de_login()
        if not resp_de_login:
            print("Falha no login.")
            bot.destroy()
            return False
        print("Login Concluído")

        # Carrega informações
        bot.carregar_informacoes("Últimos 7 Dias")
        print("Download Concluído")

        # Encerra o navegador
        bot.destroy()
        return True

    def executar_extracao(self) -> bool:
        """
        Executa o processo de extração dos dados baixados.
        Substitui o processo que antes era feito com exec() do arquivo Extrador.py
        """
        try:
            extrator = Extrador()
            extrator.verificar_converter()
            extrator.enviar()

            extrator.destroy()
            return True
        except Exception as e:
            print(f"Erro durante a extração: {e}")
            return False


def main():
    """
    Função principal que executa o fluxo completo da aplicação.
    """
    # Instanciar a aplicação com os dados de acesso importados do arquivo de configuração
    app = WebScrapperApp(
        LOGIN_URL,
        USERNAME,
        PASSWORD
    )

    # Executar a coleta de dados
    if app.executar_coleta():
        # Se a coleta foi bem-sucedida, executar a extração

        """if app.executar_extracao():
            print("Processo concluído com sucesso!")
        else:
            print("Falha durante o processo de extração.")"""
    else:
        print("Falha durante o processo de coleta.")


if __name__ == "__main__":
    # Vamos criar a lógica do schedule aqui
    horario_desejado_de_execucao = "12:00:00"

    horario_desejado_de_execucao = datetime.strptime(
        horario_desejado_de_execucao,
        "%H:%M:%S"
    )

    TEMPO_ADORMECIDO_DE_ESPERA = (
        4  # Quantidade de horas esperando
    ) * 60 * 60

    primeira_dia_de_execucao = True
    while True:

        agora = datetime.now()

        if primeira_dia_de_execucao:
            # Consertamos a data, ano, mês e dia do horário desejado.
            # Vamos colocá-los em sincronia
            horario_desejado_de_execucao = agora.replace(
                hour=horario_desejado_de_execucao.hour,
                minute=horario_desejado_de_execucao.minute,
                second=horario_desejado_de_execucao.second
            )

            primeira_dia_de_execucao = False

        if agora >= horario_desejado_de_execucao:
            # Finalmente executamos.
            main()

            # Desejamos executar novamente no próximo dia
            horario_desejado_de_execucao += timedelta(days=1)

        sleep(
            TEMPO_ADORMECIDO_DE_ESPERA
        )
