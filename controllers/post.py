from datetime import UTC, datetime
from typing import Annotated

from fastapi import Response, Cookie, Header, status, APIRouter
from pydantic import BaseModel

from schemas.post import PostRequest
from views.post import PostResponse


router = APIRouter(prefix="/posts")    # Cannot import 'app' directly from 'main.py', must use a router to have acess to 'app' on 'main'


fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), "published": False},
    {"title": "Criando uma aplicação com Starlett", "date": datetime.now(UTC), "published": True},
]



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostRequest):
    fake_db.append(post.model_dump())   # '.model_dump()' --> Transforms the class representations into a dict
    return post


@router.get("/", response_model=list[PostResponse])
def read_posts(
    response: Response,
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None , Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None, # user_agent --> stores 'who is calling the API' (Chrome, Postman, etc...)
):
    response.set_cookie(key='user', value='email@email.com')
    print(f"Cookie: {ads_id}")
    print(f"user_agent: {user_agent}")
    return [post for post in fake_db[skip: skip + limit] if post["published"] is published]


@router.get("/{framework}", response_model=PostResponse)
def read_frameworks(framework: str):
    return {
        "posts": [
            {
                "title": "Criando uma aplicação com o {framwork}",
                "date" : datetime.now(UTC)
            },
            {
                "title": "Criando uma aplicação com o {framwork}",
                "date" : datetime.now(UTC)
            },
        ]
    }