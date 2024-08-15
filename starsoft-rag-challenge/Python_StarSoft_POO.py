from langchain.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.llms.ollama import Ollama

print("Inicializando as Classes...\n")
class DocumentLoader:
    """
    Carregar documentos PDF.
    Classe responsável por receber o doc em PDF e retornar-lo para processamento.
    """
    def __init__(self, caminho: str):
        self.caminho = caminho
    
    def load(self):
        loader = PyPDFLoader(self.caminho)
        return loader.load()

class TextSplitter:
    """
    Realiza a divisão do PDF em partes menores, para processamento do texto 
    utiliza o RecursiveCharacterTextSplitter.
    """
    def __init__(self, chunk_size: int, chunk_overlap: int, separators: list):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators
    
    def split(self, documentos):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators
        )
        return splitter.split_documents(documentos)

class EmbeddingsGenerator:
    """
    Gera embeddings para cada parte do documento utilizando o modelo OllamaEmbeddings.
    """
    def __init__(self, model_name: str):
        self.model = OllamaEmbeddings(model=model_name)
    
    def generate(self, partes):
        return [self.model.embed_query(parte.page_content) for parte in partes]

class ChromaDBHandler:
    """
    Classe responsável por salvar os embeddings no banco de dados ChromaDB.
    """
    def __init__(self, persist_directory: str):
        self.persist_directory = persist_directory
    
    def store(self, partes, embeddings_model):
        return Chroma.from_documents(
            partes,
            embeddings_model,
            persist_directory=self.persist_directory
        )
    
    def search(self, vetores, pergunta: str, k: int = 3, fetch_k: int = 10):
        return vetores.max_marginal_relevance_search(
            pergunta,
            k=k,
            fetch_k=fetch_k
        )

class OllamaChat:
    """
    Utiliza o ChatPromptTemplate para formatar o prompt e o Ollama para interagir
    com o modelo.
    """
    def __init__(self, model_name: str):
        self.model = Ollama(model=model_name)
    
    def create_prompt(self, context: str, question: str):
        template = """
        Responda à pergunta com base apenas no seguinte contexto: {context}

        ---

        Responda a pergunta com base no contexto acima, se não houver, não responda: {question}
        """
        prompt_template = ChatPromptTemplate.from_template(template)
        return prompt_template.format(context=context, question=question)
    
    def get_response(self, prompt):
        return self.model.invoke(prompt)


# Carregando documento.
print("Carregando documento...\n")
doc_loader = DocumentLoader("Data\Politica_de_Privacidade.pdf")
documentos = doc_loader.load()

# Separando documento em partes.
print("Realizando split do PDF...\n")
text_splitter = TextSplitter(chunk_size=150, chunk_overlap=15, separators=[".", ","])
partes = text_splitter.split(documentos)

# Gerando embeddings.
print("Gerando e armazenando embeddings...\n")
embeddings_generator = EmbeddingsGenerator(model_name="llama3.1")
document_embeddings = embeddings_generator.generate(partes)

# Armazenando embeddings no ChromaDB.
chroma_db = ChromaDBHandler(persist_directory='Chroma_Banco')
vetores = chroma_db.store(partes, embeddings_generator.model)
print("Vetores criados com sucesso!\n")

# Recuperando arquivos da Base com MMR.
pergunta = "Quais direitos eu tenho?"
docs = chroma_db.search(vetores, pergunta)

# for doc in docs:
#     source = doc.metadata.get("source")
#     page = doc.metadata.get("page")
#     print(f"Resposta: {doc.page_content}")
#     print(f"Fonte da informação: {source}: Página: {page}\n --- \n") 

# Interagindo com o modelo Ollama.
print("Iniciando Ollama...\n")

ollama_chat = OllamaChat(model_name="llama3.1")
contexto = "\n\n---\n\n".join([doc.page_content for doc in docs])
prompt = ollama_chat.create_prompt(context=contexto, question=pergunta)
response_text = ollama_chat.get_response(prompt)

print(f"Pergunta: {pergunta}")
print(response_text)

