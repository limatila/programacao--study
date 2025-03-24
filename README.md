# FastAPI-Pokedex - Quick Guide
## en_US version
 A study-based API for Pokemon related data, ready for local usage. Provides data and details stored in a local database, about Pokemons, Abilitys, Ability Types and Categories, and other more. \
 Some data can be setted up in DB, with effective test-oriented data.
 
 Created with FastAPI and SQLModel, aswell as other necessary packages (described in <b>requirements.txt</b> and <b>dev-dependencies.txt</b>)

## Installation and Usage
For general usage, you'll just need to setup a database and run the API with the specified packages in <b>requirements.txt</b> \
This tutorial is gonna assume you use Windows for your OS. If not, please search the equivalent of the commands below.

### So, in a step-by-step instalation:
1. Clone the repo:
	 ```bash
	 git clone https://github.com/limatila/programacao--study 
	 ```

2. Checkout to this branch:
	 ```bash
	 git checkout fastapi-pokedex & git pull
	 ``` 

- Optional: create a VEnv to isolate packages that will be needed:
	 ```bash
	 python -m venv venv 
	 powershell  # Needs powershell to run activation script
	 .\venv\Scripts\activate 
	 ```
3. Install main requirements (you can read these if you want):
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize a default SQLite db with ORM defined structure:
   ```bash
   python -m pokedex.models.models 
	 ```

- Optional: startup your db with some arbitrary objects, for local tests:
   ```bash
   python -m pokedex.models.setup.startup_basic_inserts # Will insert a basic set of objects
   ```

	and if you will:

	 ```bash
   pip install -r dev-dependencies.txt # Install another API for data gathering
   python -m pokedex.models.setup.startup_pokemon_all # Will insert all pokemons known to date
	 ```

