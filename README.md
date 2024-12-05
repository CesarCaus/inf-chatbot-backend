# Documentação do Chatbot QA

## **Introdução**
Este projeto é um chatbot baseado em um modelo de Perguntas e Respostas (**QA - Question Answering**) projetado para facilitar a vida dos estudantes do Instituto Federal, auxiliando em atividades cotidianas dentro do Instituto de Informática. O chatbot utiliza inteligência artificial para processar perguntas em linguagem natural e fornecer respostas precisas, acessando um conjunto de dados pré-definido.

---

## **Estrutura do Código**

### **1. Funcionalidades Principais**
#### **Correção Ortográfica**
- Função: `corrigir_frase(frase_errada)`
- Objetivo: Corrigir erros de digitação ou ortografia na entrada do usuário antes de processar a pergunta.
- Implementação: Usa a biblioteca `autocorrect` para verificar e corrigir cada palavra da frase fornecida.

#### **Processamento de Perguntas e Respostas**
- Função: `buscar_resposta_com_contexto(pergunta_usuario)`
- Objetivo: Determinar a resposta mais relevante do dataset com base na similaridade semântica.
- Implementação:
  - Utiliza o modelo `SentenceTransformer` para gerar embeddings da pergunta do usuário e das perguntas alternativas no dataset.
  - Calcula a similaridade entre os embeddings usando `cosine_similarity`.
  - Retorna a resposta com maior similaridade acima de um limiar.

#### **Recepção e Validação de Dados**
- Função: `receive_message(request)`
- Objetivo: Receber requisições HTTP POST com mensagens do usuário, validar os dados e retornar uma resposta processada.
- Implementação:
  - Usa `MessageSerializer` para validar e desserializar os dados recebidos.
  - Corrige a frase e processa a pergunta para obter a resposta.

---

### **2. Estrutura do Dataset**
- Arquivo: `dataset_inf_ufg.json`
- Descrição: Contém perguntas alternativas e suas respectivas respostas relacionadas ao Instituto de Informática.
- Formato:
```json
[
  {
    "questions": ["Onde fica o laboratório 154?", "Qual é a localização do laboratório 154?"],
    "answer": "O laboratório está localizado no primeiro andar, no final do corredor aonde fica o bebedouro."
  }
]
```

---

### **3. Modelos e Serialização**
#### **Modelo Django**
- Classe: `Message`
- Descrição: Define a estrutura da tabela no banco de dados para armazenar mensagens do chatbot.
- Campos:
  - `text`: Texto da mensagem.
  - `type`: Tipo de mensagem (ex.: enviada ou recebida).

#### **Serializador**
- Classe: `MessageSerializer`
- Descrição: Serializa/deserializa os objetos `Message` para validação e transferência de dados.

---

### **4. URLs e Endpoints**
- Arquivo: `urls.py`
- Endereço: `/chat/`
- Função: `receive_message`
- Descrição: Endpoint para receber mensagens do usuário e retornar respostas do chatbot.

---

## **Requisitos do Projeto**

### **Dependências**
- **Bibliotecas Python**:
  - `Django` e `Django REST Framework`: Para gerenciamento do backend e APIs RESTful.
  - `autocorrect`: Para correção ortográfica.
  - `sentence_transformers`: Para embeddings de texto.
  - `scikit-learn`: Para cálculo de similaridade.
  - `numpy`: Para manipulação de vetores.
  - `json`: Para manipulação de arquivos JSON.

### **Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/CesarCaus/inf-chatbot-backend.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor local:
   ```bash
   python manage.py runserver
   ```

---

## **Fluxo de Funcionamento**
1. O usuário envia uma pergunta via requisição POST para o endpoint `/chat/`.
2. O texto da pergunta é corrigido pela função `corrigir_frase`.
3. A pergunta corrigida é processada pela função `buscar_resposta_com_contexto`, que compara embeddings e identifica a resposta mais relevante.
4. A resposta é retornada em formato JSON, contendo o texto e o tipo de mensagem.

---

## **Possíveis Melhorias Futuras**
- **Integração com APIs Externas:** Para obter informações em tempo real, como horários de aulas e eventos.
- **Aprendizado Contínuo:** Atualizar o dataset automaticamente com novas perguntas e respostas frequentes.
- **Suporte Multilíngue:** Permitir interações em outros idiomas.
- **Banco de Dados** Integrar um banco de dados para registrar usuários e salvar histórico.

---

## **Exemplo de Requisição e Resposta**

### **Requisição POST:**
```json
{
  "text": "Onde é a sala do professor?"
}
```

### **Resposta:**
```json
{
  "text": "A sala do professor está no bloco A, sala 101.",
  "type": "received"
}
```

---

## **Conclusão**
Este chatbot, baseado em um modelo QA, é uma solução prática e inteligente para atender às necessidades dos estudantes do Instituto Federal. Combinando tecnologias modernas e um design focado no usuário, ele representa um passo importante na digitalização e acessibilidade das informações institucionais.
