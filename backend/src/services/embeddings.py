from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_text_embedding(text: str):
    """
    Преобразует входной текст в эмбеддинг (numpy-массив).
    """
    embedding = model.encode([text])[0]
    return embedding
