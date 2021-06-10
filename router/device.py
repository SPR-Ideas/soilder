from fastapi import APIRouter
from pydantic import BaseModel
from database.database import SessionLocal
from database.models import soldier


router_device = APIRouter()

class _soldier(BaseModel):
    soldier_id : str
    BPM : int
    temp : float

def update_db(obj):
    s = SessionLocal()
    temp = s.query(soldier).filter(soldier.soldier_id == obj.soldier_id)[0]
    temp.BPM = obj.BPM
    temp.temp = obj.temp
    s.commit()
    s.close()



@router_device.post("/device")
def update(obj : _soldier):
    update_db(obj)
    return "done"

