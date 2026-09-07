from pydantic import BaseModel, field_validator, model_validator
from typing import Optional


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[list["Comment"]] = None


Comment.model_rebuild()


comment = {
    "id": 1,
    "content": "dflka jflkasf ",
    "replies": [
        Comment(id=2, content="this is reply-1"),
        Comment(id=3, content="thithis ie reply-222"),
    ],
}

commnt = Comment(**comment)

print(commnt)