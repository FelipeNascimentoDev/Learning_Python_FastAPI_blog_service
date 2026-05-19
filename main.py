from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI

from controllers import post



app = FastAPI()

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