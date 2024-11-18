from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import os

# Carregar embeddings
embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')

caminho_dataset = os.path.join(os.path.dirname(__file__), 'dataset_inf_ufg.json')

# Carregar o dataset JSON
with open(caminho_dataset, 'r', encoding='utf-8') as file:
    dataset = json.load(file)

# Pré-calcular embeddings para cada pergunta alternativa no dataset
dataset_embeddings = []
for item in dataset:
    question_embeddings = [embedder.encode(question) for question in item["questions"]]
    dataset_embeddings.append((question_embeddings, item["answer"]))

# Função para buscar a resposta mais relevante e retornar com base na pergunta mais similar
def buscar_resposta_com_contexto(pergunta_usuario):
    pergunta_embedding = embedder.encode(pergunta_usuario)
    maior_similaridade = 0.5
    resposta_relevante = "Desculpe, não consegui encontrar uma resposta adequada."

    # Avaliar similaridade com cada pergunta alternativa no dataset
    for question_embeddings, answer in dataset_embeddings:
        for embedding in question_embeddings:
            similaridade = cosine_similarity([pergunta_embedding], [embedding])[0][0]

            # Seleciona a resposta com a maior similaridade
            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                resposta_relevante = answer

    return resposta_relevante

