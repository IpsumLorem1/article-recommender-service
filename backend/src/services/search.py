import os
import faiss
import pandas as pd
import numpy as np
from src.core.definitions import MODEL_DIR

# Путь к файлам
faiss_index_path = MODEL_DIR / "faiss_index.idx"
articles_path = MODEL_DIR / "articles.csv"

# Проверка существования файлов
if not os.path.exists(faiss_index_path):
    raise FileNotFoundError(f"FAISS index not found at {faiss_index_path}")
if not os.path.exists(articles_path):
    raise FileNotFoundError(f"Articles CSV not found at {articles_path}")

# Загрузка FAISS индекса
faiss_index = faiss.read_index(str(faiss_index_path))
print("FAISS index loaded successfully.")

# Загрузка данных о статьях
articles_df = pd.read_csv(str(articles_path))
if articles_df.empty:
    raise ValueError("Articles CSV is empty.")
print(f"Loaded {len(articles_df)} articles.")


def search_similar_articles(user_emb, top_k=10):
    """
    Ищет в FAISS-индексе ближайшие статьи по пользовательскому эмбеддингу (косинусное сходство).

    Args:
        user_emb (numpy.ndarray): Вектор эмбеддинга пользователя.
        top_k (int): Количество ближайших статей для поиска.

    Returns:
        list[dict]: Список ближайших статей с метаданными.
    """
    # Проверяем размерность пользовательского эмбеддинга
    if user_emb.ndim != 1 or user_emb.shape[0] != faiss_index.d:
        raise ValueError(
            f"Invalid user embedding shape: {user_emb.shape}. Expected shape: ({faiss_index.d},)"
        )

    # Нормализуем пользовательский эмбеддинг (для косинусного сходства)
    user_emb = np.expand_dims(user_emb, axis=0)
    faiss.normalize_L2(user_emb)

    # Выполняем поиск по индексу
    distances, indices = faiss_index.search(user_emb, top_k)

    # Формируем результаты поиска
    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if idx == -1:  # Если индекс не найден
            continue
        if idx >= len(articles_df):  # Проверка на корректный индекс
            raise IndexError(f"Index {idx} out of range for articles DataFrame.")

        # Извлекаем данные о статье
        row = articles_df.iloc[idx]
        results.append(
            {
                "title": row.get("title", "No Title"),
                "text": row.get("text", "No Text"),
                "index": int(idx),
                "distance": float(dist),  # Косинусное сходство
            }
        )

    return results
