# Django learning
Essa pasta conterá todo o meu estudo sobre Django, uma framework de Python,
estudo esse feito pelo do curso da Udemy "Aprenda Django Web Framework" ministrado por Luiz Otávio, 
<a href=https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/>neste link</a>

## Django
Uma framework que permite criar aplicações web back-end robustas, escaláveis, rápidamente. Utilizada por grandes aplicações
como o Instagram, tem um respaldo mundial no quesito de desenvolvimento de aplicações para Web.

Django usa uma arquitetura MVT (Models, Views e Templates) predefinida, onde uma aplicação Web já tem muitas configurações pré-montadas para fornecer páginas web com arquitetura completa, apenas necessitando da configuração do próprio site, páginas, e dados.

### em Ordem lógica:
1. **Modelos** carregam dados de BDs, de forma a definir objetos com informações, interpretando assim as Tabelas relacionais (compatível com NoSQLs também.).
2. **Views** usam *Modelos* para renderizarem seus dados em páginas, montadas com *Templates*.
3. **Templates** são usados como padrões de arquitetura da página, arranjados em hierarquia definidas que mostram de forma intuitiva os dados de *Modelos*.

Django é amplamente usado para montar páginas Web, com compatibilidade em várias Stacks, mas também pode ser usado como um servidor Back-End alheio, aliado à diversas outras Stacks como NextJS, Express, Typescript, e outros.

# Setup do VEnv
Pode ser utilizado um ambiente virtualizado para os estudos, usando os comandos <i>venv</i>, para isolar pacotes necessários para o estudo.

* <code>powershell</code> (inicia powershell, necessário)
* <code>Set-ExecutionPolicy Unrestricted -Scope Process</code> (habilita execução de scripts)
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
 
<a href="[https://imgbb.com/](https://i.ibb.co/2k7tvN9/Image.png)"><img src="https://i.ibb.co/2k7tvN9/Image.png" alt="Comando tree na pasta" border="0" title="Usando Comando tree na pasta do MyProject"></a> 
<sub>*ou similar, no fim o server é só para desenvolvimento.</sub>

---

# Configurações de projeto e app
Fica evidente pela organização do Projeto Django, que ele tende a organizar separadamente cada arquivo e cada app, gerando segmentações onde cada arquivo necessário, como html, css, js, imagens, e outros devem ficar isolados em cada App respectivo do desenvolvimento.

Como parte dessa organização, alguns padrões e arquivos são automáticamente criados ao criar o Server e o App. alguns arquivos são criados e usados pelo Django:
### no Server
- <code>settings.py</code> - configura diversas variáveis úteis que definem o comportamento do servidor ao fornecer os Apps. Ele é a configuração padrão, mas pode ser definido uma config. específica para cada App também. 
- <code>urls.py</code> - configura URLs que o server deve fornecer. Daqui serão definidos quais endereços o server atende, com uma View específica e outras configurações.
### e no App
- <code>models.py</code> - organiza modelos de objetos vindos de bancos de dados.
- <code>admin.py</code> - registra e customiza para a visão e configuração em Admin. (no momento sei que se usa para registrar os modelos, podendo adicionar novos registros por lá)
- <code>tests.py</code> - deve reunir códigos de Test definidos com TestCases. Não ideal pra sistemas maiores...
- <code>views.py</code> - define as Views do App, para renderização das páginas
- <code>urls.py</code> - define URLs localmente, pode e deve ser importado às URLs do server.

## Settings.py
Há várias configurações específicas muito úteis para qualquer desenvolvimento, e serão definidas aqui elas, bem como um link para a documentação oficial sobre elas. Lembrando que, ao documentar aqui, sempre saiba que essas configurações já foram descritas nos Docs de Django.

- **INSTALLED_APPS**: utilizado para indicar quais Apps e serviços deverão executar com o Server django (ou outro servidor de produção), inclusive *'django.contrib.staticfiles'* (!importante no desenvolvimento!), e nomes dos Apps a serem carregados.
- **TEMPLATES**: utilizado para indicar opções de carregamento de Templates, sendo importante a key *'DIRS'*, que deve conter caminhos-base de templates que serão carregados.
- **DATABASES**: configura conexões com DBs, locais ou não. Por padrão, inicia como um SQLite3 local, mas pode ser mudado para PostgreSQL por exemplo, apenas adicionando configurações padrões de login no banco: **NAME** do banco de dados na conexão, **USER** name, **PASSWORD** de conexão, **HOST** abriga o IP ou URL de conexão, e **PORT** porta de conexão.
- ***TEST*** Key em DATABASES: define o nome de um banco de TESTE para uso quando TestCases forem executadas. Pode ser feito a transferência de dados entre o banco base e o banco de teste, se julgar necessário.
- **STATIC** Configs: existem 3: <code>STATIC_URL</code> define a URL gerada pelo servidor, ao servir um arquivo estático; <code>STATIC_ROOT</code> define o caminho (local) onde ficarão todos os arquivos estáticos, para serem servidos; e <code>STATICFILES_DIRS</code> é uma lista que define diretórios onde devem estar statics que devem ser coletados para a *STATIC_ROOT*, com <code>py manage.py collectstatic</code>.
- **MEDIA** Configs: existem 2(?): <code>MEDIA_URL</code> define a URL gerada pelo servidor, ao servir mídias (fotos, vídeos, docs.); e <code>MEDIA_ROOT</code>, caminho (local) onde ficam armazenados os arquivos de mídia.

### Adicionais:
- **LANGUAGE_CODE**: define a linguagem padrão do servidor, usado por exemplo na página Admin, ou em outros casos.
- **TIME_ZONE**: Timezones definidas em padrão internacional, pode ser necessário em questões de conexões com bancos de dados em outras TZs, por exemplo.
- **USE_TZ**: Booleano, define se usa ou não a TZ definida acima.

# A seguir:
outras integrações com serviços, como Tailwind CSS
