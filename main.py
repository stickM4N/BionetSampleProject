from fastapi import FastAPI

from api.router import router as api_router

app = FastAPI(swagger_ui_parameters={})

app.include_router(api_router)
