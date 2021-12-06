from fastapi import FastAPI
from app.muv import muv

app = FastAPI()
app.include_router(muv.router)

@app.get("/")
async def root():
    return {"message": "Hello World Team"}
