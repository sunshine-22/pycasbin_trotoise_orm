from fastapi import FastAPI,Request,Depends,HTTPException,status
import models
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
import casbin_tortoise_adapter
from tortoise import Tortoise
import casbin
import uuid
app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://root:root@localhost:5432/test_db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)



@app.get("/get_data")
async def get_all_contacts():
    
    return {"hi":"response"}



@app.post("/add_user")
async def add_user(name:str):
    add_user =  await models.usertable.create(name = name)
    return {"response":"created"}

@app.post("/country")
async def add_user(name:str,country_name:str):
    add_user =  await models.usertable.get(name = name)
    country  =  await models.Country.create(country_name = country_name, created_by = add_user)
    return {"response":"created"}

@app.post("/state")
async def add_user(name:str,country_name:str,state_name : str):
    add_user =  await models.usertable.get(name = name)
    print(">>>>>>>zcc>>>",add_user)
    country =  await models.Country.get(country_name = country_name)
    print("?????????????????",country)
    state_add = await models.State.create(state_name = state_name,created_by = add_user,country = country)
    return {"response":"created"}

if __name__ == "__main__":
    uvicorn.run(
        host = "0.0.0.0",
        port=8000,
      
    )