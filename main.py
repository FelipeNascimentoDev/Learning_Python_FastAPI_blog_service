from scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import database, metadata, engine

from controllers import post



@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts   # 1. Force the execution of the 'table code' to creat it

    await database.connect()
    metadata.create_all(engine)     #  2. Create all the 'tables'
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)     # Allows the router usage on the file 'post.py' from the 'controller' folder







# -_-_-_-_-_-_-_- SCALAR DOCS -_-_-_-_-_-_-_-
#Acess: /scalar#description/introduction
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-