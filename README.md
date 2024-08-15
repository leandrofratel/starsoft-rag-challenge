# Starsoft Rag Challenge
O objetivo deste teste é criar uma aplicaçao de IA capaz de processar e interagir com dados fornecidos diretamente de um documento PDF.

A aplicaçao utiliza as seguintes tecnologias:

1. Ollama: Modelo de linguagem que irá processar e interagir com o arquivo.
2. LangChain: Framework responsável pela criaçao da base da IA.
3. ChromaDB: Bando de dados baseado em vetores para armaezar o documento após processamento.
4. Docker e Docker Compose: Para orquestração.

Este projeto usa Docker para facilitar a configuração do ambiente e a execução do arquivo Python `Python_StarSoft_POO.py`. O script carrega, processa e gera embeddings de um documento PDF, armazenando-os em um banco de dados ChromaDB e interagindo com um modelo de linguagem.## Pré-requisitos

- **Docker e Docker Compose:** Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
- **Ollama:** Para este projeto funcionar corretamente, é necessário ter o Ollama instalado na máquina. Ele é utilizado para gerar embeddings e para a interação com o modelo de linguagem.

## Estrutura do Projeto

- `Dockerfile`: Define a imagem Docker e as instruções para criar o ambiente de execução.
- `docker-compose.yml`: Orquestra a construção e a execução do contêiner Docker.
- `requirements.txt`: Lista as dependências Python necessárias.
- `Python_StarSoft_POO.py`: O script principal que realiza o processamento dos documentos.

## Passos para Uso

### 1. Clone o Repositório

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Certifique-se de que o Ollama está Instalado

Garanta que o Ollama esteja instalado e configurado corretamente na sua máquina.

### 3. Construa e Inicie o Contêiner Docker

Use o Docker Compose para construir a imagem e iniciar o contêiner:

```bash
docker-compose up --build
```

Este comando irá:

- Construir a imagem Docker com base no `Dockerfile`.
- Instalar as dependências listadas no `requirements.txt`.
- Executar o script `Python_StarSoft_POO.py`.

### 4. Executando Novamente

Se você precisar executar o script novamente, use:

```bash
docker-compose up
```

### 5. Parar o Contêiner

Para parar o contêiner em execução, utilize:

```bash
docker-compose down
```

## Observações

- **Ollama:** Como mencionado, o Ollama deve estar instalado localmente, pois ele é utilizado pelo script para a geração de embeddings e para a interação com o modelo de linguagem.
- **Modificações:** Se fizer alterações no código ou nas dependências, reconstrua a imagem Docker usando `docker-compose up --build`.

## Solução de Problemas

- **Erros de Conexão com Ollama:** Verifique se o Ollama está corretamente instalado e configurado.
- **Problemas com Dependências:** Certifique-se de que o `requirements.txt` está atualizado e contém todas as bibliotecas necessárias.
