from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Expect_Condit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from time import sleep

from os import listdir, remove, rename
from pathlib import Path

import openpyxl
import pandas as pd


def obter_todos_elementos_disponiveis(
        HTML: str
):
    """
    Descrição:
        Apresentará todos os elementos disponiveis na página
        no instante da chamada.

    Parâmetros:
        -> HTML, str
            Código Fonte da página
    """

    from pprint import pprint
    pprint(HTML)

    for elemento in BeautifulSoup(
        HTML,
        "html.parser"
    ).find_all(True):
        tag = elemento.name
        id_attr = elemento.get('id')
        name_attr = elemento.get('name')
        class_attr = elemento.get('class')

        print(f"Tag: {tag}")
        print(f"  ID: {id_attr}")
        print(f"  Name: {name_attr}")
        print(f"  Class: {class_attr}")
        print("-" * 40)




