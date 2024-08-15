# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da sua aplicação para o diretório de trabalho no contêiner
COPY . .

# Comando para rodar seu script Python
CMD ["python", "Python_StarSoft_POO.py"]
