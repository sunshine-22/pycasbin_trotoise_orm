from fastapi import FastAPI,Request,Depends,HTTPException,status
import models
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
import casbin_tortoise_adapter
from tortoise import Tortoise
import casbin

app = FastAPI()



async def get_access(request : Request):
    method = request.method
    path = dict(request).get("path")
    await Tortoise.init(
        db_url="postgres://root:root@192.168.145.169:5432/test_db",
        modules={"models": ["models","aerich.models"]},
    )
    await Tortoise.generate_schemas()
    e = casbin.Enforcer('model.conf',adapter=casbin_tortoise_adapter.TortoiseAdapter())
    sub = "member"  # the user that wants to access a resource.
    obj = path  # the resource that is going to be accessed.
    act = method  # the operation that the user performs on the resource.
    print(sub,obj,act)
    print(e.enforce(sub,obj,act))

@app.get("/get_data")
async def get_all_contacts(user = Depends(get_access)):
    data = await models.Contact.all().values()
    return data


if __name__ == "__main__":
    uvicorn.run(
        host = "0.0.0.0",
        port=8000,
        reload=True
    )