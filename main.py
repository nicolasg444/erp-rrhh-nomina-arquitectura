from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ERP RRHH - API Empleados")

class Empleado(BaseModel):
    nombre: str
    cargo: str
    salario_base: float
    departamento: str

empleados = []

@app.post("/api/empleados")
def registrar_empleado(empleado: Empleado):
    empleados.append(empleado.dict())
    return {"mensaje": "Empleado registrado exitosamente", "empleado": empleado}

@app.get("/api/empleados")
def listar_empleados():
    return {"empleados": empleados, "total": len(empleados)}
