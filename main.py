from fastapi import templating
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from starlette.requests import Request
from database import models
from database.database import engine
from router.device import router_device
from router.create import router_create
from router.users import router_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# remove the commet on line 9 to activate datbase connection

models.Base.metadata.create_all(bind=engine)
app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="templates")

app.include_router(router_device)
app.include_router(router_create)
app.include_router(router_users)

@app.get("/")
def home(req:Request):
    return template.TemplateResponse("home.html",{"request":req})