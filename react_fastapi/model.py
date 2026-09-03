from pydantic import BaseModel


class Books(BaseModel):
      # id : int
      title: str
      author: str
      year: int
      genre: str
      rating: float
      pages: int
      price: float
      image: str