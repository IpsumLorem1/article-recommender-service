from fastapi import APIRouter
from src.schemas.requests import ArticleQuery
from src.services.embeddings import get_text_embedding
from src.services.search import search_similar_articles

router = APIRouter()


@router.post("/search")
async def search_articles(query: ArticleQuery):
    """
    Обработчик поиска статей.
    """
    # Преобразуем текст в эмбеддинг
    user_emb = get_text_embedding(query.query)

    # Ищем похожие статьи
    results = search_similar_articles(user_emb, top_k=10)

    # Возвращаем JSON с результатами
    return {"results": results}
