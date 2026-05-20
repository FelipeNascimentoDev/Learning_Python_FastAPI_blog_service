from fastapi import status, APIRouter

from schemas.post import PostRequest
from views.post import PostResponse
from models.post import posts
from database import database


router = APIRouter(prefix="/posts")    # Cannot import 'app' directly from 'main.py', must use a router to have acess to 'app' on 'main'


@router.get("/", response_model=list[PostResponse])
async def read_posts(
    published: bool,
    limit: int,
    skip: int = 0,
   ):
    query = posts.select()
    return await database.fetch_all(query)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(post: PostRequest):
    command = posts.insert().values(
                          title=post.title,
                          content=post.content,
                          published_at=post.published_at,
                          published=post.published,
                          )
    last_record_id = await database.execute(command)
    # fake_db.append(post.model_dump())   # '.model_dump()' --> Transforms the class representations into a dict
    return {**post.model_dump(), "id": last_record_id}

