from data.database import database
from typing import Union

from fastapi import FastAPI, Request
from data.modelo.menu import Menu
from data.dao.dao_hospitales import DaoHospitales
from typing import Annotated
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root(request:Request, min_pacientes: int = 0):
    dao = DaoHospitales()
    hospitales = dao.get_all(database)
    if min_pacientes > 0:
        hospitales = [h for h in hospitales if h.numero_pacientes >= min_pacientes]
    return templates.TemplateResponse(
    request=request, name="principal.html", context={"hospitales": hospitales}
)


@app.get("/addHospital")
def form_add_alumnos(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddHospitales.html"
    )
@app.get("/delHospital", response_class=HTMLResponse)
async def test(request: Request):
    dao = DaoHospitales()
    hospitales = dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="formdelHospital.html", context={"hospitales": hospitales}                                                      
    )
@app.get("/updateHospital", response_class=HTMLResponse)
async def read_item(request: Request):
    dao = DaoHospitales()
    hospitales = dao.get_all(database)

    return templates.TemplateResponse(
        request=request, name="fomupdateHospital.html" , context={"hospitales": hospitales}
                                                      
    )



@app.post("/add_hospital")
def add_hospital(request: Request, nombre: Annotated[str, Form()] = None, numero_pacientes: Annotated[int, Form()] = None ):
    if nombre is None or numero_pacientes is None:
        dao = DaoHospitales()
        hospitales = dao.get_all(database) 
        return templates.TemplateResponse(
            request=request, name="formaddHospitales.html", context={"hospitales": hospitales}
        )
    
    dao = DaoHospitales()
    dao.insert(database, nombre, numero_pacientes)  
    
    hospitales = dao.get_all(database)  
    
    return templates.TemplateResponse(
        request=request, name="formaddHospitales.html", context={"hospitales": hospitales, "mensaje": "hospital correctamente introducido jejeje "}
    )

@app.post("/delHospital")
def delete_hospital(request: Request, id: Annotated[int, Form()] = None):
    if id is None:
        return templates.TemplateResponse(
            request=request, name="formdelHospital.html", context={"error": "nombre no proporcionado"}
        )
    
    dao = DaoHospitales()
    dao.delete(database, id)
    
    hospitales = dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="formdelHospital.html", context={"hospitales": hospitales}
    )

@app.post("/updateHospital")
def update_hospital(request: Request, id: Annotated[int, Form()] = None, nombre: Annotated[str, Form()] = None, numero_pacientes: Annotated[int, Form()]= None):
    if id is None or nombre is None or numero_pacientes is None:
        return templates.TemplateResponse(
            request=request, name="fomupdateHospital.html", context={"error": "ID o nombre o numero de pacientes no proporcionado"}
        )
    
    dao = DaoHospitales()
    dao.update(database, id, nombre, numero_pacientes) 
    hospitales = dao.get_all(database)

    return templates.TemplateResponse(
        request=request, name="fomupdateHospital.html", context={"hospitales": hospitales, "mensaje" : "hospital actualizado correctamente"}
    )





