# Django learning
Essa pasta conterá todo o meu estudo sobre Django, uma framework de Python,
estudo esse feito pelo do curso da Udemy "Aprenda Django Web Framework" ministrado por Luiz Otávio, 
<a href=https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/>neste link</a>

## Django
Uma framework que permite criar aplicações web back-end robustas, escaláveis, rápidamente. Utilizada por grandes aplicações
como o Instagram, tem um respaldo mundial no quesito de desenvolvimento de aplicações para Web.

## Uso do VEnv
Será utilizado um ambiente virtualizado para os estudos, usando os comandos <i>venv</i>, para isolar pacotes necessários para o estudo.

* <code>py -m venv venv</code> (cria o venv)
* <code>venv\Scripts\activate</code> (ativa ele)

# Setup do Django
Sobre ativação e manejo de projetos e Apps Django

Primeiramente, com o venv ativado(para isolamento de conteúdo), <code>'pip install django'</code>

### Criando o servidor:
Ao usar o Django, se adiciona primeiro um diretório de <i>Projeto</i> para o desenvolvimento.
* <code>mkdir MyProject & cd MyProject</code> (cria uma pasta base <i>MyProject</i> e navega para ela)
* <code>django-admin startproject mysite .</code> (cria um projeto-diretório 'mysite' e servidor no localhost, dentro da pasta raíz)
* Atenção ao rodar junto com o '<b>.</b>' pois ele é primordial para a organização das pastas.
* <code>manage.py runserver</code> (conecta um server na porta 8000) 
 
Depois se acessa o servidor pelo Browser, utilizando http://127.0.0.1:8000, por padrão.
 
#Pode ser adicionado um launch.json para o VSCode executar 'manage.py runserver' em um clique (veja '.vscode/launch.json')

### Criando o App:
Ao ter um projeto criado, vários <i>Apps</i> podem ser criados no mesmo diretório, caracterizando várias partições de um sistema completo, de forma organizada.
* <code>manage.py startapp myapp</code> (Cria um app, com todos seus conteúdos específicos)
 
logo, a estrutura deve ser apresentar assim: 
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/2k7tvN9/Image.png" alt="Comando tree na pasta" border="0" title="Usando Comando tree na pasta do MyProject"></a>
 
---

# Configurações de projeto e app
Fica evidente pela organização do Projeto Django, que ele tende a organizar separadamente cada arquivo e cada app, gerando segmentações onde cada arquivo necessário, como html, css, js, imagens, e outros devem ficar isolados em cada App respectivo do desenvolvimento.

# URLs, HttpResponses e Views 
Dentro do projeto, em <i>urls.py</i>, TODO!

### mais para ser adicionado enquanto estudo...