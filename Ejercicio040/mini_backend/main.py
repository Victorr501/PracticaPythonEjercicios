from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api import router as usuarios_router


app = FastAPI()

@app.exception_handler(RequestValidationError)
def validation_exception_handlen(request, axc):
    return JSONResponse(status_code= 400, content={"detail": "Body inválido"})


app.include_router(usuarios_router)