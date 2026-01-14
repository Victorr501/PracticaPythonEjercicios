from fastapi import APIRouter, HTTPException, Response, status
from models import UsuarioCreate, UsuarioUpdate, UsuarioOut

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

