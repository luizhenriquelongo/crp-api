from fastapi import FastAPI

from api.user import router as user_router
from api.crp import router as crp_router

app = FastAPI(
    title='CRP API',
    version='0.0.1',
    redoc_url='/'
)

app.include_router(user_router.router)
app.include_router(crp_router.router)
