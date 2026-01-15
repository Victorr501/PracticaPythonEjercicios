from fastapi import APIRouter, HTTPException, Response, status
from app.models import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.repository import UsuarioRepository
from app.service import UsuarioService
from app.errors import UsuarioDuplicadoError, UsuarioNoEncontradoError, DatosUsuarioInvalidosError

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

repo = UsuarioRepository()
service = UsuarioService(repo)

@router.post("", status_code=201, response_model=UsuarioOut)
def post_usuario(body: UsuarioCreate):
    try:
        return service.crear_usuario(body.model_dump())
    except UsuarioDuplicadoError:
        raise HTTPException(status_code=409, detail="Usuario duplicado")
    except DatosUsuarioInvalidosError:
        raise HTTPException(status_code=400, detail="Datos invalidos")
    
@router.get("/{nombre}", response_model=UsuarioOut)
def get_usuario(nombre: str):
    try:
        return service.obtener_usuario(nombre)
    except UsuarioNoEncontradoError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
@router.put("/{nombre}", response_model=UsuarioOut)
def put_usuario(nombre: str, body: UsuarioUpdate):
    data = body.model_dump(exclude_none=True)
    try:
        return service.actualizar_usuario(nombre, data)
    except DatosUsuarioInvalidosError:
        raise HTTPException(status_code=400, detail="Datos invalidos")
    except UsuarioNoEncontradoError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
@router.delete("/{nombre}", status_code=204)
def delete_usuario(nombre: str):
    try:
        service.eliminar_usuario(nombre)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except UsuarioNoEncontradoError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")