5. Create your secret key and set it as environment variable (need for methods that modify data) 
   1. install OpenSSL, in [mainly here](https://slproweb.com/products/Win32OpenSSL.html), or any other binaries source 
   2. create your new random key with: <code> openssl rand -hex 32 </code> 
   3. set your environment variable with the key: <code> setx SECRET_KEY_POKEDEX your_secret_code </code> 
   4. verify the variable setted with: <code> echo %SECRET_KEY_POKEDEX%</code>

6. Initialize your API server:
  *in powershell (with venv)* \
	<code> up-server.ps1 </code>
	
   - If you do not trust this script (or any malfunction reason happens) you can run at this point:
		```bash
		uvicorn pokedex.main.api_pokedex:app --host 127.0.0.1 --port 55001
		```

#### OBS: always run .py files with 'python -m', at the root folder
#### OBS 2: any configuration of Database connections must be defined at 'pokedex.dependencies.config', which now only supports SQLite and PostgreSQL connections.

### Available API urls include:
- **GET(Read):**
  - [Get pokemon of specific ID](http://localhost:55001/v1/get/pokemon/id/20/)
  - [Get pokemon of specific Name](http://localhost:55001/v1/get/pokemon/name/pikachu/)
  - [Get ability of specific ID](http://localhost:55001/v1/get/ability/id/2/)
  - [Get ability of specific Name](http://localhost:55001/v1/get/ability/name/fire%20spin/)
  - [Get ability compatibility (if 'x' pokemon is compatible with 'y' ability) with specific Names](http://localhost:55001/v1/get/abilitycompatibility?pokemon=charmander&ability=fire%20spin)
- **POST(Create) - uses Bearer token:**
  - [Insert new ability with defined attributes](http://localhost:55001/v1/post/ability?id=3&name=Fire%20Spin&effect=continuous%20damage&generation=1&category=special&type=fire)
  - [Insert new ability with defined attributes](http://localhost:55001/v1/post/abilitytype?id=4&name=eletric&color=%23FFD351)
  - [Insert new ability compatibility with specific Names](http://localhost:55001/v1/post/abilitycompatibility?id=5&pokemon=charmander&ability=fire%20spin)
- **DELETE - uses Bearer token:**
  - [Delete a ability compatibility (include only ID, or only pokemon and ability Names)](http://localhost:55001/v1/delete/abilitycompatibility?pokemon=charmander&ability=fire%20spin)

## versão pt-BR
Uma API baseada em estudos para dados relacionados a Pokémon, pronta para uso local. Fornece dados e detalhes armazenados em um banco de dados local sobre Pokémons, Habilidades, Tipos de Habilidades e Categorias, entre outros (urls de uso tem nomes em en_US, além do código inteiro).
Alguns dados podem ser configurados no banco de dados, com dados eficazes orientados para testes.

Criado com FastAPI e SQLModel, além de outros pacotes necessários (descritos em **requirements.txt** e **dev-dependencies.txt**).

## Instalação e Uso
Para uso geral, você precisará apenas configurar um banco de dados e executar a API com os pacotes especificados em **requirements.txt**. Esse tutorial assume que você está usando Windows como seu sistema operacional. Caso contrário, procure os comandos equivalentes abaixo.

### Passo a passo da instalação:
1. Clone o repositório:
   ```bash
   git clone https://github.com/limatila/programacao--study
   ```

2. Acesse esta branch:
   ```bash
   git checkout fastapi-pokedex & git pull
   ```

- Opcional: crie um VEnv para isolar os pacotes necessários:
   ```bash
   python -m venv venv
   powershell # Necessário para executar o script de ativação
   .\venv\Scripts\activate
   ```

3. Instale os requisitos principais (você pode lê-los se quiser):
   ```bash
   pip install -r requirements.txt
   ```

4. Inicialize um banco de dados SQLite padrão com a estrutura definida pelo ORM:
   ```bash
   python -m pokedex.models.models
   ```

- Opcional: inicie seu banco de dados com alguns objetos arbitrários, para testes locais:
   ```bash
   python -m pokedex.models.setup.startup_basic_inserts # Irá inserir um conjunto básico de objetos
   ```

   e se desejar:
   ```bash
   pip install -r dev-dependencies.txt # Instala outra API para coleta de dados
   python -m pokedex.models.setup.startup_pokemon_all # Irá inserir todos os pokémons conhecidos
   ```

5. Crie sua chave secreta e defina-a como uma variável de ambiente (necessário para métodos que modificam dados):
   1. Instale o OpenSSL, [principalmente aqui](https://slproweb.com/products/Win32OpenSSL.html), ou qualquer outra fonte de binários dele.
   2. Crie sua nova chave aleatória com: <code>openssl rand -hex 32</code>   
   3. Defina sua variável de ambiente com a chave: <code>setx SECRET_KEY_POKEDEX seu_codigo_secreto</code>   
   4. Verifique a variável definida com: <code>echo %SECRET_KEY_POKEDEX%</code>
   
6. Inicialize seu servidor API:
   *No PowerShell (com venv):* \
	<code> up-server.ps1 </code>

   - Se você não confiar neste script (ou ocorrer algum motivo de mau funcionamento), você pode executar:
     ```bash
     uvicorn pokedex.main.api_pokedex:app --host 127.0.0.1 --port 55001
     ```

#### OBS: sempre execute arquivos .py com 'python -m', na pasta raiz.
#### OBS 2: qualquer configuração de conexões de banco de dados deve ser definida em 'pokedex.dependencies.config', que atualmente suporta apenas conexões SQLite e PostgreSQL.

### URLs disponíveis da API incluem:
- **GET (Leitura):**
  - [Obter pokemon por ID específico](http://localhost:55001/v1/get/pokemon/id/20/)
  - [Obter pokemon por Nome específico](http://localhost:55001/v1/get/pokemon/name/pikachu/)
  - [Obter ability por ID específico](http://localhost:55001/v1/get/ability/id/2/)
  - [Obter ability por Nome específico](http://localhost:55001/v1/get/ability/name/fire%20spin/)
  - [Obter compatibilidade de ability (se 'x' pokemon é compatível com 'y' ability) com Nomes](http://localhost:55001/v1/get/abilitycompatibility?pokemon=charmander&ability=fire%20spin)

- **POST (Criação) - usa token Bearer:**
  - [Inserir nova ability com atributos definidos](http://localhost:55001/v1/post/ability?id=3&name=Fire%20Spin&effect=continuous%20damage&generation=1&category=special&type=fire)
  - [Inserir novo tipo de ability com atributos definidos](http://localhost:55001/v1/post/abilitytype?id=4&name=eletric&color=%23FFD351)
  - [Inserir nova compatibilidade de ability com Nomes](http://localhost:55001/v1/post/abilitycompatibility?id=5&pokemon=charmander&ability=fire%20spin)

- **DELETE - usa token Bearer:**
  - [Excluir uma compatibilidade de ability (inclua apenas ID, ou apenas Nomes do pokemon e da ability)](http://localhost:55001/v1/delete/abilitycompatibility?pokemon=charmander&ability=fire%20spin)

# Qualquer dúvida, adiciona nas issues do repositório!
# Any question, you can add to this repo's issues!
