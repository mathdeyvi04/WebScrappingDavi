from FuncoesBasicas import *


class Coletor:
    """
    Descrição:
        Classe representante do bot que coletará as informações.
    """

    def __init__(self, usuario=None, senha=None):
        """
        Apenas a declaração default de variáveis.
        """

        self.__usuario, self.__senha = self.__obter_login(
            # Caminho para Login
            r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\login_webscrapping_davi.txt"
        ) if usuario is None else (usuario, senha)

        self.waiter = None
        self.navegador_web = None

    @staticmethod
    def __obter_login(
            caminho_para_login: str
    ) -> list[str]:
        """
        Descrição:
            Obter login de forma confidencial.

        Retorno:
            Usuário e Senha válidos.
        """

        arq_confidente = open(caminho_para_login, "r")

        info = arq_confidente.read()

        arq_confidente.close()

        return info.split("\n")

    def init(
            self,
            url_desejada: str,
            caso_deseje_que_seja_escondido: bool = False
    ) -> bool:
        """
        Descrição:
            Iniciará execução do bot e seus respectivos
            componentes:

            - Navegador
            - Waiter
            - Site

            Haverá garantia de que os elementos foram
            suficientemente carregados.
        """

        opcoes_de_abertura = webdriver.ChromeOptions()

        if caso_deseje_que_seja_escondido:
            opcoes_de_abertura.add_argument(
                "--headless"
            )

        try:
            self.navegador_web = webdriver.Chrome(
                opcoes_de_abertura
            )

            self.waiter = WebDriverWait(
                self.navegador_web,
                10  # Para qualquer coisa, vamos esperar no máximo 10 segundos.
            )

            # Acessamos o site e verificamos se houve carregamento completo
            # Só então liberamos
            self.navegador_web.get(
                url_desejada
            )

            self.waiter.until(
                Expect_Condit.presence_of_element_located(
                    (
                        By.NAME,
                        "user"
                    )
                )
            )

            # Apenas para verificações
            # obter_todos_elementos_disponiveis(
            #     self.navegador_web.page_source
            # )

            return True

        except Exception as error:
            print(f"Erro identificado no carregamento do navegador ou do site: {error}")

            return False

    def tentativa_de_login(self) -> bool:
        """
        Descrição:
            Tentará preencher usuário e senha.
            Caso sucedido, retornará true.
        """

        try:
            sleep(0.5)
            self.navegador_web.find_element(
                By.NAME,
                "user"
            ).send_keys(
                self.__usuario
            )

            sleep(0.5)
            self.navegador_web.find_element(
                By.NAME,
                "password"
            ).send_keys(
                self.__senha
            )

            sleep(0.5)
            self.navegador_web.find_element(
                By.CLASS_NAME,
                "submit-btn"
            ).click()

            sleep(0.5)
            # Normalmente será bem rápido, mas dependerá da internet,
            # Por isso, manteremos o waiter.
            self.waiter.until(
                Expect_Condit.presence_of_element_located(
                    (
                        By.ID,
                        "mobileToggle"
                    )
                )
            )

        except Exception as error:
            print(f"Erro identificado ao completar login: {error}")
            return False

        return True

    def carregar_informacoes(
            self,
            range_de_data_desejado: str = None
    ) -> bool:
        """
        Descrição:
            Finalmente após carregamento e login completados,
            extrair as informações possíveis.

        Retorno:
            False se não deu certo.
            True caso tenha dado certo.



        """

        sleep(0.5)
        # Garante que estaremos no local certo para extrair as informações
        self.navegador_web.find_element(
            By.ID,
            "mobileToggle"
        ).click()

        sleep(0.5)
        self.navegador_web.find_element(
            By.LINK_TEXT,
            "Relatórios"
        ).click()

        # Vamos varrer cada uma das abas
        sleep(0.5)
        abas_a_serem_varridas = (
            "Relatório de Mídia",
            "Relatório de Registros",
            "Relatório de Ganhos",
            "Relatório de atividades"
        )
        possibilidades_de_range_de_data = {
            "Ontem",
            "Últimos 7 Dias",
            "Últimos 30 Dias",
            "Início da semana até hoje",
            "Ano até hoje",
            "Semana Passada",
            "Mês Passado"
        }

        # Dependendo do horário, devemos escolher o melhor
        # resultado para range de intervalo de tempo
        range_de_data_desejado = "Ontem" if range_de_data_desejado is None else range_de_data_desejado

        for cada_aba in abas_a_serem_varridas:
            # Selecionar aba correta
            self.navegador_web.find_element(
                By.LINK_TEXT,
                cada_aba
            ).click()
            sleep(0.5)

            # Verificar e selecionar range de tempo desejado
            if range_de_data_desejado not in possibilidades_de_range_de_data:
                print(f"Não há essa opção de range de data desejado, escolha dentre: {possibilidades_de_range_de_data}")
                return False

            elemento_select_de_range_de_data = Select(
                self.navegador_web.find_element(
                    By.TAG_NAME,
                    "select"
                )
            )
            elemento_select_de_range_de_data.select_by_visible_text(range_de_data_desejado)

            # Gerar relatório e esperar conclusão do mesmo e clicar no exportar
            sleep(1)
            index_min_de_botao = 0  # Apenas para não percorrermos futuramente os elementos desnecessários
            for elemento_de_botao in self.navegador_web.find_elements(
                    By.TAG_NAME,
                    "button"
            ):
                if elemento_de_botao.text.startswith('G'):
                    # A clicagem forçará o carregamento e o surgimento
                    # do botão de exportação.
                    elemento_de_botao.click()

                    break

                index_min_de_botao += 1

            # Clickar no exportar
            while True:

                elemento_desejado = list(
                    filter(
                        lambda elemento: elemento.text.startswith('E') and elemento.is_enabled(),
                        self.navegador_web.find_elements(By.TAG_NAME, "button")
                    )
                )

                if len(elemento_desejado) != 0:
                    sleep(1)
                    # Se há pelo menos, temos garantia que de que é único
                    elemento_desejado = elemento_desejado[0]

                    elemento_desejado.click()

                    break

                sleep(1)

            # Devemos esperar até o finalize, pois uma notificação surgirá
            # interrompendo o nosso processo
            sleep(10)

            # Abrimos o toggle novamente
            self.navegador_web.find_element(
                By.ID,
                "mobileToggle"
            ).click()

            sleep(0.5)
            self.navegador_web.find_element(
                By.LINK_TEXT,
                "Relatórios"
            ).click()

    def destroy(self) -> None:
        """
        Descrição:
            Apenas executará finalização de carregamentos e
            fechará o navegador.
        """

        self.navegador_web.quit()
