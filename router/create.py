from fastapi import APIRouter
# from fastapi.routing import APIRoute
from pydantic import BaseModel
from database.database import SessionLocal
from database.models import soldier


router_create = APIRouter()

class _soldier(BaseModel):
    soldier_id : str
    name : str
    BPM : int
    temp : float

def create_db(obj):
    s = SessionLocal()
    soldierobj = soldier(soldier_id = obj.soldier_id, name = obj.name, BPM = obj.BPM, temp = obj.temp)
    s.add(soldierobj)
    s.commit()
    s.close()


@router_create.post("/create")
def soldier_details(req : _soldier):
    create_db(req)
    return req

