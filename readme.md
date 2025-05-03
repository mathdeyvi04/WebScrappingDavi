# Descrição

Um amigo pediu-me que eu desenvolvesse uma aplicação 
capaz de realziar WebScrapping em um determinado site,
além de hospedá-lo no Google Cloud, a fim de possuir
certa periodicidade de execução.

Sendo assim, desenvolvi este mesmo programa no qual pude
compreender melhor sobre a tecnlogia em nuvem e sobre o
uso prático de POO.

Desenvolvi de tal forma que a aplicação possa rodar sem
surgimento de console.

# Portabilidade

* Necessidade do Navegador Chrome

A aplicação utiliza o navegador Chrome, logo é necessário que ele esteja instalado.

* Necessidade do WebDriver correspondente ao Chrome

Basta seguir o [link](https://youtu.be/FT0cWOUkCzI). 

* Máquina

Dependendo de como vc gerar o executável, somente será aceito em ambientes
Windows, Linux ou Android, certifique-se.

* Usuário e Senha

Por serem informações confidenciais, devem ser colocadas no arquivo `config.py`.
Um modelo de configuração está disponível em `config_sample.py`. 
Copie este arquivo para `config.py` e preencha com suas credenciais reais.
O arquivo `config.py` está incluído no `.gitignore` para garantir que suas credenciais
não sejam acidentalmente compartilhadas em repositórios Git.

# Como gerar o executável

Note que o arquivo ```criar_executavel.py``` garante que alterações
no código dos arquivos sejam repassadas, logo este arquivo é apenas 
um centralizador.

Sendo assim, há duas possibilidades:

* Gerar com Nuitka

```str
nuitka --standalone --onefile main.py
```

* Gerar com Pyinstaller

```str
pyinstaller --onefile --noconsole main.py
```



