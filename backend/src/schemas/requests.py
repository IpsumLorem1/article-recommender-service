from pydantic import BaseModel


class ArticleQuery(BaseModel):
    """
    Схема запроса для поиска статей.
    """

    query: str
