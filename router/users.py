from fastapi import APIRouter ,Request
from database.database import SessionLocal
from database.models import soldier
from fastapi.templating import Jinja2Templates

router_users = APIRouter()
templates = Jinja2Templates(directory="templates")

@router_users.get("/soldiers")
def display_soldier(request:Request):
    s=SessionLocal()
    result = s.query(soldier).all()
    s.close()
    return templates.TemplateResponse("index2.html",{"request":request,"all":result})

@router_users.get("/users")
def search_soldier(request: Request,id : int):
    s=SessionLocal()
    result = s.query(soldier).get(id)
    print(result)
    s.close()
    return templates.TemplateResponse("index3.html",{"request":request,"final":result})  