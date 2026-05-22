from fastapi import status, APIRouter

from schemas.post import PostRequest, PostUpdateRequest
from views.post import PostResponse
from models.post import posts
from services.post_service import PostService


router = APIRouter(prefix="/posts")    # Cannot import 'app' directly from 'main.py', must use a router to have acess to 'app' on 'main'

service = PostService()

@router.get("/", response_model=list[PostResponse])
async def read_posts(
    published: bool,
    limit: int,
    skip: int = 0,
   ):
    return await service.read_all(
        published=published,
        limit=limit,
        skip=skip)


@router.get("/{id}", response_model=PostResponse)
async def read_post(id: int):
    return await service.read(id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(post: PostRequest):
    command = posts.insert().values(
                          title=post.title,
                          content=post.content,
                          published_at=post.published_at,
                          published=post.published,
                          ) 
    return {**post.model_dump(), "id": await service.create(post)}    # '.model_dump()' --> Transforms the class representations into a dict


@router.patch("/{id}", response_model=PostResponse)
async def update_post(id: int, post: PostUpdateRequest):
    return await service.update(id=id, post=post)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    return await service.delete(id)

