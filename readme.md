# Descrição

Um amigo pediu-me que eu desenvolvesse uma aplicação 
capaz de realiziar WebScrapping em um determinado site,
além de desenvolver uma forma de executá-lo com periodicidade.

Sendo assim, desenvolvi este conjunto de programas que 
alcançam essas necessidades.

Tecnologias Utilizadas:

* PostGreSQL
* Selenium
* Schedule

Tive o prazer também de trabalhar em grupo com outros profissionais, posso
citar, por exemplo, [JP](https://github.com/JoaoPSilvaDev), a partir do qual pude 
aprender muito.

# Portabilidade da Aplicação

* Necessidade do Navegador Chrome

A aplicação utiliza o navegador Chrome, logo é necessário que ele esteja instalado.

* Necessidade do WebDriver correspondente ao Chrome

É como se utilizássemos uma "api" do chrome, basta seguir o [link](https://youtu.be/FT0cWOUkCzI).

* Usuário e Senha

Por serem informações confidenciais, devem ser colocadas no arquivo `config.py`.
Um modelo de configuração está disponível em `config_sample.py`. 
Copie este arquivo para `config.py` e preencha com suas credenciais reais.
O arquivo `config.py` está incluído no `.gitignore` para garantir que suas credenciais
não sejam acidentalmente compartilhadas em repositórios Git.

> Apenas para demonstrar o grau de satisfação:
<div align="center">
<img src="https://github.com/user-attachments/assets/9ab740a8-3f0c-49ad-abc4-729753f3687b" height="500"/>
</div>